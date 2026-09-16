# Execução dos Casos de Teste — BuskMate (ao vivo)

Site testado: https://silvanoandrade.github.io/buskmate/

## Navegação
- TC-001 Header completo em todas as páginas — **Passou** (index, login, cadastro, mapa: logo, Mapa/Login/Cadastrar, seletor de idioma presentes)
- TC-002 Logo redireciona para a home — **Passou**
- TC-003 Link "Mapa" destacado na página do mapa — **Passou**
- TC-004 Footer presente em todas as páginas — **FALHOU** — `mapa.html` não tem elemento `<footer>` nenhum (texto "BuskMate Beta" ausente do DOM). Presente em index/login/cadastro.

## Cadastro
- TC-015 Campos obrigatórios exibidos no cadastro — **Passou**
- TC-016 Senha curta bloqueia cadastro — **Passou** — mensagem "A senha deve ter pelo menos 6 caracteres." exibida ao tentar senha "123"
- TC-017 Senhas diferentes bloqueiam cadastro — **Passou** — mensagem "As senhas não coincidem." exibida
- TC-018 Cadastro com email duplicado é bloqueado — **Passou** — mensagem "Já existe uma conta com este email." exibida
- TC-019 Cadastro válido tem sucesso e redireciona — **Passou** — usuário Maria Teste (maria.teste@example.com) criado, mensagem de sucesso exibida e redirecionamento automático para login.html confirmado
- TC-020 Envio com campos vazios é bloqueado pelo navegador — **Passou** — validação HTML5 nativa impediu o envio

## Login
- TC-021 Campos obrigatórios exibidos no login — **Passou**
- TC-022 Login com credenciais inválidas é bloqueado — **Passou** — mensagem "Email ou senha inválidos." exibida
- TC-023 Login válido cria sessão e redireciona — **Passou** — login com maria.teste@example.com / 123456 redirecionou para mapa.html
- TC-024 Envio com campos vazios é bloqueado — **Passou**

## Sessão
- TC-025 Navbar mostra saudação quando logado — **Passou** — "Olá, Maria · Sair" exibido na navbar do mapa
- TC-026 "Sair" encerra a sessão — **Passou** — redirecionou para index.html e a navbar voltou a exibir Login/Cadastrar
- TC-027 Sessão persiste ao recarregar — **Passou**
- TC-028 Visitante deslogado não vê saudação — **Passou** — navbar mostra Login/Cadastrar, sem saudação nem link Sair

## Mapa
- TC-029 Mapa carrega centrado no Porto — **Passou**
- TC-030 Mapa exibe os 10 marcadores — **Passou**
- TC-031 Tooltip exibe nome do spot — **Passou**
- TC-032 Clique no marcador abre o painel — **Passou**
- TC-033 Painel exibe "Ainda sem avaliações" quando aplicável — **Passou** — confirmado no spot "Cais da Ribeira"
- TC-034 Painel exibe média e contagem quando há avaliações — **Passou** — confirmado em "Praça dos Aliados" (★★★★★ 4.5 (2 avaliações))
- TC-035 Painel exibe descrição e melhor horário — **Passou**
- TC-036 Botão × fecha o painel — **Passou**
- TC-037 Zoom in/out funciona — **Passou**

## Internacionalização
- TC-005 Seletor mostra as 3 opções de idioma — **Passou** — menu exibe Português 🇵🇹, English 🇬🇧, Español 🇪🇸
- TC-006 Troca para inglês traduz a home — **Passou** — textos, botões e menu mudaram para inglês instantaneamente, sem reload
- TC-007 Troca para espanhol traduz a home — **Passou** — confirmado (home e demais páginas mudaram para espanhol instantaneamente)
- TC-008 Idioma persiste ao navegar entre páginas — **Passou** — idioma English mantido ao navegar da home para mapa.html
- TC-009 Idioma persiste após fechar e reabrir o navegador — **Passou** — idioma Español (selecionado no dia anterior) permaneceu ativo ao reabrir o site em uma nova sessão do navegador
- TC-010 Painel do spot é retraduzido sem fechar — **Passou** — com o painel "Cais da Ribeira" aberto em English, trocar para Português retraduziu todo o conteúdo do painel (título, descrição, "Avaliar este spot", "Enviar avaliação", "Comentários") sem fechá-lo
- TC-011 Saudação do usuário é retraduzida — **Passou** — logado como Maria, saudação mudou de "Olá, Maria ·" para "Hi, Maria ·" imediatamente ao trocar para English
- TC-012 Idioma padrão é Português na primeira visita — **Passou**
- TC-013 Clicar fora fecha o menu de idiomas — **Passou**
- TC-014 Descrição do spot muda conforme idioma — **Passou** — descrição e "melhor horário" do spot "Cais da Ribeira" mudaram corretamente em PT, EN e ES

