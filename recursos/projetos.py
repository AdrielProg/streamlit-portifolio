import streamlit as st
from recursos import styles

def exibir_projetos():
    st.header("Projetos")
    st.write("Aqui estão alguns dos projetos em que trabalhei:")

    # Informações sobre os projetos
    projetos = [
        {
            "nome": "FinanceiraMente",
            "descricao": "Este é um projeto aplicado da Faculdade XPE desenvolvido pelo Squad 1. O objetivo principal deste projeto é promover a educação financeira de forma simples e interativa, tornando os conceitos financeiros básicos mais acessíveis ao público em geral. O FinanceiraMente é uma página web interativa que oferece uma variedade de recursos para ensinar educação financeira de maneira envolvente e intuitiva, incluindo um jogo de perguntas e respostas, calculadoras financeiras e conteúdo educativo",
            "link_github": "https://github.com/FinanceiraMente/projeto_aplicado_XPE"
        },
        {
            "nome": "X-men Project",
            "descricao": "O projeto 'X-men Project' é uma aplicação interativa desenvolvida em JavaScript, HTML e CSS que permite aos usuários explorar e aprender mais sobre os famosos personagens da série de quadrinhos X-Men. Este projeto oferece uma experiência envolvente, onde os usuários podem selecionar diferentes personagens e obter informações detalhadas sobre eles.",
            "link_github": "https://github.com/AdrielProg/x-men-project"
        },
        {
            "nome": "Simulador de iPhone em Java",
            "descricao": "Este é um projeto de Simulador de iPhone em Java que visa demonstrar conceitos de programação orientada a objetos.",
            "link_github": "https://github.com/AdrielProg/Dio-Trilha-Java-Basico-Diagrama-Iphone"
        }
    ]

    # Chame o estilo CSS personalizado
    st.markdown(styles.estilo, unsafe_allow_html=True)

    # Loop através dos projetos e exibição com expander
    for projeto in projetos:
      with    st.expander(f"{projeto['nome']}"):
              st.markdown(projeto["descricao"])
              st.markdown(
                f'<a href="{projeto["link_github"]}" target="_blank" class="link-externo">Clique aqui para acessar o projeto no GitHub</a>',
                unsafe_allow_html=True
            )

# Chame a função para exibir os projetos

