# 🐳 Docker Compose — Python API + Nginx

Petit projet DevOps permettant de découvrir Docker Compose et la communication entre plusieurs conteneurs.

## 🎯 Objectif

L'objectif est de créer une petite architecture composée de deux services :

- 🐍 une API Python ;
- 🌐 un serveur Nginx utilisé comme reverse proxy.

## Architecture :

```text
              Client
                 │
                 ▼
          localhost:8080
                 │
                 ▼
             🌐 Nginx
                 │
                 ▼
          🐍 Python API
              :5000



## 📁 Structure
docker-compose-python-nginx/
├── app/
│   ├── app.py
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── compose.yaml
└── README.md

🐍 Application Python

L'application Python utilise uniquement la bibliothèque standard Python.

Elle écoute sur le port :

5000

Elle retourne une réponse JSON :

{
  "message": "Hello from Python!",
  "service": "python-api",
  "status": "running"
}

🌐 Nginx
## Nginx fonctionne comme reverse proxy.
## Il reçoit les requêtes sur le port :
80

##puis les transmet au service Python :
python-api:5000

🐳 Docker Compose
##Le fichier compose.yaml définit deux services :

python-api
nginx

##Docker Compose permet de lancer les deux services avec une seule commande.

🚀 Démarrage
##Construire les images et démarrer les services :
docker compose up --build

##Pour lancer en arrière-plan :
docker compose up -d

🌐 Tester
##Dans un navigateur :
http://localhost:8080
##Ou avec curl :
curl http://localhost:8080
curl -i http://localhost:8080/
curl -i http://localhost:8080/api/health
curl -i http://localhost:8080/api/info

🔎 Vérifier les conteneurs
docker compose ps
##ou :
docker ps

📜 Voir les logs
docker compose logs

## Logs Python :
docker compose logs python-api

## Logs Nginx :
docker compose logs nginx

🛑 Arrêter / supprimer
sudo docker-compose -f compose.yaml down
