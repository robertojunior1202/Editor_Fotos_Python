import streamlit as st
from PIL import Image
from dashboard.sidebar import filtros
from backend.processing import aplicar_filtros, salvar_imagem
import cv2 as cv
import numpy as np
import os
from datetime import datetime


def upload_imagem():
    # Checagem se já existe imagem carregada
    if "imagem_carregada" in st.session_state:       
        #Aplicar Filtros
        rotacao, escala, def_horiz, def_vert, brilho, contraste, transformacao_intensidade_potencia,transformacao_intensidade_log, filtro_negativo = filtros()
        #imagem_processada = aplicar_filtros(st.session_state.imagem_carregada,rotacao_graus=rotacao)
        imagem_processada = aplicar_filtros(st.session_state.imagem_carregada, rotacao_graus=rotacao, escala=escala, def_horiz=def_horiz, 
                    def_vert=def_vert,brilho=brilho, contraste=contraste, transformacao_intensidade_potencia=transformacao_intensidade_potencia, 
                    transformacao_intensidade_log=transformacao_intensidade_log,filtro_negativo=filtro_negativo)
        st.session_state.imagem_processada = imagem_processada
          
        col1, col2 = st.columns(2)
        with col1:
             # Botão para remover a imagem
            if st.button("Remover Imagem"):
                del st.session_state.imagem_carregada
                st.rerun()
                
            # Exibe imagem carregada
            st.image(st.session_state.imagem_carregada, caption="Imagem enviada", use_container_width=True)
            
        with col2:
            salvar_imagem(st.session_state.imagem_processada)
            # Exibe imagem processada
            st.image(st.session_state.imagem_processada, caption="Imagem processada", use_container_width=True)

        # Retorna imagem
        return st.session_state.imagem_carregada, st.session_state.imagem_processada

    # Caso não exista imagem carregada
    else:
        st.markdown("### Upload de Imagem")
        upload = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

        if upload is not None:
            imagem = Image.open(upload)
            st.session_state.imagem_carregada = imagem
            st.rerun() 
   
        
def captura_imagem():
    # Checagem se já existe imagem carregada
    if "imagem_carregada" in st.session_state:
        #Aplicar Filtros
        rotacao, escala, def_horiz, def_vert, brilho, contraste, transformacao_intensidade_potencia,transformacao_intensidade_log, filtro_negativo = filtros()
        #imagem_processada = aplicar_filtros(st.session_state.imagem_carregada,rotacao_graus=rotacao)
        imagem_processada = aplicar_filtros(st.session_state.imagem_carregada, rotacao_graus=rotacao, escala=escala, def_horiz=def_horiz, 
                    def_vert=def_vert,brilho=brilho, contraste=contraste, transformacao_intensidade_potencia=transformacao_intensidade_potencia, 
                    transformacao_intensidade_log = transformacao_intensidade_log, filtro_negativo=filtro_negativo)
        st.session_state.imagem_processada = imagem_processada
          
        col1, col2 = st.columns(2)
        with col1:
             # Botão para remover a imagem
            if st.button("Remover Imagem"):
                del st.session_state.imagem_carregada
                st.rerun()
                
            # Exibe imagem carregada
            st.image(st.session_state.imagem_carregada, caption="Imagem enviada", use_container_width=True)
            
        with col2:
            salvar_imagem(st.session_state.imagem_processada)
            # Exibe imagem processada
            st.image(st.session_state.imagem_processada, caption="Imagem processada", use_container_width=True)

        # Retorna imagem
        return st.session_state.imagem_carregada, st.session_state.imagem_processada
        

    # Caso não exista imagem carregada
    else:
        st.markdown("### Captura de Imagem")
        captura = st.camera_input("")

        if captura is not None:
            bytes_data = captura.getvalue()
            imagem = cv.imdecode(np.frombuffer(bytes_data, np.uint8), cv.IMREAD_COLOR)
            st.session_state.imagem_carregada = imagem
            st.rerun() 


    