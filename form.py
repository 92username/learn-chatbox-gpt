import openai
import os
import time
import streamlit as st

# Função para gerar exercícios
def gerar_exercicios(linguagem, niveis, tema, quantidades):
    prompt = "vamos definir um nivel de dificuldade crescente para elaborarmos exercicios para que eu aprenda python de forma direta e descomplicada.Utilizar a seguinte escala de 1 a 5, onde o nível 1 é Muito Fácil e o nível 5 é Muito dificil.  Portanto, é uma escala de dificuldade crescente, separada em níveis de dificuldade.Utilize esses parametros para elaborar os exercícios, do nível 1 ao 5: 1: Exercicio muito Fácil: para a fixação dos conceitos básicos do conteudo atual. 2: Exercicio Fácil: Após o entendimento dos conceitos básicos, o aluno deve começar a saber como utilizar esses conceitos no código. 3: Exercicío Médio: Com os conceitos básicos fixados e aprendidos pelo aluno, o código começa a ganhar corpo e ter elaboração concatenando idéias e conceitos aprendidos anteriormente.  4: Exercício Difícil: Concatenar o conteudo atual com o conteudo aprendido anteriormente com nivel de dificuldade 4. Utilização elaborada do conteudo atual com conteúdos aprendidos anteriormente.  5: Exercício Muito difícil:  Elaborar exercícios que utilize todos os conceitos aprendidos anteriormente, de forma elaborada, preferencialmente tentar utilizar o máximo de conceitos possiveis dentro do que já foi estudado pelo aluno anteriormente, sendo que todos esses conceitos devem estar em um nível dificil de ser realizado."
    for i, nivel in enumerate(niveis):
        if quantidades[i] > 0:
            prompt += f"Elabore {quantidades[i]} exercícios sobre {tema} no nível de dificuldade {nivel}.\n"
    
    # Chamada à API do OpenAI usando o método chat completions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que gera exercícios de programação."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,  # Limitar a quantidade de tokens
        temperature=0.7,
    )
    
    return response['choices'][0]['message']['content'].strip()

# Função principal
def main():
    st.markdown("<h1 style='color:#00FF00;'>Gerador de Exercícios com GPT</h1>", unsafe_allow_html=True)
    
    # Inserir a chave da API na tela
    api_key = st.text_input("Insira sua chave API do OpenAI", type="password")
    
    if api_key:
        openai.api_key = api_key  # Configura a chave da API informada pelo usuário
    
        with st.form("formulario_exercicios"):
            # Seleção de linguagem e tema
            linguagem = st.selectbox("Linguagem de Programação", ["Python", "Shell", "Rust", "JavaScript"])
            tema = st.text_input("Tema Específico (Ex.: Listas, Funções)", value="Listas")
            
            # Campos para inserir a quantidade de exercícios para cada nível
            quantidade_nivel1 = st.number_input("Quantidade de exercícios para Nível 1: Muito Fácil", min_value=0, max_value=20, value=0, step=1)
            quantidade_nivel2 = st.number_input("Quantidade de exercícios para Nível 2: Fácil", min_value=0, max_value=20, value=0, step=1)
            quantidade_nivel3 = st.number_input("Quantidade de exercícios para Nível 3: Médio", min_value=0, max_value=20, value=0, step=1)
            quantidade_nivel4 = st.number_input("Quantidade de exercícios para Nível 4: Difícil", min_value=0, max_value=20, value=0, step=1)
            quantidade_nivel5 = st.number_input("Quantidade de exercícios para Nível 5: Muito Difícil", min_value=0, max_value=20, value=0, step=1)
            
            submit_button = st.form_submit_button("Gerar Exercícios")

        if submit_button:
            # Coletar as quantidades e níveis selecionados
            niveis = [1, 2, 3, 4, 5]
            quantidades = [quantidade_nivel1, quantidade_nivel2, quantidade_nivel3, quantidade_nivel4, quantidade_nivel5]
            
            if any(q > 0 for q in quantidades):  # Verifica se pelo menos um nível tem quantidade > 0
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
    else:
        st.warning("Por favor, insira a chave da API para continuar.")

if __name__ == "__main__":
    main()
