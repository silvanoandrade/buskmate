# =============================================================================
# AULA 3 (lote 3/8) — Módulo Sessão: os 2 casos de prioridade "Alta"
# =============================================================================
# Mesmo padrão dos lotes anteriores (Cadastro, Login). A novidade aqui é só a
# forma de "entrar logado": em vez de preencher o formulário de login de
# novo, escrevemos direto a chave que o auth.js espera encontrar no
# localStorage (buskmate_session) — mais rápido, e deixa o teste focado só
# no que ele quer validar (a navbar), não no formulário de login de novo.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL
import json


def plantar_sessao(driver, nome, email):
    """Loga o usuário 'na marra', sem passar pelo formulário.

    Precisa estar numa página do site primeiro (senão não tem acesso ao
    localStorage daquele domínio) — mesmo truque já usado em test_cadastro.py
    (TC-018) e test_login.py (TC-023). Depois de plantar, recarrega a
    página: a navbar (nav-user) só é montada 1x, quando a página termina de
    carregar (updateNavAuthState() roda no DOMContentLoaded) — sem esse
    reload ela não ia saber que agora existe uma sessão.
    """
    driver.get(f"{URL}mapa.html")
    sessao = json.dumps({"nome": nome, "email": email})
    driver.execute_script("localStorage.setItem('buskmate_session', arguments[0]);", sessao)
    driver.get(f"{URL}mapa.html")


# --- TC-025 (RF-SESSAO-01) — Navbar mostra saudação quando logado ----------
def test_TC025_navbar_saudacao_logado(driver):
    plantar_sessao(driver, nome="Maria Teste", email="maria.teste@example.com")

    nav_user = driver.find_element(By.ID, "nav-user")
    assert nav_user.is_displayed()
    assert "Maria" in nav_user.text
    assert "Sair" in nav_user.text


# --- TC-026 (RF-SESSAO-02) — "Sair" encerra a sessão ------------------------
def test_TC026_logout_encerra_sessao(driver):
    plantar_sessao(driver, nome="Maria Teste", email="maria.teste@example.com")

    driver.find_element(By.ID, "logout-link").click()
    assert driver.current_url.endswith("index.html")

    # Volta pro mapa pra confirmar que a sessão realmente foi apagada do
    # localStorage (não só que a gente foi redirecionado).
    driver.get(f"{URL}mapa.html")
    assert driver.find_element(By.ID, "nav-login").is_displayed()
    assert driver.find_element(By.ID, "nav-cadastro").is_displayed()
    assert not driver.find_element(By.ID, "nav-user").is_displayed()

