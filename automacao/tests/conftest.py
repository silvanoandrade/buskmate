# =============================================================================
# AULA 2 — conftest.py e a fixture "driver"
# =============================================================================
# "conftest.py" é um nome especial: o pytest carrega esse arquivo sozinho,
# sem ninguém precisar dar import, e todo teste na pasta "tests/" passa a
# enxergar as fixtures definidas aqui.
#
# Uma fixture é uma função marcada com @pytest.fixture. A palavra "yield"
# é o pulo do gato: tudo ANTES do yield roda como preparação (setup), e tudo
# DEPOIS do yield roda como limpeza (teardown) — e o pytest garante que a
# parte de limpeza roda mesmo se o teste falhar no meio. É basicamente um
# "try/finally" automático, entregue pronto pro seu teste usar.
# =============================================================================

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL do site publicado. Fica aqui, num lugar só, pra todos os testes
# importarem — em vez de cada arquivo de teste repetir essa string.
URL = "https://silvanoandrade.github.io/buskmate/"


@pytest.fixture
def driver():
    # --- SETUP: tudo isso roda ANTES do teste que pediu "driver" começar ---
    options = Options()
    options.add_argument("--headless=new")   # comente pra ver o Chrome abrindo
    options.add_argument("--window-size=1280,900")

    # NOVO (Aula 7 — CI): flags padrão pra rodar o Chrome numa máquina
    # de CI (GitHub Actions) sem problemas de permissão/memória
    # compartilhada. Não atrapalham em nada rodando local — por isso
    # ficam sempre ligadas, aqui e lá.
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # NOVO: pede pro Chrome guardar os logs do console (os mesmos que
    # aparecem no DevTools, aba "Console") pra gente poder ler depois com
    # driver.get_log("browser"). Sem isso, get_log sempre volta vazio.
    # É o TC-050 (módulo Não-funcional) que usa isso pra checar que o
    # site não solta nenhum erro de JavaScript.
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    navegador = webdriver.Chrome(options=options)

    # --- ENTREGA: o teste recebe "navegador" aqui, roda o corpo dele ---
    yield navegador

    # --- TEARDOWN: roda DEPOIS do teste terminar, falhando ou não ---
    navegador.quit()
