# =============================================================================
# AULA 4 — Page Object Model: MapaPage
# =============================================================================
# A página mais "cheia" do site: mapa Leaflet, painel lateral do spot,
# formulário de avaliação por estrelas... Concentrar tudo isso numa classe
# só é o que mais vale a pena no Page Object Model — sem isso, os testes de
# Mapa e Avaliação (9 casos ao todo) ficariam cheios de seletor repetido.
# =============================================================================

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL


class MapaPage:
    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(f"{URL}mapa.html")
        # NOVO: espera explícita. O Leaflet desenha o mapa e os marcadores
        # de forma assíncrona (via JavaScript), depois que a página já
        # "carregou" do ponto de vista do Selenium — sem essa espera, um
        # teste que rode rápido demais (como no CI, que costuma ser mais
        # rápido que a máquina local) pode tentar clicar num marcador antes
        # dele existir. WebDriverWait é melhor que time.sleep: ele não
        # espera um tempo fixo, só até a condição virar verdadeira (ou até
        # o timeout de 10s, se algo estiver realmente quebrado).
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".leaflet-marker-icon"))
        )
        return self

    @property
    def marcadores(self):
        """Marcadores do Leaflet, na mesma ordem de BUSKMATE_SPOTS em
        spots.js (0 = Cais da Ribeira, 1 = Praça dos Aliados, 2 = Rua de
        Santa Catarina, 3 = Torre dos Clérigos...) — o Leaflet não dá um id
        próprio pra cada um, então usamos a posição na lista."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")

    def abrir_spot(self, indice):
        self.marcadores[indice].click()
        return self

    @property
    def painel(self):
        return self.driver.find_element(By.ID, "spot-panel")

    @property
    def texto_painel(self):
        return self.driver.find_element(By.ID, "spot-content").text

    @property
    def prompt_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".login-prompt").text

    def centro_do_mapa(self):
        """Pergunta direto pro JavaScript da página (execute_script) onde o
        objeto Leaflet (a variável global `map`, de map.js) está centrado."""
        return self.driver.execute_script("return [map.getCenter().lat, map.getCenter().lng];")

    # --- formulário de avaliação (dentro do painel, só aparece logado) -----
    def avaliar(self, estrelas, comentario=""):
        self.driver.find_element(By.CSS_SELECTOR, f"#star-input .star[data-value='{estrelas}']").click()
        if comentario:
            self.driver.find_element(By.ID, "comentario").send_keys(comentario)
        self.enviar_avaliacao()

    def enviar_avaliacao(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-avaliar button[type=submit]").click()

    @property
    def form_avaliar(self):
        return self.driver.find_element(By.ID, "form-avaliar")

    @property
    def mensagem_avaliacao(self):
        return self.driver.find_element(By.ID, "avaliar-message").text
