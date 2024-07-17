import streamlit as st

def display_hard_skills():
  
    st.header("Hard Skills")

    skills_data = {
        "C#": 75,
        "Spring Boot": 30,
        "Java": 65,
        "Database": 85,
        "SQL": 95,
        "Python": 60,
        "JavaScript": 70,
        "Node.js": 45
    }

    for skill, proficiency in skills_data.items():
        with st.container():
            col1, col2 = st.columns([3, 7]) 
            col1.write(skill)
            col2.progress(proficiency)