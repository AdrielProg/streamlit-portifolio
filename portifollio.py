import streamlit as st
from recursos.paginaPrincipal import mostrar_pagina_principal
from recursos import sobre_mim , hard_skills , projetos , experiencia
from recursos.sorfSkills import mostrar_habilidades_interpessoais



mostrar_pagina_principal()


pagina_selecionada = st.sidebar.radio("Portifólio", ["\U0001F464 Sobre Mim", "\U0001F4BB Projetos", "\U0001F4A1 Hard Skills", "\U0001F4AC Soft Skills", "\U0001F4DA Experiência Acadêmica"])


if pagina_selecionada == "\U0001F464 Sobre Mim":
    sobre_mim.sobre_mim()
    

elif pagina_selecionada == "\U0001F4AC Soft Skills":
   mostrar_habilidades_interpessoais()


elif pagina_selecionada == "\U0001F4BB Projetos":
    projetos.exibir_projetos()


elif pagina_selecionada == "\U0001F4A1 Hard Skills":
   hard_skills.mostrar_hard_skills()


elif pagina_selecionada == "\U0001F4DA Experiência Acadêmica":
     experiencia.mostrar_experiencia()
