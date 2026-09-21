# =============================================================================
# AULA 3 (lote 2/6) — Módulo Login: os 3 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/login_page.py)
# =============================================================================
from pages.login_page import LoginPage


# --- TC-021 (RF-LOGIN-01) — Campos obrigatórios exibidos no login -----------
def test_TC021_campos_visiveis(driver):
    pagina = LoginPage(driver).abrir()
    assert pagina.campo_email.is_displayed()
    assert pagina.campo_senha.is_displayed()


# --- TC-022 (RF-LOGIN-02) — Login com credenciais inválidas é bloqueado -----
def test_TC022_credenciais_invalidas_bloqueiam(driver):
    pagina = LoginPage(driver).abrir()
    pagina.fazer_login(email="naoexiste@example.com", senha="qualquer123")
    assert pagina.mensagem == "Email ou senha inválidos."


# --- TC-023 (RF-LOGIN-03) — Login válido cria sessão e redireciona ----------
def test_TC023_login_valido_redireciona(driver):
    email = "usuario.login.selenium@example.com"
    senha = "123456"
    pagina = LoginPage(driver).abrir()

    driver.execute_script(
        "localStorage.setItem('buskmate_users', JSON.stringify("
        "[{nome:'Usuario Login', email:arguments[0], senha:arguments[1]}]));",
        email,
        senha,
    )

    pagina.fazer_login(email=email, senha=senha)
    assert driver.current_url.endswith("mapa.html")
