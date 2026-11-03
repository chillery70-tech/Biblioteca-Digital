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
