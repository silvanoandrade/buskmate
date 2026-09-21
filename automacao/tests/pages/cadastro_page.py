# =============================================================================
# AULA 4 — Page Object Model: CadastroPage
# =============================================================================
from selenium.webdriver.common.by import By
from conftest import URL


class CadastroPage:
    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(f"{URL}cadastro.html")
        return self

    @property
    def campo_nome(self):
        return self.driver.find_element(By.ID, "nome")

    @property
    def campo_email(self):
        return self.driver.find_element(By.ID, "email")

    @property
    def campo_senha(self):
        return self.driver.find_element(By.ID, "senha")

    @property
    def campo_confirmar_senha(self):
        return self.driver.find_element(By.ID, "confirmar-senha")

    @property
    def mensagem(self):
        return self.driver.find_element(By.ID, "form-message").text

    def cadastrar(self, nome, email, senha, confirmar_senha):
        """Preenche e envia o formulário de cadastro."""
        self.campo_nome.send_keys(nome)
        self.campo_email.send_keys(email)
        self.campo_senha.send_keys(senha)
        self.campo_confirmar_senha.send_keys(confirmar_senha)
        self.driver.find_element(By.CSS_SELECTOR, "#form-cadastro button[type=submit]").click()
