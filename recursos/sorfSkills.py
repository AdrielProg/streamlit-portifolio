import streamlit as st

def mostrar_habilidades_interpessoais():
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