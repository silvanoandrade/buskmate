# =============================================================================
# AULA 3 (lote 8/8, parte 2) — Módulo Não-funcional: os 3 casos de
# prioridade "Alta"
# =============================================================================
from conftest import URL


# --- TC-048 (RF-NF-01) — Site acessível publicamente ------------------------
def test_TC048_site_acessivel_publicamente(driver):
    driver.get(URL)
    assert "BuskMate" in driver.title


# --- TC-049 (RF-NF-02) — Layout responsivo em mobile ------------------------
def test_TC049_layout_responsivo_mobile(driver):
    """
    ATENÇÃO: esse teste tem boas chances de FALHAR — e está certo em falhar.
    Na execução manual (docs/execucao_resultados.md) esse mesmo caso já
    tinha sido reprovado: em telas de 375px o header não se adapta e o site
    ganha scroll horizontal. Automatizar esse caso não conserta o bug — só
    prova, de forma repetível, que ele continua lá. É uma automação boa de
    mostrar em entrevista justamente por isso: automação não serve só pra
    confirmar que tá tudo bem, serve (e principalmente) pra pegar quando
    algo está errado.
    """
    # Novidade: em vez de só encolher a JANELA do Chrome (que tem um
    # tamanho mínimo e não reflete um celular de verdade), mandamos um
    # comando direto pro Chrome DevTools Protocol (CDP) pedindo pra ele
    # EMULAR um dispositivo móvel de verdade — a mesma engrenagem por trás
    # do modo "Toggle device toolbar" do DevTools.
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 375,
        "height": 812,
        "deviceScaleFactor": 2,
        "mobile": True,
    })
    driver.get(URL)

    largura_janela = driver.execute_script("return window.innerWidth;")
    largura_conteudo = driver.execute_script("return document.documentElement.scrollWidth;")

    driver.execute_cdp_cmd("Emulation.clearDeviceMetricsOverride", {})

    assert largura_conteudo <= largura_janela, (
        f"scroll horizontal detectado: conteúdo tem {largura_conteudo}px, "
        f"janela emulada tem {largura_janela}px"
    )


# --- TC-050 (RF-NF-03) — Console sem erros ----------------------------------
def test_TC050_console_sem_erros(driver):
    driver.get(URL)

    # Novidade: get_log("browser") lê os logs que o Chrome registrou nessa
    # aba — os mesmos que aparecem na aba "Console" do DevTools. Só
    # funciona porque ativamos "goog:loggingPrefs" no conftest.py.
    logs = driver.get_log("browser")
    erros = [log for log in logs if log["level"] == "SEVERE"]

    assert erros == [], f"erro(s) de console encontrado(s): {erros}"

