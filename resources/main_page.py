import streamlit as st
from resources import styles as stl  
from resources import contact_bar as cb 

def display_home_page():

    st.markdown(stl.style, unsafe_allow_html=True)  

    with st.container():
        image_col, info_col = st.columns(2, gap="large")

        with image_col:
            st.image('Adriel2.png')

            contact_info = cb.get_contact_info()
            badges = [cb.generate_badge(*info) for info in contact_info]
            st.markdown(f'<div class="badge-container">{" ".join(badges)}</div>', unsafe_allow_html=True)

        with info_col:
            st.markdown(
                """
                    <div class="container" style="text-align: center; margin-top: -4px;">
                        <h1 class='custom-title' style='color: #3dd56d; background-color: #0A0127;'>Adriel Alexander</h1>
                    </div>
                    <div class="main-description"> 
                        <ul>
                            <li><h6>Aspiring Software Developer & Microsoft Certified: Azure Developer Associate</h6></li>
                            <li><h6>Systems Analysis and Development Student at Faculdade XP</h6></li>
                            <li><h6>Passionate about data modeling and cloud technologies</h6></li> 
                            <li><h6>Driven to innovate, collaborate, and make a positive impact</h6></li>
                        </ul>
                    </div>
                """, 
                unsafe_allow_html=True
            )
    
    st.markdown('<div class="horizontal-line"></div>', unsafe_allow_html=True) 