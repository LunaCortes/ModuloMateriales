import tkinter as tk
from tkinter import ttk


def mostrar_bill_of_material(container):
    """Función para mostrar la tabla de Bill of Material en la interfaz."""
    # Limpiamos el contenido actual del contenedor
    for widget in container.winfo_children():
        widget.destroy()

    # Frame que contendrá la tabla
    frame = tk.Frame(container, bg="#ffffff")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Definimos las columnas para el Treeview
    columnas = (
        "BOM_ID", "PRODUCTO_ID", "FRACCION_ID", "PRODUCTO_DESCRIPCION",
        "PRODUCTO_UNIDAD", "FECHA_CREACION", "MATERIA_ID", "CANTIDAD",
        "MATERIAL_UNIDAD", "CANTIDAD_DESPERDICIO", "FECHA_INICIO", "FECHA_FINAL"
    )

    # Creamos el Treeview con las columnas definidas
    tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10)

    # Definimos los encabezados de las columnas
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=120)

    # Barra de desplazamiento para la tabla
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    # Posicionamos la tabla y la barra de desplazamiento
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Datos de ejemplo (puedes agregar tus datos reales aquí)
    datos_ejemplo = [
        (1, 101, 1, "Producto A", "Unidad A", "2024-10-20", 201, 50, "kg", 5, "2024-10-01", "2024-10-30"),
        (2, 102, 2, "Producto B", "Unidad B", "2024-10-19", 202, 30, "lt", 2, "2024-09-15", "2024-10-15"),
    ]

    # Insertamos los datos de ejemplo en la tabla
    for fila in datos_ejemplo:
        tabla.insert("", "end", values=fila)
