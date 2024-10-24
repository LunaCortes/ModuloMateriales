import tkinter as tk
from tkinter import ttk
from views.maquinaria_view import mostrar_maquinaria
from views.materia_prima_view import mostrar_materia_prima
from views.producto_terminado_view import mostrar_producto_terminado
from views.bill_of_material_view import mostrar_bill_of_material  # Importación necesaria

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Control de Producción")
        self.geometry("1000x600")  # Tamaño de la ventana
        self.config(bg="#f0f4f8")  # Color de fondo

        # Aplicamos estilo a los widgets usando ttk.Style
        self.estilizar_interfaz()

        # Frame para el menú en la parte superior
        self.menu_frame = tk.Frame(self, bg="#344955", height=60)
        self.menu_frame.pack(side="top", fill="x")

        # Contenedor principal para las vistas
        self.container = tk.Frame(self, bg="#ffffff", relief="sunken", bd=2)
        self.container.pack(expand=True, fill="both", padx=10, pady=10)

        self.crear_menu()

    def estilizar_interfaz(self):
        """Estiliza la interfaz usando ttk.Style."""
        style = ttk.Style()
        style.theme_use("clam")  # Tema moderno sin colores personalizados

        # Estilos para botones estándar
        style.configure("TButton",
                        font=("Arial", 14),
                        padding=10)
        style.map("TButton",
                  background=[("active", "#e1e1e1")])

        # Estilos para el Menubutton estándar
        style.configure("TMenubutton",
                        font=("Arial", 14, "bold"),
                        padding=10)

    def crear_menu(self):
        # Etiqueta de título en el menú superior
        titulo = tk.Label(self.menu_frame, text="Menú Principal",
                          bg="#344955", fg="white",
                          font=("Arial", 18, "bold"), pady=10)
        titulo.pack(side="left", padx=20)

        # Menú desplegable con opciones
        self.crear_menu_desplegable()

    def crear_menu_desplegable(self):
        # Crear un botón de menú desplegable con estilos estándar
        menu_button = ttk.Menubutton(self.menu_frame, text="Materiales", style="TMenubutton")
        menu = tk.Menu(menu_button, tearoff=0, font=("Arial", 12))

        # Agregar las opciones al menú desplegable
        menu.add_command(label="Bill of Material", command=self.mostrar_bill_of_material)
        menu.add_command(label="Maquinaria", command=self.mostrar_maquinaria)
        menu.add_command(label="Materia Prima", command=self.mostrar_materia_prima)
        menu.add_command(label="Productos Terminados", command=self.mostrar_producto_terminado)

        # Configurar el menú en el botón
        menu_button.config(menu=menu)
        menu_button.pack(side="left", padx=10, pady=5)

    def mostrar_bill_of_material(self):
        self.limpiar_vista()
        mostrar_bill_of_material(self.container)

    def mostrar_maquinaria(self):
        self.limpiar_vista()
        mostrar_maquinaria(self.container)

    def mostrar_materia_prima(self):
        self.limpiar_vista()
        mostrar_materia_prima(self.container)

    def mostrar_producto_terminado(self):
        self.limpiar_vista()
        mostrar_producto_terminado(self.container)

    def limpiar_vista(self):
        """Limpia el contenedor antes de cargar una nueva vista."""
        for widget in self.container.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
