# Casos de Teste Manuais — BuskMate

Casos de teste manuais do frontend do BuskMate, um ou mais por requisito do [Plano de Requisitos](../BuskMate_Plano_de_Requisitos.pdf). Cada caso referencia o ID do requisito que cobre (ex.: `RF-CAD-02`), garantindo rastreabilidade completa.

> Esta é a versão em Markdown, para consulta rápida direto no navegador. A planilha `.xlsx` completa (com filtros, coluna de status editável e fórmulas de resumo) está disponível separadamente com o time de QA.

**Total:** 54 casos de teste · **Site:** https://silvanoandrade.github.io/buskmate/

## Índice

| Módulo | Casos | Prioridade Alta |
|---|---|---|
| [Navegação](#navegação) | 4 | 1 |
| [Internacionalização](#internacionalização) | 10 | 5 |
| [Cadastro](#cadastro) | 6 | 5 |
| [Login](#login) | 4 | 3 |
| [Sessão](#sessão) | 4 | 2 |
| [Mapa](#mapa) | 9 | 6 |
| [Avaliação](#avaliação) | 7 | 4 |
| [Persistência de Dados](#persistência-de-dados) | 3 | 1 |
| [Não-funcional](#não-funcional) | 7 | 3 |

<details>
<summary><b>Ver lista completa (54 casos)</b></summary>

| ID | Requisito | Título | Prioridade |
|---|---|---|---|
| [TC-001](#tc-001-header-completo-em-todas-as-páginas) | RF-NAV-01 | Header completo em todas as páginas | 🔴 Alta |
| [TC-002](#tc-002-logo-redireciona-para-a-home) | RF-NAV-02 | Logo redireciona para a home | 🟡 Média |
| [TC-003](#tc-003-link-mapa-destacado-na-página-do-mapa) | RF-NAV-03 | Link "Mapa" destacado na página do mapa | 🟢 Baixa |
| [TC-004](#tc-004-footer-presente-em-todas-as-páginas) | RF-NAV-04 | Footer presente em todas as páginas | 🟢 Baixa |
| [TC-005](#tc-005-seletor-mostra-as-3-opções-de-idioma) | RF-I18N-01 | Seletor mostra as 3 opções de idioma | 🔴 Alta |
| [TC-006](#tc-006-troca-para-inglês-traduz-a-home) | RF-I18N-02 | Troca para inglês traduz a home | 🔴 Alta |
| [TC-007](#tc-007-troca-para-espanhol-traduz-a-home) | RF-I18N-02 | Troca para espanhol traduz a home | 🔴 Alta |
| [TC-008](#tc-008-idioma-persiste-ao-navegar-entre-páginas) | RF-I18N-03 | Idioma persiste ao navegar entre páginas | 🔴 Alta |
| [TC-009](#tc-009-idioma-persiste-após-fechar-e-reabrir-o-navegador) | RF-I18N-04 | Idioma persiste após fechar e reabrir o navegador | 🟡 Média |
| [TC-010](#tc-010-painel-do-spot-é-retraduzido-sem-fechar) | RF-I18N-05 | Painel do spot é retraduzido sem fechar | 🟡 Média |
| [TC-011](#tc-011-saudação-do-usuário-é-retraduzida) | RF-I18N-06 | Saudação do usuário é retraduzida | 🟡 Média |
| [TC-012](#tc-012-idioma-padrão-é-português-na-primeira-visita) | RF-I18N-07 | Idioma padrão é Português na primeira visita | 🟡 Média |
| [TC-013](#tc-013-clicar-fora-fecha-o-menu-de-idiomas) | RF-I18N-08 | Clicar fora fecha o menu de idiomas | 🟢 Baixa |
| [TC-014](#tc-014-descrição-do-spot-muda-conforme-idioma) | RF-I18N-09 | Descrição do spot muda conforme idioma | 🔴 Alta |
| [TC-015](#tc-015-campos-obrigatórios-exibidos-no-cadastro) | RF-CAD-01 | Campos obrigatórios exibidos no cadastro | 🔴 Alta |
| [TC-016](#tc-016-senha-curta-bloqueia-cadastro) | RF-CAD-02 | Senha curta bloqueia cadastro | 🔴 Alta |
| [TC-017](#tc-017-senhas-diferentes-bloqueiam-cadastro) | RF-CAD-03 | Senhas diferentes bloqueiam cadastro | 🔴 Alta |
| [TC-018](#tc-018-cadastro-com-email-duplicado-é-bloqueado) | RF-CAD-04 | Cadastro com email duplicado é bloqueado | 🔴 Alta |
| [TC-019](#tc-019-cadastro-válido-tem-sucesso-e-redireciona) | RF-CAD-05 / RF-CAD-06 | Cadastro válido tem sucesso e redireciona | 🔴 Alta |
| [TC-020](#tc-020-envio-com-campos-vazios-é-bloqueado-pelo-navegador) | RF-CAD-07 | Envio com campos vazios é bloqueado pelo navegador | 🟡 Média |
| [TC-021](#tc-021-campos-obrigatórios-exibidos-no-login) | RF-LOG-01 | Campos obrigatórios exibidos no login | 🔴 Alta |
| [TC-022](#tc-022-login-com-credenciais-inválidas-é-bloqueado) | RF-LOG-02 | Login com credenciais inválidas é bloqueado | 🔴 Alta |
| [TC-023](#tc-023-login-válido-cria-sessão-e-redireciona) | RF-LOG-03 | Login válido cria sessão e redireciona | 🔴 Alta |
| [TC-024](#tc-024-envio-com-campos-vazios-é-bloqueado) | RF-LOG-04 | Envio com campos vazios é bloqueado | 🟡 Média |
| [TC-025](#tc-025-navbar-mostra-saudação-quando-logado) | RF-SESS-01 | Navbar mostra saudação quando logado | 🔴 Alta |
| [TC-026](#tc-026-sair-encerra-a-sessão) | RF-SESS-02 | "Sair" encerra a sessão | 🔴 Alta |
| [TC-027](#tc-027-sessão-persiste-ao-recarregar) | RF-SESS-03 | Sessão persiste ao recarregar | 🟡 Média |
| [TC-028](#tc-028-visitante-deslogado-não-vê-saudação) | RF-SESS-04 | Visitante deslogado não vê saudação | 🟡 Média |
| [TC-029](#tc-029-mapa-carrega-centrado-no-porto) | RF-MAPA-01 | Mapa carrega centrado no Porto | 🔴 Alta |
| [TC-030](#tc-030-mapa-exibe-os-10-marcadores) | RF-MAPA-02 | Mapa exibe os 10 marcadores | 🔴 Alta |
| [TC-031](#tc-031-tooltip-exibe-nome-do-spot) | RF-MAPA-03 | Tooltip exibe nome do spot | 🟢 Baixa |
| [TC-032](#tc-032-clique-no-marcador-abre-o-painel) | RF-MAPA-04 | Clique no marcador abre o painel | 🔴 Alta |
| [TC-033](#tc-033-painel-exibe-ainda-sem-avaliações-quando-aplicável) | RF-MAPA-05 | Painel exibe "Ainda sem avaliações" quando aplicável | 🔴 Alta |
| [TC-034](#tc-034-painel-exibe-média-e-contagem-quando-há-avaliações) | RF-MAPA-05 | Painel exibe média e contagem quando há avaliações | 🔴 Alta |
| [TC-035](#tc-035-painel-exibe-descrição-e-melhor-horário) | RF-MAPA-06 | Painel exibe descrição e melhor horário | 🔴 Alta |
| [TC-036](#tc-036-botão--fecha-o-painel) | RF-MAPA-07 | Botão × fecha o painel | 🟡 Média |
| [TC-037](#tc-037-zoom-inout-funciona) | RF-MAPA-08 | Zoom in/out funciona | 🟢 Baixa |
| [TC-038](#tc-038-formulário-de-avaliação-visível-quando-logado) | RF-AVAL-01 | Formulário de avaliação visível quando logado | 🔴 Alta |
| [TC-039](#tc-039-prompt-de-login-exibido-quando-deslogado) | RF-AVAL-02 | Prompt de login exibido quando deslogado | 🔴 Alta |
| [TC-040](#tc-040-seleção-de-estrelas-preenche-visualmente) | RF-AVAL-03 | Seleção de estrelas preenche visualmente | 🟡 Média |
| [TC-041](#tc-041-envio-sem-estrelas-selecionadas-é-bloqueado) | RF-AVAL-04 | Envio sem estrelas selecionadas é bloqueado | 🔴 Alta |
| [TC-042](#tc-042-avaliação-enviada-atualiza-lista-e-média) | RF-AVAL-05 / RF-AVAL-06 | Avaliação enviada atualiza lista e média | 🔴 Alta |
| [TC-043](#tc-043-avaliação-sem-comentário-é-aceita) | RF-AVAL-07 | Avaliação sem comentário é aceita | 🟢 Baixa |
| [TC-044](#tc-044-comentários-exibidos-mais-recente-primeiro) | RF-AVAL-08 | Comentários exibidos mais recente primeiro | 🟡 Média |
| [TC-045](#tc-045-dados-persistem-após-reload) | RF-DATA-01 | Dados persistem após reload | 🔴 Alta |
| [TC-046](#tc-046-dados-não-aparecem-em-outro-navegador) | RF-DATA-02 | Dados não aparecem em outro navegador | 🟡 Média |
| [TC-047](#tc-047-limpar-localstorage-reseta-o-app) | RF-DATA-03 | Limpar localStorage reseta o app | 🟢 Baixa |
| [TC-048](#tc-048-site-acessível-publicamente) | RNF-01 | Site acessível publicamente | 🔴 Alta |
| [TC-049](#tc-049-layout-responsivo-em-mobile) | RNF-02 | Layout responsivo em mobile | 🔴 Alta |
| [TC-050](#tc-050-console-sem-erros) | RNF-03 | Console sem erros | 🔴 Alta |
| [TC-051](#tc-051-compatibilidade-entre-navegadores) | RNF-04 | Compatibilidade entre navegadores | 🟡 Média |
| [TC-052](#tc-052-tempo-de-carregamento-aceitável) | RNF-05 | Tempo de carregamento aceitável | 🟢 Baixa |
| [TC-053](#tc-053-navegação-por-teclado) | RNF-06 | Navegação por teclado | 🟡 Média |
| [TC-054](#tc-054-imagens-possuem-texto-alternativo) | RNF-07 | Imagens possuem texto alternativo | 🟢 Baixa |

</details>

---

## Navegação

_4 caso(s) de teste._

### TC-001: Header completo em todas as páginas

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-NAV-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir index.html
1. Abrir login.html
1. Abrir cadastro.html
1. Abrir mapa.html

**Resultado esperado:** Em todas as páginas o header mostra logo, links Mapa/Login/Cadastrar e o seletor de idioma

### TC-002: Logo redireciona para a home

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-NAV-02` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Estar em qualquer página que não seja index

**Passos:**

1. Clicar no logo BuskMate no header

**Resultado esperado:** É redirecionado para index.html

### TC-003: Link "Mapa" destacado na página do mapa

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-NAV-03` | 🎨 UI | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Estar em mapa.html

**Passos:**

1. Abrir mapa.html e observar o link "Mapa" no header

**Resultado esperado:** O link "Mapa" aparece com estilo diferenciado (ativo) em relação aos demais links

### TC-004: Footer presente em todas as páginas

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-NAV-04` | 🎨 UI | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir cada uma das 4 páginas e rolar até o rodapé

**Resultado esperado:** O texto "BuskMate Beta" aparece no rodapé de todas as páginas

---

## Internacionalização

_10 caso(s) de teste._

### TC-005: Seletor mostra as 3 opções de idioma

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Clicar no botão de idioma (🌐) no header

**Resultado esperado:** Menu abre mostrando Português 🇵🇹, English 🇬🇧 e Español 🇪🇸

### TC-006: Troca para inglês traduz a home

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-02` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em index.html

**Passos:**

1. Abrir seletor de idioma
1. Clicar em English

**Resultado esperado:** Título, textos, botões e menu mudam para inglês instantaneamente, sem reload da página

### TC-007: Troca para espanhol traduz a home

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-02` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em index.html

**Passos:**

1. Abrir seletor de idioma
1. Clicar em Español

**Resultado esperado:** Título, textos, botões e menu mudam para espanhol instantaneamente

### TC-008: Idioma persiste ao navegar entre páginas

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-03` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Idioma alterado para English na home

**Passos:**

1. Selecionar English na home
1. Clicar no link Mapa

**Resultado esperado:** A página do mapa carrega já em inglês

### TC-009: Idioma persiste após fechar e reabrir o navegador

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-04` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Idioma alterado para Español

**Passos:**

1. Selecionar Español
1. Fechar a aba/navegador
1. Reabrir o site

**Resultado esperado:** O site abre em espanhol

### TC-010: Painel do spot é retraduzido sem fechar

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-05` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Estar logado, com painel de um spot aberto em Português

**Passos:**

1. Com o painel aberto, trocar idioma para English

**Resultado esperado:** O conteúdo do painel (descrição, horário, textos) muda para inglês sem o painel fechar

### TC-011: Saudação do usuário é retraduzida

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-06` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Estar logado no mapa, idioma em Português ("Olá, Nome")

**Passos:**

1. Trocar idioma para English

**Resultado esperado:** Saudação muda para "Hi, Nome"

### TC-012: Idioma padrão é Português na primeira visita

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-07` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Navegador/localStorage limpo (sem idioma salvo)

**Passos:**

1. Abrir o site pela primeira vez

**Resultado esperado:** Todo o conteúdo aparece em Português e o seletor mostra "PT"

### TC-013: Clicar fora fecha o menu de idiomas

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-08` | 🎨 UI | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Menu de idiomas aberto

**Passos:**

1. Abrir o menu de idiomas
1. Clicar em qualquer área fora do menu

**Resultado esperado:** O menu se fecha

### TC-014: Descrição do spot muda conforme idioma

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-I18N-09` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Painel de um spot aberto

**Passos:**

1. Abrir painel do spot "Cais da Ribeira" em Português
1. Trocar para English
1. Trocar para Español

**Resultado esperado:** A descrição e o "melhor horário" mudam de idioma a cada troca, mantendo a mesma informação

---

## Cadastro

_6 caso(s) de teste._

### TC-015: Campos obrigatórios exibidos no cadastro

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-01` | 🎨 UI | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir cadastro.html

**Resultado esperado:** Campos Nome, Email, Senha e Confirmar Senha estão visíveis

### TC-016: Senha curta bloqueia cadastro

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-02` | 🚫 Negativo | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em cadastro.html

**Passos:**

1. Preencher Nome e Email válidos
1. Digitar "123" em Senha e Confirmar Senha
1. Enviar

**Resultado esperado:** Mensagem "A senha deve ter pelo menos 6 caracteres." é exibida e o cadastro não é concluído

### TC-017: Senhas diferentes bloqueiam cadastro

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-03` | 🚫 Negativo | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em cadastro.html

**Passos:**

1. Preencher Nome e Email
1. Senha "123456" e Confirmar Senha "654321"
1. Enviar

**Resultado esperado:** Mensagem "As senhas não coincidem." é exibida e o cadastro não é concluído

### TC-018: Cadastro com email duplicado é bloqueado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-04` | 🚫 Negativo | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Já existe um usuário cadastrado com email "teste@teste.com"

**Passos:**

1. Preencher o formulário novamente com email "teste@teste.com"
1. Enviar

**Resultado esperado:** Mensagem "Já existe uma conta com este email." é exibida

### TC-019: Cadastro válido tem sucesso e redireciona

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-05 / RF-CAD-06` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Email ainda não usado

**Passos:**

1. Preencher Nome, Email novo, Senha e Confirmar Senha iguais (6+ caracteres)
1. Enviar

**Resultado esperado:** Mensagem de sucesso é exibida e, após ~1,2s, a página redireciona para login.html

### TC-020: Envio com campos vazios é bloqueado pelo navegador

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-CAD-07` | 🚫 Negativo | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Estar em cadastro.html

**Passos:**

1. Deixar todos os campos vazios
1. Clicar em Cadastrar

**Resultado esperado:** O navegador impede o envio e sinaliza os campos obrigatórios (validação HTML5)

---

## Login

_4 caso(s) de teste._

### TC-021: Campos obrigatórios exibidos no login

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-LOG-01` | 🎨 UI | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir login.html

**Resultado esperado:** Campos Email e Senha estão visíveis

### TC-022: Login com credenciais inválidas é bloqueado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-LOG-02` | 🚫 Negativo | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhum usuário com esse email, ou senha errada

**Passos:**

1. Preencher email/senha inexistentes
1. Enviar

**Resultado esperado:** Mensagem "Email ou senha inválidos." é exibida

### TC-023: Login válido cria sessão e redireciona

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-LOG-03` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Usuário previamente cadastrado

**Passos:**

1. Preencher email/senha corretos
1. Enviar

**Resultado esperado:** Usuário é redirecionado para mapa.html e a sessão é criada

### TC-024: Envio com campos vazios é bloqueado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-LOG-04` | 🚫 Negativo | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Estar em login.html

**Passos:**

1. Deixar campos vazios
1. Clicar em Entrar

**Resultado esperado:** O navegador impede o envio (validação HTML5)

---

## Sessão

_4 caso(s) de teste._

### TC-025: Navbar mostra saudação quando logado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-SESS-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Login realizado

**Passos:**

1. Fazer login
1. Observar a navbar do mapa

**Resultado esperado:** Aparece "Olá, {PrimeiroNome} · Sair" no lugar de Login/Cadastrar

### TC-026: "Sair" encerra a sessão

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-SESS-02` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Usuário logado no mapa

**Passos:**

1. Clicar em "Sair"

**Resultado esperado:** Usuário é redirecionado para index.html e a navbar volta a exibir Login/Cadastrar

### TC-027: Sessão persiste ao recarregar

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-SESS-03` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Usuário logado

**Passos:**

1. Fazer login
1. Recarregar (F5) a página do mapa

**Resultado esperado:** Usuário continua logado, saudação continua visível

### TC-028: Visitante deslogado não vê saudação

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-SESS-04` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Nenhuma sessão ativa

**Passos:**

1. Abrir mapa.html sem estar logado

**Resultado esperado:** Navbar mostra Login/Cadastrar, sem saudação nem link Sair

---

## Mapa

_9 caso(s) de teste._

### TC-029: Mapa carrega centrado no Porto

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir mapa.html

**Resultado esperado:** O mapa é exibido com tiles do OpenStreetMap, centralizado na região do Porto

### TC-030: Mapa exibe os 10 marcadores

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-02` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em mapa.html

**Passos:**

1. Contar os marcadores exibidos no mapa

**Resultado esperado:** Exatamente 10 marcadores (pins) estão visíveis, correspondendo aos spots cadastrados

### TC-031: Tooltip exibe nome do spot

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-03` | 🎨 UI | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Estar em mapa.html

**Passos:**

1. Passar o mouse sobre um marcador

**Resultado esperado:** Um tooltip com o nome do spot aparece

### TC-032: Clique no marcador abre o painel

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-04` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Estar em mapa.html

**Passos:**

1. Clicar em um marcador

**Resultado esperado:** O painel lateral abre exibindo as informações daquele spot

### TC-033: Painel exibe "Ainda sem avaliações" quando aplicável

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-05` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Spot sem avaliações prévias

**Passos:**

1. Abrir o painel de um spot sem avaliações

**Resultado esperado:** Texto "Ainda sem avaliações" é exibido no lugar da média

### TC-034: Painel exibe média e contagem quando há avaliações

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-05` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Spot com ao menos 1 avaliação

**Passos:**

1. Abrir o painel de um spot já avaliado

**Resultado esperado:** Estrelas, nota média e "(N avaliações)" são exibidas corretamente

### TC-035: Painel exibe descrição e melhor horário

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-06` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Painel de um spot aberto

**Passos:**

1. Observar o conteúdo do painel

**Resultado esperado:** Descrição e "Melhor horário:" com o respectivo texto aparecem corretamente

### TC-036: Botão × fecha o painel

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-07` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Painel de um spot aberto

**Passos:**

1. Clicar no botão × no canto do painel

**Resultado esperado:** O painel é ocultado

### TC-037: Zoom in/out funciona

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-MAPA-08` | 🎨 UI | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Estar em mapa.html

**Passos:**

1. Clicar no botão "+"
1. Clicar no botão "−"

**Resultado esperado:** O mapa aumenta e diminui o zoom corretamente

---

## Avaliação

_7 caso(s) de teste._

### TC-038: Formulário de avaliação visível quando logado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Usuário logado, painel de spot aberto

**Passos:**

1. Fazer login
1. Abrir o painel de um spot

**Resultado esperado:** Formulário com 5 estrelas e campo de comentário é exibido

### TC-039: Prompt de login exibido quando deslogado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-02` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Usuário deslogado, painel de spot aberto

**Passos:**

1. Sem estar logado, abrir o painel de um spot

**Resultado esperado:** Mensagem convidando a fazer login é exibida no lugar do formulário

### TC-040: Seleção de estrelas preenche visualmente

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-03` | 🎨 UI | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Formulário de avaliação visível

**Passos:**

1. Clicar na 4ª estrela

**Resultado esperado:** As 4 primeiras estrelas ficam preenchidas (★) e a 5ª vazia (☆)

### TC-041: Envio sem estrelas selecionadas é bloqueado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-04` | 🚫 Negativo | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Formulário de avaliação visível, nenhuma estrela selecionada

**Passos:**

1. Preencher apenas o comentário
1. Clicar em Enviar avaliação

**Resultado esperado:** Mensagem "Selecione de 1 a 5 estrelas." é exibida e a avaliação não é salva

### TC-042: Avaliação enviada atualiza lista e média

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-05 / RF-AVAL-06` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Formulário de avaliação visível

**Passos:**

1. Selecionar 4 estrelas
1. Escrever um comentário
1. Enviar

**Resultado esperado:** A nova avaliação aparece no topo da lista de comentários e a média/nº de avaliações é atualizada imediatamente

### TC-043: Avaliação sem comentário é aceita

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-07` | ⚙️ Funcional | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Formulário de avaliação visível

**Passos:**

1. Selecionar 5 estrelas
1. Deixar o comentário vazio
1. Enviar

**Resultado esperado:** Avaliação é salva normalmente, sem comentário exibido

### TC-044: Comentários exibidos mais recente primeiro

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-AVAL-08` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Spot com 2+ avaliações

**Passos:**

1. Enviar uma nova avaliação em um spot que já possui avaliações

**Resultado esperado:** A avaliação mais recente aparece no topo da lista, com autor e estrelas corretos

---

## Persistência de Dados

_3 caso(s) de teste._

### TC-045: Dados persistem após reload

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-DATA-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Usuário cadastrado, avaliação enviada

**Passos:**

1. Cadastrar usuário, logar, enviar uma avaliação
1. Recarregar a página

**Resultado esperado:** Usuário, sessão e avaliação continuam presentes

### TC-046: Dados não aparecem em outro navegador

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-DATA-02` | ⚙️ Funcional | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Dados criados em um navegador (ex: Chrome)

**Passos:**

1. Criar usuário/avaliação no Chrome
1. Abrir o site em outro navegador (ex: Firefox)

**Resultado esperado:** O usuário/avaliação criados não aparecem no outro navegador

### TC-047: Limpar localStorage reseta o app

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RF-DATA-03` | ⚙️ Funcional | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Usuário logado com dados salvos

**Passos:**

1. Limpar o localStorage do site (DevTools > Application)
1. Recarregar a página

**Resultado esperado:** Usuário aparece deslogado e nenhum dado criado anteriormente é exibido

---

## Não-funcional

_7 caso(s) de teste._

### TC-048: Site acessível publicamente

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-01` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Acessar https://silvanoandrade.github.io/buskmate/ em uma aba anônima

**Resultado esperado:** O site carrega normalmente, sem necessidade de login no GitHub

### TC-049: Layout responsivo em mobile

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-02` | 🎨 UI | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir o site com a janela/emulador em ~375px de largura, em cada uma das 4 páginas

**Resultado esperado:** Layout se adapta sem elementos cortados, sobrepostos ou com scroll horizontal

### TC-050: Console sem erros

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-03` | ⚙️ Funcional | 🔴 Alta | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir o DevTools (Console)
1. Navegar pelas 4 páginas

**Resultado esperado:** Nenhum erro (vermelho) aparece no console em nenhuma página

### TC-051: Compatibilidade entre navegadores

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-04` | 🌐 Compatibilidade | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Abrir o site no Chrome
1. Abrir no Firefox
1. Abrir no Safari

**Resultado esperado:** O site funciona e aparenta-se igual nos três navegadores

### TC-052: Tempo de carregamento aceitável

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-05` | ⚡ Performance | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Conexão de internet normal

**Passos:**

1. Medir o tempo de carregamento da home (DevTools > Network)

**Resultado esperado:** A página termina de carregar em menos de 3 segundos

### TC-053: Navegação por teclado

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-06` | ♿ Acessibilidade | 🟡 Média | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Usar a tecla Tab para navegar pelos elementos da página
1. Usar Enter para ativar links/botões

**Resultado esperado:** O foco visual percorre logo, links, seletor de idioma e botões em ordem lógica, e Enter ativa o item focado

### TC-054: Imagens possuem texto alternativo

| Requisito | Tipo | Prioridade | Status |
|---|---|---|---|
| `RNF-07` | ♿ Acessibilidade | 🟢 Baixa | ⬜ Pendente |

**Pré-condições:** Nenhuma

**Passos:**

1. Inspecionar (DevTools) as imagens do logo e ícones do site

**Resultado esperado:** Todas possuem atributo alt preenchido de forma descritiva

---

_Documento gerado a partir do Plano de Requisitos do BuskMate. Marque o Status ao executar os testes e abra uma [Issue](https://github.com/silvanoandrade/buskmate/issues/new) para qualquer bug encontrado._
