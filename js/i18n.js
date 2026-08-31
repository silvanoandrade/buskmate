// Sistema de internacionalização (i18n) do BuskMate — PT / EN / ES
const BUSKMATE_LANG_KEY = "buskmate_lang";
const SUPPORTED_LANGS = ["pt", "en", "es"];

const TRANSLATIONS = {
  pt: {
    nav_map: "Mapa",
    nav_login: "Login",
    nav_register: "Cadastrar",
    nav_hello: "Olá",
    nav_logout: "Sair",

    hero_title: "Encontre o spot certo. Toque no seu melhor lugar.",
    hero_subtitle: "O BuskMate ajuda músicos de rua a descobrir, avaliar e compartilhar os melhores locais para tocar no Porto.",
    hero_cta_start: "Começar agora",
    hero_cta_map: "Ver mapa dos spots",

    features_title: "Como funciona",
    feature1_title: "Cadastre-se",
    feature1_desc: "Crie sua conta em segundos e junte-se à comunidade de músicos de rua.",
    feature2_title: "Explore o mapa",
    feature2_desc: "Veja spots de busking espalhados pelo Porto, com informações detalhadas.",
    feature3_title: "Avalie e comente",
    feature3_desc: "Compartilhe sua experiência avaliando de 1 a 5 estrelas e deixando comentários.",

    login_title: "Entrar",
    login_subtitle: "Acesse sua conta para avaliar e comentar spots.",
    label_email: "Email",
    label_senha: "Senha",
    btn_entrar: "Entrar",
    login_switch: "Ainda não tem conta?",
    login_switch_link: "Cadastre-se",

    cadastro_title: "Criar conta",
    cadastro_subtitle: "Junte-se à comunidade BuskMate e comece a descobrir spots.",
    label_nome: "Nome",
    label_confirmar_senha: "Confirmar senha",
    btn_cadastrar: "Cadastrar",
    cadastro_switch: "Já tem conta?",
    cadastro_switch_link: "Entrar",

    msg_senha_curta: "A senha deve ter pelo menos 6 caracteres.",
    msg_senhas_diferentes: "As senhas não coincidem.",
    msg_email_existente: "Já existe uma conta com este email.",
    msg_conta_criada: "Conta criada! Redirecionando para o login...",
    msg_login_invalido: "Email ou senha inválidos.",

    footer_text: "BuskMate Beta · MVP para localização e avaliação de spots de música de rua no Porto",

    map_no_reviews: "Ainda sem avaliações",
    map_reviews_count: "avaliações",
    map_best_time: "Melhor horário:",
    map_rate_title: "Avaliar este spot",
    map_comment_placeholder: "Escreva um comentário sobre este spot...",
    map_send_review: "Enviar avaliação",
    map_select_stars: "Selecione de 1 a 5 estrelas.",
    map_comments_title: "Comentários",
    map_no_comments: "Seja o primeiro a comentar.",
    map_login_prompt_pre: "Faça",
    map_login_prompt_link: "login",
    map_login_prompt_post: "para avaliar e comentar este spot.",

    lang_name: "Português"
  },
  en: {
    nav_map: "Map",
    nav_login: "Login",
    nav_register: "Sign up",
    nav_hello: "Hi",
    nav_logout: "Log out",

    hero_title: "Find the right spot. Play where you belong.",
    hero_subtitle: "BuskMate helps street musicians discover, rate and share the best places to perform in Porto.",
    hero_cta_start: "Get started",
    hero_cta_map: "View spots map",

    features_title: "How it works",
    feature1_title: "Sign up",
    feature1_desc: "Create your account in seconds and join the street musicians' community.",
    feature2_title: "Explore the map",
    feature2_desc: "See busking spots across Porto, with detailed information for each one.",
    feature3_title: "Rate and comment",
    feature3_desc: "Share your experience with a 1 to 5 star rating and leave a comment.",

    login_title: "Log in",
    login_subtitle: "Access your account to rate and comment on spots.",
    label_email: "Email",
    label_senha: "Password",
    btn_entrar: "Log in",
    login_switch: "Don't have an account yet?",
    login_switch_link: "Sign up",

    cadastro_title: "Create account",
    cadastro_subtitle: "Join the BuskMate community and start discovering spots.",
    label_nome: "Name",
    label_confirmar_senha: "Confirm password",
    btn_cadastrar: "Sign up",
    cadastro_switch: "Already have an account?",
    cadastro_switch_link: "Log in",

    msg_senha_curta: "Password must be at least 6 characters long.",
    msg_senhas_diferentes: "Passwords don't match.",
    msg_email_existente: "An account with this email already exists.",
    msg_conta_criada: "Account created! Redirecting to login...",
    msg_login_invalido: "Invalid email or password.",

    footer_text: "BuskMate Beta · MVP for finding and rating street music spots in Porto",

    map_no_reviews: "No ratings yet",
    map_reviews_count: "ratings",
    map_best_time: "Best time:",
    map_rate_title: "Rate this spot",
    map_comment_placeholder: "Write a comment about this spot...",
    map_send_review: "Submit rating",
    map_select_stars: "Select 1 to 5 stars.",
    map_comments_title: "Comments",
    map_no_comments: "Be the first to comment.",
    map_login_prompt_pre: "Please",
    map_login_prompt_link: "log in",
    map_login_prompt_post: "to rate and comment on this spot.",

    lang_name: "English"
  },
  es: {
    nav_map: "Mapa",
    nav_login: "Iniciar sesión",
    nav_register: "Registrarse",
    nav_hello: "Hola",
    nav_logout: "Salir",

    hero_title: "Encuentra el lugar ideal. Toca donde perteneces.",
    hero_subtitle: "BuskMate ayuda a los músicos callejeros a descubrir, valorar y compartir los mejores lugares para tocar en Oporto.",
    hero_cta_start: "Empezar ahora",
    hero_cta_map: "Ver mapa de lugares",

    features_title: "Cómo funciona",
    feature1_title: "Regístrate",
    feature1_desc: "Crea tu cuenta en segundos y únete a la comunidad de músicos callejeros.",
    feature2_title: "Explora el mapa",
    feature2_desc: "Descubre lugares de música callejera por todo Oporto, con información detallada.",
    feature3_title: "Valora y comenta",
    feature3_desc: "Comparte tu experiencia con una valoración de 1 a 5 estrellas y deja un comentario.",

    login_title: "Iniciar sesión",
    login_subtitle: "Accede a tu cuenta para valorar y comentar lugares.",
    label_email: "Correo electrónico",
    label_senha: "Contraseña",
    btn_entrar: "Iniciar sesión",
    login_switch: "¿Aún no tienes cuenta?",
    login_switch_link: "Regístrate",

    cadastro_title: "Crear cuenta",
    cadastro_subtitle: "Únete a la comunidad BuskMate y empieza a descubrir lugares.",
    label_nome: "Nombre",
    label_confirmar_senha: "Confirmar contraseña",
    btn_cadastrar: "Registrarse",
    cadastro_switch: "¿Ya tienes cuenta?",
    cadastro_switch_link: "Iniciar sesión",

    msg_senha_curta: "La contraseña debe tener al menos 6 caracteres.",
    msg_senhas_diferentes: "Las contraseñas no coinciden.",
    msg_email_existente: "Ya existe una cuenta con este correo.",
    msg_conta_criada: "¡Cuenta creada! Redirigiendo al inicio de sesión...",
    msg_login_invalido: "Correo o contraseña incorrectos.",

    footer_text: "BuskMate Beta · MVP para localizar y valorar lugares de música callejera en Oporto",

    map_no_reviews: "Aún sin valoraciones",
    map_reviews_count: "valoraciones",
    map_best_time: "Mejor horario:",
    map_rate_title: "Valorar este lugar",
    map_comment_placeholder: "Escribe un comentario sobre este lugar...",
    map_send_review: "Enviar valoración",
    map_select_stars: "Selecciona de 1 a 5 estrellas.",
    map_comments_title: "Comentarios",
    map_no_comments: "Sé el primero en comentar.",
    map_login_prompt_pre: "Inicia",
    map_login_prompt_link: "sesión",
    map_login_prompt_post: "para valorar y comentar este lugar.",

    lang_name: "Español"
  }
};

