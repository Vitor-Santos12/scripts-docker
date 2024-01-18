# Base da imagem Docker a ser utilizada
FROM python:3.9-alpine

# Defina a variável de ambiente PYTHONUNBUFFERED para garantir a saída em tempo real
ENV PYTHONUNBUFFERED 1

# Configurar terminal interativo
ENV TERM=xterm-256color

# Copie arquivos ou pastas da origem para o caminho de destino no sistema de arquivos da imagem.
COPY . .

# Configura o contêiner para ser executado como um executável.
ENTRYPOINT ["python","script.py"]