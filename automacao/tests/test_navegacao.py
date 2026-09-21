# =============================================================================
# AULA 3 (lote 4/8) — Módulo Navegação: o caso de prioridade "Alta"
# =============================================================================
# Só 1 caso aqui, mas ele pede pra checar a MESMA coisa em 4 páginas
# diferentes. A novidade é só essa: reaproveitar o mesmo navegador (a mesma
# fixture "driver") pra visitar várias páginas em sequência dentro de UM
# teste só, usando um for comum. Isso é diferente de
# @pytest.mark.parametrize (que cria 4 testes INDEPENDENTES, cada um com seu
# próprio navegador) — parametrize é assunto da Aula 5.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL

PAGINAS = ["index.html", "login.html", "cadastro.html", "mapa.html"]


# --- TC-001 (RF-NAV-01) — Header completo em todas as páginas --------------
def test_TC001_header_completo_em_todas_paginas(driver):
    for pagina in PAGINAS:
        driver.get(f"{URL}{pagina}")
        assert driver.find_element(By.CSS_SELECTOR, "a.logo").is_displayed(), f"logo ausente em {pagina}"
        assert driver.find_element(By.CSS_SELECTOR, "a[href='mapa.html']").is_displayed(), f"link Mapa ausente em {pagina}"
        assert driver.find_element(By.CSS_SELECTOR, "a[href='login.html']").is_displayed(), f"link Login ausente em {pagina}"
        assert driver.find_element(By.CSS_SELECTOR, "a[href='cadastro.html']").is_displayed(), f"link Cadastrar ausente em {pagina}"
        assert driver.find_element(By.ID, "lang-toggle").is_displayed(), f"seletor de idioma ausente em {pagina}"

