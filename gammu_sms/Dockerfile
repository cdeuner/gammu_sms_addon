FROM alpine:3.19

# Installer python3, pip, gammu et dépendances build nécessaires
RUN apk add --no-cache python3 py3-pip gammu \
    build-base libffi-dev openssl-dev musl-dev cargo

# Mettre à jour pip et installer Flask
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install flask

COPY gammurc /root/.gammurc
COPY run.py /run.py

EXPOSE 5005

CMD ["python3", "/run.py"]

