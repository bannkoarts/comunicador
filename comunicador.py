import streamlit as st
from PIL import Image
import pyttsx3
import os

# Inicializa mecanismo de voz (só funciona localmente, não na nuvem)
engine = pyttsx3.init()

# Função para falar
def falar(frase):
    engine.say(frase)
    engine.runAndWait()

# Dados das categorias e frases
categorias = {
    "Saudações": [
        ("Olá!", "imagens/ola.png"),
        ("Obrigado!", "imagens/obrigado.png"),
        ("Sim", "imagens/sim.png"),
        ("Não", "imagens/nao.png"),
    ],
    "Necessidades": [
        ("Quero comer.", "imagens/comer.png"),
        ("Estou com sede.", "imagens/sede.png"),
        ("Estou com frio.", "imagens/frio.png"),
        ("Estou com calor.", "imagens/calor.png"),
        ("Youtube.", "imagens/youtube.png"),
    ],
    "Sentimentos": [
        ("Estou com dor.", "imagens/dor.png"),
        ("Me ajude, por favor.", "imagens/ajuda.png"),
        ("Estou cansado.", "imagens/cansado.png"),
    ]
}

# Layout do app
st.set_page_config(page_title="Comunicador AAC", layout="centered")
st.title("🗣️ Comunicador com Imagens")

categoria_escolhida = st.selectbox("Escolha uma categoria:", list(categorias.keys()))

colunas = st.columns(2)

for idx, (frase, imagem_path) in enumerate(categorias[categoria_escolhida]):
    with colunas[idx % 2]:
        if os.path.exists(imagem_path):
            imagem = Image.open(imagem_path)
            st.image(imagem, width=80)
        if st.button(frase):
            falar(frase)