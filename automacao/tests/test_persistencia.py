# =============================================================================
# AULA 3 (lote 8/8, parte 1) — Módulo Persistência de Dados: o caso de
# prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/mapa_page.py,
# pages/navbar.py) e o helper compartilhado plantar_sessao
# =============================================================================
import json
from pages.mapa_page import MapaPage
from pages.navbar import Navbar
from pages.auth_helpers import plantar_sessao


# --- TC-045 (RF-PERSIST-01) — Dados persistem após reload ------------------
def test_TC045_dados_persistem_apos_reload(driver):
    mapa = MapaPage(driver).abrir()

    plantar_sessao(driver, nome="Maria Teste", email="maria.teste@example.com")
    avaliacoes = json.dumps({
        "aliados": [{"autor": "Maria", "nota": 5, "comentario": "Top!", "data": "2026-01-01T10:00:00.000Z"}]
    })
    driver.execute_script("localStorage.setItem('buskmate_reviews', arguments[0]);", avaliacoes)

    driver.refresh()

    navbar = Navbar(driver)
    assert "Maria" in navbar.nav_user.text

    mapa.abrir_spot(1)  # Praça dos Aliados
    assert "5.0" in mapa.texto_painel
    assert "1 avaliações" in mapa.texto_painel
