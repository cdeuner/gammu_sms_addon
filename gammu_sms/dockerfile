FROM debian:bullseye

# Installer dépendances
RUN apt-get update && \
    apt-get install -y gammu gammu-smsd python3 python3-pip && \
    pip3 install flask && \
    apt-get clean

# Copier les fichiers de l'add-on
COPY run.py /run.py
COPY gammurc /root/.gammurc

# Exposer le port du serveur Flask
EXPOSE 5005

# Commande de démarrage
CMD ["python3", "/run.py"]
