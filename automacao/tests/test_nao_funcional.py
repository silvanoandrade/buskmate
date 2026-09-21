import pytest
from conftest import URL


def test_TC048_site_acessivel_publicamente(driver):
    driver.get(URL)
    assert "BuskMate" in driver.title


@pytest.mark.xfail(reason="Bug conhecido: header não é responsivo em telas <768px (ver docs/execucao_resultados.md)")
def test_TC049_layout_responsivo_mobile(driver):
    """Automatizar esse caso não conserta o bug — só prova, de forma
    repetível, que ele continua lá. Enquanto o bug não for corrigido, esse
    teste falha de propósito — por isso o @pytest.mark.xfail acima: ele diz
    pro pytest "eu sei que esse teste falha, não conte isso como uma
    regressão nova". Quando o bug for corrigido, esse teste vai passar, e
    o pytest vai avisar isso como "XPASS" (um sinal pra gente remover o
    xfail).
    """
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": 375, "height": 812, "deviceScaleFactor": 2, "mobile": True,
    })
    driver.get(URL)
    largura_janela = driver.execute_script("return window.innerWidth;")
    largura_conteudo = driver.execute_script("return document.documentElement.scrollWidth;")
    driver.execute_cdp_cmd("Emulation.clearDeviceMetricsOverride", {})
    assert largura_conteudo <= largura_janela, (
        f"conteúdo ({largura_conteudo}px) estoura a largura da tela "
        f"({largura_janela}px) — scroll horizontal indevido"
    )


def test_TC050_console_sem_erros(driver):
    driver.get(URL)
    logs = driver.get_log("browser")
    erros = [log for log in logs if log["level"] == "SEVERE"]
    assert erros == [], f"erro(s) de console encontrado(s): {erros}"
