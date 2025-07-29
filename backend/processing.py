from PIL import Image, ImageFilter, ImageOps
from datetime import datetime
import os
import streamlit as st
import cv2 as cv
import numpy as np

def aplicar_filtros(imagem, rotacao_graus, escala, def_horiz, def_vert, brilho, 
                    contraste, transformacao_intensidade_potencia,transformacao_intensidade_log, filtro_negativo):
    #Filtros de Ajuste Geométrico
    #if rotacao_graus != 0:
        #imagem = imagem.rotate(rotacao_graus, expand=True)
    imagem_cv = cv.cvtColor(np.array(imagem), cv.COLOR_RGB2BGR) 
        
    if rotacao_graus != 0  or escala != 0:
        rows, cols = imagem_cv.shape[:2]
        center = ((cols-1)/2.0, (rows-1)/2.0)
        angle = rotacao_graus
        scale = escala
        m =cv.getRotationMatrix2D(center, angle, scale)
        imagem_cv = cv.warpAffine(imagem_cv, m, (cols, rows))
        
    
    if def_horiz != 0 or def_vert != 0:
        rows, cols = imagem_cv.shape[:2]
        m = np.float32([
            [1, -def_vert, 0],
            [-def_horiz, 1, 0],
            [0, 0, 1]])
        imagem_cv = cv.warpPerspective(imagem_cv, m, (cols, rows))
      
    
    if brilho !=0 or contraste !=0:
        imagem_cv = cv.convertScaleAbs(imagem_cv, alpha=contraste, beta=brilho)
        #imagem_brilho = cv.convertScaleAbs(imagem_cv, alpha=contraste, beta=brilho)
        #imagem_rgb = cv.cvtColor(imagem_brilho, cv.COLOR_BGR2RGB)
        #imagem = Image.fromarray(imagem_rgb)

    
    if transformacao_intensidade_potencia !=0:
        # Convertendo para escala de 0 a 1
        r = imagem_cv.astype(np.float32) / 255.0
        gamma = transformacao_intensidade_potencia 
        c = 255.0

        # Aplicando a transformação
        imagem_transformada = c * np.power(r, gamma)

        # Convertendo de volta para uint8
        imagem_cv = np.uint8(np.clip(imagem_transformada, 0, 255))
        
        
    if transformacao_intensidade_log !=0:
        imagem_float = imagem_cv.astype(np.float32)
        imagem_log = transformacao_intensidade_log * np.log1p(imagem_float)
        imagem_cv = np.uint8(np.clip(imagem_log, 0, 255))
        
    
            
    if filtro_negativo:
        imagem_cv = cv.bitwise_not(imagem_cv)  
    
    
    #Converte de Volta para o Padrão RGB
    imagem_rgb = cv.cvtColor(imagem_cv, cv.COLOR_BGR2RGB)
    imagem = Image.fromarray(imagem_rgb)
    
    return imagem


def salvar_imagem(imagem):
                if st.button("Salvar Imagem Processada"):
                    if not os.path.exists("output"):
                        os.makedirs("output")
                    caminho = f"output/imagem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    imagem.save(caminho)
                    st.success(f"Imagem salva em: {caminho}")