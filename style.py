# style.py

import streamlit as st

def set_custom_style():
    # Personalize a aparência do aplicativo
    st.set_page_config(
        page_title="Meu Portfólio",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Define a cor de fundo da barra lateral
color_page = """
        <style>
        .css-6qob1r{
             background-image: url(https://st2.depositphotos.com/23139684/49123/i/600/depositphotos_491233374-stock-photo-abstract-blurred-background-defocused-blue.jpg);
         background-size: cover;

        </style>
        """
    


   
  
