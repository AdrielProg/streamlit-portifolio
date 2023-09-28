import streamlit as st

def mostrar_experiencia():
     st.header("Experiência Acadêmica")
     experiencia = """
    <div class="categoria">
        <h2>Ensino Superior</h2>
            <h3>XP Educação</h3>
            <p>Análise e Desenvolvimento de Sistemas</p>
            <p>Outubro de 2022 - 2025</p>
            <p>Competências: Programação Orientada a Objetos (POO), Python, HTML, CSS</p>
        </div>
    <div class="categoria">
        <h2>Ensino Médio</h2>
            <h3>IFRN</h3>
            <p>Ensino Médio, Técnico em Eletrotécnica</p>
            <p>Maio de 2014 - Dezembro de 2018</p>
            <p>Competências: Inglês</p>
        </div>
    <div class="categoria">
        <h2>Demais Cursos e Bootcamps</h2>
            <h3>Udemy Alumni</h3>
            <p>Java Completo 2023 Programação Orientada a Objetos + Projetos</p>
            <p>Nota: Em andamento</p>
            <p>Curso completo de Java e OO, UML, JDBC, JavaFX, Spring Boot, JPA, Hibernate, MySQL, MongoDB</p>
            <p>Competências: Java · Programação Orientada a Objetos (POO)</p>  
    </div>

"""

     st.markdown(experiencia, unsafe_allow_html=True)