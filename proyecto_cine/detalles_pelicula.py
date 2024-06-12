import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import webbrowser
from eventos import bind_hover_events
from registrar_asientos import mostrar_registro_asientos
from colores import *

def mostrar_detalles_pelicula(cuerpo_principal, pelicula):
    """
    Muestra los detalles de una película en un contenedor principal.
    
    Args:
        cuerpo_principal (tk.Frame): El marco donde se mostrarán los detalles de la película.
        pelicula (dict): Un diccionario con los detalles de la película.
        
    """
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()

    cuerpo_principal.frame_salas_actual = None

    try:
        imagen = Image.open(pelicula["imagen"])
        imagen_resized = imagen.resize((360, 400))
        imagen_tk = ImageTk.PhotoImage(imagen_resized)
    except IOError as e:
        print("Error al cargar la imagen:", e)
        return

    cuerpo_principal.configure(bg=color_fondo, padx=20, pady=20)

    frame_izquierdo = tk.Frame(cuerpo_principal, bg=color_fondo)
    frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    label_imagen = tk.Label(frame_izquierdo, image=imagen_tk,
                            bg=color_fondo)
    label_imagen.image = imagen_tk
    label_imagen.pack(pady=(0, 20))

    label_titulo = tk.Label(frame_izquierdo, text=pelicula["titulo"], 
                            font=(fuente_personalizada[0], 18, "bold"), 
                            fg=color_titulo, bg=color_fondo)
    label_titulo.pack(pady=(0, 10))

    label_genero = tk.Label(frame_izquierdo, text=f"Género: {pelicula['Genero']}",
                            font=(fuente_personalizada[0], 14), 
                            fg=color_texto, bg=color_fondo)
    label_genero.pack(pady=(0, 5))

    label_duracion = tk.Label(frame_izquierdo, text=f"Duración: {pelicula['Duracion']}",
                            font=(fuente_personalizada[0], 14),
                            fg=color_texto, bg=color_fondo)
    label_duracion.pack(pady=(0, 5))

    try:
        button_trailer = tk.Button(frame_izquierdo, text="Ver trailer", 
                                fg=COLOR_TEXTO_NORMAL, bg=COLOR_BOTON_NORMAL, 
                                font=fuente_personalizada, bd=2, relief="groove",
                                command=lambda: webbrowser.open("https://www.youtube.com/watch?v=CpXJHWSXJW0"))
        button_trailer.pack(pady=(10, 20))
        bind_hover_events(button_trailer)
    except Exception as e:
        print("Error al abrir el enlace del tráiler:", e)

    frame_derecho = tk.Frame(cuerpo_principal, bg=color_fondo)
    frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    label_sinopsis = tk.Label(frame_derecho, text="Sinopsis:", font=(fuente_personalizada[0], 16, "bold"), 
                            fg=color_titulo, bg=color_fondo)
    label_sinopsis.pack(pady=(10, 15), anchor='w')

    sinopsis_texto = pelicula["sinopsis"]
    label_sinopsis_contenido = tk.Label(frame_derecho, text=sinopsis_texto, wraplength=500, justify="left",
                                        font=(fuente_personalizada[0], 12), fg=color_texto, bg=color_fondo)
    label_sinopsis_contenido.pack(pady=(0, 20), anchor='w')

    label_horarios = tk.Label(frame_derecho, text="Horarios:", font=(fuente_personalizada[0], 16, "bold"), 
                            fg=color_titulo, bg=color_fondo)
    label_horarios.pack(pady=(0,10), anchor='w')

    frame_horarios = tk.Frame(frame_derecho, bg=color_fondo)
    frame_horarios.pack(pady=(10, 10))

    # Este marco contendrá los botones adicionales
    frame_botones_adicionales = tk.Frame(frame_derecho, bg=color_fondo)
    frame_botones_adicionales.pack(pady=(10, 10))

    def mostrar_botones_adicionales(cuerpo_principal, pelicula, horario):
        print(f"pelicula: {pelicula}, tipo: {type(pelicula)}")  # Línea de depuración

        # Limpiar el contenido del frame_botones_adicionales
        for widget in frame_botones_adicionales.winfo_children():
            widget.destroy()

        for sala_index, texto_boton in enumerate(["Sala 1", "Sala 2", "Sala 3"]):
            boton_adicional = tk.Button(
                frame_botones_adicionales, 
                text=texto_boton, 
                fg="#FFFFFF", 
                bg="#FF5722", 
                font=fuente_personalizada, 
                bd=2, 
                relief="groove", 
                command=lambda s=sala_index: mostrar_registro_asientos(cuerpo_principal, pelicula, horario, s)
            )
            boton_adicional.pack(side=tk.TOP, padx=5, pady=5)

        cuerpo_principal.frame_salas_actual = frame_botones_adicionales

    for sala_index, hora in enumerate(pelicula["horario"]):
        button_horario = tk.Button(
            frame_horarios, 
            text=f"{hora}", 
            fg=COLOR_TEXTO_NORMAL, 
            bg=COLOR_BOTON_NORMAL, 
            font=fuente_personalizada, 
            bd=2, 
            relief="groove", 
            command=lambda si=sala_index, h=hora: mostrar_botones_adicionales(cuerpo_principal, pelicula, h)
        )
        button_horario.pack(side=tk.LEFT, padx=(5, 10))
        bind_hover_events(button_horario)









