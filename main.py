usuarios = {"admin": "1234"}
# Tarjeta 1_Ideas: Usuario de entrada y Contraseña
def registrar_libro():
    # Tarjeta 4_En desarrollo - Registro de libros
    # Lista 9_Terminado Diseño de fichas de libros
    titulo = entry_titulo.get()
    genero = combo_genero.get()
    if titulo:
        libros[titulo] = {"genero": genero, "estado": "Disponible"}
        actualizar_lista()

# Agrega en tu interfaz:
entry_titulo = tk.Entry(frame_reg)
entry_titulo.pack()
combo_genero = ttk.Combobox(frame_reg, values=["Todos los generos", "Fantasia", "Infantil"])
combo_genero.set("Libros de todos los generos")
combo_genero.pack()
tk.Button(frame_reg, text="Registrar", command=registrar_libro).pack()
