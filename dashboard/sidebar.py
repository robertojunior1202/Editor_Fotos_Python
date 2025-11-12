import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
  

def sidebar_busca():
    with st.sidebar:
        escolha = option_menu(
            menu_title="Menu",
            options=["Upload", "Capturar"],
            icons=["cloud-upload", "camera"],
            menu_icon="cast",
            default_index=0,
            key="menu_lateral",
            styles={
                "container": {"padding": "5px", "background-color": "#f0f2f6"},
                "icon": {"color": "#004080", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#e0e0e0",
                },
            "nav-link-selected": {"background-color": "#d0d0d0"},})
        
    return escolha

        
        
        
# Painel Filtros
def filtros():
    with st.sidebar:
        
        
        st.markdown("---")
        st.markdown("### Ajustes Geométricos")
        rotacao = st.slider("Rotação", min_value=-180, max_value=180, value=0)
        escala = st.slider("Escala", 0.0, 2.0, 1.0, 0.1)
        st.subheader("Cisalhamento")
        def_horiz= st.slider("Deformação Horizontal", -0.5, 0.5, 0.0, 0.01)
        def_vert = st.slider("Deformação Vertical", -0.5, 0.5, 0.0, 0.01)
        
        
        st.markdown("---")
        st.markdown("### Ajustes de Intensidade")
        brilho = st.slider("Brilho", -100, 100, 0, 1)
        contraste = st.slider("Contraste", 0.5, 3.0, 1.0, 0.1)
        transformacao_intensidade_potencia = st.slider("Transformação de Intensidade (Potência)", 0.1, 3.0, 1.0, 0.1)
        transformacao_intensidade_log = st.slider("Transformação Logarítmica (c)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
        filtro_negativo = st.toggle("Aplicar Filtro Negativo")
        
        
        st.markdown("---")
        st.markdown("### Filtros de Imagem")
        
        # Threshold
        limiarizacao = st.slider("Threshold (Limiarização)", 0, 255, 0, 1)
        # AdaptativeThreshold media local
        limiarizacao_at_mean = st.slider("Adaptive Threshold (Local Mean)", 0, 255, 0, 1)
        # AdaptativeThreshold gaussiana
        limiarizacao_at_g = st.slider("Adaptive Threshold (Gaussian)", 0, 255, 0, 1)
        # AdaptativeThreshold mediana
        limiarizacao_at_mediana = st.slider("Adaptive Threshold (Mediana)", 0, 255, 0, 1)
        # Limiarização adaptativa - Método de Otsu
        limiarizacao_at_otsu = st.slider("Adaptive Threshold (Otsu)", 0, 255, 0, 1)
        # Limiarização adaptativa - Método de Riddler-Calvard
        limiarizacao_at_rc = st.slider("Adaptive Threshold (Riddler-Calvard)", 0, 255, 0, 1)
        

        # Recortar a imagem pela segmentação (Segmentação por Regiões)
        st.markdown("### Segmentação por Regiões (em desenvolvimento)")
        # Recortar a imagem pela segmentação (Segmentação por Regiões Baseadas em Clustering)
        st.markdown("### Segmentação por Regiões Baseadas em Clustering (em desenvolvimento)")
        # Recortar a imagem pela segmentação (Segmentação por Regiões Mean-Sheet)
        st.markdown("### Segmentação por Regiões Mean-Sheet (em desenvolvimento)")
        
        
        return rotacao, escala, def_horiz, def_vert, brilho, contraste, transformacao_intensidade_potencia,transformacao_intensidade_log,\
        filtro_negativo,limiarizacao,limiarizacao_at_mean,limiarizacao_at_g,limiarizacao_at_mediana,limiarizacao_at_otsu,limiarizacao_at_rc
    
    
