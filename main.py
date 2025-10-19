import sympy as sp
import tkinter as tk
from tkinter import messagebox

def calcular_limite():
    x = sp.symbols('x')
    func_input = entrada_funcao.get()
    ponto_input = entrada_ponto.get().strip()
    lado = var_lado.get()

    try:
        func = sp.sympify(func_input)
    except (sp.SympifyError, SyntaxError):
        messagebox.showerror("Erro", "Função inválida.")
        return

    try:
        if ponto_input.lower() == 'oo':
            ponto = sp.oo
        elif ponto_input.lower() == '-oo':
            ponto = -sp.oo
        else:
            ponto = float(ponto_input)
    except ValueError:
        messagebox.showerror("Erro", "Ponto inválido.")
        return

    try:
        limite = sp.limit(func, x, ponto, dir=lado if lado else '+-')
        resultado_var.set(f"lim[x→{ponto_input}{lado}] {func_input} = {limite}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o limite:\n{str(e)}")

# Criação da janela
janela = tk.Tk()
janela.title("Calculadora de Limites (com SymPy)")
janela.geometry("450x300")

# Função
tk.Label(janela, text="Função f(x):").pack()
entrada_funcao = tk.Entry(janela, width=40)
entrada_funcao.pack()

# Ponto
tk.Label(janela, text="Ponto para o qual x tende (ex: 0, 2, oo, -oo):").pack()
entrada_ponto = tk.Entry(janela, width=20)
entrada_ponto.pack()

# Lado da tendência
tk.Label(janela, text="Tendência (lado):").pack()
var_lado = tk.StringVar(value="")
frame_lado = tk.Frame(janela)
frame_lado.pack()

tk.Radiobutton(frame_lado, text="Ambos os lados", variable=var_lado, value="").pack(side=tk.LEFT)
tk.Radiobutton(frame_lado, text="Pela direita (+)", variable=var_lado, value="+").pack(side=tk.LEFT)
tk.Radiobutton(frame_lado, text="Pela esquerda (-)", variable=var_lado, value="-").pack(side=tk.LEFT)

# Botão de calcular
tk.Button(janela, text="Calcular Limite", command=calcular_limite).pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, fg="blue", wraplength=400, justify="center").pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()
