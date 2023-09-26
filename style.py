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
    st.markdown(
        """
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
    
         width: 100%;
         height: 100%;
     
         
        }
        .css-1avcm0n{
       
        background: linear-gradient(60deg, #01392B, black);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Define a cor de fundo das páginas
    st.markdown(
        """
        <style>
        body {
            background-color: #E6E6E6;  # Altere para a cor desejada
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
  

   
  
