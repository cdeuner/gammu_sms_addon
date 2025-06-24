FROM alpine:3.19

# Installer Python3, pip, gammu et dépendances de build
RUN apk add --no-cache python3 py3-pip gammu ca-certificates openssl \
    build-base libffi-dev openssl-dev musl-dev cargo py3-cryptography

# Créer un environnement virtuel et installer Flask dedans
RUN python3 -m venv /venv

# Utiliser le pip du venv pour upgrade et installation
RUN /venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel
RUN /venv/bin/pip install --no-cache-dir flask

# Copier fichiers de configuration et script
COPY gammurc /root/.gammurc
COPY run.py /run.py

# Exposer le port Flask
EXPOSE 5005

# Démarrer l’application avec python du venv
CMD ["/venv/bin/python", "/run.py"]


