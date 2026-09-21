# =============================================================================
# AULA 3 (lote 5/8) — Módulo Internacionalização: os 5 casos de prioridade "Alta"
# =============================================================================
# Novidade: o menu de idiomas (#lang-menu) começa com o atributo HTML
# `hidden` — só fica visível depois que a gente clica no botão #lang-toggle
# (o próprio JS do site remove o hidden). Então trocar de idioma sempre são
# 2 cliques: abre o menu, depois clica na opção. E pra selecionar a opção
# certa a gente usa um seletor CSS de atributo: [data-lang='en'].
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL


def trocar_idioma(driver, lang):
    """Abre o menu de idiomas e clica na opção pedida ('pt', 'en' ou 'es')."""
    driver.find_element(By.ID, "lang-toggle").click()
    driver.find_element(By.CSS_SELECTOR, f"li.lang-option[data-lang='{lang}']").click()


# --- TC-005 (RF-I18N-01) — Seletor mostra as 3 opções de idioma ------------
def test_TC005_seletor_mostra_3_idiomas(driver):
    driver.get(URL)
    driver.find_element(By.ID, "lang-toggle").click()
    opcoes = driver.find_elements(By.CSS_SELECTOR, "li.lang-option")
    assert len(opcoes) == 3
    textos = [o.text for o in opcoes]
    assert any("Português" in texto for texto in textos)
    assert any("English" in texto for texto in textos)
    assert any("Español" in texto for texto in textos)


# --- TC-006 (RF-I18N-02) — Troca para inglês traduz a home ------------------
def test_TC006_troca_para_ingles_traduz_home(driver):
    driver.get(URL)
    titulo_antes = driver.find_element(By.TAG_NAME, "h1").text
    trocar_idioma(driver, "en")
    titulo_depois = driver.find_element(By.TAG_NAME, "h1").text
    assert titulo_depois != titulo_antes
    assert titulo_depois == "Find the right spot. Play where you belong."


# --- TC-007 (RF-I18N-03) — Troca para espanhol traduz a home ----------------
def test_TC007_troca_para_espanhol_traduz_home(driver):
    driver.get(URL)
    trocar_idioma(driver, "es")
    titulo = driver.find_element(By.TAG_NAME, "h1").text
    assert titulo == "Encuentra el lugar ideal. Toca donde perteneces."


# --- TC-008 (RF-I18N-04) — Idioma persiste ao navegar entre páginas --------
def test_TC008_idioma_persiste_ao_navegar(driver):
    driver.get(URL)
    trocar_idioma(driver, "en")
    driver.get(f"{URL}mapa.html")
    link_mapa = driver.find_element(By.CSS_SELECTOR, "a[href='mapa.html']")
    assert link_mapa.text == "Map"


# --- TC-014 (RF-I18N-08) — Descrição do spot muda conforme idioma ---------
def test_TC014_descricao_spot_muda_conforme_idioma(driver):
    driver.get(f"{URL}mapa.html")
    marcadores = driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")
    marcadores[0].click()  # 1º spot cadastrado em spots.js: "Cais da Ribeira"

    descricao_pt = driver.find_element(By.CSS_SELECTOR, "#spot-content p:nth-of-type(2)").text
    trocar_idioma(driver, "en")
    # A troca de idioma redesenha o painel inteiro (o map.js escuta o evento
    # de troca de idioma e reabre o spot sozinho) — por isso buscamos o
    # elemento de novo em vez de reusar a variável "descricao_pt" de cima.
    descricao_en = driver.find_element(By.CSS_SELECTOR, "#spot-content p:nth-of-type(2)").text

    assert descricao_pt != descricao_en
    assert descricao_en == "Steady flow of tourists by the riverside, great acoustics under the arches."

