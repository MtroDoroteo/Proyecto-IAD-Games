#IMPORTACIÓN DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox

#VARIABLES GLOBALES

def cambiar_tablero():
    global tablero
    tablero = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    tablero[head["x"]][head["y"]] = 1

colores = {
    "COLOR_FONDO" : "#6e85d4"
}

head = {
    "x":0,
    "y":0
}

cambiar_tablero()

#FUNCIONES

def arriba():
    global head
    head["x"] -= 1
    cambiar_tablero()
    borrar_tablero()
    dibujar_tablero()


def abajo():
    global head
    head["x"] += 1
    cambiar_tablero()
    borrar_tablero()
    dibujar_tablero()

def izquierda():
    global head
    head["y"] -= 1
    cambiar_tablero()
    borrar_tablero()
    dibujar_tablero()

def derecha():
    global head
    head["y"] += 1
    cambiar_tablero()
    borrar_tablero()
    dibujar_tablero()

def borrar_tablero():
    canva.delete("all")

def dibujar_tablero():
    for fila in range(0,5):
        for columna in range(0,10):
            x1 = (columna * 75) + 10
            x2 = x1 + 75
            y1 = (fila * 75) + 10
            y2 = y1 + 75

            canva.create_rectangle(
                x1,y1, #COORDENADAS DE INICIO
                x2,y2, #TAMAÑO DEL RECTANGULO
                outline="#000000",
                width=1
            )

            if tablero[fila][columna] == 1:
                canva.create_oval(
                    x1+5, y1+5,
                    x2-5, y2-5,
                    fill="#00ff00",
                    outline="#000000"
                )


#CODIGO PRINCIPAL / FUNCION PRINCIPAL
def snake():
    ventana = tk.Tk()
    ventana.title("Snake")
    ventana.geometry("900x600")
    ventana.resizable(False,False)
    ventana.config(bg=colores["COLOR_FONDO"])

    titulo = tk.PhotoImage(file="assets/snake.png")
    
    canva_titulo = tk.Canvas(
        ventana,
        width=800,
        height=100,
        bg=colores["COLOR_FONDO"],
        highlightbackground = colores['COLOR_FONDO']
    )
    canva_titulo.pack()
    canva_titulo.create_image(
        400,50,
        image=titulo
    )

    global canva
    canva = tk.Canvas( #CANVAS SON LOS LIENZOS SOBRE LOS QUE DIBUJARÉ
        ventana,
        width = 800,
        height = 400,
        bg = colores["COLOR_FONDO"],
        highlightbackground=colores['COLOR_FONDO']
    )
    canva.pack()

    dibujar_tablero()

    ventana.bind("<Up>", lambda event: arriba())
    ventana.bind("<Down>",lambda event: abajo())
    ventana.bind("<Left>", lambda event: izquierda())
    ventana.bind("<Right>", lambda event: derecha())
    ventana.mainloop()

snake()