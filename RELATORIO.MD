# Relatório Técnico – Projeto Chatbox GPT (DevOps)

## Visão Geral

Este documento apresenta o fluxo completo de desenvolvimento, containerização e deployment do projeto **Chatbox GPT - Gerador de Exercícios**, com foco nas práticas de DevOps utilizadas para viabilizar sua execução em produção via AWS.

---

## 1. Estrutura do Projeto

A aplicação foi desenvolvida em Python, utilizando o framework **Streamlit** para interface interativa com o usuário. Seu objetivo é gerar listas de exercícios personalizados com base em três parâmetros: linguagem de programação, tema e nível de dificuldade.

O projeto utiliza a API da OpenAI para geração dinâmica de conteúdo com inteligência artificial. O modelo utilizado é o 'gpt-3.5-turbo' para interpretar os parâmetros fornecidos pelo usuário e criar exercícios personalizados em tempo real.

### Stack Utilizada
- **Linguagem:** Python 3.x
- **Framework:** Streamlit
- **Variáveis sensíveis:** `.env` com `python-dotenv`

---

## 2. Containerização com Docker

Para facilitar o deploy e a portabilidade, a aplicação foi containerizada com Docker.

### Dockerfile
- Base: `python:3.9-slim`
- Copia do código-fonte para o container
- Exposição da porta `8501`
- Execução do comando `streamlit run form.py`

### docker-compose.yml
- Build da imagem local `learn-chatbox-gpt`
- Uso de variáveis de ambiente via `.env`
- Mapeamento da porta `8501:8501`
- Restart automático do container

---

## 3. Versionamento e CI/CD

O projeto está versionado no GitHub:

**Repositório:** [github.com/92username/learn-chatbox-gpt](https://github.com/92username/learn-chatbox-gpt)

### Práticas DevOps Adotadas:

- Planejamento para implementação de CI/CD com GitHub Actions
- CI/CD configurado com **GitHub Actions**, realizando etapas de build e deploy automatizado

---

## 4. Deploy na AWS

A aplicação foi hospedada em uma instância EC2 (Ubuntu 22.04) utilizando o Docker como ambiente de execução.

### 4.1 Acesso à Instância e Setup Inicial

O setup da instância foi realizado via terminal com autenticação por chave SSH.

### 4.2 Configuração da AWS
- Liberação da porta `8501` no Security Group
- Configuração de variáveis via `.env`
- Planejamento para HTTPS com Nginx + Certbot

---

## 5. Segurança e Boas Práticas

- Variáveis sensíveis isoladas via `.env`
- Ambiente isolado com Docker
---

## 6. Monitoramento e Expansão (Roadmap)

- Integração com Nginx como reverse proxy para domínio customizado
- Configuração HTTPS com Certbot e renovação automática
- Monitoramento de containers com Prometheus + Grafana (planejado)
---

## Conclusão

Este projeto demonstra competências técnicas em:
- Desenvolvimento Python
- Containerização com Docker
- Versionamento com Git e GitHub
- Configuração e deploy em cloud (AWS EC2)
- Boas práticas DevOps em ambientes Linux
