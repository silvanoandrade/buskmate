# =============================================================================
# AULA 3 (lote 7/8) — Módulo Avaliação: os 4 casos de prioridade "Alta"
# =============================================================================
# Novidade: as estrelas de avaliação não são um <input> comum — são 5 <span>
# clicáveis desenhados pelo map.js (um "widget" próprio). Selenium não liga:
# clica em qualquer elemento, não só em controles de formulário de verdade.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL
import json


def plantar_sessao(driver, nome="Maria Teste", email="maria.teste@example.com"):
    """Mesmo truque de plantar sessão usado em test_sessao.py."""
    sessao = json.dumps({"nome": nome, "email": email})
    driver.execute_script("localStorage.setItem('buskmate_session', arguments[0]);", sessao)


def abrir_spot(driver, indice):
    marcadores = driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")
    marcadores[indice].click()


# --- TC-038 (RF-AVAL-01) — Formulário de avaliação visível quando logado --
def test_TC038_formulario_visivel_logado(driver):
    driver.get(f"{URL}mapa.html")
    plantar_sessao(driver)

    # Diferente da navbar (TC-025, que só é montada 1x quando a página
    # carrega — por isso aquele teste precisa de reload depois de plantar a
    # sessão), o formulário de avaliação é decidido TODA VEZ que você clica
    # num spot (abrirSpot(), no map.js, lê a sessão na hora do clique). Por
    # isso aqui não precisa de reload.
    abrir_spot(driver, 0)
    assert driver.find_element(By.ID, "form-avaliar").is_displayed()


# --- TC-039 (RF-AVAL-02) — Prompt de login exibido quando deslogado -------
def test_TC039_prompt_login_deslogado(driver):
    driver.get(f"{URL}mapa.html")
    abrir_spot(driver, 0)
    prompt = driver.find_element(By.CSS_SELECTOR, ".login-prompt").text
    assert "login" in prompt.lower()
    assert "avaliar" in prompt.lower()


# --- TC-041 (RF-AVAL-04) — Envio sem estrelas selecionadas é bloqueado ----
def test_TC041_envio_sem_estrelas_bloqueia(driver):
    driver.get(f"{URL}mapa.html")
    plantar_sessao(driver)
    abrir_spot(driver, 2)  # Rua de Santa Catarina
    driver.find_element(By.CSS_SELECTOR, "#form-avaliar button[type=submit]").click()
    mensagem = driver.find_element(By.ID, "avaliar-message").text
    assert mensagem == "Selecione de 1 a 5 estrelas."


# --- TC-042 (RF-AVAL-05) — Avaliação enviada atualiza lista e média -------
def test_TC042_avaliacao_atualiza_lista_e_media(driver):
    driver.get(f"{URL}mapa.html")
    plantar_sessao(driver, nome="Carlos Silva")
    abrir_spot(driver, 3)  # Torre dos Clérigos

    driver.find_element(By.CSS_SELECTOR, "#star-input .star[data-value='4']").click()
    driver.find_element(By.ID, "comentario").send_keys("Ótimo lugar pra tocar!")
    driver.find_element(By.CSS_SELECTOR, "#form-avaliar button[type=submit]").click()

    texto_painel = driver.find_element(By.ID, "spot-content").text
    assert "4.0" in texto_painel  # média com 1 avaliação de nota 4 = 4.0
    assert "Ótimo lugar pra tocar!" in texto_painel
    assert "Carlos" in texto_painel

