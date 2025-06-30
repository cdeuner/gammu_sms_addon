FROM alpine:3.19

# Installer Python3, pip, gammu et dépendances de build
RUN apk add --no-cache \
    python3 py3-pip gammu ca-certificates openssl \
    build-base libffi-dev openssl-dev musl-dev cargo py3-cryptography

# Créer un environnement virtuel
RUN python3 -m venv /venv

# Installer pip packages dans l'environnement virtuel
RUN /venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel
RUN /venv/bin/pip install --no-cache-dir flask gunicorn

# Créer le répertoire pour l'application
WORKDIR /app

# Copier fichiers de configuration et source
COPY gammurc /root/.gammurc
COPY run.py wsgi.py /app/

# Exposer le port utilisé par l'application
EXPOSE 5005

# Lancer Gunicorn via le Python du venv
#CMD ["/venv/bin/gunicorn", "wsgi:app", "--bind", "0.0.0.0:5005", "--workers", "2"]
CMD ["/venv/bin/gunicorn", "wsgi:app", "--bind", "0.0.0.0:5005", "--workers", "2", "--timeout", "60"]

