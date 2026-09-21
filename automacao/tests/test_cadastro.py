# =============================================================================
# AULA 3 (lote 1/6) — Módulo Cadastro: os 5 casos de prioridade "Alta"
# AULA 4 — refatorado pra usar Page Object Model (pages/cadastro_page.py)
# =============================================================================
from pages.cadastro_page import CadastroPage
import time


# --- TC-015 (RF-CAD-01) — Campos obrigatórios exibidos no cadastro ----------
def test_TC015_campos_visiveis(driver):
    pagina = CadastroPage(driver).abrir()
    assert pagina.campo_nome.is_displayed()
    assert pagina.campo_email.is_displayed()
    assert pagina.campo_senha.is_displayed()
    assert pagina.campo_confirmar_senha.is_displayed()


# --- TC-016 (RF-CAD-02) — Senha curta bloqueia cadastro ---------------------
def test_TC016_senha_curta_bloqueia(driver):
    pagina = CadastroPage(driver).abrir()
    pagina.cadastrar(
        nome="Teste Selenium",
        email="teste.senha.curta@example.com",
        senha="123",
        confirmar_senha="123",
    )
    assert pagina.mensagem == "A senha deve ter pelo menos 6 caracteres."


# --- TC-017 (RF-CAD-03) — Senhas diferentes bloqueiam cadastro --------------
def test_TC017_senhas_diferentes_bloqueiam(driver):
    pagina = CadastroPage(driver).abrir()
    pagina.cadastrar(
        nome="Teste Selenium",
        email="teste.senhas.diferentes@example.com",
        senha="123456",
        confirmar_senha="654321",
    )
    assert pagina.mensagem == "As senhas não coincidem."


# --- TC-018 (RF-CAD-04) — Cadastro com email duplicado é bloqueado ----------
def test_TC018_email_duplicado_bloqueia(driver):
    email_repetido = "duplicado@example.com"
    pagina = CadastroPage(driver).abrir()

    # "Planto" o usuário direto no localStorage antes de tentar cadastrar de
    # novo — mesma ideia do plantar_sessao (pages/auth_helpers.py), só que
    # pra lista de usuários em vez da sessão.
    driver.execute_script(
        "localStorage.setItem('buskmate_users', JSON.stringify("
        "[{nome:'Existente', email:arguments[0], senha:'123456'}]));",
        email_repetido,
    )

    pagina.cadastrar(
        nome="Outro Nome",
        email=email_repetido,
        senha="123456",
        confirmar_senha="123456",
    )
    assert pagina.mensagem == "Já existe uma conta com este email."


# --- TC-019 (RF-CAD-05 / RF-CAD-06) — Cadastro válido tem sucesso e redireciona
def test_TC019_cadastro_valido_redireciona(driver):
    pagina = CadastroPage(driver).abrir()
    pagina.cadastrar(
        nome="Usuario Valido",
        email="usuario.valido.selenium@example.com",
        senha="123456",
        confirmar_senha="123456",
    )
    assert pagina.mensagem == "Conta criada! Redirecionando para o login..."

    # O redirecionamento real só acontece depois de 1.2s (é o app.js que
    # define isso, não nós) — time.sleep aqui é a forma mais simples de
    # esperar isso acontecer (uma espera "cega"; WebDriverWait seria a
    # forma mais esperta, fica de exercício pra depois).
    time.sleep(1.5)
    assert driver.current_url.endswith("login.html")
