# Description: Dockerfile for Streamlit app
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8501
ENV HTTP_PROXY=
ENV HTTPS_PROXY=
CMD ["streamlit", "run", "form.py"]
