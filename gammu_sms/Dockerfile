FROM alpine:3.19

# Installer gammu, python3, pip, et dépendances
RUN apk add --no-cache python3 py3-pip gammu

# Installer Flask via pip
RUN pip3 install flask

# Copier fichiers
COPY gammurc /root/.gammurc
COPY run.py /run.py

EXPOSE 5005

CMD ["python3", "/run.py"]

