import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Interfaz")

# Crear un widget de etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Dile algo a garrido!")

# Colocar la etiqueta en la ventana
etiqueta.pack()

# Función que se ejecuta al hacer clic en el botón
def saludar():
    etiqueta.config(text="¡Hola, " + entrada.get() + "!")

# Crear un widget de entrada de texto
entrada = tk.Entry(ventana)

# Colocar la entrada en la ventana
entrada.pack()

# Crear un botón
boton = tk.Button(ventana, text="Habla", command=saludar)
boton_1 = tk.Button(ventana, text="Habla_2", command=saludar)

boton.pack()
boton_1.pack()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
