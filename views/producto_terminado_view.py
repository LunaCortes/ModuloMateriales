import tkinter as tk
from tkinter import ttk

def mostrar_producto_terminado(container):
    """Función para mostrar la tabla de Producto Terminado en la interfaz."""
    # Limpiar el contenedor antes de agregar la tabla
    for widget in container.winfo_children():
        widget.destroy()

    # Frame que contendrá la tabla
    frame = tk.Frame(container, bg="#ffffff")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Definimos las columnas para el Treeview
    columnas = ("PRODUCTO_ID", "FRACCION_ID", "PRODUCTO_DESCRIPCION", "PRODUCTO_UNIDAD")

    # Creamos el Treeview con las columnas definidas
    tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10)

    # Configuramos los encabezados de las columnas
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150)

    # Barra de desplazamiento vertical para la tabla
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    # Posicionamos la tabla y la barra de desplazamiento
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Datos de ejemplo (puedes reemplazarlos con datos reales)
    datos_ejemplo = [
        (1, 10, "Producto A", "Unidad"),
        (2, 20, "Producto B", "Caja"),
        (3, 30, "Producto C", "Kg"),
    ]

    # Insertamos los datos de ejemplo en la tabla
    for fila in datos_ejemplo:
        tabla.insert("", "end", values=fila)
