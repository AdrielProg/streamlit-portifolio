import streamlit as st
def exibir_projetos():
     st.header("Projetos")
     st.write("Aqui estão alguns dos projetos em que trabalhei:")

     conteudo_projetos = """
    <div class="projeto">
        <h3 class="titulo-projeto">FinanceiraMente</h3>
        <p>Bem-vindo ao projeto FinanceiraMente! Este é um projeto aplicado da Faculdade XPE desenvolvido pelo Squad 1. O objetivo principal deste projeto é promover a educação financeira de forma simples e interativa, tornando os conceitos financeiros básicos mais acessíveis ao público em geral. O FinanceiraMente é uma página web interativa que oferece uma variedade de recursos para ensinar educação financeira de maneira envolvente e intuitiva, incluindo um jogo de perguntas e respostas, calculadoras financeiras e conteúdo educativo.</p>
        <a class="link-externo" href="https://github.com/FinanceiraMente/projeto_aplicado_XPE" target="_blank">Clique aqui para acessar o FinanceiraMente</a>
    </div>
    <div class="projeto">
        <h3 class="titulo-projeto">X-men Project</h3>
        <p>O projeto 'X-men Project' é uma aplicação interativa desenvolvida em JavaScript, HTML e CSS que permite aos usuários explorar e aprender mais sobre os famosos personagens da série de quadrinhos X-Men. Este projeto oferece uma experiência envolvente, onde os usuários podem selecionar diferentes personagens e obter informações detalhadas sobre eles.</p>
        <a class="link-externo" href="https://github.com/AdrielProg/x-men-project" target="_blank">Clique aqui para acessar o X-men Project</a>
    </div>
    <div class="projeto">
        <h3 class="titulo-projeto">Simulador de iPhone em Java</h3>
        <p>Este é um projeto de Simulador de iPhone em Java que visa demonstrar conceitos de programação orientada a objetos.</p>
        <a class="link-externo" href="https://github.com/AdrielProg/Dio-Trilha-Java-Basico-Diagrama-Iphone" target="_blank">Clique aqui para acessar o projeto no GitHub</a>
    </div>
</div>
"""

     st.markdown(conteudo_projetos, unsafe_allow_html=True)