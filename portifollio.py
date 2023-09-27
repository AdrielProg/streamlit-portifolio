import streamlit as st
from styles import estilo
 

st.set_page_config(
        page_title="Meu Portfólio",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
)
st.markdown(estilo, unsafe_allow_html=True)
# Definindo o título do aplicativo
st.write(
  """
<div class="container" style="text-align: center; margin-top: -4px;">
    <h1 class='titulo-personalizado' style='color: white; background-color: #01392B;'>Adriel Alexander</h1>
    <div class="profile-img">
        <img src="https://i.imgur.com/Ux9sLQp.jpg" alt="Foto de Perfil" width="300" height="300" style="border-radius: 50%; max-width: 300px; border: 8px solid #01392B; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3); margin: 0 auto; margin-top: 7px;">
    </div>
</div>
""",
    unsafe_allow_html=True
)
# Sidebar com links para as páginas
pagina_selecionada = st.sidebar.radio("Navegue", ["\U0001F464 Sobre Mim", "\U0001F4AC Soft Skills", "\U0001F4A1 Hard Skills", "\U0001F4BB Projetos", "\U0001F4DA Experiência Acadêmica", "\U0001F4E7 Contato"])


# Seção 'Sobre Mim'
if pagina_selecionada == "\U0001F464 Sobre Mim":
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

    st.markdown(conteudo_sobre_mim, unsafe_allow_html=True)

# Seção 'Habilidades'
elif pagina_selecionada == "\U0001F4AC Soft Skills":
    st.header("Habilidades Interpessoais")
    titulo_html = "<h1 style='color: white;'>Proposta do Plano de Desenvolvimento Individual (PDI)</h1>"
    st.markdown(titulo_html, unsafe_allow_html=True)
    conteudo_habilidades_interpessoais = """
<p>O Plano de Desenvolvimento Individual (PDI) é uma ferramenta valiosa para o meu crescimento pessoal e profissional. Através deste plano, busco aprimorar minhas habilidades, adquirir novos conhecimentos e alcançar metas significativas. <a class="link-externo" href="https://online.igti.com.br/eportfolios/2585?verifier=W6qU2RuJtOLvvZQzQLFFhskQ2tOzOdxP3PIn9kZv" target="_blank">Confira meu PDI</a></p>

<div class="lista-container">
<h2 class="subtitulo">Objetivos do PDI</h2>
    <ul class="lista-objetivos">
        <li><strong>Desenvolvimento Profissional</strong>: Através do PDI, pretendo aperfeiçoar minhas habilidades técnicas e competências profissionais, tornando-me um membro mais eficaz e valioso para a equipe.</li>
        <li><strong>Aprendizado Contínuo</strong>: Estabeleci metas de aprendizado contínuo, incluindo a exploração de novas tecnologias, aprofundamento em conceitos-chave e a participação em cursos relevantes.</li>
        <li><strong>Crescimento Pessoal</strong>: Além do desenvolvimento profissional, o PDI também se concentra no meu crescimento pessoal, promovendo habilidades interpessoais, resiliência emocional e equilíbrio entre trabalho e vida pessoal.</li>
        <li><strong>Contribuição para a Comunidade</strong>: Tenho o objetivo de aplicar o que aprendo não apenas em benefício próprio, mas também para contribuir positivamente para a comunidade e para as equipes com as quais colaboro.</li>
    </ul>
</div>

<div class="lista-container">
<h2 class="subtitulo">Metodologia do PDI</h2>
    <ul class="lista-metodologia">
        <li><strong>70%</strong>: A maior parte do meu desenvolvimento virá da experiência prática e do trabalho do dia-a-dia.</li>
        <li><strong>20%</strong>: Também valorizo a aprendizagem por meio da interação com colegas e mentores, trocando experiências e conhecimentos.</li>
        <li><strong>10%</strong>: Complementarei meu PDI com aprendizado formal, incluindo cursos, leituras e workshops.</li>
    </ul>
</div>
<div class="lista-container">
<h2 class="subtitulo">Compromisso com o PDI</h2>
<p>Este PDI reflete meu compromisso com o crescimento e o aprimoramento contínuos. Acredito que investir em meu próprio desenvolvimento é fundamental para alcançar meus objetivos profissionais e pessoais.</p>
<p>Ao longo deste processo, estou ansioso para aprender, evoluir e contribuir de maneira significativa para as equipes e comunidades das quais faço parte.</p>
<p>Juntos, podemos construir um futuro brilhante e cheio de oportunidades.</p>
</div>
"""

    st.markdown(conteudo_habilidades_interpessoais, unsafe_allow_html=True)


   

