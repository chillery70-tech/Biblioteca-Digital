usuarios = {"admin": "1234"}
# Tarjeta 1_Ideas: Usuario de entrada y Contraseña
def buscar():
    # Tarjeta 3_Priorizado - Pantalla principal con buscador
    texto = entry_buscar.get().lower()
    lista.delete(0, tk.END)
    for titulo, datos in libros.items():
        if texto in titulo.lower():
            lista.insert(tk.END, f"{titulo} | {datos['genero']} | {datos['estado']}")

# En tu interfaz agrega esto:
entry_buscar = tk.Entry(frame_biblio)
entry_buscar.pack()
tk.Button(frame_biblio, text="Buscar", command=buscar).pack()
