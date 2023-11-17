import tkinter as tk
from tkinter import ttk, messagebox

def adicionar_entrada():
    modo = combo_modo.get()
    try:
        distancia = float(entry_distancia.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma distância válida.")
        return

    entradas.append((modo, distancia))
    atualizar_lista()

def calcular_pegada_total():
    total_emissao = 0
    emissao_por_km = {
        "Carro": 0.2,
        "Trem": 0.04,
        "Bicicleta": 0,
        "A pé": 0,
        "Ônibus": 0.1
    }

    for modo, distancia in entradas:
        total_emissao += emissao_por_km.get(modo, 0) * distancia

    return total_emissao

def mostrar_resultado():
    total_emissao = calcular_pegada_total()
    messagebox.showinfo("Resultado", f"A pegada de carbono total é de {total_emissao:.2f} kg de CO2.")

def calcular_creditos_carbono():
    total_emissao = calcular_pegada_total()
    creditos_necessarios = total_emissao / 1000
    messagebox.showinfo("Créditos de Carbono", f"Créditos de carbono necessários para neutralizar: {creditos_necessarios:.2f}")

def comprar_creditos():
    cotação_credito = 78.56 #Cotação de 14/11
    creditos_necessarios = calcular_pegada_total() / 1000
    valor_total = creditos_necessarios * cotação_credito
    messagebox.showinfo("Compra de Créditos", f"Você comprou {creditos_necessarios:.2f} créditos de carbono por R$ {valor_total:.2f}!")


def atualizar_lista():
    lista_entradas.delete(0, tk.END)
    for modo, distancia in entradas:
        lista_entradas.insert(tk.END, f"{modo} - {distancia} km")

def limpar_entradas():
    entradas.clear()
    atualizar_lista()

def calcular_pegada_anual_e_creditos():
    total_emissao = calcular_pegada_total()
    pegada_anual = total_emissao * 252
    creditos_necessarios = pegada_anual / 1000 
    messagebox.showinfo("Pegada de Carbono Anual e Créditos", f"A pegada de carbono anual é de {pegada_anual:.2f} kg de CO2.\nCréditos de carbono necessários para neutralizar: {creditos_necessarios:.2f}")


entradas = []

app = tk.Tk()
app.title("Calculadora de Pegada de Carbono")

label_modo = ttk.Label(app, text="Modo de Transporte:")
label_modo.grid(column=0, row=0, padx=10, pady=10)

modos = ["Carro", "Trem", "Bicicleta", "A pé", "Ônibus"]
combo_modo = ttk.Combobox(app, values=modos)
combo_modo.grid(column=1, row=0, padx=10, pady=10)
combo_modo.set(modos[0])

label_distancia = ttk.Label(app, text="Distância (km):")
label_distancia.grid(column=0, row=1, padx=10, pady=10)

entry_distancia = ttk.Entry(app)
entry_distancia.grid(column=1, row=1, padx=10, pady=10)

btn_adicionar = ttk.Button(app, text="Adicionar", command=adicionar_entrada)
btn_adicionar.grid(column=2, row=1, padx=10, pady=10)

lista_entradas = tk.Listbox(app, width=30)
lista_entradas.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

btn_calcular = ttk.Button(app, text="Calcular Pegada de Carbono", command=mostrar_resultado)
btn_calcular.grid(column=1, row=3, padx=10, pady=10)

btn_calcular_creditos = ttk.Button(app, text="Calcular Créditos de Carbono", command=calcular_creditos_carbono)
btn_calcular_creditos.grid(column=0, row=4, padx=10, pady=10)

btn_comprar_creditos = ttk.Button(app, text="Comprar Créditos de Carbono", command=comprar_creditos)
btn_comprar_creditos.grid(column=0, row=3, padx=10, pady=10)

btn_limpar = ttk.Button(app, text="Limpar Entradas", command=limpar_entradas)
btn_limpar.grid(column=2, row=3, padx=10, pady=10)

btn_calcular_anual_creditos = ttk.Button(app, text="Pegada e Créditos Anuais", command=calcular_pegada_anual_e_creditos)
btn_calcular_anual_creditos.grid(column=1, row=4, padx=10, pady=10)

app.mainloop()
