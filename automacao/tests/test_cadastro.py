# =============================================================================
# AULA 3 (lote 1/6) — Módulo Cadastro: os 5 casos de prioridade "Alta"
# =============================================================================
# Cada função de teste aqui corresponde a um caso do
# docs/BuskMate_QA_Plano_de_Testes.xlsx (aba "Casos de Teste"). Mantive o
# ID do caso (TC-xxx) e do requisito (RF-CAD-xx) no nome/docstring de cada
# teste — é assim que se mantém rastreabilidade entre o plano de testes e
# o código, coisa que interviewer de QA gosta de ver.
#
# Repare que NENHUM desses testes abre/fecha o navegador manualmente — eles
# só pedem "driver" como parâmetro, e o conftest.py cuida do resto (Aula 2).
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL
import time


def preencher_cadastro(driver, nome, email, senha, confirmar_senha):
    """Função auxiliar: preenche e envia o formulário de cadastro.

    Escrevi isso porque as 5 funções abaixo, de um jeito ou de outro, todas
    precisam "abrir a página de cadastro e preencher o formulário" — só muda
    O QUE cada uma preenche e o que espera ver depois. Repetir esse trecho
    5 vezes ia deixar o arquivo enorme e chato de manter; então virou uma
    função normal do Python (nada de especial do pytest aqui, diferente da
    fixture do conftest.py).
    """
    driver.get(f"{URL}cadastro.html")
    driver.find_element(By.ID, "nome").send_keys(nome)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "senha").send_keys(senha)
    driver.find_element(By.ID, "confirmar-senha").send_keys(confirmar_senha)
    driver.find_element(By.CSS_SELECTOR, "#form-cadastro button[type=submit]").click()


# --- TC-015 (RF-CAD-01) — Campos obrigatórios exibidos no cadastro ----------
def test_TC015_campos_visiveis(driver):
    driver.get(f"{URL}cadastro.html")
    assert driver.find_element(By.ID, "nome").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "senha").is_displayed()
    assert driver.find_element(By.ID, "confirmar-senha").is_displayed()


# --- TC-016 (RF-CAD-02) — Senha curta bloqueia cadastro ---------------------
def test_TC016_senha_curta_bloqueia(driver):
    preencher_cadastro(
        driver,
        nome="Teste Selenium",
        email="teste.senha.curta@example.com",
        senha="123",
        confirmar_senha="123",
    )
    mensagem = driver.find_element(By.ID, "form-message").text
    assert mensagem == "A senha deve ter pelo menos 6 caracteres."


# --- TC-017 (RF-CAD-03) — Senhas diferentes bloqueiam cadastro --------------
def test_TC017_senhas_diferentes_bloqueiam(driver):
    preencher_cadastro(
        driver,
        nome="Teste Selenium",
        email="teste.senhas.diferentes@example.com",
        senha="123456",
        confirmar_senha="654321",
    )
    mensagem = driver.find_element(By.ID, "form-message").text
    assert mensagem == "As senhas não coincidem."


# --- TC-018 (RF-CAD-04) — Cadastro com email duplicado é bloqueado ----------
def test_TC018_email_duplicado_bloqueia(driver):
    email_repetido = "duplicado@example.com"

    # Esse caso PRECISA que o e-mail já exista antes de tentar de novo.
    # Em vez de cadastrar de verdade duas vezes (mais lento, e o 2º cadastro
    # falharia antes mesmo de testar o que queremos), eu "planto" o usuário
    # direto no localStorage com uma linha de JavaScript. Isso já apareceu
    # antes, lá na execução manual (quando conferimos os dados salvos) —
    # aqui é a mesma ideia, só que dentro do teste automatizado.
    driver.get(f"{URL}cadastro.html")  # precisa estar numa página do site pra ter acesso ao localStorage dele
    driver.execute_script(
        "localStorage.setItem('buskmate_users', JSON.stringify("
        "[{nome:'Existente', email:arguments[0], senha:'123456'}]));",
        email_repetido,
    )

    preencher_cadastro(
        driver,
        nome="Outro Nome",
        email=email_repetido,
        senha="123456",
        confirmar_senha="123456",
    )
    mensagem = driver.find_element(By.ID, "form-message").text
    assert mensagem == "Já existe uma conta com este email."


# --- TC-019 (RF-CAD-05 / RF-CAD-06) — Cadastro válido tem sucesso e redireciona
def test_TC019_cadastro_valido_redireciona(driver):
    preencher_cadastro(
        driver,
        nome="Usuario Valido",
        email="usuario.valido.selenium@example.com",
        senha="123456",
        confirmar_senha="123456",
    )
    mensagem = driver.find_element(By.ID, "form-message").text
    assert mensagem == "Conta criada! Redirecionando para o login..."

    # O redirecionamento real só acontece depois de 1.2s (é o app.js que
    # define isso, não nós). "time.sleep" aqui é a forma MAIS SIMPLES de
    # esperar isso acontecer — mas é uma espera "cega" (sempre espera 1.5s,
    # rápido ou devagar). Existe uma forma mais esperta (WebDriverWait, que
    # espera só o necessário) — fica pra uma aula futura, quando isso
    # começar a incomodar de verdade.
    time.sleep(1.5)
    assert driver.current_url.endswith("login.html")

