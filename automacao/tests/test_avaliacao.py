# =============================================================================
# AULA 3 (lote 7/8) — Módulo Avaliação: os 4 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/mapa_page.py) e o
# helper compartilhado plantar_sessao (pages/auth_helpers.py)
# =============================================================================
from pages.mapa_page import MapaPage
from pages.auth_helpers import plantar_sessao


# --- TC-038 (RF-AVAL-01) — Formulário de avaliação visível quando logado --
def test_TC038_formulario_visivel_logado(driver):
    mapa = MapaPage(driver).abrir()
    plantar_sessao(driver)

    # Diferente da navbar (TC-025, que só é montada 1x quando a página
    # carrega), o formulário de avaliação é decidido TODA VEZ que você
    # clica num spot — por isso aqui não precisa de reload.
    mapa.abrir_spot(0)
    assert mapa.form_avaliar.is_displayed()


# --- TC-039 (RF-AVAL-02) — Prompt de login exibido quando deslogado -------
def test_TC039_prompt_login_deslogado(driver):
    mapa = MapaPage(driver).abrir()
    mapa.abrir_spot(0)
    prompt = mapa.prompt_login.lower()
    assert "login" in prompt
    assert "avaliar" in prompt


# --- TC-041 (RF-AVAL-04) — Envio sem estrelas selecionadas é bloqueado ----
def test_TC041_envio_sem_estrelas_bloqueia(driver):
    mapa = MapaPage(driver).abrir()
    plantar_sessao(driver)
    mapa.abrir_spot(2)  # Rua de Santa Catarina
    mapa.enviar_avaliacao()
    assert mapa.mensagem_avaliacao == "Selecione de 1 a 5 estrelas."


# --- TC-042 (RF-AVAL-05) — Avaliação enviada atualiza lista e média -------
def test_TC042_avaliacao_atualiza_lista_e_media(driver):
    mapa = MapaPage(driver).abrir()
    plantar_sessao(driver, nome="Carlos Silva")
    mapa.abrir_spot(3)  # Torre dos Clérigos

    mapa.avaliar(estrelas=4, comentario="Ótimo lugar pra tocar!")

    assert "4.0" in mapa.texto_painel  # média com 1 avaliação de nota 4 = 4.0
    assert "Ótimo lugar pra tocar!" in mapa.texto_painel
    assert "Carlos" in mapa.texto_painel
