import streamlit as st

projetos = [
    {
        "nome": "Projeto 1",
        "descricao": "Descrição do Projeto 1",
        "link_github": "https://github.com/projeto1",
    },
    {
        "nome": "Projeto 2",
        "descricao": "Descrição do Projeto 2",
        "link_github": "https://github.com/projeto2",
    },
]

for projeto in projetos:
    with st.expander(f'{projeto["nome"]}'):
        st.markdown(projeto["descricao"])
        st.markdown(
            f'[Clique aqui para acessar o projeto no GitHub]({projeto["link_github"]})',
            unsafe_allow_html=True
        )