const SPOT_TRANSLATIONS = {
  ribeira: {
    pt: { descricao: "Movimento constante de turistas à beira-rio, ótima acústica junto aos arcos.", melhorHorario: "Tardes e fins de tarde, 15h-19h" },
    en: { descricao: "Steady flow of tourists by the riverside, great acoustics under the arches.", melhorHorario: "Afternoons and early evening, 3-7pm" },
    es: { descricao: "Flujo constante de turistas junto al río, gran acústica bajo los arcos.", melhorHorario: "Tardes y atardecer, 15h-19h" }
  },
  aliados: {
    pt: { descricao: "Grande praça central, alto fluxo de pessoas, espaço amplo para instrumentos maiores.", melhorHorario: "Fins de semana, 11h-14h" },
    en: { descricao: "Large central square, high foot traffic, plenty of room for bigger instruments.", melhorHorario: "Weekends, 11am-2pm" },
    es: { descricao: "Gran plaza central, mucho flujo de gente, espacio amplio para instrumentos grandes.", melhorHorario: "Fines de semana, 11h-14h" }
  },
  "santa-catarina": {
    pt: { descricao: "Rua comercial movimentada, bom para público que caminha e para.", melhorHorario: "Sábados, 14h-18h" },
    en: { descricao: "Busy shopping street, good for passers-by who stop to listen.", melhorHorario: "Saturdays, 2-6pm" },
    es: { descricao: "Calle comercial concurrida, buena para un público que camina y se detiene.", melhorHorario: "Sábados, 14h-18h" }
  },
  clerigos: {
    pt: { descricao: "Ponto turístico icônico, fila de visitantes garante audiência constante.", melhorHorario: "Manhãs, 10h-13h" },
    en: { descricao: "Iconic landmark, the queue of visitors guarantees a steady audience.", melhorHorario: "Mornings, 10am-1pm" },
    es: { descricao: "Punto turístico icónico, la cola de visitantes garantiza público constante.", melhorHorario: "Mañanas, 10h-13h" }
  },
  cristal: {
    pt: { descricao: "Ambiente tranquilo com vista para o rio, público mais relaxado.", melhorHorario: "Fim de tarde, 17h-20h" },
    en: { descricao: "Peaceful setting with a river view, a more relaxed audience.", melhorHorario: "Early evening, 5-8pm" },
    es: { descricao: "Ambiente tranquilo con vistas al río, público más relajado.", melhorHorario: "Atardecer, 17h-20h" }
  },
  batalha: {
    pt: { descricao: "Próxima a paragens de transporte, bom fluxo de passantes.", melhorHorario: "Dias úteis, 17h-19h" },
    en: { descricao: "Close to public transport stops, good flow of passers-by.", melhorHorario: "Weekdays, 5-7pm" },
    es: { descricao: "Cerca de paradas de transporte, buen flujo de transeúntes.", melhorHorario: "Días laborables, 17h-19h" }
  },
  foz: {
    pt: { descricao: "Área nobre à beira-mar, público mais tranquilo, ideal para sets acústicos.", melhorHorario: "Fins de semana, 16h-19h" },
    en: { descricao: "Upscale seafront area, a calmer crowd, ideal for acoustic sets.", melhorHorario: "Weekends, 4-7pm" },
    es: { descricao: "Zona exclusiva junto al mar, público más tranquilo, ideal para sets acústicos.", melhorHorario: "Fines de semana, 16h-19h" }
  },
  bolhao: {
    pt: { descricao: "Entrada do mercado recém-renovado, bom para performances curtas.", melhorHorario: "Manhãs de sábado, 9h-12h" },
    en: { descricao: "Entrance to the recently renovated market, good for short performances.", melhorHorario: "Saturday mornings, 9am-12pm" },
    es: { descricao: "Entrada del mercado recién renovado, bueno para actuaciones cortas.", melhorHorario: "Sábados por la mañana, 9h-12h" }
  },
  "miguel-bombarda": {
    pt: { descricao: "Rua das galerias de arte, público mais alternativo e atento.", melhorHorario: "Tardes de sábado, 15h-18h" },
    en: { descricao: "Street of art galleries, a more alternative and attentive crowd.", melhorHorario: "Saturday afternoons, 3-6pm" },
    es: { descricao: "Calle de las galerías de arte, público más alternativo y atento.", melhorHorario: "Sábados por la tarde, 15h-18h" }
  },
  "sao-bento": {
    pt: { descricao: "Entrada da estação com azulejos famosos, alto fluxo turístico o dia todo.", melhorHorario: "Qualquer horário, picos às 12h e 18h" },
    en: { descricao: "Station entrance with its famous tiles, heavy tourist flow all day.", melhorHorario: "Any time, peaks at 12pm and 6pm" },
    es: { descricao: "Entrada de la estación con sus famosos azulejos, alto flujo turístico todo el día.", melhorHorario: "Cualquier hora, picos a las 12h y 18h" }
  }
};

