# =============================================================================
# AULA 4 — Page Object Model: Navbar
# =============================================================================
# Isso é o Page Object Model: em vez de cada teste escrever os seletores
# (By.ID, By.CSS_SELECTOR...) direto no corpo do teste, a gente concentra
# esses seletores em CLASSES que representam pedaços da tela — aqui, o
# cabeçalho, que é igual em index.html, login.html, cadastro.html e
# mapa.html. Se o site mudar um id ou uma classe algum dia, conserta em 1
# lugar só (aqui), não em 9 arquivos de teste espalhados.
#
# Repare que os métodos têm nome de AÇÃO em português (trocar_idioma,
# fazer_logout...) — quem lê o teste não precisa saber COMO a troca de
# idioma funciona (2 cliques, seletor CSS de atributo...), só que ela
# troca o idioma. Esconder o "como" e expor só o "o quê" é o objetivo do
# Page Object.
# =============================================================================

from selenium.webdriver.common.by import By


class Navbar:
    def __init__(self, driver):
        self.driver = driver

    @property
    def logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.logo")

    def link(self, href):
        """Um dos links do menu (mapa.html, login.html ou cadastro.html)."""
        return self.driver.find_element(By.CSS_SELECTOR, f"a[href='{href}']")

    @property
    def lang_toggle(self):
        return self.driver.find_element(By.ID, "lang-toggle")

    def trocar_idioma(self, lang):
        """Abre o menu de idiomas e clica na opção pedida ('pt', 'en' ou 'es')."""
        self.lang_toggle.click()
        opcao = self.driver.find_element(By.CSS_SELECTOR, f"li.lang-option[data-lang='{lang}']")
        # NOVO: clique via JavaScript em vez de opcao.click() direto. Quando
        # o painel do spot está aberto (TC-014), ele às vezes fica por cima
        # do dropdown de idiomas — o Selenium então recusa o clique "de
        # verdade" (ElementClickInterceptedException), mesmo a opção estando
        # visível e clicável pra um usuário real. O clique via JS dispara o
        # evento diretamente no elemento, sem checar o que está por cima.
        self.driver.execute_script("arguments[0].click();", opcao)

    def opcoes_de_idioma(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "li.lang-option")

    @property
    def nav_user(self):
        """Só existe em mapa.html (as outras páginas não têm essa saudação)."""
        return self.driver.find_element(By.ID, "nav-user")

    @property
    def nav_login(self):
        return self.driver.find_element(By.ID, "nav-login")

    @property
    def nav_cadastro(self):
        return self.driver.find_element(By.ID, "nav-cadastro")

    def fazer_logout(self):
        self.driver.find_element(By.ID, "logout-link").click()
