# =============================================================================
# AULA 3 (lote 6/8) — Módulo Mapa: os 6 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/mapa_page.py)
# =============================================================================
import json
from pages.mapa_page import MapaPage


# --- TC-029 (RF-MAPA-01) — Mapa carrega centrado no Porto -------------------
def test_TC029_mapa_carrega_centrado_no_porto(driver):
    mapa = MapaPage(driver).abrir()
    centro = mapa.centro_do_mapa()
    # Coordenadas aproximadas do centro do Porto (41.1479, -8.6291) — com
    # margem de tolerância em vez de exigir o valor exato.
    assert abs(centro[0] - 41.1479) < 0.05
    assert abs(centro[1] - (-8.6291)) < 0.05


# --- TC-030 (RF-MAPA-02) — Mapa exibe os 10 marcadores ----------------------
def test_TC030_mapa_exibe_10_marcadores(driver):
    mapa = MapaPage(driver).abrir()
    assert len(mapa.marcadores) == 10


# --- TC-032 (RF-MAPA-04) — Clique no marcador abre o painel -----------------
def test_TC032_clique_marcador_abre_painel(driver):
    mapa = MapaPage(driver).abrir()
    assert not mapa.painel.is_displayed()  # começa escondido (atributo "hidden")

    mapa.abrir_spot(0)
    assert mapa.painel.is_displayed()


# --- TC-033 (RF-MAPA-05) — Painel exibe "Ainda sem avaliações" -------------
def test_TC033_painel_sem_avaliacoes(driver):
    mapa = MapaPage(driver).abrir()
    mapa.abrir_spot(0)  # Cais da Ribeira: nenhum teste planta avaliação pra ele
    assert "Ainda sem avaliações" in mapa.texto_painel


# --- TC-034 (RF-MAPA-06) — Painel exibe média e contagem com avaliações ----
def test_TC034_painel_media_e_contagem(driver):
    mapa = MapaPage(driver).abrir()

    # "Planto" 2 avaliações pra "aliados" direto no localStorage — mais
    # rápido e confiável do que preencher o formulário 2 vezes.
    avaliacoes = {
        "aliados": [
            {"autor": "Maria", "nota": 4, "comentario": "Muito bom!", "data": "2026-01-01T10:00:00.000Z"},
            {"autor": "João", "nota": 5, "comentario": "", "data": "2026-01-02T10:00:00.000Z"},
        ]
    }
    mapa.driver.execute_script("localStorage.setItem('buskmate_reviews', arguments[0]);", json.dumps(avaliacoes))

    mapa.abrir_spot(1)  # índice 1 em spots.js = "Praça dos Aliados"
    assert "4.5" in mapa.texto_painel
    assert "2 avaliações" in mapa.texto_painel


# --- TC-035 (RF-MAPA-07) — Painel exibe descrição e melhor horário --------
def test_TC035_painel_descricao_e_melhor_horario(driver):
    mapa = MapaPage(driver).abrir()
    mapa.abrir_spot(0)  # Cais da Ribeira
    assert "Movimento constante de turistas à beira-rio" in mapa.texto_painel
    assert "Melhor horário:" in mapa.texto_painel
    assert "Tardes e fins de tarde, 15h-19h" in mapa.texto_painel
