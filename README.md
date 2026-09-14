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
Docker
Docker Compose

🎉 Mission 9 vérifiée !

J’ai regardé directement ton dépôt GitHub : docker-compose-python-nginx

✅ Ce qui est bon
compose.yaml présent et fonctionnel dans sa logique : 2 services api + nginx, port 8080, volume de configuration Nginx.
API Python avec Flask, deux endpoints /api/health et /api/info.
Dockerfile Python correctement configuré avec Flask.
Nginx configuré comme reverse proxy vers api:5000.
Le dépôt est public et sur main.
⚠️ Une petite chose à corriger

Ton README.md contient encore quelques problèmes de Markdown : plusieurs blocs de code ne sont pas correctement fermés et certains titres commencent par ## au milieu des commandes.

Mais le projet lui-même est bien construit. 👍

👉 Je considère donc la Mission 9 validée côté technique, avec simplement le README à nettoyer pour avoir un portfolio vraiment propre.

Et surtout : tu viens de passer à une vraie architecture multi-conteneurs + API + reverse proxy, ce qui est une belle progression DevOps. 🚀

Mission 10 : CI/CD avec GitHub Actions — là, on va commencer à automatiser automatiquement les tests de ton code à chaque git push. 🔥

tonne moi le Readme comple, du debtut a l'utilisation.
sur une seul paege la je peux copie coller diretement

Bien sûr 👍 Voici le README complet pour la Mission 9 docker-compose-python-nginx, propre et professionnel, en une seule page. Tu peux copier-coller directement tout le contenu dans ton README.md.

# 🐳 Docker Compose — Python API + Nginx

![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?logo=nginx&logoColor=white)

## 📌 Description

Ce projet est un mini-laboratoire DevOps réalisé avec **Docker Compose**.

L'objectif est de faire fonctionner plusieurs conteneurs ensemble :

- 🐍 une API Python avec Flask
- 🌐 un serveur Nginx
- 🔄 Nginx joue le rôle de **reverse proxy**
- 🐳 Docker Compose orchestre les différents services

L'utilisateur accède uniquement à Nginx sur le port `8080`.

