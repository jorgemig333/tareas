import tkinter as tk
from PIL import Image, ImageTk


# FUNCION DE ENTRADA
def main():

    # 1. Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Mi perfil")
    ventana.geometry("1000x1000")
    ventana.configure(bg="#A7A19A")
    ventana.resizable(False, False)

    # 2. titulo principal
    titulo = tk.Label(
        ventana,
        text="MI PRESENTACIÓN",
        font=("arial", 20, "bold"),
        bg="#EAF2F8",
        fg="#154360"
    )
    titulo.pack(pady=15)

    # 3. fotografia
    imagen = Image.open("mifoto.jpg")
    imagen = imagen.resize((150, 150))
    foto = ImageTk.PhotoImage(imagen)

    etiqueta_foto = tk.Label(
        ventana,
        image=foto,
        bg="#EAF2F8"
    )
    etiqueta_foto.pack(pady=10)

    # 4. Mostrar el nombre completo
    nombre = tk.Label(
        ventana,
        text="JORGE MIGUEL MAMANI CANAVIRI",
        font=("Arial", 16, "bold"),
        bg="#EAF2F8",
        fg="#2874A6"
    )
    nombre.pack(pady=10)

    # 5. Agregar una descripcion personal
    descripcion = tk.Label(
        ventana,
        text="Hola, me presento:",
        font=("Arial", 11),
        bg="#EAF2F8",
        fg="#34495E"
    )
    descripcion.pack(pady=5)

    # 6. Titulo de los pasatiempos
    gustos_titulo = tk.Label(
        ventana,
        text="MIS PASATIEMPOS",
        font=("Arial", 14, "bold"),
        bg="#EAF2F8",
        fg="#154360"
    )
    gustos_titulo.pack(pady=10)

    # 7. Mostrar las cosas que me gusta hacer
    gustos = tk.Label(
        ventana,
        text="Me gusta manejar mi moto, escuchando musica, por momentos jugar en la pc y seguir estudiando",
        font=("Arial", 12),
        bg="#EAF2F8",
        fg="#34495E",
        justify="left"
    )
    gustos.pack(pady=5)

    # 8. Agregar un mensaje final
    boton = tk.Button(
        ventana,
        text="¡Gracias por ver mi perfil!",
        font=("Arial", 11, "bold"),
        bg="#154360",
        fg="white",
        activebackground="#2874A6",
        activeforeground="white",
        cursor="hand2",
        command=lambda: print("¡Gracias por ver mi perfil!")
    )

    boton.pack(pady=20)

    # 9. Mantener la ventana abierta
    ventana.mainloop()


# INICIAR EL PROGRAMA
if __name__ == "__main__":
    main()
