import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox


def renomear_xmls(pasta):
    padrao_chave = re.compile(r"\d{44}")
    renomeados = 0

    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(".xml"):
            match = padrao_chave.search(arquivo)
            if not match:
                continue

            chave_44 = match.group()
            novo_nome = f"{chave_44}-nfe.xml"

            caminho_antigo = os.path.join(pasta, arquivo)
            caminho_novo = os.path.join(pasta, novo_nome)

            if not os.path.exists(caminho_novo):
                os.rename(caminho_antigo, caminho_novo)
                renomeados += 1

    return renomeados


def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_selecionada.set(pasta)


def processar():
    pasta = pasta_selecionada.get()
    if not pasta:
        messagebox.showwarning("Atenção", "Selecione uma pasta primeiro.")
        return

    total = renomear_xmls(pasta)
    messagebox.showinfo("Concluído", f"{total} arquivos renomeados com sucesso!")



janela = tk.Tk()
janela.title("Renomear XML - NFe")
janela.geometry("500x260")
janela.resizable(False, False)

# Frame principal
frame = tk.Frame(janela, padx=20, pady=20)
frame.pack(expand=True)

# Título
tk.Label(
    frame,
    text="Renomear XML de NFe",
    font=("Segoe UI", 14, "bold")
).pack(pady=(0, 20))

# Texto
tk.Label(
    frame,
    text="Selecione a pasta onde estão os XMLs:",
    font=("Segoe UI", 10)
).pack(pady=(0, 10))

# Variável da pasta
pasta_selecionada = tk.StringVar()

# Botão escolher pasta
tk.Button(
    frame,
    text="Escolher pasta",
    width=25,
    height=2,
    command=escolher_pasta
).pack()

# Caminho
tk.Label(
    frame,
    textvariable=pasta_selecionada,
    wraplength=440,
    fg="#1a73e8",
    font=("Segoe UI", 9)
).pack(pady=10)

# Botão processar
tk.Button(
    frame,
    text="Renomear arquivos",
    width=25,
    height=2,
    bg="#0b5ed7",
    fg="white",
    activebackground="#084298",
    activeforeground="white",
    command=processar
).pack(pady=15)

janela.mainloop()
