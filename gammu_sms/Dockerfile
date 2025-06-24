FROM alpine:3.19

# Installer gammu, python3, pip et dépendances
RUN apk add --no-cache python3 py3-pip gammu

# Installer Flask via pip
RUN pip3 install flask

# Copier les fichiers nécessaires dans le container
COPY gammurc /root/.gammurc
COPY run.py /run.py

# Exposer le port 5005 pour le serveur Flask
EXPOSE 5005

# Lancer le script Python au démarrage
CMD ["python3", "/run.py"]
