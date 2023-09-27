import streamlit as st

def generate_badge(image_url, link):
    badge = f'<div><a href="{link}" target="_blank"><img src="{image_url}" alt="Badge" width="40px"></a></div>'
    return badge

def adciona_badges():
    badge_info_list = [
    ("https://img.icons8.com/fluency/48/linkedin.png", "https://www.linkedin.com/in/adriel-alexs/"),
    ("https://img.icons8.com/fluency/48/github.png", "https://github.com/AdrielProg"),
    ("https://img.icons8.com/fluency/48/email.png", "mailto:adriel.alexs123@gmail.com"),
    ("https://img.icons8.com/fluency/48/phone.png", "tel:+5583998178892")
]  
    return badge_info_list

def start(badge_info_list):
    badge_list = [generate_badge(image_url, link) for image_url, link in badge_info_list]