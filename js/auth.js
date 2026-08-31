// Autenticação mockada com localStorage (sem backend nesta etapa do MVP)
const USERS_KEY = "buskmate_users";
const SESSION_KEY = "buskmate_session";

function getUsers() {
  return JSON.parse(localStorage.getItem(USERS_KEY) || "[]");
}

function saveUsers(users) {
  localStorage.setItem(USERS_KEY, JSON.stringify(users));
}

function getSession() {
  return JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
}

function setSession(user) {
  localStorage.setItem(SESSION_KEY, JSON.stringify({ nome: user.nome, email: user.email }));
}

function logout() {
  localStorage.removeItem(SESSION_KEY);
  window.location.href = "index.html";
}

// --- Formulário de cadastro ---
const formCadastro = document.getElementById("form-cadastro");
if (formCadastro) {
  formCadastro.addEventListener("submit", (e) => {
    e.preventDefault();
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim().toLowerCase();
    const senha = document.getElementById("senha").value;
    const confirmarSenha = document.getElementById("confirmar-senha").value;
    const message = document.getElementById("form-message");

    if (senha.length < 6) {
      message.textContent = t("msg_senha_curta");
      return;
    }
    if (senha !== confirmarSenha) {
      message.textContent = t("msg_senhas_diferentes");
      return;
    }

    const users = getUsers();
    if (users.some((u) => u.email === email)) {
      message.textContent = t("msg_email_existente");
      return;
    }

    users.push({ nome, email, senha });
    saveUsers(users);
    message.style.color = "green";
    message.textContent = t("msg_conta_criada");
    setTimeout(() => (window.location.href = "login.html"), 1200);
  });
}

// --- Formulário de login ---
const formLogin = document.getElementById("form-login");
if (formLogin) {
  formLogin.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value.trim().toLowerCase();
    const senha = document.getElementById("senha").value;
    const message = document.getElementById("form-message");

    const users = getUsers();
    const user = users.find((u) => u.email === email && u.senha === senha);
    if (!user) {
      message.textContent = t("msg_login_invalido");
      return;
    }

    setSession(user);
    window.location.href = "mapa.html";
  });
}

// --- Atualiza navegação conforme sessão ---
function updateNavAuthState() {
  const session = getSession();
  const navLogin = document.getElementById("nav-login");
  const navCadastro = document.getElementById("nav-cadastro");
  const navUser = document.getElementById("nav-user");
  if (session && navUser) {
    if (navLogin) navLogin.hidden = true;
    if (navCadastro) navCadastro.hidden = true;
    navUser.hidden = false;
    navUser.innerHTML = `${t("nav_hello")}, ${session.nome.split(" ")[0]} · <a href="#" id="logout-link">${t("nav_logout")}</a>`;
    const logoutLink = document.getElementById("logout-link");
    if (logoutLink) {
      logoutLink.addEventListener("click", (e) => {
        e.preventDefault();
        logout();
      });
    }
  }
}
updateNavAuthState();
document.addEventListener("buskmate:langchange", updateNavAuthState);
