import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

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
        self.crear_boton_seleccionar_tabla()
        self.crear_botones_operaciones()  # Agrega los botones "Validar", "Cargar" y "Salir"

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

    def crear_boton_seleccionar_tabla(self):
        """Crear un botón independiente para seleccionar una tabla de Excel."""
        boton_excel = ttk.Button(self.menu_frame, text="Seleccionar Tabla", command=self.seleccionar_tabla_excel)
        boton_excel.pack(side="right", padx=10, pady=5)

    def crear_botones_operaciones(self):
        """Crear botones para validar, cargar y salir."""
        boton_validar = ttk.Button(self.menu_frame, text="Validar", command=self.validar_datos)
        boton_validar.pack(side="right", padx=10, pady=5)

        boton_cargar = ttk.Button(self.menu_frame, text="Cargar", command=self.cargar_datos)
        boton_cargar.pack(side="right", padx=10, pady=5)

        boton_salir = ttk.Button(self.menu_frame, text="Salir", command=self.quit)
        boton_salir.pack(side="right", padx=10, pady=5)

    def mostrar_bill_of_material(self):
        self.limpiar_vista()

    def mostrar_maquinaria(self):
        self.limpiar_vista()

    def mostrar_materia_prima(self):
        self.limpiar_vista()

    def mostrar_producto_terminado(self):
        self.limpiar_vista()

    def seleccionar_tabla_excel(self):
        """Función para abrir un archivo Excel y seleccionar una tabla."""
        archivo_excel = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx *.xls")]
        )
        if not archivo_excel:
            return

        try:
            excel_data = pd.ExcelFile(archivo_excel)
            hoja_seleccionada = self.seleccionar_hoja(excel_data.sheet_names)
            if hoja_seleccionada:
                self.df = pd.read_excel(archivo_excel, sheet_name=hoja_seleccionada)
                self.mostrar_tabla(self.df)
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó ninguna hoja.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {e}")

    def seleccionar_hoja(self, hojas):
        """Muestra un cuadro de diálogo para seleccionar una hoja de Excel."""
        hoja_seleccionada = tk.StringVar()
        dialogo = tk.Toplevel(self)
        dialogo.title("Seleccionar Hoja de Excel")
        dialogo.geometry("300x200")

        label = tk.Label(dialogo, text="Selecciona una hoja:", font=("Arial", 14))
        label.pack(pady=10)

        combo = ttk.Combobox(dialogo, values=hojas, textvariable=hoja_seleccionada)
        combo.pack(pady=10)
        combo.current(0)

        boton_ok = ttk.Button(dialogo, text="OK", command=dialogo.destroy)
        boton_ok.pack(pady=10)

        self.wait_window(dialogo)
        return hoja_seleccionada.get()

    def mostrar_tabla(self, dataframe):
        """Muestra la tabla en el contenedor."""
        self.limpiar_vista()
        tree = ttk.Treeview(self.container, columns=dataframe.columns, show="headings")
        tree.pack(expand=True, fill="both")

        for col in dataframe.columns:
            tree.heading(col, text=col)

        for index, row in dataframe.iterrows():
            tree.insert("", "end", values=list(row))

    def limpiar_vista(self):
        """Limpia el contenedor antes de cargar una nueva vista."""
        for widget in self.container.winfo_children():
            widget.destroy()

    def validar_datos(self):
        """Función de validación de datos en el DataFrame cargado."""
        if hasattr(self, 'df'):
            # Aquí implementar lógica de validación
            messagebox.showinfo("Validación", "Validación completada.")
        else:
            messagebox.showwarning("Advertencia", "No se ha cargado ninguna tabla.")

    def cargar_datos(self):
        """Función para cargar los datos del DataFrame al archivo Excel."""
        if hasattr(self, 'df'):
            try:
                ruta_guardado = filedialog.asksaveasfilename(
                    defaultextension=".xlsx",
                    filetypes=[("Archivos Excel", "*.xlsx")]
                )
                if ruta_guardado:
                    self.df.to_excel(ruta_guardado, index=False)
                    messagebox.showinfo("Cargar Datos", "Datos cargados correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar los datos: {e}")
        else:
            messagebox.showwarning("Advertencia", "No se ha cargado ninguna tabla.")

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