# Seção 'Projetos'
elif pagina_selecionada == "\U0001F4BB Projetos":
    st.header("Projetos")
    st.write("Aqui estão alguns dos projetos em que trabalhei:")

    conteudo_projetos = """
    <div class="projeto">
        <h3 class="titulo-projeto">FinanceiraMente</h3>
        <p>Bem-vindo ao projeto FinanceiraMente! Este é um projeto aplicado da Faculdade XPE desenvolvido pelo Squad 1. O objetivo principal deste projeto é promover a educação financeira de forma simples e interativa, tornando os conceitos financeiros básicos mais acessíveis ao público em geral. O FinanceiraMente é uma página web interativa que oferece uma variedade de recursos para ensinar educação financeira de maneira envolvente e intuitiva, incluindo um jogo de perguntas e respostas, calculadoras financeiras e conteúdo educativo.</p>
        <a class="link-externo" href="https://projetoaplicadoxpe-financeiramente.streamlit.app" target="_blank">Clique aqui para acessar o FinanceiraMente</a>
    </div>
    <div class="projeto">
        <h3 class="titulo-projeto">X-men Project</h3>
        <p>O projeto 'X-men Project' é uma aplicação interativa desenvolvida em JavaScript, HTML e CSS que permite aos usuários explorar e aprender mais sobre os famosos personagens da série de quadrinhos X-Men. Este projeto oferece uma experiência envolvente, onde os usuários podem selecionar diferentes personagens e obter informações detalhadas sobre eles.</p>
        <a class="link-externo" href="https://adrielprog.github.io/x-men-project/" target="_blank">Clique aqui para acessar o X-men Project</a>
    </div>
    <div class="projeto">
        <h3 class="titulo-projeto">Simulador de iPhone em Java</h3>
        <p>Este é um projeto de Simulador de iPhone em Java que visa demonstrar conceitos de programação orientada a objetos.</p>
        <a class="link-externo" href="https://github.com/AdrielProg/Dio-Trilha-Java-Basico-Diagrama-Iphone" target="_blank">Clique aqui para acessar o projeto no GitHub</a>
    </div>
</div>
"""

    st.markdown(conteudo_projetos, unsafe_allow_html=True)



# Seção 'Contato'
elif pagina_selecionada == "\U0001F4E7 Contato":
    st.header("Contato")
    st.write("Ficou interessado? Entre em contato comigo!")

    st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/adriel-alexs/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/AdrielProg) [![Email](https://img.icons8.com/fluency/48/email.png)](mailto:adriel.alexs123@gmail.com) [![Telefone](https://img.icons8.com/fluency/48/phone.png)](tel:+5583998178892)")


# Seção 'Hard Skills'
elif pagina_selecionada == "\U0001F4A1 Hard Skills":
    st.header("Hard Skills")

    st.write("Spring Boot")
    st.progress(30)  

    st.write("Java")
    st.progress(85) 
    
    st.write("DataBase")
    st.progress(45)

    
    st.write("Python")
    st.progress(60)  

    
    st.write("JavaScript")
    st.progress(60) 



# Seção 'Experiência Acadêmica'
elif pagina_selecionada == "\U0001F4DA Experiência Acadêmica":
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

