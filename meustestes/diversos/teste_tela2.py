import tkinter as tk

def exibir_mensagem():
    nome = entrada.get()
    rotulo_resultado.config(text=f"Olá, {nome}!")

# Criando a janela
janela = tk.Tk()
janela.title("Tela Interativa")
janela.geometry("400x300")

# Adicionando widgets
rotulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
rotulo.pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=5)

botao = tk.Button(janela, text="Enviar", font=("Arial", 12), command=exibir_mensagem)
botao.pack(pady=10)

rotulo_resultado = tk.Label(janela, text="", font=("Arial", 12))
rotulo_resultado.pack(pady=10)

# Loop principal
janela.mainloop()
