import os
import time
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key não encontrada. Verifique se o arquivo .env está configurado corretamente.")
print("API key encontrada. Inicializando o aplicativo...")

openai.api_key = api_key

lista_linguagens = ["Python", "JavaScript", "Java", "C++", "C#", "Dart"]

def gerar_exercicios(linguagem, niveis, tema, quantidades):
    """
    Gera exercícios de programação com base na linguagem, níveis, tema e quantidades fornecidos.

    Args:
        linguagem (str): A linguagem de programação para os exercícios.
        niveis (list): Uma lista de níveis de dificuldade.
        tema (str): O tema dos exercícios.
        quantidades (list): A quantidade de exercícios para cada nível.

    Returns:
        str: Os exercícios gerados pela API OpenAI.
    """

    messages = [
        {
            "role": "system",
            "content": (
                f"""Você é um gerador de exercícios de programação. Não exibir as respostas dos exercícios.
                Vamos definir um nível de dificuldade crescente para elaborarmos exercícios para que 
                eu aprenda {', '.join(lista_linguagens)} de programação de forma direta e descomplicada. 
                Utilize uma escala de 1 a 5, onde o nível 1 é 'Muito Fácil' e o 
                nível 5 é 'Muito Difícil'. Elabore exercícios 
                para cada nível com base na seguinte descrição:
                - Nível 1: Conceitos básicos e fixação.
                - Nível 2: Aplicação de conceitos básicos.
                - Nível 3: Construção de lógica com conceitos aprendidos.
                - Nível 4: Integração com conteúdos anteriores.
                - Nível 5: Uso avançado de todos os conceitos estudados."""
            )
        },
        {
            "role": "user",
            "content": f"Crie exercícios de {linguagem} sobre o tema {tema}."
        }
    ]
    for i, nivel in enumerate(niveis):
        if quantidades[i] > 0:
            messages.append({
                "role": "user",
                "content": f"Elabore {quantidades[i]} exercícios no nível {nivel}."
            })    

    # Chamada à API OpenAI
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",      
        messages=messages,
        max_tokens=1000,  # Limitar a quantidade de tokens
        temperature=0.7,
    )

    # Retornar o texto gerado pela API
    return response.choices[0].message.content.strip()

# Função principal
def main():
    st.markdown("<h1 style='color:#00FF00;'>Gerador de Exercícios com GPT</h1>", unsafe_allow_html=True)

    with st.form("formulario_exercicios"):
        # Seleção de linguagem e tema
        linguagem = st.selectbox("Linguagem de Programação", ["Python", "JavaScript", "Java", "C++", "C#", "Dart"], format_func=lambda x: "Escolha a linguagem" if x == "" else x)
        tema = st.text_input("Escolha o tema dos exercícios (Ex.: Listas, Funções, etc)", value="", placeholder="Digite o tema do exercício...")
        
        # Slider para definir o limite máximo de exercícios
        limite_exercicios = st.slider("Limite máximo de exercícios por nível", min_value=1, max_value=10, value=10)
        
        # Campos para inserir a quantidade de exercícios para cada nível
        quantidade_nivel1 = st.number_input("Quantidade de exercícios para Nível 1: Muito Fácil", min_value=0, max_value=limite_exercicios, value=0, step=1, placeholder="0")
        quantidade_nivel2 = st.number_input("Quantidade de exercícios para Nível 2: Fácil", min_value=0, max_value=limite_exercicios, value=0, step=1, placeholder="0")
        quantidade_nivel3 = st.number_input("Quantidade de exercícios para Nível 3: Médio", min_value=0, max_value=limite_exercicios, value=0, step=1, placeholder="0")
        quantidade_nivel4 = st.number_input("Quantidade de exercícios para Nível 4: Difícil", min_value=0, max_value=limite_exercicios, value=0, step=1, placeholder="0")
        quantidade_nivel5 = st.number_input("Quantidade de exercícios para Nível 5: Muito Difícil", min_value=0, max_value=limite_exercicios, value=0, step=1, placeholder="0")
        
        submit_button = st.form_submit_button("Gerar Exercícios")

    if submit_button:
        # Coletar as quantidades e níveis selecionados
        niveis = [1, 2, 3, 4, 5]
        quantidades = [quantidade_nivel1, quantidade_nivel2, quantidade_nivel3, quantidade_nivel4, quantidade_nivel5]
        
        if sum(quantidades) > 0:  # Verifica se pelo menos um nível tem quantidade > 0
            # Barra de progresso inicial (em verde)
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.05)  # Simula o tempo de processamento
                progress_bar.progress(percent_complete + 1)
            
            with st.spinner("Gerando exercícios..."):
                exercicios = gerar_exercicios(linguagem, niveis, tema, quantidades)
                st.markdown("<h3 style='color:#00FF00;'>Exercícios Gerados:</h3>", unsafe_allow_html=True)
                st.write(exercicios)
        else:
            st.warning("Por favor, insira a quantidade de exercícios para pelo menos um nível de dificuldade.")

if __name__ == "__main__":
    main()