Nginx transmet ensuite les requêtes `/api/*` à l'API Python.

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
              │     :80          │
              └────────┬─────────┘
                       │
                       │ /api/*
                       ▼
              ┌──────────────────┐
              │    PYTHON API    │
              │     Flask        │
              │     :5000        │
              └──────────────────┘
Fonctionnement
http://localhost:8080
        │
        ▼
      Nginx
        │
        ├── /api/health ──► Python API
        │
        └── /api/info   ──► Python API
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
🚀 Installation et utilisation
1️⃣ Prérequis

Avant de commencer, il faut avoir installé :

Docker
Docker Compose

Vérifier Docker :

docker --version

Vérifier Docker Compose :

docker compose version
2️⃣ Cloner le projet
git clone https://github.com/cis-debug/docker-compose-python-nginx.git

Entrer dans le projet :

cd docker-compose-python-nginx
3️⃣ Démarrer les conteneurs

Lancer Docker Compose :

docker compose up -d --build
Explication
up → démarre les services
-d → démarre en arrière-plan
--build → reconstruit les images si nécessaire
4️⃣ Vérifier les conteneurs
docker compose ps

Vous devez voir deux services :

api
nginx

Vous pouvez également utiliser :

docker ps
🧪 Tester l'application
Test 1 — Vérifier Nginx

Dans le navigateur ou le terminal :

curl http://localhost:8080

Résultat attendu :

Nginx is running. Try /api/health or /api/info
Test 2 — Vérifier l'API Python

Tester l'endpoint de santé :

curl http://localhost:8080/api/health

Résultat attendu :

{
  "hostname": "xxxxxxxxxxxx",
  "message": "Hello from Ndeye's DevOps lab!",
  "service": "python-api"
}

Le hostname peut être différent car il correspond au conteneur Python.

Test 3 — Informations de l'API
curl http://localhost:8080/api/info

Résultat attendu :

{
  "hostname": "xxxxxxxxxxxx",
  "service": "python-api"
}
🌐 Tester avec un navigateur

Vous pouvez également ouvrir :

http://localhost:8080

Puis :

http://localhost:8080/api/health

Et :

http://localhost:8080/api/info
🔄 Comment fonctionne le Reverse Proxy ?

Nginx reçoit les requêtes HTTP.

Lorsqu'une requête commence par :

/api/

Nginx la transmet automatiquement au service Python.

Configuration utilisée :

location /api/ {
    proxy_pass http://api:5000;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}

Docker Compose permet à Nginx de communiquer avec le service Python grâce au nom du service :

api

Il n'est donc pas nécessaire d'utiliser une adresse IP fixe.

🐳 Services Docker

Le projet utilise deux services.

🐍 API Python

L'API utilise :

Python 3.12
Flask
Port interne : 5000

Elle fournit deux endpoints :

/api/health
/api/info
🌐 Nginx

Nginx utilise l'image :

nginx:alpine

Il écoute sur le port :

80

Le port est exposé sur la machine hôte :

8080:80

Cela signifie :

localhost:8080 → Nginx:80
📄 Docker Compose

Le fichier compose.yaml orchestre les deux services :

services:
  api:
    build:
      context: ./app
    container_name: python-api
    expose:
      - "5000"

  nginx:
    image: nginx:alpine
    container_name: nginx-front
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
🛑 Arrêter les conteneurs

Pour arrêter le projet :

docker compose down
▶️ Redémarrer le projet

Pour relancer les conteneurs :

docker compose up -d

Si vous avez modifié le Dockerfile ou le code :

docker compose up -d --build
📋 Voir les logs

Voir les logs de tous les services :

docker compose logs

Suivre les logs en temps réel :

docker compose logs -f

Voir uniquement les logs de l'API :

docker compose logs api

Voir uniquement les logs de Nginx :

docker compose logs nginx
🔍 Vérifier les conteneurs
docker compose ps

Voir les images utilisées :

docker images
🧹 Nettoyage

Pour arrêter et supprimer les conteneurs :

docker compose down

Pour supprimer également les images créées par Compose :

docker compose down --rmi local

⚠️ Utiliser cette commande uniquement si vous souhaitez nettoyer les images Docker du projet.

🧠 Compétences développées

Ce projet permet de pratiquer :

🐳 Docker
🧩 Docker Compose
🐍 Python
🌶️ Flask
🌐 Nginx
🔄 Reverse Proxy
🔗 Communication entre conteneurs
📦 Dockerfile
🔧 Configuration Nginx
📝 YAML
🛠️ Linux / Bash
🔍 Logs Docker
🚀 Architecture multi-conteneurs
🎯 Objectif DevOps

Ce projet représente une première approche d'une architecture composée de plusieurs services.

Utilisateur
     │
     ▼
   Nginx
     │
     ▼
 Python API

Cette architecture peut ensuite évoluer vers :

Utilisateur
     │
     ▼
Load Balancer
     │
     ▼
   Nginx
     │
     ├──────────┐
     ▼          ▼
 API 1        API 2
     │          │
     └────┬─────┘
          ▼
       Database
📚 Commandes principales
Commande	Utilisation
docker compose up -d --build	Construire et démarrer
docker compose ps	Voir les conteneurs
docker compose logs	Voir les logs
docker compose logs -f	Suivre les logs
docker compose down	Arrêter le projet
docker compose restart	Redémarrer les services
docker compose build	Reconstruire les images
👩🏾‍💻 Projet réalisé par

Cisse Ndeye

Ingénieure DevOps / Systèmes & Réseaux / Cybersécurité
Data & Programmation

GitHub : https://github.com/cis-debug

⭐ Projet réalisé dans le cadre de mon parcours de pratique DevOps / Linux / Docker / Automatisation.

donne moi que ce que je dois mettre sur mon readme

Oui 👍 Voici uniquement le contenu à mettre dans ton README.md. Copie-colle tout le bloc :

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





