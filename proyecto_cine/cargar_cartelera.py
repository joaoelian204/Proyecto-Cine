import tkinter as tk
from detalles_pelicula import mostrar_detalles_pelicula
from imagenes import leer_imagen
from eventos import bind_hover_events
from colores import COLOR_BOTON_NORMAL, COLOR_TEXTO_NORMAL, COLOR_CUERPO_PRINCIPAL

def cargar_cartelera(cuerpo_principal):
    """
    Carga la información de las películas en el área principal.

    Args:
        cuerpo_principal (tk.Frame): El marco del cuerpo principal donde se mostrarán las películas.
    """
    peliculas = [
        
            {"titulo": "Bohemian Rhapsody", 
            "Genero": "Biografía/Drama", 
            "Duracion": "2h 14min", 
            "imagen": "/home/joaoelian/Descargas/bohemian_rhapsody.jpg", 
            "sinopsis": "Bohemian Rhapsody es una celebración del grupo Queen, su música y su extraordinario cantante principal Freddie Mercury. Freddie desafió estereotipos y destruyó convenciones para convertirse en uno de los artistas más queridos del planeta.\n La película sigue el ascenso meteórico de la banda a través de sus canciones icónicas y su sonido revolucionario,\n desde el momento en que Mercury se unió a los compañeros de banda Brian May y Roger Taylor hasta el legendario concierto en vivo en el estadio Wembley de Londres en 1985.",
            "horarios": "Horarios de Bohemian Rhapsody",
            "horario":["10:00 AM", "13:00 PM", "15:00 PM", "17:30 PM", "20:00 PM"]
                },
            
            {"titulo": "Avatar", 
            "Genero": "Ciencia ficción", 
            "Duracion": "2h 42min", 
            "imagen": "/home/joaoelian/Descargas/avatar.jpg", 
            "sinopsis": "Avatar lleva al espectador a un impresionante mundo más allá de la imaginación, donde un héroe renuente se embarca en una aventura épica y heroica, luchando por salvar la vida de su gente y recuperar el amor de una mujer. Es la historia de un ex marine parapléjico, Jake Sully, que se embarca en una misión única a la lejana luna Pandora, donde un conflicto de interés se desata entre los nativos Na'vi y los invasores humanos.",
            "horarios": "Horarios de Avatar",
            "horario":["08:00 AM", "11:00 PM", "13:00 PM", "16:30 PM", "19:00 PM"]
                },
            
            {"titulo": "Back to the Future",
            "Genero": "Ciencia ficción/\nAventura",
            "Duracion": "1h 56min", 
            "imagen": "/home/joaoelian/Descargas/back_to_the_future.jpg",
            "sinopsis": "Marty McFly, un adolescente de 17 años, es enviado accidentalmente al pasado en un DeLorean modificado por su amigo científico loco, el Dr. Emmett Brown. Viajando a 1955, Marty conoce a sus futuros padres y debe asegurarse de que se enamoren y se casen o de lo contrario, no existirá en el futuro. Pero cuando su madre se enamora de él en lugar de su padre, Marty debe arreglar la línea de tiempo y hacer que sus padres se enamoren para volver a casa.", "horarios": "Horarios de Back to the Future:","horario":["09:00 AM", "12:00 PM", "14:00 PM", "17:30 PM", "20:00 PM"]
                },
            
            {"titulo": "The Godfather", 
            "Genero": "Crimen/Drama", 
            "Duracion": "2h 55min", 
            "imagen": "/home/joaoelian/Descargas/the_godfather.jpg",
            "sinopsis": "La historia se desarrolla en 1945, donde el líder de la familia mafiosa Corleone, Don Vito Corleone, se prepara para la boda de su hija. Mientras tanto, un rival del clan intenta asesinar a Don Vito. La película trata sobre la lucha por el poder, la familia y la moralidad, y sigue la vida de la familia Corleone durante una década.", "horarios": "Horarios de The Godfather","horario":["11:00 AM", "13:00 PM", "15:40 PM", "17:30 PM", "20:20 PM"]
                },
            
            {"titulo": "The Shawshank\n Redemption", 
            "Genero": "Drama",
            "Duracion": "2h 22min", 
            "imagen": "/home/joaoelian/Descargas/redemption.jpg", 
            "sinopsis": "La película sigue la historia de Andy Dufresne, un banquero que es condenado por un crimen que no cometió y enviado a la prisión de Shawshank. Allí, se hace amigo de Red, un prisionero experimentado que puede conseguir cualquier cosa que la gente quiera. A medida que pasa el tiempo, Andy encuentra una manera de sobrevivir y hacer una vida para sí mismo dentro de los confines de la prisión, manteniendo su esperanza de libertad y su determinación inquebrantable.", 
            "horarios": "Horarios de The Shawshank Redemption:",
            "horario":["10:00 AM", "13:00 PM", "15:00 PM", "17:30 PM", "20:00 PM"]
                },
            
            {"titulo": "The Dark Knight", 
            "Genero": "Acción/Crimen", 
            "Duracion": "2h 32min", 
            "imagen": "/home/joaoelian/Descargas/the_Dark_Knight.jpg", 
            "sinopsis": "The Dark Knight sigue al Caballero Oscuro mientras se enfrenta a su archienemigo, el Joker, que siembra el caos y el terror en la ciudad de Gotham. Batman debe enfrentarse a decisiones morales difíciles y poner a prueba su voluntad mientras lucha contra el crimen y trata de salvar a la ciudad de la destrucción total.", 
            "horarios": "Horarios de The Dark Knight",
            "horario":["08:40 AM", "11:20 AM", "14:00 PM", "17:30 PM", "19:45 PM"]
                },
            
            {"titulo": "Inception", 
            "Genero": "Acción/Aventura", 
            "Duracion": "2h 28min", 
            "imagen": "/home/joaoelian/Descargas/inception.jpg",
            "sinopsis": "Inception sigue a Dom Cobb, un ladrón hábil que se especializa en la extracción de secretos del subconsciente de sus objetivos mientras están en un estado de sueño. Es contratado para realizar la operación inversa, implantar una idea en la mente de alguien. A medida que la misión se vuelve más compleja y peligrosa, Cobb se enfrenta a sus propios demonios personales y a los desafíos del mundo del sueño.", 
            "horarios": "Horarios de Inception",
            "horario":["09:00 AM", "12:00 PM", "14:00 PM", "17:30 PM", "20:00 PM"]
                },
            
            {"titulo": "Interstellar",
            "Genero": "Aventura/Drama", 
            "Duracion": "2h 49min",
            "imagen": "/home/joaoelian/Descargas/interstellar.jpg", 
            "sinopsis": "Interstellar sigue a un grupo de astronautas que emprenden un viaje interestelar en busca de un nuevo hogar para la humanidad después de que la Tierra se vuelva inhabitable. La película explora temas de amor, pérdida, sacrificio y la naturaleza del tiempo y el espacio en un viaje épico a través de las estrellas.", 
            "horarios": "Horarios de Interstellar",
            "horario":["10:00 AM", "13:00 PM", "15:00 PM", "17:30 PM", "20:00 PM"]
                },
            {"titulo": "Soy Leyenda",
            "Genero": "Ciencia ficción/\n Drama",
            "Duracion": "1h 41min",
            "imagen": "/home/joaoelian/Descargas/soyleyenda.jpg",
            "sinopsis": "Soy Leyenda sigue al científico militar Robert Neville, quien lucha por sobrevivir en un mundo postapocalíptico poblado por seres humanos mutantes infectados por un virus. La película explora temas de soledad, esperanza y sacrificio mientras Neville lucha por encontrar una cura y redimirse por sus acciones pasadas.",
            "horarios": "Horarios de Soy Leyenda",
            "horario": ["11:00 AM", "14:00 PM", "16:30 PM", "19:00 PM", "21:30 PM"]
                },
            {"titulo": "Soy como niño",
            "Genero": "Comedia",
            "Duracion": "1h 45min",
            "imagen": "/home/joaoelian/Descargas/soncomoniños.jpg",
            "sinopsis": "Soy como niño sigue la historia de un hombre adulto que, después de un accidente, comienza a comportarse como un niño pequeño. La película explora temas de madurez, responsabilidad y la importancia de mantener vivo el espíritu joven. Con situaciones cómicas y conmovedoras, Soy como niño es una película que te hará reír y reflexionar.",
            "horarios": "Horarios de Soy como niño",
            "horario": ["10:30 AM", "13:15 PM", "15:45 PM", "18:20 PM", "21:00 PM"]
                },
            
                    ]
    
    row_count = 0
    column_count = 0
    max_columns = 5
    padding_x = 20
    padding_y = 20

