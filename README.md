# 🐳 Docker Compose — Python API + Nginx

![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?logo=nginx&logoColor=white)

## 📌 Description

Mini-projet DevOps avec **Docker Compose**.

L'objectif est de faire fonctionner plusieurs conteneurs ensemble :

- 🐍 une API Python avec Flask
- 🌐 un serveur Nginx
- 🔄 Nginx utilisé comme reverse proxy
- 🐳 Docker Compose pour orchestrer les services

L'utilisateur accède à Nginx sur le port `8080`.

Nginx transmet ensuite les requêtes `/api/*` vers l'API Python.

---

## 🏗️ Architecture

```text
                    Navigateur
                        │
                        │ HTTP :8080
                        ▼
              ┌──────────────────┐
              │      NGINX       │
              │  Reverse Proxy   │
              │      :80         │
              └────────┬─────────┘
                       │
                       │ /api/*
                       ▼
              ┌──────────────────┐
              │    PYTHON API    │
              │      Flask       │
              │      :5000       │
              └──────────────────┘




📁 Structure du projet
docker-compose-python-nginx/
│
├── app/
│   ├── app.py
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── compose.yaml
│
└── README.md

🚀 Installation
docker --version
docker compose version
## Cloner le projet
git clone https://github.com/cis-debug/docker-compose-python-nginx.git
cd docker-compose-python-nginx

## Démarrer les services
docker compose up -d --build

## Vérifier les conteneurs
docker compose ps

🧪 Tests
curl http://localhost:8080

## Test de l'API
curl http://localhost:8080/api/health

🌐 Tester dans un navigateur
http://localhost:8080
http://localhost:8080/api/health
http://localhost:8080/api/info





