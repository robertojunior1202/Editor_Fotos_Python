import streamlit as st
from streamlit_option_menu import option_menu

def navbar():
    # Navbar
    pagina = option_menu(
        menu_title=None,
        options=["Editor de Fotos"],
        icons=["bar-chart"],# "briefcase", "building", "bar-chart"],
        orientation="horizontal",
        key="navbar",
        styles={
            "container": {"background-color": "#063970"},
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#003153","color": "white"},
            "nav-link-selected": {"background-color": "#002244"},
        },
    )
    
def render():
    navbar()