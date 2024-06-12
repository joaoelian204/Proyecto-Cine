import tkinter as tk
from tkinter import messagebox
from colores import *

# Variable global para almacenar los asientos seleccionados
asientos_seleccionados = {}

# Función para crear y mostrar el estado de los asientos
def crear_estado_asientos(frame):
    """
    Crea y muestra etiquetas y lienzos para representar el estado de los asientos.
    """
    estado = {
        "simbolo": ("L", "O", "S"),
        "estados": ("libre", "ocupado", "seleccionado"),
        "colores": (color_libre, color_ocupado, color_seleccionado)
    }
    for i in range(3):
        tk.Label(frame, text=f"{estado['simbolo'][i]}: {estado['estados'][i]}", bg=color_fondo, fg="black", font= fuente_estado_asiento).pack(anchor=tk.W)
        canvas_estado = tk.Canvas(frame, width=15, height=15, bg=color_fondo, highlightthickness=0)
        canvas_estado.create_rectangle(5, 5, 15, 15, fill=estado['colores'][i])
        canvas_estado.pack(anchor=tk.W,pady=(0,10))

# Función para mostrar el registro de asientos
def mostrar_registro_asientos(cuerpo_principal, pelicula, hora, sala_index):
    """
    Muestra el registro de asientos en el cuerpo principal.

    Args:
        cuerpo_principal (tk.Frame): El marco del cuerpo principal donde se mostrarán los asientos.
        pelicula (str): El nombre de la película.
        hora (str): La hora de la función.
        sala (str): El número de la sala.
    """

    # Limpiar el cuerpo_principal
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

    # Obtener los asientos seleccionados para esta combinación de película, hora y sala
    key = (pelicula["titulo"], hora)
    
    if key not in asientos_seleccionados:
        asientos_seleccionados[key] = [[[0]*7 for _ in range(7)] for _ in range(3)]
    matriz_asientos = asientos_seleccionados[key][sala_index]

    # Función para seleccionar un asiento
    def seleccionar_asiento(i, j):
        if 0 <= i < 7 and 0 <= j < 7:  # Verificar que los índices estén dentro de los límites de la matriz
            estado_actual = matriz_asientos[i][j]
            if estado_actual == 0:
                matriz_asientos[i][j] = 1
                botones_asientos[i][j].configure(bg=color_seleccionado, text="S")
            elif estado_actual == 1:
                matriz_asientos[i][j] = 0
                botones_asientos[i][j].configure(bg=color_libre, text="L")
                
    # Crear y mostrar el título de la selección de asientos
    label_horarios = tk.Label(cuerpo_principal, text="    Selecciona tu asiento", font=fuente_titulo, fg=color_titulo, bg=color_fondo)
    label_horarios.pack(pady=(5,0), anchor='w')
    
    # Crear un frame para contener la matriz de botones
    frame_asientos = tk.Frame(cuerpo_principal, bg=color_fondo)
    frame_asientos.pack(pady=7, side=tk.LEFT)
    
    # Crear la matriz de botones para los asientos
    botones_asientos = []
    for i in range(7):  # Ajustado a 7 en lugar de 8
        fila_botones = []
        frame_fila = tk.Frame(frame_asientos, bg=color_fondo)
        frame_fila.pack()
        for j in range(7):  # Ajustado a 7 en lugar de 8
            boton = tk.Button(frame_fila, text="L", width=5, height=2, font=fuente_personalizada, bg=color_libre, bd=1, relief="groove")
            boton.pack(side=tk.LEFT, padx=5, pady=5)
            boton.config(command=lambda i=i, j=j: seleccionar_asiento(i, j))
            if matriz_asientos[i][j] == 1:
                boton.config(bg=color_seleccionado, text="S")
            elif matriz_asientos[i][j] == 2:
                boton.config(bg=color_ocupado, text="O")
            fila_botones.append(boton)
        botones_asientos.append(fila_botones)
        

    # Función para buscar el mejor asiento
    def buscar_mejor_asiento():
        mejor_asiento = None
        for i in range(7):
            for j in range(7):
                if matriz_asientos[i][j] == 0:
                    if mejor_asiento is None:
                        mejor_asiento = (i, j)
                    elif abs(3 - i) + abs(3 - j) < abs(3 - mejor_asiento[0]) + abs(3 - mejor_asiento[1]):
                        mejor_asiento = (i, j)
            if mejor_asiento:
                i, j = mejor_asiento
                botones_asientos[i][j].configure(bg=color_mejor_asiento)


    # Función para confirmar las reservas
    def confirmar_reservas():
        asientos_seleccionados[key][sala_index] = matriz_asientos
        for i in range(7):
            for j in range(7):
                if matriz_asientos[i][j] == 1:
                    matriz_asientos[i][j] = 2
                    botones_asientos[i][j].configure(bg=color_ocupado, text="O")
        messagebox.showinfo("Reservas Confirmadas", "¡Tus reservas han sido confirmadas!")
        
    # Crear un frame para los botones adicionales
    frame_botones = tk.Frame(cuerpo_principal, bg=color_fondo)
    frame_botones.pack(pady=10, side=tk.RIGHT)

    # Crear y colocar el botón para confirmar reservas
    boton_confirmar = tk.Button(frame_botones, text="Guardar Selección", fg=COLOR_TEXTO_NORMAL, bg=COLOR_BOTON_NORMAL, font=fuente_personalizada, bd=2, relief="groove", command=confirmar_reservas)
    boton_confirmar.pack(pady=10)

    # Crear y colocar el botón para buscar el mejor asiento
    boton_buscar_mejor = tk.Button(frame_botones, text="Buscar Mejor Asiento", fg=COLOR_TEXTO_NORMAL, bg=COLOR_BOTON_NORMAL, font=fuente_personalizada, bd=2, relief="groove", command=buscar_mejor_asiento)
    boton_buscar_mejor.pack(pady=10)
    
    # Crear y mostrar el estado de los asientos
    crear_estado_asientos(cuerpo_principal)






