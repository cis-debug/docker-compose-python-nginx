#!/usr/bin/env python3
"""
Python API (Flask)
- /api/health : endpoint de santé (healthcheck)
- /api/info   : informations simples (hostname)
"""

import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/health")
def health():
    # Utile pour vérifier que le service répond
    return jsonify(
        service="python-api",
        hostname=socket.gethostname(),
        message="Hello from Ndeye's DevOps lab!"
    )

@app.get("/api/info")
def info():
    # Dans Docker, le hostname est souvent l'ID du conteneur
    return jsonify(service="python-api", hostname=socket.gethostname())

if __name__ == "__main__":
    # host=0.0.0.0 obligatoire dans Docker, sinon ce n'est visible que depuis le conteneur
    app.run(host="0.0.0.0", port=5000)
