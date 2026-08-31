// Mapa interativo com Leaflet.js + OpenStreetMap
const REVIEWS_KEY = "buskmate_reviews"; // { [spotId]: [{ autor, nota, comentario, data }] }

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
  const reviews = getReviews(spot.id);
  const media = mediaAvaliacoes(reviews);
  const session = typeof getSession === "function" ? getSession() : null;

  spotContent.innerHTML = `
    <h2>${spot.nome}</h2>
    <p class="spot-rating">${media ? `${renderEstrelas(media)} ${media} (${reviews.length} avaliações)` : "Ainda sem avaliações"}</p>
    <p>${spot.descricao}</p>
    <p><strong>Melhor horário:</strong> ${spot.melhorHorario}</p>

    <hr>

    <div class="avaliar-area">
      ${
        session
          ? `
        <h3>Avaliar este spot</h3>
        <form id="form-avaliar">
          <div class="star-input" id="star-input">
            ${[1, 2, 3, 4, 5].map((n) => `<span class="star" data-value="${n}">☆</span>`).join("")}
          </div>
          <input type="hidden" id="nota-selecionada" value="0">
          <textarea id="comentario" placeholder="Escreva um comentário sobre este spot..." rows="3"></textarea>
          <button type="submit" class="btn btn-primary btn-block">Enviar avaliação</button>
          <p class="form-message" id="avaliar-message"></p>
        </form>
      `
          : `<p class="login-prompt">Faça <a href="login.html">login</a> para avaliar e comentar este spot.</p>`
      }
    </div>

    <div class="comentarios-lista">
      <h3>Comentários</h3>
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
          : "<p>Seja o primeiro a comentar.</p>"
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
        msg.textContent = "Selecione de 1 a 5 estrelas.";
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
