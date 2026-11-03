/prestamo-duplicado---viene-de-tu-tarjeta-6_Correcciones->-Corrección-de-errores
usuarios = {"admin": "1234"}
# Tarjeta 1_Ideas: Usuario de entrada y Contraseña
def prestar_libro_corregido():
    # Tarjeta 6_Correcciones - Corrección de errores
    # FIX: Valida que no se preste 2 veces el mismo libro
    try:
        seleccion = lista.get(lista.curselection())
        titulo = seleccion.split(" | ")[0]
        
        # ESTA ES LA CORRECCIÓN
        if libros[titulo]["estado"] != "Disponible":
            messagebox.showerror("Error", "¡Libro ya prestado! No se puede prestar 2 veces")
            return
            
        if titulo in prestamos:
            messagebox.showerror("Error", "Error de prestamo duplicado - tarjeta 6_Correcciones")
            return
            
        libros[titulo]["estado"] = "Prestado"
        actualizar_lista()
        messagebox.showinfo("OK", "Préstamo corregido y validado")
        
    except Exception as e:
        messagebox.showerror("Error", f"Corrección de errores: {e}")
/prestamos---viene-de-tu-tarjeta-5_En-revision->-Sistema-de-préstamos
from datetime import datetime, timedelta

prestamos = {}

def prestar_libro():
    # Tarjeta 5_En revision - Sistema de préstamos y devoluciones
    # Tarjeta 1_Ideas - tiempo limite de prestamo
    # Tarjeta 2_Por hacer - Módulo de usuarios
    try:
        seleccion = lista.get(lista.curselection())
        titulo = seleccion.split(" | ")[0]
        if libros[titulo]["estado"] == "Disponible":
            libros[titulo]["estado"] = "Prestado"
            fecha_limite = datetime.now() + timedelta(days=14)
            prestamos[titulo] = fecha_limite.strftime("%d/%m/%Y")
            actualizar_lista()
    except:
        pass

def devolver_libro():
    try:
        seleccion = lista.get(lista.curselection())
        titulo = seleccion.split(" | ")[0]
        libros[titulo]["estado"] = "Disponible"
        prestamos.pop(titulo, None)
        actualizar_lista()
    except:
        pass
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

