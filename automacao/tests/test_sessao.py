# =============================================================================
# AULA 3 (lote 3/8) — Módulo Sessão: os 2 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/navbar.py) e o
# helper compartilhado plantar_sessao (pages/auth_helpers.py)
# =============================================================================
from conftest import URL
from pages.navbar import Navbar
from pages.auth_helpers import plantar_sessao


def _entrar_logado(driver, nome, email):
    driver.get(f"{URL}mapa.html")
    plantar_sessao(driver, nome=nome, email=email)
    driver.get(f"{URL}mapa.html")  # a navbar só é montada 1x, no carregamento


# --- TC-025 (RF-SESSAO-01) — Navbar mostra saudação quando logado ----------
def test_TC025_navbar_saudacao_logado(driver):
    _entrar_logado(driver, nome="Maria Teste", email="maria.teste@example.com")
    navbar = Navbar(driver)

    assert navbar.nav_user.is_displayed()
    assert "Maria" in navbar.nav_user.text
    assert "Sair" in navbar.nav_user.text


# --- TC-026 (RF-SESSAO-02) — "Sair" encerra a sessão ------------------------
def test_TC026_logout_encerra_sessao(driver):
    _entrar_logado(driver, nome="Maria Teste", email="maria.teste@example.com")
    navbar = Navbar(driver)

    navbar.fazer_logout()
    assert driver.current_url.endswith("index.html")

    driver.get(f"{URL}mapa.html")
    assert navbar.nav_login.is_displayed()
    assert navbar.nav_cadastro.is_displayed()
    assert not navbar.nav_user.is_displayed()
