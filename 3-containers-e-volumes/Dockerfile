# Base da imagem Docker a ser utilizada
FROM python:3.9-alpine

# Adicionar o interpretador de comandos bash
RUN apk update && apk add bash

# Adicionar a camada que será o diretório padrão a ser utilizado
WORKDIR /app

# Comando para o container não parar após a leitura de todas as camadas
ENTRYPOINT ["tail", "-f", "/dev/null"]