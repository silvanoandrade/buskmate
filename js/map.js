// Mapa interativo com Leaflet.js + OpenStreetMap
const REVIEWS_KEY = "buskmate_reviews"; // { [spotId]: [{ autor, nota, comentario, data }] }
let currentSpot = null;

function getReviews(spotId) {
  const all = JSON.parse(localStorage.getItem(REVIEWS_KEY) || "{}");
  return all[spotId] || [];
}

function addReview(spotId, review) {
  const all = JSON.parse(localStorage.getItem(REVIEWS_KEY) || "{}");
  all[spotId] = all[spotId] || [];
  all[spotId].push(review);
  localStorage.setItem(REVIEWS_KEY, JSON.stringify(all));
}

function mediaAvaliacoes(reviews) {
  if (!reviews.length) return null;
  const soma = reviews.reduce((acc, r) => acc + r.nota, 0);
  return (soma / reviews.length).toFixed(1);
}

function renderEstrelas(nota) {
  const cheias = Math.round(nota);
  return "★".repeat(cheias) + "☆".repeat(5 - cheias);
}

// Inicializa o mapa centrado no Porto
const map = L.map("map").setView([41.1479, -8.6291], 13);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "&copy; OpenStreetMap contributors",
  maxZoom: 19
}).addTo(map);

const spotPanel = document.getElementById("spot-panel");
const spotContent = document.getElementById("spot-content");
const closePanelBtn = document.getElementById("close-panel");

function abrirSpot(spot) {
  currentSpot = spot;
  const reviews = getReviews(spot.id);
  const media = mediaAvaliacoes(reviews);
  const session = typeof getSession === "function" ? getSession() : null;
  const descricao = translateSpot(spot.id, "descricao") || spot.descricao;
  const melhorHorario = translateSpot(spot.id, "melhorHorario") || spot.melhorHorario;

  spotContent.innerHTML = `
    <h2>${spot.nome}</h2>
    <p class="spot-rating">${media ? `${renderEstrelas(media)} ${media} (${reviews.length} ${t("map_reviews_count")})` : t("map_no_reviews")}</p>
    <p>${descricao}</p>
    <p><strong>${t("map_best_time")}</strong> ${melhorHorario}</p>

    <hr>

    <div class="avaliar-area">
      ${
        session
          ? `
        <h3>${t("map_rate_title")}</h3>
        <form id="form-avaliar">
          <div class="star-input" id="star-input">
            ${[1, 2, 3, 4, 5].map((n) => `<span class="star" data-value="${n}">☆</span>`).join("")}
          </div>
          <input type="hidden" id="nota-selecionada" value="0">
          <textarea id="comentario" placeholder="${t("map_comment_placeholder")}" rows="3"></textarea>
          <button type="submit" class="btn btn-primary btn-block">${t("map_send_review")}</button>
          <p class="form-message" id="avaliar-message"></p>
        </form>
      `
          : `<p class="login-prompt">${t("map_login_prompt_pre")} <a href="login.html">${t("map_login_prompt_link")}</a> ${t("map_login_prompt_post")}</p>`
      }
    </div>

    <div class="comentarios-lista">
      <h3>${t("map_comments_title")}</h3>
      ${
        reviews.length
          ? reviews
              .slice()
              .reverse()
              .map(
                (r) => `
            <div class="comentario">
              <p class="comentario-header"><strong>${r.autor}</strong> ${renderEstrelas(r.nota)}</p>
              <p>${r.comentario || ""}</p>
            </div>`
              )
              .join("")
          : `<p>${t("map_no_comments")}</p>`
      }
    </div>
  `;

  spotPanel.hidden = false;

  const formAvaliar = document.getElementById("form-avaliar");
  if (formAvaliar) {
    const stars = document.querySelectorAll("#star-input .star");
    const notaInput = document.getElementById("nota-selecionada");
    stars.forEach((star) => {
      star.addEventListener("click", () => {
        const value = Number(star.dataset.value);
        notaInput.value = value;
        stars.forEach((s, i) => (s.textContent = i < value ? "★" : "☆"));
      });
    });

    formAvaliar.addEventListener("submit", (e) => {
      e.preventDefault();
      const nota = Number(notaInput.value);
      const msg = document.getElementById("avaliar-message");
      if (!nota) {
        msg.textContent = t("map_select_stars");
        return;
      }
      const comentario = document.getElementById("comentario").value.trim();
      addReview(spot.id, {
        autor: session.nome.split(" ")[0],
        nota,
        comentario,
        data: new Date().toISOString()
      });
      abrirSpot(spot); // recarrega painel com nova avaliação
    });
  }
}

closePanelBtn.addEventListener("click", () => {
  spotPanel.hidden = true;
});

BUSKMATE_SPOTS.forEach((spot) => {
  const marker = L.marker([spot.lat, spot.lng]).addTo(map);
  marker.bindTooltip(spot.nome);
  marker.on("click", () => abrirSpot(spot));
});

document.addEventListener("buskmate:langchange", () => {
  if (currentSpot) abrirSpot(currentSpot);
});
