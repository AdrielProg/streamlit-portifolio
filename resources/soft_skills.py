import streamlit as st

def display_interpersonal_skills():

    st.header("Interpersonal Skills")

    title_html = "<h1 style='color: white;'>Individual Development Plan (IDP) Proposal</h1>"
    st.markdown(title_html, unsafe_allow_html=True)

    interpersonal_skills_content = """
    <p>The Individual Development Plan (IDP) is a valuable tool for my personal and professional growth. Through this plan, I aim to enhance my skills, acquire new knowledge, and achieve meaningful goals. <a class="link-externo" href="https://online.igti.com.br/eportfolios/2585?verifier=W6qU2RuJtOLvvZQzQLFFhskQ2tOzOdxP3PIn9kZv" target="_blank">Check out my IDP</a></p>

    <div class="list-container">
    <h2 class="subtitle">IDP Objectives</h2>
        <ul class="objectives-list">
            <li><strong>Professional Development</strong>: Through the IDP, I intend to refine my technical skills and professional competencies, becoming a more effective and valuable team member.</li>
            <li><strong>Continuous Learning</strong>: I have set goals for continuous learning, including exploring new technologies, deepening my understanding of key concepts, and participating in relevant courses.</li>
            <li><strong>Personal Growth</strong>: Beyond professional development, the IDP also focuses on my personal growth, fostering interpersonal skills, emotional resilience, and work-life balance.</li>
            <li><strong>Community Contribution</strong>: I aim to apply what I learn not only for my own benefit but also to contribute positively to the community and the teams I collaborate with.</li>
        </ul>
    </div>

    <div class="list-container">
    <h2 class="subtitle">IDP Methodology</h2>
        <ul class="methodology-list">
            <li><strong>70%</strong>: Most of my development will come from hands-on experience and day-to-day work.</li>
            <li><strong>20%</strong>: I also value learning through interaction with colleagues and mentors, exchanging experiences and knowledge.</li>
            <li><strong>10%</strong>: I will complement my IDP with formal learning, including courses, readings, and workshops.</li>
        </ul>
    </div>

    <div class="list-container">
    <h2 class="subtitle">Commitment to the IDP</h2>
    <p>This IDP reflects my commitment to continuous growth and improvement. I believe that investing in my own development is essential to achieving my professional and personal goals.</p>
    <p>Throughout this process, I am eager to learn, evolve, and contribute meaningfully to the teams and communities I am a part of.</p>
    <p>Together, we can build a bright future full of opportunities.</p>
    </div>
    """

    st.markdown(interpersonal_skills_content, unsafe_allow_html=True)