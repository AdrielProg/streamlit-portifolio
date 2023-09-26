import streamlit as st
import style as stl 
from style import color_page  

stl.set_custom_style()
st.markdown(color_page, unsafe_allow_html=True)

# Definindo o título do aplicativo
st.title("Adriel Alexander")

# Adicionando a imagem de perfil com estilo
st.markdown(
    f'<img src="https://i.imgur.com/Ux9sLQp.jpg" alt="Foto de Perfil" width="200" height="200" style="border-radius: 50%;">',
    unsafe_allow_html=True
)

# Sidebar com links para as páginas
pagina_selecionada = st.sidebar.radio("Navegue", ["\U0001F464 Sobre Mim", "\U0001F4AC Soft Skills", "\U0001F4A1 Hard Skills", "\U0001F4BB Projetos", "\U0001F4DA Experiência Acadêmica", "\U0001F4E7 Contato"])


# Seção 'Sobre Mim'
if pagina_selecionada == "\U0001F464 Sobre Mim":
    st.header("Sobre Mim")
    markdown_text = """
    Olá! \U0001F44B Sou um entusiasta de desenvolvimento de software, recentemente graduado no bootcamp de BackEnd Java da DIO. 
    Tenho uma paixão ardente por programação orientada a objetos, especialmente na linguagem Java \U00002615. 

    Além disso, sou estudante de Análise e Desenvolvimento de Sistemas na Faculdade XP, 
    buscando constantemente aprimorar minhas habilidades e conhecimentos.

    \U0001F4A1 Minhas Habilidades:
    - Desenvolvimento de Aplicativos Java
    - Conhecimentos em MySQL (MariaDB) e NoSQL (MongoDB)

    \U0001F3AE Nas horas vagas, sou um grande fã de video games, especialmente League of Legends, 
    onde busco melhorar minhas habilidades em partidas ranqueadas.

    \U0001F431 Também sou um orgulhoso dono de um gato de estimação, que é uma fonte constante de alegria e inspiração.

    \U00002B50 Estou ansioso para contribuir com ideias inovadoras, participar de equipes colaborativas e comunicativas e 
    continuar minha jornada no mundo do desenvolvimento de software.

    Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/Adriel-alexs/) para oportunidades de aprendizado e colaboração!  
    
    Confira meus trabalho acadêmicos no [GitHub](https://github.com/AdrielProg). \U0001F4BB
    """
    
    st.markdown(markdown_text, unsafe_allow_html=True)

# Seção 'Habilidades'
elif pagina_selecionada == "\U0001F4AC Soft Skills":
    st.header("Habilidades Interpessoais")
    st.markdown("# Proposta do Plano de Desenvolvimento Individual (PDI)")

    st.write("O Plano de Desenvolvimento Individual (PDI) é uma ferramenta valiosa para o meu crescimento pessoal e profissional. Através deste plano, busco aprimorar minhas habilidades, adquirir novos conhecimentos e alcançar metas significativas. [Confira meu PDI](https://online.igti.com.br/eportfolios/2585?verifier=W6qU2RuJtOLvvZQzQLFFhskQ2tOzOdxP3PIn9kZv)")
    

    st.markdown("## Objetivos do PDI")
    st.write("- **Desenvolvimento Profissional**: Através do PDI, pretendo aperfeiçoar minhas habilidades técnicas e competências profissionais, tornando-me um membro mais eficaz e valioso para a equipe.")
    st.write("- **Aprendizado Contínuo**: Estabeleci metas de aprendizado contínuo, incluindo a exploração de novas tecnologias, aprofundamento em conceitos-chave e a participação em cursos relevantes.")
    st.write("- **Crescimento Pessoal**: Além do desenvolvimento profissional, o PDI também se concentra no meu crescimento pessoal, promovendo habilidades interpessoais, resiliência emocional e equilíbrio entre trabalho e vida pessoal.")
    st.write("- **Contribuição para a Comunidade**: Tenho o objetivo de aplicar o que aprendo não apenas em benefício próprio, mas também para contribuir positivamente para a comunidade e para as equipes com as quais colaboro.")

    st.markdown("## Metodologia do PDI")
    st.write("O PDI será conduzido de acordo com o modelo 70/20/10, que enfatiza a importância de diferentes formas de aprendizado:")
    st.write("- **70%**: A maior parte do meu desenvolvimento virá da experiência prática e do trabalho do dia-a-dia.")
    st.write("- **20%**: Também valorizo a aprendizagem por meio da interação com colegas e mentores, trocando experiências e conhecimentos.")
    st.write("- **10%**: Complementarei meu PDI com aprendizado formal, incluindo cursos, leituras e workshops.")

    st.markdown("## Compromisso com o PDI")
    st.write("Este PDI reflete meu compromisso com o crescimento e o aprimoramento contínuos. Acredito que investir em meu próprio desenvolvimento é fundamental para alcançar meus objetivos profissionais e pessoais.")
    st.write("Ao longo deste processo, estou ansioso para aprender, evoluir e contribuir de maneira significativa para as equipes e comunidades das quais faço parte.")
    st.write("Juntos, podemos construir um futuro brilhante e cheio de oportunidades.")
   

