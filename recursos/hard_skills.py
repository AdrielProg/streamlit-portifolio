import streamlit as st


# Defina um estilo CSS personalizado
custom_css = f"""
    <style>
        .streamlit-expander {{
            background-color: #0A0127;
            border: 2px solid #00A86B;
            border-radius: 10px; 
        }}
        .streamlit-expanderHeader {{
            color: #00A86B;;
            font-size: 25px; /* Aumenta o tamanho da fonte do cabeçalho */
        }}
    </style>
"""


def mostrar_hard_skills():
    st.header("Hard Skills")

    # Lista de linguagens de programação
    linguagens = [
        {"nome": "Spring Boot", "progresso": 30},
        {"nome": "Java", "progresso": 85},
        {"nome": "DataBase", "progresso": 45},
        {"nome": "Python", "progresso": 60},
        {"nome": "JavaScript", "progresso": 60},
    ]
    st.markdown(custom_css, unsafe_allow_html=True)

    # Use um único expander com o atributo data-testid
    with st.expander("Minhas Hard Skills"):
        for linguagem in linguagens:
            st.markdown(f'<p>{linguagem["nome"]}</p>', unsafe_allow_html=True)
            st.progress(linguagem["progresso"])
           