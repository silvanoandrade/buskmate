# Automação de Testes — BuskMate (Python + Selenium)

Esta pasta é o começo da suíte de testes automatizados do BuskMate, construída
aos poucos, aula por aula, para servir tanto como suíte de regressão real
quanto como peça de portfólio.

## Como rodar

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests/ -v
```

(`test_00_hello_selenium.py` ainda roda sozinho com `python3 tests/test_00_hello_selenium.py`
se quiser revisar a Aula 1; os demais arquivos já usam pytest + a fixture do
`conftest.py`, então rodam com `pytest`.)

No seu Mac, o Selenium (a partir da versão 4.6) baixa sozinho o driver do
Chrome certo na primeira execução — não precisa instalar nada manualmente.
(Se aparecer um erro de driver, veja a seção "Nota técnica" abaixo.)

## Plano de aulas (o que já foi feito e o que vem a seguir)

- [x] **Aula 1 — Hello Selenium** (`test_00_hello_selenium.py`): as 5 peças
  básicas de um teste Selenium — Options, Service/driver, find_element,
  assert, e por que sempre fechar o navegador no `finally`.
- [x] **Aula 2 — De script pra teste de verdade** (`conftest.py`): reescrito
  usando `pytest` e uma *fixture* (`driver`) que abre/fecha o navegador
  automaticamente pra cada teste — inclusive se o teste falhar no meio.
- [ ] **Aula 3 — Os 30 casos de prioridade "Alta"**: automatizar, módulo por
  módulo, os casos marcados "Alta" no `BuskMate_QA_Plano_de_Testes.xlsx`.
  Progresso:
  - [x] Cadastro — TC-015 a TC-019 (`test_cadastro.py`) ✅ 5/5
  - [ ] Login — TC-021, TC-022, TC-023 (3 casos)
  - [ ] Sessão — TC-025, TC-026 (2 casos)
  - [ ] Navegação — TC-001 (1 caso)
  - [ ] Internacionalização — TC-005, TC-006, TC-007, TC-008, TC-014 (5 casos)
  - [ ] Mapa — TC-029, TC-030, TC-032, TC-033, TC-034, TC-035 (6 casos)
  - [ ] Avaliação — TC-038, TC-039, TC-041, TC-042 (4 casos)
  - [ ] Persistência de Dados — TC-045 (1 caso)
  - [ ] Não-funcional — TC-048, TC-049, TC-050 (3 casos)
- [ ] **Aula 4 — Page Object Model**: organizar o código por página
  (`LoginPage`, `CadastroPage`, `MapaPage`) pra parar de repetir seletores CSS
  espalhados pelos testes — é assim que suítes de verdade em empresas ficam
  organizadas.
- [ ] **Aula 5 — Dados e parametrização**: rodar o mesmo teste com várias
  entradas diferentes (`@pytest.mark.parametrize`) — por exemplo, todos os
  casos de senha inválida de uma vez só.
- [ ] **Aula 6 — Relatório visual**: gerar um relatório HTML (`pytest-html`)
  bonito pra mostrar em entrevista.
- [ ] **Aula 7 (opcional) — CI**: rodar a suíte automaticamente a cada `git
  push`, via GitHub Actions — isso é o que mais impressiona em entrevista,
  porque mostra testes rodando sozinhos, sem ninguém precisar lembrar de
  rodar manualmente.

## Nota técnica: por que existe uma decisão de "local vs. ao vivo"

Os testes apontam por padrão para o site publicado
(`https://silvanoandrade.github.io/buskmate/`). Ao desenvolver esse primeiro
script, eu estava rodando num ambiente de nuvem com acesso à internet restrito
por política da organização (só consegue alcançar o GitHub, não sites
publicados como GitHub Pages em geral) — por isso, pra testar e confirmar que
o código realmente funcionava antes de te entregar, cloneiquei o repositório e
servi localmente com `python3 -m http.server`, e testei contra
`http://localhost`. É uma prática real de QA/automação, aliás: muitas
empresas rodam a suíte de testes contra uma versão local ou de *staging*
antes de rodar contra produção, justamente pra não depender do site estar no
ar. No seu Mac isso não é necessário — o site publicado é público e acessível
normalmente.

