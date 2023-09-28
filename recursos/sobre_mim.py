import streamlit as st
from recursos import styles
def sobre_mim():
    conteudo_sobre_mim = """
<div class="secao-sobre-mim">
    <h2 class="titulo-secao">Sobre Mim</h2>
    <p class="paragrafo-introducao">Olá! &#128075; Sou um entusiasta de desenvolvimento de software, recentemente graduado no bootcamp de BackEnd Java da DIO.</p>
    <p class="paragrafo-introducao">Tenho muita  paixão e foco por programação orientada a objetos, especialmente na linguagem Java, gosto muito de tecnologia e exploro,constatemente, outras linguagens de programação &#9749;.</p>
    <p class="paragrafo-introducao">Além disso, sou estudante de Análise e Desenvolvimento de Sistemas na Faculdade XP, buscando constantemente aprimorar minhas habilidades e conhecimentos.</p>
    <div class="habilidades">
    <p class="paragrafo-introducao">Nas horas vagas, sou um grande fã de video games, especialmente League of Legends, onde busco melhorar minhas habilidades em partidas ranqueadas.</p>
    <p class="paragrafo-introducao">Também sou um cuidadoso dono de um gato de estimação chamado Tapioca (Ele é muito branco), que é uma fonte constante de alegria pra mim, mas isso é indiferente para ele. &#128049;</p>
    <p class="paragrafo-introducao">Estou ansioso para contribuir com ideias inovadoras, participar de equipes colaborativas e comunicativas e continuar minha jornada no mundo do desenvolvimento de software.</p>
    <p class="paragrafo-introducao">Conecte-se comigo no <a class="link-externo" href="https://www.linkedin.com/in/Adriel-alexs/" target="_blank">LinkedIn</a> para oportunidades de aprendizado e colaboração!</p>
    <p class="paragrafo-introducao">Confira meus trabalhos acadêmicos no <a class="link-externo" href="https://github.com/AdrielProg" target="_blank">GitHub</a> &#128187;</p>
</div>
"""
    st.markdown(styles.estilo, unsafe_allow_html=True)
    st.markdown(conteudo_sobre_mim, unsafe_allow_html=True)