function getLang() {
  const saved = localStorage.getItem(BUSKMATE_LANG_KEY);
  return SUPPORTED_LANGS.includes(saved) ? saved : "pt";
}

function setLang(lang) {
  if (!SUPPORTED_LANGS.includes(lang)) return;
  localStorage.setItem(BUSKMATE_LANG_KEY, lang);
  applyTranslations();
  document.dispatchEvent(new CustomEvent("buskmate:langchange", { detail: { lang } }));
}

function t(key) {
  const lang = getLang();
  return (TRANSLATIONS[lang] && TRANSLATIONS[lang][key]) || TRANSLATIONS.pt[key] || key;
}

function translateSpot(spotId, field) {
  const lang = getLang();
  const entry = SPOT_TRANSLATIONS[spotId];
  if (!entry) return null;
  return (entry[lang] && entry[lang][field]) || (entry.pt && entry.pt[field]) || null;
}

function applyTranslations() {
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    el.textContent = t(key);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.setAttribute("placeholder", t(el.getAttribute("data-i18n-placeholder")));
  });
  const activeLabel = document.getElementById("lang-current");
  if (activeLabel) activeLabel.textContent = getLang().toUpperCase();
  document.querySelectorAll(".lang-option").forEach((el) => {
    el.classList.toggle("active", el.dataset.lang === getLang());
  });
}

function initLangSwitcher() {
  const toggle = document.getElementById("lang-toggle");
  const menu = document.getElementById("lang-menu");
  if (!toggle || !menu) return;

  toggle.addEventListener("click", (e) => {
    e.stopPropagation();
    menu.hidden = !menu.hidden;
  });

  menu.querySelectorAll(".lang-option").forEach((option) => {
    option.addEventListener("click", () => {
      setLang(option.dataset.lang);
      menu.hidden = true;
    });
  });

  document.addEventListener("click", () => {
    menu.hidden = true;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initLangSwitcher();
  applyTranslations();
});
