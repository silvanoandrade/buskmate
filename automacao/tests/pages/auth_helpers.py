# =============================================================================
# AULA 4 — helper compartilhado: plantar sessão via localStorage
# =============================================================================
# Antes esse mesmo trecho estava duplicado em test_sessao.py, test_avaliacao.py
# e test_persistencia.py. Virou uma função só, reaproveitada pelos 3 — outra
# vantagem prática de organizar o código em módulos.
# =============================================================================

import json


def plantar_sessao(driver, nome="Maria Teste", email="maria.teste@example.com"):
    """Loga o usuário 'na marra', escrevendo direto a chave que o auth.js
    espera encontrar no localStorage — sem passar pelo formulário de login.
    Precisa estar numa página do site primeiro (localStorage é por domínio).
    """
    sessao = json.dumps({"nome": nome, "email": email})
    driver.execute_script("localStorage.setItem('buskmate_session', arguments[0]);", sessao)