# Seção 'Projetos'
elif pagina_selecionada == "\U0001F4BB Projetos":
    st.header("Projetos")
    st.write("Aqui estão alguns dos projetos em que trabalhei:")

    # Projeto 1
    st.write("## FinanceiraMente")
    st.write("Bem-vindo ao projeto FinanceiraMente! Este é um projeto aplicado da Faculdade XPE desenvolvido pelo Squad 1. O objetivo principal deste projeto é promover a educação financeira de forma simples e interativa, tornando os conceitos financeiros básicos mais acessíveis ao público em geral. O FinanceiraMente é uma página web interativa que oferece uma variedade de recursos para ensinar educação financeira de maneira envolvente e intuitiva, incluindo um jogo de perguntas e respostas, calculadoras financeiras e conteúdo educativo.")
    st.write("[Clique aqui para acessar o FinanceiraMente](https://projetoaplicadoxpe-financeiramente.streamlit.app)")

    st.write("## X-men Project")
    st.write("O projeto 'X-men Project' é uma aplicação interativa desenvolvida em JavaScript, HTML e CSS que permite aos usuários explorar e aprender mais sobre os famosos personagens da série de quadrinhos X-Men. Este projeto oferece uma experiência envolvente, onde os usuários podem selecionar diferentes personagens e obter informações detalhadas sobre eles.")
    st.write("[Clique aqui para acessar o X-men Project](https://adrielprog.github.io/x-men-project/)")
    # Projeto 2
   

# Título do projeto e link
    st.write("## Simulador de iPhone em Java")
    st.write("Este é um projeto de Simulador de iPhone em Java que visa demonstrar conceitos de programação orientada a objetos.")
    st.write("[Clique aqui para acessar o projeto no GitHub](https://github.com/AdrielProg/Dio-Trilha-Java-Basico-Diagrama-Iphone)")


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

  

# Título da seção
    st.write("## Experiência Acadêmica")

    st.write("### Ensino Superior")

# XP Educação
    st.write("**XP Educação**")
    st.write("Análise e Desenvolvimento de Sistemas")
    st.write("Outubro de 2022 - 2025")
    st.write("Competências: Programação Orientada a Objetos (POO), python, HTML, CSS")

    # Universidade Federal da Paraíba
    st.write("### Ensino Médio")

# IFRN
    st.write("**IFRN**")
    st.write("Ensino Médio, Técnico em Eletrotécnica")
    st.write("Maio de 2014 - Dezembro de 2018")
    st.write("Competências: Inglês")

    st.write("### Demais Cursos e Bootcamps")
    # Udemy Alumni
    st.write("**Udemy Alumni**")
    st.write("Java Completo 2023 Programação Orientada a Objetos + Projetos")
    st.write("Nota: Em andamento")
    st.write("Curso completo de Java e OO, UML, JDBC, JavaFX, Spring Boot, JPA, Hibernate, MySQL, MongoDB")
    st.write("Competências: Java · Programação Orientada a Objetos (POO)")


    # Rodapé
st.sidebar.write("Desenvolvido por Adriel Alexander de Sousa")
