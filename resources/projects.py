import streamlit as st

custom_css = f"""
    <style>
        .streamlit-expander {{
            background-color: #0A0127;
            border: 2px solid #3dd56d;
            border-radius: 10px; 
        }}
        .streamlit-expanderHeader {{
            color: #3dd56d;;
            font-size: 25px; /* Increase header font size */
        }}
        .st-emotion-cache-1d9fzic p{{
            font-size:24px
        }}
    </style>
"""

def display_projects():

    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")

    projects = [
        {
            "name": "Hotels-API",
            "description": "The Hotels-API ASP.NET project is a RESTful API designed to streamline hotel management. It provides essential CRUD (Create, Read, Update, Delete) operations for managing hotels, rooms and reservation",
            "github_link": "https://github.com/AdrielProg/hotels-api-asp.net"
        },
        {
            "name": "Banking Management API",
            "description": "project is a Spring Boot/JPA application demonstrating basic user management for banking systems. It currently allows user creation and retrieval by ID, with future plans for full CRUD functionality. Developed in collaboration with DIO, this project serves as a foundation for building more comprehensive banking applications.",
            "github_link": "https://github.com/AdrielProg/bootcamp-santander-api-restful"
        },
        {
            "name": "FinanceiraMente",
            "description": "This is an applied project from Faculdade XPE developed by Squad 1. The main objective of this project is to promote financial education in a simple and interactive way, making basic financial concepts more accessible to the general public. FinanceiraMente is an interactive web page that offers a variety of resources to teach financial education in an engaging and intuitive way, including a quiz game, financial calculators, and educational content.",
            "github_link": "https://github.com/FinanceiraMente/projeto_aplicado_XPE"
        },
        {
            "name": "X-men Project",
            "description": "The 'X-men Project' is an interactive application developed in JavaScript, HTML, and CSS that allows users to explore and learn more about the famous characters from the X-Men comic book series. This project offers an engaging experience where users can select different characters and get detailed information about them.",
            "github_link": "https://github.com/AdrielProg/x-men-project"
        },
        {
            "name": "iPhone Simulator in Java",
            "description": "This is an iPhone Simulator project in Java that aims to demonstrate object-oriented programming concepts.",
            "github_link": "https://github.com/AdrielProg/Dio-Trilha-Java-Basico-Diagrama-Iphone"
        }
    ]

    st.markdown(custom_css, unsafe_allow_html=True)

    for project in projects:
        with st.expander(project["name"]):
            st.markdown(project["description"])
            st.markdown(
                f'<a href="{project["github_link"]}" target="_blank" class="link-externo">Click here to access the project on GitHub</a>',
                unsafe_allow_html=True
            )

display_projects()
