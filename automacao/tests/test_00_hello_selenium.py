# =============================================================================
# AULA 1 — "Hello Selenium"
# =============================================================================
# Objetivo desta aula: entender as 5 peças básicas de QUALQUER teste Selenium,
# sem pytest, sem Page Object, sem nada além do essencial. Depois que isso
# fizer sentido, a gente vai empacotando em coisas mais organizadas.
#
# As 5 peças são:
#   1. Options   -> como o navegador deve se comportar (headless? tamanho?)
#   2. Service    -> qual "driver" (executável) vai controlar o Chrome
#   3. webdriver  -> a conexão viva com o navegador (é o seu "controle remoto")
#   4. find_element(By.X, "valor") -> como você acha um elemento na página
#   5. assert     -> como você afirma "isso TEM que ser verdade", senão falha
#
# COMO RODAR (no seu terminal, dentro da pasta automacao/):
#   python3 -m pip install -r requirements.txt
#   python3 tests/test_00_hello_selenium.py
#
# No SEU Mac, você não vai precisar do "chromedriver-py" que eu usei aqui no
# meu ambiente de nuvem — expliquei o porquê no README_AUTOMACAO.md. No seu
# PyCharm, o Selenium 4.6+ já baixa sozinho o driver certo na primeira vez
# que você rodar (é o "Selenium Manager", automático).
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# URL do site. Por padrão apontamos pro site publicado no GitHub Pages.
# (Se um dia você precisar testar uma versão local antes de subir pro ar,
# troque essa linha pra "http://localhost:8899" — foi assim que eu testei
# esse script aqui do meu lado, porque meu ambiente de nuvem não tem acesso
# livre à internet, só ao GitHub. No seu Mac isso não é um problema: pode
# deixar apontado pro site publicado mesmo.)
URL = "https://silvanoandrade.github.io/buskmate/"


def test_titulo_da_home():
    # --- 1. Options: como o Chrome deve se comportar --------------------
    # "headless" = sem interface gráfica visível (mais rápido, ótimo pra
    # rodar em CI/servidor). Enquanto você está aprendendo, é ÓTIMO comentar
    # essa linha uma vez pra VER o navegador abrindo e clicando sozinho —
    # isso ajuda muito a entender o que está acontecendo.
    options = Options()
    options.add_argument("--headless=new")   # comente esta linha pra "ver" o teste rodando
    options.add_argument("--window-size=1280,900")

    # --- 2 e 3. Service + webdriver: abre o navegador de verdade --------
    # No seu Mac isso é só `driver = webdriver.Chrome(options=options)`.
    driver = webdriver.Chrome(options=options)

    try:
        # --- Ação: navegar até a página ----------------------------------
        driver.get(URL)

        # --- 4. find_element: achando elementos na página ----------------
        # "By" é o TIPO de localizador. Os mais comuns:
        #   By.TAG_NAME     -> pelo nome da tag html (ex: "h1")
        #   By.CSS_SELECTOR -> por seletor CSS (ex: ".btn-nav", "#id")
        #   By.LINK_TEXT    -> pelo texto exato de um link
        #   By.XPATH        -> o mais poderoso e o mais verboso
        titulo_h1 = driver.find_element(By.TAG_NAME, "h1")
        link_cadastrar = driver.find_element(By.LINK_TEXT, "Cadastrar")

        # --- 5. assert: a afirmação que faz o teste falhar se for mentira -
        # Repare: eu NÃO travei o texto inteiro do h1 (frases mudam fácil).
        # Testei uma PARTE estável do texto — é mais resistente a pequenas
        # edições de copywriting no site.
        assert "spot" in titulo_h1.text.lower(), (
            f"Esperava a palavra 'spot' no H1, mas veio: {titulo_h1.text!r}"
        )
        assert link_cadastrar.is_displayed()
        assert driver.title.startswith("BuskMate")

        print("✅ passou: home carrega com H1 e link Cadastrar visíveis")

    finally:
        # --- SEMPRE feche o navegador, mesmo se um assert falhar acima ---
        # É por isso que essa parte fica num "finally": senão, cada teste
        # que falha deixa um processo de Chrome "fantasma" aberto.
        driver.quit()


if __name__ == "__main__":
    # Isso permite rodar o arquivo direto com "python3 test_00_hello_selenium.py"
    # sem precisar do pytest ainda — só pra essa primeira aula.
    test_titulo_da_home()

