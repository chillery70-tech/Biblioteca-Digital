usuarios = {"admin": "1234"}
# Tarjeta 1_Ideas: Usuario de entrada y Contraseña
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
