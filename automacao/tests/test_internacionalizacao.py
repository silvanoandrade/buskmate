# =============================================================================
# AULA 3 (lote 5/8) — Módulo Internacionalização: os 5 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/navbar.py, pages/mapa_page.py)
# AULA 5 — TC-006 e TC-007 viraram 1 teste parametrizado
# =============================================================================
import pytest
from selenium.webdriver.common.by import By
from conftest import URL
from pages.navbar import Navbar
from pages.mapa_page import MapaPage


# --- TC-005 (RF-I18N-01) — Seletor mostra as 3 opções de idioma ------------
def test_TC005_seletor_mostra_3_idiomas(driver):
    driver.get(URL)
    navbar = Navbar(driver)
    navbar.lang_toggle.click()
    opcoes = navbar.opcoes_de_idioma()
    assert len(opcoes) == 3
    textos = [o.text for o in opcoes]
    assert any("Português" in texto for texto in textos)
    assert any("English" in texto for texto in textos)
    assert any("Español" in texto for texto in textos)


# --- TC-006 / TC-007 (RF-I18N-02/03) — Troca de idioma traduz a home -------
# AULA 5 — pytest.mark.parametrize: em vez de 2 funções quase idênticas (uma
# pra inglês, outra pra espanhol), descrevemos os DADOS que mudam numa lista
# e deixamos o pytest rodar a MESMA função uma vez por item. No relatório
# (-v) cada execução aparece separada: [TC-006] e [TC-007].
CASOS_TRADUCAO_HOME = [
    pytest.param("en", "Find the right spot. Play where you belong.", id="TC-006"),
    pytest.param("es", "Encuentra el lugar ideal. Toca donde perteneces.", id="TC-007"),
]


@pytest.mark.parametrize("lang, titulo_esperado", CASOS_TRADUCAO_HOME)
def test_troca_de_idioma_traduz_home(driver, lang, titulo_esperado):
    driver.get(URL)
    Navbar(driver).trocar_idioma(lang)
    titulo = driver.find_element(By.TAG_NAME, "h1").text
    assert titulo == titulo_esperado


# --- TC-008 (RF-I18N-04) — Idioma persiste ao navegar entre páginas --------
def test_TC008_idioma_persiste_ao_navegar(driver):
    driver.get(URL)
    navbar = Navbar(driver)
    navbar.trocar_idioma("en")
    driver.get(f"{URL}mapa.html")
    assert navbar.link("mapa.html").text == "Map"


# --- TC-014 (RF-I18N-08) — Descrição do spot muda conforme idioma ---------
def test_TC014_descricao_spot_muda_conforme_idioma(driver):
    mapa = MapaPage(driver).abrir()
    mapa.abrir_spot(0)  # Cais da Ribeira

    descricao_pt = driver.find_element(By.CSS_SELECTOR, "#spot-content p:nth-of-type(2)").text
    Navbar(driver).trocar_idioma("en")
    # A troca de idioma redesenha o painel inteiro (map.js escuta o evento
    # e reabre o spot sozinho) — por isso buscamos o elemento de novo.
    descricao_en = driver.find_element(By.CSS_SELECTOR, "#spot-content p:nth-of-type(2)").text

    assert descricao_pt != descricao_en
    assert descricao_en == "Steady flow of tourists by the riverside, great acoustics under the arches."
