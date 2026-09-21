# =============================================================================
# AULA 3 (lote 6/8) — Módulo Mapa: os 6 casos de prioridade "Alta"
# =============================================================================
# Novidade: o mapa é desenhado pela biblioteca Leaflet.js, então os
# marcadores não têm um id próprio de cada spot no HTML — viram uma lista de
# imagens (.leaflet-marker-icon) na MESMA ORDEM em que foram adicionados no
# spots.js. Por isso selecionamos por posição na lista (índice), não por id.
#
# Outra novidade: pra checar onde o mapa está centrado, em vez de ler algo
# da TELA, perguntamos direto pro JavaScript da página o estado do objeto do
# mapa (a variável global `map`, criada em map.js) via execute_script.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL
import json


def abrir_spot(driver, indice):
    """Clica no marcador de índice `indice` (0 = 'Cais da Ribeira', 1 =
    'Praça dos Aliados', 2 = 'Rua de Santa Catarina', 3 = 'Torre dos
    Clérigos'... na mesma ordem da lista BUSKMATE_SPOTS em spots.js)."""
    marcadores = driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")
    marcadores[indice].click()


# --- TC-029 (RF-MAPA-01) — Mapa carrega centrado no Porto -------------------
def test_TC029_mapa_carrega_centrado_no_porto(driver):
    driver.get(f"{URL}mapa.html")
    centro = driver.execute_script("return [map.getCenter().lat, map.getCenter().lng];")
    # Coordenadas aproximadas do centro do Porto (41.1479, -8.6291) — com
    # margem de tolerância em vez de exigir o valor exato.
    assert abs(centro[0] - 41.1479) < 0.05
    assert abs(centro[1] - (-8.6291)) < 0.05


# --- TC-030 (RF-MAPA-02) — Mapa exibe os 10 marcadores ----------------------
def test_TC030_mapa_exibe_10_marcadores(driver):
    driver.get(f"{URL}mapa.html")
    marcadores = driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")
    assert len(marcadores) == 10


# --- TC-032 (RF-MAPA-04) — Clique no marcador abre o painel -----------------
def test_TC032_clique_marcador_abre_painel(driver):
    driver.get(f"{URL}mapa.html")
    painel = driver.find_element(By.ID, "spot-panel")
    assert not painel.is_displayed()  # começa escondido (atributo "hidden")

    abrir_spot(driver, 0)
    assert painel.is_displayed()


# --- TC-033 (RF-MAPA-05) — Painel exibe "Ainda sem avaliações" -------------
def test_TC033_painel_sem_avaliacoes(driver):
    driver.get(f"{URL}mapa.html")
    abrir_spot(driver, 0)  # Cais da Ribeira: nenhum teste planta avaliação pra ele
    texto_painel = driver.find_element(By.ID, "spot-content").text
    assert "Ainda sem avaliações" in texto_painel


# --- TC-034 (RF-MAPA-06) — Painel exibe média e contagem com avaliações ----
def test_TC034_painel_media_e_contagem(driver):
    driver.get(f"{URL}mapa.html")

    # "Planto" 2 avaliações pra "aliados" direto no localStorage, do mesmo
    # jeito que já plantamos usuário/sessão em testes anteriores — mais
    # rápido e confiável do que preencher o formulário 2 vezes só pra
    # chegar nesse estado.
    avaliacoes = {
        "aliados": [
            {"autor": "Maria", "nota": 4, "comentario": "Muito bom!", "data": "2026-01-01T10:00:00.000Z"},
            {"autor": "João", "nota": 5, "comentario": "", "data": "2026-01-02T10:00:00.000Z"},
        ]
    }
    driver.execute_script("localStorage.setItem('buskmate_reviews', arguments[0]);", json.dumps(avaliacoes))

    abrir_spot(driver, 1)  # índice 1 em spots.js = "Praça dos Aliados"
    texto_painel = driver.find_element(By.ID, "spot-content").text
    assert "4.5" in texto_painel
    assert "2 avaliações" in texto_painel


# --- TC-035 (RF-MAPA-07) — Painel exibe descrição e melhor horário --------
def test_TC035_painel_descricao_e_melhor_horario(driver):
    driver.get(f"{URL}mapa.html")
    abrir_spot(driver, 0)  # Cais da Ribeira
    texto_painel = driver.find_element(By.ID, "spot-content").text
    assert "Movimento constante de turistas à beira-rio" in texto_painel
    assert "Melhor horário:" in texto_painel
    assert "Tardes e fins de tarde, 15h-19h" in texto_painel

