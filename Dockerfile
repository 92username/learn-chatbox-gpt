# Dockerfile para rodar Streamlit com OpenAI de forma compatível
FROM python:3.12-slim

# Evita prompts no build
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema (evita erros com streamlit/openai)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Variáveis de ambiente (opcional)
ENV HTTP_PROXY=
ENV HTTPS_PROXY=

# Comando para iniciar o app com acesso externo
CMD ["streamlit", "run", "form.py", "--server.address=0.0.0.0"]
