import streamlit as st


# Configurações da página
st.set_page_config(page_title="Editor de Fotos", layout="wide")

# Importa os módulos das páginas
from dashboard import navbar, sidebar
from dashboard.sidebar import sidebar_busca, filtros
from backend.main import captura_imagem, upload_imagem



def main():
    st.set_page_config(page_title="Editor de Fotos", layout="wide")
    navbar.render()
    escolha = sidebar_busca()  # Cria Sidebar e captura a escolha de upload

    # Lógica do upload
    if escolha == "Upload":
        upload_imagem()
    
        
    # Lógica da camera       
    elif escolha == "Capturar":
        captura_imagem()    
  

if __name__ == "__main__":
    main()

