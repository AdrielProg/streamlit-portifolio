import streamlit as st
from recursos.paginaPrincipal import show_pagina_principal
from recursos import sobre_mim , hard_skills , projetos , experiencia
from recursos.sorfSkills import mostrar_habilidades_interpessoais



show_pagina_principal()

# Sidebar com links para as páginas
pagina_selecionada = st.sidebar.radio("Navegue", ["\U0001F464 Sobre Mim", "\U0001F4BB Projetos", "\U0001F4A1 Hard Skills", "\U0001F4AC Soft Skills", "\U0001F4DA Experiência Acadêmica"])

# Seção 'Sobre Mim'
if pagina_selecionada == "\U0001F464 Sobre Mim":
    sobre_mim.sobre_mim()
    
# Seção 'Habilidades'
elif pagina_selecionada == "\U0001F4AC Soft Skills":
   mostrar_habilidades_interpessoais()


   

# Seção 'Projetos'
elif pagina_selecionada == "\U0001F4BB Projetos":
    projetos.exibir_projetos()


# Seção 'Hard Skills'
elif pagina_selecionada == "\U0001F4A1 Hard Skills":
   hard_skills.mostrar_hard_skills()


# Seção 'Experiência Acadêmica'
elif pagina_selecionada == "\U0001F4DA Experiência Acadêmica":
     experiencia.mostrar_experiencia()