**Observação de UI (não é bug de requisito, mas vale registrar):** com o painel lateral do spot aberto, o menu suspenso de idioma abre visualmente *atrás* do painel (z-index), ficando invisível e não clicável por coordenada de tela nessa situação — só foi possível confirmar TC-010 via clique programático no item do menu. Não afeta nenhum requisito testado (RF-I18N-05 não exige que o seletor fique visível com o painel aberto), mas é um incômodo de usabilidade que pode valer a pena corrigir.

## Não-funcional
- TC-048 Site acessível publicamente — **Passou** — o site em https://silvanoandrade.github.io/buskmate/ carregou normalmente em todas as sessões de teste, sem exigir login no GitHub
- TC-049 Layout responsivo em mobile — **FALHOU** — com viewport emulado em 375px, `window.innerWidth` fica em 479px (não 375px) e `document.documentElement.scrollWidth` também é 479px em index.html, mapa.html e login.html: a página tem **scroll horizontal** nessa largura. O header (`<header>`/`<nav>`) não quebra/adapta os itens (logo + Mapa + Login + Cadastrar + seletor de idioma) em telas estreitas, forçando a largura mínima do conteúdo acima de 375px e "empurrando" o layout inteiro para o lado
- TC-050 Console sem erros — **Passou** — nenhum erro no console em index, login, cadastro e mapa
- TC-051 Compatibilidade entre navegadores — **Bloqueado/Não testado** — só havia disponível o navegador embutido (baseado em Chromium) neste ambiente; a extensão Claude para Chrome não estava conectada e não há Firefox/Safari acessíveis para comparação direta
- TC-052 Tempo de carregamento aceitável — **Passou** — `loadEventEnd` ≈ 173ms tanto em index.html quanto em cadastro.html (bem abaixo de 3s)
- TC-053 Navegação por teclado — **Passou** — Tab percorre os elementos em ordem lógica (logo → Mapa → Login → Cadastrar → seletor de idioma → botões da hero) com contorno de foco visível (`outline: auto`); Enter no link focado ("Mapa") ativou a navegação para mapa.html
- TC-054 Imagens possuem texto alternativo — **Passou** — o logo tem `alt="BuskMate"` descritivo; os ícones de marcador do Leaflet têm `alt="Marker"`; os tiles do mapa e a sombra dos marcadores (imagens puramente decorativas, geradas pela biblioteca Leaflet/OpenStreetMap) usam `alt=""`, que é o padrão correto de acessibilidade para imagens decorativas — nenhuma imagem está sem o atributo `alt`

## Persistência de Dados
- TC-045 Dados persistem após reload — **Passou** — usuário Maria Teste, sessão e as 2 avaliações enviadas em "Praça dos Aliados" continuaram presentes em `localStorage` (chaves `buskmate_users`, `buskmate_session`, `buskmate_reviews`) após recarregar a página, inclusive no dia seguinte
- TC-046 Dados não aparecem em outro navegador — **Passou (validado por arquitetura)** — os dados são gravados exclusivamente em `localStorage` do navegador, que é isolado por origem+perfil de navegador; não há nenhum mecanismo de sincronização no código. Não foi possível confirmar empiricamente com um segundo navegador real neste ambiente (a extensão Claude para Chrome não está conectada neste dispositivo), mas o comportamento é garantido pela própria API do `localStorage`
- TC-047 Limpar localStorage reseta o app — **Passou** — após `localStorage.clear()` + reload, usuário voltou a aparecer deslogado (Login/Cadastrar na navbar) e o idioma voltou ao padrão (Português)

## Avaliação
- TC-038 Formulário de avaliação visível quando logado — **Passou**
- TC-039 Prompt de login exibido quando deslogado — **Passou** — mensagem "Faça login para avaliar e comentar este spot." exibida no lugar do formulário
- TC-040 Seleção de estrelas preenche visualmente — **Passou** — clique na 4ª estrela preencheu as 4 primeiras, 5ª ficou vazia
- TC-041 Envio sem estrelas selecionadas é bloqueado — **Passou** — mensagem "Selecione de 1 a 5 estrelas." exibida
- TC-042 Avaliação enviada atualiza lista e média — **Passou** — envio de 4 estrelas + comentário atualizou lista de comentários e média (★★★★☆ 4.0 (1 avaliações)) imediatamente
- TC-043 Avaliação sem comentário é aceita — **Passou** — avaliação de 5 estrelas sem comentário foi salva normalmente, média recalculada para 4.5 (2 avaliações)
- TC-044 Comentários exibidos mais recente primeiro — **Passou** — nova avaliação (5 estrelas, sem comentário) apareceu no topo da lista, acima da avaliação anterior (4 estrelas)

