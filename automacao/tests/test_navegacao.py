# =============================================================================
# AULA 3 (lote 4/8) — Módulo Navegação: o caso de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/navbar.py)
# =============================================================================
from conftest import URL
from pages.navbar import Navbar

PAGINAS = ["index.html", "login.html", "cadastro.html", "mapa.html"]


# --- TC-001 (RF-NAV-01) — Header completo em todas as páginas --------------
def test_TC001_header_completo_em_todas_paginas(driver):
    navbar = Navbar(driver)
    for pagina in PAGINAS:
        driver.get(f"{URL}{pagina}")
        assert navbar.logo.is_displayed(), f"logo ausente em {pagina}"
        assert navbar.link("mapa.html").is_displayed(), f"link Mapa ausente em {pagina}"
        assert navbar.link("login.html").is_displayed(), f"link Login ausente em {pagina}"
        assert navbar.link("cadastro.html").is_displayed(), f"link Cadastrar ausente em {pagina}"
        assert navbar.lang_toggle.is_displayed(), f"seletor de idioma ausente em {pagina}"
