# Automação de Testes — BuskMate (Python + Selenium)

![Testes](https://github.com/silvanoandrade/buskmate/actions/workflows/selenium-tests.yml/badge.svg)

Esta pasta é a suíte de testes automatizados do BuskMate, construída aos
poucos, aula por aula, para servir tanto como suíte de regressão real quanto
como peça de portfólio.

## Estrutura

```
automacao/
├── requirements.txt
├── README_AUTOMACAO.md
└── tests/
    ├── conftest.py              # fixture "driver" (Aula 2)
    ├── pages/                   # Page Object Model (Aula 4)
    │   ├── navbar.py            # cabeçalho, comum a todas as páginas
    │   ├── cadastro_page.py
    │   ├── login_page.py
    │   ├── mapa_page.py         # mapa, painel do spot, avaliação
    │   └── auth_helpers.py      # plantar_sessao (usado por 3 arquivos)
    ├── test_00_hello_selenium.py   # Aula 1
    ├── test_cadastro.py            # Aula 3 — TC-015 a TC-019
    ├── test_login.py               # Aula 3 — TC-021 a TC-023
    ├── test_sessao.py              # Aula 3 — TC-025, TC-026
    ├── test_navegacao.py           # Aula 3 — TC-001
    ├── test_internacionalizacao.py # Aula 3 — TC-005 a TC-014 (+ Aula 5)
    ├── test_mapa.py                # Aula 3 — TC-029 a TC-035
    ├── test_avaliacao.py           # Aula 3 — TC-038 a TC-042
    ├── test_persistencia.py        # Aula 3 — TC-045
    └── test_nao_funcional.py       # Aula 3 — TC-048 a TC-050 (+ Aula 7)
```

## Como rodar

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests/ -v
```

Pra gerar o relatório HTML (Aula 6) pra mostrar em entrevista:

```bash
python3 -m pytest tests/ -v --html=relatorio.html --self-contained-html
```

(`--self-contained-html` embute o CSS/JS no próprio arquivo — dá pra abrir
`relatorio.html` direto no navegador, sem depender de mais nada.)

(`test_00_hello_selenium.py` ainda roda sozinho com `python3 tests/test_00_hello_selenium.py`
se quiser revisar a Aula 1; os demais arquivos já usam pytest + a fixture do
`conftest.py`, então rodam com `pytest`.)

No seu Mac, o Selenium (a partir da versão 4.6) baixa sozinho o driver do
Chrome certo na primeira execução — não precisa instalar nada manualmente.
(Se aparecer um erro de driver, veja a seção "Nota técnica" abaixo.)

## Plano de aulas

- [x] **Aula 1 — Hello Selenium** (`test_00_hello_selenium.py`): as 5 peças
  básicas de um teste Selenium — Options, Service/driver, find_element,
  assert, e por que sempre fechar o navegador no `finally`.
- [x] **Aula 2 — De script pra teste de verdade** (`conftest.py`): reescrito
  usando `pytest` e uma *fixture* (`driver`) que abre/fecha o navegador
  automaticamente pra cada teste — inclusive se o teste falhar no meio.
- [x] **Aula 3 — Os 30 casos de prioridade "Alta"** ✅ 30/30: automatizados
  todos os casos marcados "Alta" no `BuskMate_QA_Plano_de_Testes.xlsx`, em 9
  módulos — Cadastro (5), Login (3), Sessão (2), Navegação (1),
  Internacionalização (5), Mapa (6), Avaliação (4), Persistência de Dados
  (1) e Não-funcional (3).
- [x] **Aula 4 — Page Object Model**: código reorganizado em `pages/` —
  `Navbar`, `CadastroPage`, `LoginPage`, `MapaPage` — pra parar de repetir
  seletor CSS espalhado pelos testes. É assim que suítes de verdade em
  empresas ficam organizadas: o teste descreve O QUE checar, a página
  descreve COMO encontrar cada elemento.
- [x] **Aula 5 — Parametrização**: os testes de tradução da home (antes
  TC-006 e TC-007, quase idênticos) viraram 1 função só com
  `@pytest.mark.parametrize` — mesma lógica, dados diferentes.
- [x] **Aula 6 — Relatório visual**: `pytest-html` no `requirements.txt` —
  comando de geração documentado acima em "Como rodar".
- [x] **Aula 7 — CI**: workflow do GitHub Actions
  (`.github/workflows/selenium-tests.yml`) roda a suíte inteira a cada
  `git push`/pull request — o selo lá em cima reflete o resultado da última
  execução. O TC-049 (bug de layout responsivo já conhecido, ver
  `docs/execucao_resultados.md`) usa `@pytest.mark.xfail`: o pytest ainda
  roda esse teste e avisa se ele falhar, mas isso não derruba o CI — é
  assim que se documenta um bug conhecido sem deixar o pipeline vermelho
  por algo que já está mapeado.

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