# Recorrer cada película y crear un widget para mostrar sus detalles
    for pelicula in peliculas:
        # Crear una etiqueta para mostrar el título de la película
        label_pelicula = tk.Label(cuerpo_principal, text=pelicula["titulo"], font=("Roboto", 10), bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL, bd=0, highlightbackground="black", highlightthickness=2)
        label_pelicula.grid(row=row_count, column=column_count, padx=padding_x, pady=padding_y, sticky="nsew")
        
        # Si hay una imagen para la película, cargarla y mostrarla
        if "imagen" in pelicula:
            imagen = leer_imagen(pelicula["imagen"], (150, 150))
            label_imagen = tk.Label(label_pelicula, image=imagen, bg=COLOR_CUERPO_PRINCIPAL)
            label_imagen.image = imagen
            label_imagen.pack()

        # Etiqueta para mostrar el título de la película (en negrita)
        label_titulo = tk.Label(label_pelicula, text=pelicula["titulo"], font=("Roboto", 10, "bold"), bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL)
        label_titulo.pack()

        # Etiqueta para mostrar el género de la película
        label_genero = tk.Label(label_pelicula, text=f"Género: {pelicula['Genero']}", font=("Roboto", 10), bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL)
        label_genero.pack()

        # Etiqueta para mostrar la duración de la película
        label_duracion = tk.Label(label_pelicula, text=f"Duración: {pelicula['Duracion']}", font=("Roboto", 10), bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL)
        label_duracion.pack()

        # Incrementar el contador de columnas
        column_count += 1
        # Si se alcanza el número máximo de columnas, reiniciar el contador de columnas y aumentar el contador de filas
        if column_count >= max_columns:
            column_count = 0
            row_count += 1
        
        # Botón para ver más detalles de la película, con la función de mostrar_detalles_pelicula como comando
        button_ver_mas = tk.Button(label_pelicula, text="Ver más", font=("Arial", 10, "bold"), bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL, bd=0, command=lambda pelicula=pelicula: mostrar_detalles_pelicula(cuerpo_principal, pelicula))
        button_ver_mas.pack(pady=7, padx=10)

    bind_hover_events(button_ver_mas)