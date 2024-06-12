import tkinter as tk
from tkinter import font
from eventos import toggle_panel, bind_hover_events
from cargar_cartelera import cargar_cartelera
from colores import *
from usuario_info import mostrar_perfil
from login import mostrar_login  # Importar la función de login desde login.py

def configurar_ventana(root):
    root.title("Plataforma de Cine")
    root.geometry("1030x650")
    root.resizable(False, False)

def crear_paneles(root):
    barra_superior = tk.Frame(root, bg=COLOR_BARRA_SUPERIOR, height=50)
    barra_superior.pack(side=tk.TOP, fill=tk.BOTH)

    menu_lateral = tk.Frame(root, bg=COLOR_MENU_LATERAL, width=200)
    menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

    canvas = tk.Canvas(root, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    cuerpo_principal = tk.Frame(canvas, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.create_window((0, 0), window=cuerpo_principal, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    cuerpo_principal.bind("<Configure>", on_configure)

    return barra_superior, menu_lateral, cuerpo_principal

def configurar_barra_superior(barra_superior, toggle_panel_callback):
    font_awesome = font.Font(family='FontAwesome', size=15)

    label_titulo = tk.Label(barra_superior, text="Plataforma Cine", fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10,highlightthickness=0)
    label_titulo.pack(side=tk.LEFT, padx=10)

    button_menu_lateral = tk.Button(barra_superior, text="☰", font=font_awesome, command=toggle_panel_callback, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="#fff", padx=10)
    button_menu_lateral.pack(side=tk.LEFT, padx=10)

    label_info = tk.Label(barra_superior, text="joaoM@example.com", fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10)
    label_info.pack(side=tk.RIGHT)

def mostrar_cartelera(cuerpo_principal):
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()
    
    cargar_cartelera(cuerpo_principal)

def configurar_menu_lateral(menu_lateral, cuerpo_principal, root, on_login_success):
    font_awesome = font.Font(family='FontAwesome', size=15)
    usuario = {
        "nombre": "Joao",
        "imagen": "/home/joaoelian/Descargas/RickMorty-removebg-preview.png",
        "apellido": "Moreira",
        "correo": "joaoM@example.com",
        "pais": "Ecuador",
        "provincia": "Manabi",
        "ciudad": "Manta",
        "cedula": "123456789"
    }

    buttons_info = [
        ("Cartelera", "🎬", lambda: mostrar_cartelera(cuerpo_principal)),
        ("Mi Perfil", "👤", lambda: mostrar_perfil(cuerpo_principal, usuario)),
        ("Cerrar Sesión", "🚪", lambda: mostrar_login(root, on_login_success))
    ]

    for txt, icon, command in buttons_info:
        button = tk.Button(menu_lateral, text=f"{icon} {txt}", anchor="w", font=font_awesome, bd=0, bg=COLOR_BOTON_NORMAL, fg="#fff", width=15, height=1, command=command)
        button.pack(side=tk.TOP, pady=10, padx=20, fill=tk.X)
        bind_hover_events(button)


