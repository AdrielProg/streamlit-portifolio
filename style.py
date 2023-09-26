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
         background-image: url(https://img.freepik.com/fotos-gratis/fundo-preto-antigo-textura-do-grunge-papel-de-parede-escuro-quadro-negro-quadro-negro-parede-da-sala_1258-28312.jpg?w=1380&t=st=1695749202~exp=1695749802~hmac=7465f15a1f95d3ecd6732aa1e7f4ec9005a729e62929fa735daf62dead56c005);
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
  

   
  
