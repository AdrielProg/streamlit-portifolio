import streamlit as st

def generate_badge(image_url, link, alt_text="Badge"):

    badge = f'<div class="badge-container"><a href="{link}" target="_blank"><img src="{image_url}" alt="{alt_text}" width="40px"></a></div>'
    return badge

def get_contact_info():

    return [
        ("https://img.icons8.com/fluency/48/linkedin.png", "https://www.linkedin.com/in/adriel-alexs/", "LinkedIn"),
        ("https://img.icons8.com/fluency/48/github.png", "https://github.com/AdrielProg", "GitHub"),
        ("https://img.icons8.com/fluency/48/new-post.png", "mailto:adriel.alexs123@gmail.com", "Email"),  # Updated email icon
        ("https://img.icons8.com/fluency/48/phone.png", "tel:+5583998178892", "Phone")
    ]

def contact():

    st.markdown("## Contact Me")

    contact_info = get_contact_info()
    badges = [generate_badge(*info) for info in contact_info]
    badge_html = "".join(badges) 

    st.markdown(badge_html, unsafe_allow_html=True)