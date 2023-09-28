# modules/paginaPrincipal.py
import streamlit as st
import recursos.styles as stl
import recursos.barraDeContatos as bc


def show_pagina_principal():
    st.set_page_config(
        page_title="Meu Portfólio",
        page_icon=":computer:",
        initial_sidebar_state="expanded",
    )
    st.markdown(stl.estilo, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image('Adriel2.png')
        badge_info_list = bc.adciona_badges()
        bc.start(badge_info_list)
        badge_list = [bc.generate_badge(image_url, link) for image_url, link in badge_info_list]

        # Engloba as divs de badge dentro de uma div container
        st.markdown('<div class="badge-container">' + ''.join(badge_list) + '</div>', unsafe_allow_html=True)
    
    with col2:
        st.write("""
        <div class="container" style="text-align: center; margin-top: -4px;">
            <h1 class='titulo-personalizado' style='color: #00A86B; background-color: #190431;'>Adriel Alexander</h1>
        </div>
        <div class = "descricao-principal"> 
        <h6 class = texto-1>Graduando Em Analise e Desenvolvimento de Sistemas Pela XPE</h6>
        <h6 class="texto-2">Desenvolvedor Java</h6>
        <h6 class="texto-3">Apaixonado pelo mundo tech</h6>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr style="border: 1px solid #00A86B; border-style: none none solid none; margin-bottom: 40px;">', unsafe_allow_html=True)
