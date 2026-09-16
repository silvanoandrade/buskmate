# BuskMate Beta

🌐 [Português](#-português) | [English](#-english) | [Español](#-español)

MVP for finding, rating and sharing street music (busking) spots — currently focused on Porto, Portugal.

**🔗 Live demo:** https://silvanoandrade.github.io/buskmate/

---

## 🇵🇹 Português

MVP para localização e avaliação de spots de música de rua no Porto.

### Sobre
O BuskMate ajuda músicos de rua a descobrir, avaliar e compartilhar os melhores locais para tocar no Porto.

### Acesse online
https://silvanoandrade.github.io/buskmate/

### Funcionalidades (MVP)
- Cadastro e login de usuário
- Mapa interativo (Leaflet.js + OpenStreetMap) com ~10 spots no Porto
- Visualização de informações de cada spot
- Avaliação por estrelas (1-5) e comentários
- Site disponível em 3 idiomas (Português, Inglês, Espanhol) através do seletor no canto superior direito

### Stack
- Frontend: HTML5, CSS3, JavaScript, Leaflet.js
- Backend (próxima etapa): Node.js, Express.js, API REST
- Banco de dados (próxima etapa): PostgreSQL
- Testes: QA manual (54 casos) + automação com Python, Selenium e pytest

### Testes / QA
Este projeto tem uma suíte de QA completa por trás do MVP:
- **Testes manuais:** 54 casos de teste planejados e executados contra o site publicado, documentados em [`Testes/BuskMate_QA_Plano_de_Testes.xlsx`](Testes/BuskMate_QA_Plano_de_Testes.xlsx) e [`Testes/execucao_resultados.md`](Testes/execucao_resultados.md).
- **Automação:** suíte em Python + Selenium + pytest, construída aula a aula, cobrindo os casos de maior prioridade — veja [`automacao/`](automacao/) e o [guia de aulas](automacao/README_AUTOMACAO.md).

### Como rodar localmente
```
python3 -m http.server 8000
```
Depois acesse `http://localhost:8000`.

### Status
Nesta versão inicial, cadastro/login/avaliações usam localStorage no navegador como mock, enquanto o backend real (Node.js + Express + PostgreSQL) ainda está em desenvolvimento.

---

## 🇬🇧 English

MVP for finding and rating street music (busking) spots in Porto.

### About
BuskMate helps street musicians discover, rate and share the best places to perform in Porto.

### Live demo
https://silvanoandrade.github.io/buskmate/

### Features (MVP)
- User sign up and login
- Interactive map (Leaflet.js + OpenStreetMap) with ~10 spots in Porto
- Detailed information for each spot
- Star rating (1-5) and comments
- Site available in 3 languages (Portuguese, English, Spanish) via the switcher in the top-right corner

### Stack
- Frontend: HTML5, CSS3, JavaScript, Leaflet.js
- Backend (next step): Node.js, Express.js, REST API
- Database (next step): PostgreSQL
- Testing: manual QA (54 cases) + automation with Python, Selenium and pytest

### Testing / QA
This project has a full QA suite behind the MVP:
- **Manual tests:** 54 test cases planned and executed against the published site, documented in [`Testes/BuskMate_QA_Plano_de_Testes.xlsx`](Testes/BuskMate_QA_Plano_de_Testes.xlsx) and [`Testes/execucao_resultados.md`](Testes/execucao_resultados.md).
- **Automation:** a Python + Selenium + pytest suite, built lesson by lesson, covering the highest-priority cases — see [`automacao/`](automacao/) and the [lesson guide](automacao/README_AUTOMACAO.md).

### Running locally
```
python3 -m http.server 8000
```
Then visit `http://localhost:8000`.

### Status
In this initial version, sign up/login/ratings use the browser's localStorage as a mock, while the real backend (Node.js + Express + PostgreSQL) is still under development.

---

## 🇪🇸 Español

MVP para localizar y valorar lugares de música callejera en Oporto.

### Sobre el proyecto
BuskMate ayuda a los músicos callejeros a descubrir, valorar y compartir los mejores lugares para tocar en Oporto.

### Demo en línea
https://silvanoandrade.github.io/buskmate/

### Funcionalidades (MVP)
- Registro e inicio de sesión de usuarios
- Mapa interactivo (Leaflet.js + OpenStreetMap) con ~10 lugares en Oporto
- Información detallada de cada lugar
- Valoración por estrellas (1-5) y comentarios
- Sitio disponible en 3 idiomas (Portugués, Inglés, Español) mediante el selector en la esquina superior derecha

### Stack
- Frontend: HTML5, CSS3, JavaScript, Leaflet.js
- Backend (próximo paso): Node.js, Express.js, API REST
- Base de datos (próximo paso): PostgreSQL
- Pruebas: QA manual (54 casos) + automatización con Python, Selenium y pytest

### Pruebas / QA
El proyecto tiene una suite de QA completa detrás del MVP:
- **Pruebas manuales:** 54 casos de prueba planificados y ejecutados contra el sitio publicado, documentados en [`Testes/BuskMate_QA_Plano_de_Testes.xlsx`](Testes/BuskMate_QA_Plano_de_Testes.xlsx) y [`Testes/execucao_resultados.md`](Testes/execucao_resultados.md).
- **Automatización:** una suite en Python + Selenium + pytest, construida clase a clase, que cubre los casos de mayor prioridad — ver [`automacao/`](automacao/) y la [guía de clases](automacao/README_AUTOMACAO.md).

### Cómo ejecutar en local
```
python3 -m http.server 8000
```
Luego visita `http://localhost:8000`.

### Estado
En esta versión inicial, el registro/inicio de sesión/valoraciones usan el localStorage del navegador como simulación, mientras que el backend real (Node.js + Express + PostgreSQL) todavía está en desarrollo.
