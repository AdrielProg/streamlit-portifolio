import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon=":computer:",
    layout="wide",  
    initial_sidebar_state="expanded"  
)


from resources.main_page import display_home_page  
from resources import about_me, hard_skills, projects, experience, soft_skills # Corrected import for soft skills


display_home_page()
about_me.about_me()
