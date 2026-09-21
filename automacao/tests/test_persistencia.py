# =============================================================================
# AULA 3 (lote 8/8, parte 1) — Módulo Persistência de Dados: o caso de
# prioridade "Alta"
# =============================================================================
# Novidade: driver.refresh() recarrega a página ATUAL (igual apertar F5) —
# diferente de driver.get(), que troca de URL. Como o localStorage pertence
# ao DOMÍNIO (não à página), os dados plantados devem continuar lá depois
# do reload — é exatamente isso que este teste prova.
# =============================================================================

from selenium.webdriver.common.by import By
from conftest import URL
import json


# --- TC-045 (RF-PERSIST-01) — Dados persistem após reload ------------------
def test_TC045_dados_persistem_apos_reload(driver):
    driver.get(f"{URL}mapa.html")

    sessao = json.dumps({"nome": "Maria Teste", "email": "maria.teste@example.com"})
    avaliacoes = json.dumps({
        "aliados": [{"autor": "Maria", "nota": 5, "comentario": "Top!", "data": "2026-01-01T10:00:00.000Z"}]
    })
    driver.execute_script("localStorage.setItem('buskmate_session', arguments[0]);", sessao)
    driver.execute_script("localStorage.setItem('buskmate_reviews', arguments[0]);", avaliacoes)

    driver.refresh()

    nav_user = driver.find_element(By.ID, "nav-user")
    assert "Maria" in nav_user.text

    marcadores = driver.find_elements(By.CSS_SELECTOR, ".leaflet-marker-icon")
    marcadores[1].click()  # Praça dos Aliados
    texto_painel = driver.find_element(By.ID, "spot-content").text
    assert "5.0" in texto_painel
    assert "1 avaliações" in texto_painel

