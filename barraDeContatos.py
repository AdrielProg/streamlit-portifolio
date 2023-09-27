import streamlit as st
def barra_contatos():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/adriel-alexs/)")
    with col2:
        st.write("[![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/AdrielProg)")   

    with col3:
        st.write("[![Email](https://img.icons8.com/fluency/48/email.png)](mailto:adriel.alexs123@gmail.com)")  
    with col4:
        st.write("[![Telefone](https://img.icons8.com/fluency/48/phone.png)](tel:+5583998178892)")