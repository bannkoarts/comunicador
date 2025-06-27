import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3
import os

# Inicializa o mecanismo de voz
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

# Cria a janela
janela = tk.Tk()
janela.title("Comunicador com Imagens")
janela.geometry("600x600")

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

# Função para mostrar frases de uma categoria
def mostrar_categoria(nome_categoria):
    for widget in frame_botoes.winfo_children():
        widget.destroy()

    frases = categorias[nome_categoria]

    for frase, imagem_path in frases:
        try:
            imagem = Image.open(imagem_path).resize((64, 64))
            imagem_tk = ImageTk.PhotoImage(imagem)
        except:
            imagem_tk = None

        botao = tk.Button(
            frame_botoes,
            text=frase,
            image=imagem_tk,
            compound="left",
            font=("Arial", 14),
            width=300,
            height=70,
            anchor="w",
            command=lambda f=frase: falar(f)
        )
        botao.image = imagem_tk  # Importante manter referência
        botao.pack(pady=5)

# Menu de categorias
frame_menu = tk.Frame(janela)
frame_menu.pack(pady=10)

tk.Label(frame_menu, text="Escolha uma categoria:", font=("Arial", 14)).pack()

for categoria in categorias:
    botao = tk.Button(frame_menu, text=categoria, font=("Arial", 12),
                      command=lambda c=categoria: mostrar_categoria(c))
    botao.pack(side="left", padx=10)

# Mostra a primeira categoria por padrão
mostrar_categoria("Saudações")

janela.mainloop()