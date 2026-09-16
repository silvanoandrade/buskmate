# =============================================================================
# AULA 3 (lote 2/6) — Módulo Login: os 3 casos de prioridade "Alta"
# =============================================================================
# Mesmo padrão do lote 1 (Cadastro, test_cadastro.py): cada teste pede
# "driver" e ganha o navegador pronto do conftest.py; cada função carrega o
# TC-xxx no nome pra manter rastreabilidade com o
# docs/BuskMate_QA_Plano_de_Testes.xlsx.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL


def fazer_login(driver, email, senha):
    """Função auxiliar: abre a página de login, preenche e envia o formulário.

    Mesma ideia do preencher_cadastro() em test_cadastro.py — evita repetir
    esse trecho nos 3 testes abaixo.
    """
    driver.get(f"{URL}login.html")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "senha").send_keys(senha)
    driver.find_element(By.CSS_SELECTOR, "#form-login button[type=submit]").click()


# --- TC-021 (RF-LOGIN-01) — Campos obrigatórios exibidos no login -----------
def test_TC021_campos_visiveis(driver):
    driver.get(f"{URL}login.html")
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "senha").is_displayed()


# --- TC-022 (RF-LOGIN-02) — Login com credenciais inválidas é bloqueado -----
def test_TC022_credenciais_invalidas_bloqueiam(driver):
    fazer_login(driver, email="naoexiste@example.com", senha="qualquer123")
    mensagem = driver.find_element(By.ID, "form-message").text
    assert mensagem == "Email ou senha inválidos."


# --- TC-023 (RF-LOGIN-03) — Login válido cria sessão e redireciona ----------
def test_TC023_login_valido_redireciona(driver):
    email = "usuario.login.selenium@example.com"
    senha = "123456"

    # Mesmo truque do TC-018 (test_cadastro.py): "plantamos" o usuário direto
    # no localStorage em vez de passar pelo cadastro de novo — o teste de
    # login não deve depender do cadastro ter rodado antes dele.
    driver.get(f"{URL}login.html")  # precisa estar numa página do site pra ter acesso ao localStorage dele
    driver.execute_script(
        "localStorage.setItem('buskmate_users', JSON.stringify("
        "[{nome:'Usuario Login', email:arguments[0], senha:arguments[1]}]));",
        email,
        senha,
    )

    fazer_login(driver, email=email, senha=senha)
    assert driver.current_url.endswith("mapa.html")

