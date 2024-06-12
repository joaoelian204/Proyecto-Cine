import tkinter as tk  # Importa la biblioteca tkinter con el alias tk
from configuracion import configurar_ventana, crear_paneles, configurar_barra_superior, configurar_menu_lateral  # Importa funciones de otros módulos
from cargar_cartelera import cargar_cartelera  # Importa la función cargar_cartelera del módulo cargar_cartelera
from eventos import toggle_panel  # Importa la función toggle_panel del módulo eventos
from login import mostrar_login  # Importar la función de login desde login.py

def main():
    root = tk.Tk()  # Crea una instancia de la clase Tk para la ventana principal

    def on_login_success():
        configurar_ventana(root)  # Configura la ventana principal
        barra_superior, menu_lateral, cuerpo_principal = crear_paneles(root)  # Crea los paneles de la interfaz
        configurar_barra_superior(barra_superior, lambda: toggle_panel(menu_lateral))  # Configura la barra superior
        configurar_menu_lateral(menu_lateral, cuerpo_principal, root, on_login_success)  # Configura el menú lateral
        cargar_cartelera(cuerpo_principal)  # Carga la cartelera en el cuerpo principal

    mostrar_login(root, on_login_success)
    root.mainloop()  # Inicia el bucle principal de la aplicación

if __name__ == "__main__":
    main()  # Llama a la función main si el script se ejecuta directamente
