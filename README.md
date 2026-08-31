# BuskMate Beta

MVP para localização e avaliação de spots de música de rua no Porto.

## Sobre
BuskMate ajuda músicos de rua a descobrir, avaliar e compartilhar os melhores locais para tocar no Porto.

## Acesse online
https://silvanoandrade.github.io/buskmate/

## Funcionalidades (MVP)
- Cadastro e login de usuário
- Mapa interativo (Leaflet.js + OpenStreetMap) com ~10 spots no Porto
- Visualização de informações de cada spot
- Avaliação por estrelas (1-5) e comentários

## Stack
- Frontend: HTML5, CSS3, JavaScript, Leaflet.js
- Backend (próxima etapa): Node.js, Express.js, API REST
- Banco de dados (próxima etapa): PostgreSQL

## Como rodar localmente
```
python3 -m http.server 8000
```
Depois acesse `http://localhost:8000`.

## Status
Nesta versão inicial, cadastro/login/avaliações usam localStorage no navegador como mock, enquanto o backend real (Node.js + Express + PostgreSQL) ainda está em desenvolvimento.
