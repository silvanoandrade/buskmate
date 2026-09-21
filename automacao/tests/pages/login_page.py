# =============================================================================
# AULA 4 — Page Object Model: LoginPage
# =============================================================================
from selenium.webdriver.common.by import By
from conftest import URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(f"{URL}login.html")
        return self

    @property
    def campo_email(self):
        return self.driver.find_element(By.ID, "email")

    @property
    def campo_senha(self):
        return self.driver.find_element(By.ID, "senha")

    @property
    def mensagem(self):
        return self.driver.find_element(By.ID, "form-message").text

    def fazer_login(self, email, senha):
        self.campo_email.send_keys(email)
        self.campo_senha.send_keys(senha)
        self.driver.find_element(By.CSS_SELECTOR, "#form-login button[type=submit]").click()

