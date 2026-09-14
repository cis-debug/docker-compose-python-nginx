# Image Python officielle (slim = plus léger)
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier le code
COPY app.py /app/app.py

# Installer Flask (dépendance de l'API)
RUN pip install --no-cache-dir flask

# Documentation: l'API écoute sur 5000
EXPOSE 5000

# Lancer l'API
CMD ["python", "/app/app.py"]
