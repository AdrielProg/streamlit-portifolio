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
           background: linear-gradient(190deg, #01392B, black);
           color: grey;
           }
        .main{
        background-color: red; 
         background-image: url(https://c4.wallpaperflare.com/wallpaper/404/355/659/concrete-texture-dark-background-abstract-hd-wallpaper-preview.jpg);
         background-repeat: no-repeat;
         background-size: cover;
        }
        .css-1avcm0n{
       
        background: linear-gradient(60deg, #01392B, black);
        }
        </style>
        """
    


   
  
