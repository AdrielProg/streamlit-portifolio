import streamlit as st
from resources import styles

def about_me():

    st.markdown(styles.style, unsafe_allow_html=True)  

    about_me_content = """
    <div class="about-me-section">
    <h2 class="section-title">About Me</h2>
    <p class="intro-paragraph">Hello! I'm a Systems Analysis and Development student at Faculdade XP. I'm passionate about technology and deeply focused on software development.  Currently, I'm sharpening my C# skills, building on my experience with T-SQL, ASP.NET MVC, Node.js, and Python.</p>
    <p class="intro-paragraph">I have a strong foundation in object-oriented programming and a keen interest in data modeling. I'm always eager to explore new technologies and broaden my skillset. 💻</p>
    <p class="intro-paragraph">My goals are to contribute to innovative projects, collaborate effectively with teams, and make a meaningful difference in the workplace. I believe in the power of continuous learning and professional growth.</p>
    <h3 class="section-subtitle">Interests & Hobbies</h3>
    <p class="intro-paragraph">When I'm not coding, you can find me immersed in the world of video games, especially League of Legends. I also enjoy spending time with my fluffy white cat, Tapioca! 🎮 🐈</p>
</div>
    """
    
    st.markdown(about_me_content, unsafe_allow_html=True)

