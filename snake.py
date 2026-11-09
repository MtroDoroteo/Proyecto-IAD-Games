#IMPORTACIÓN DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox

#VARIABLES GLOBALES
tablero = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

colores = {
    "COLOR_FONDO" : "#6e85d4"
}

#FUNCIONES

def arriba():
    pass

def abajo():
    pass

def izquierda():
    pass

def derecha():
    pass

def dibujar_snake():
    pass


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

    canva = tk.Canvas( #CANVAS SON LOS LIENZOS SOBRE LOS QUE DIBUJARÉ
        ventana,
        width = 800,
        height = 400,
        bg = colores["COLOR_FONDO"],
        highlightbackground=colores['COLOR_FONDO']
    )
    canva.pack()

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

    ventana.bind("<Up>", arriba)
    ventana.bind("<Down>", abajo)
    ventana.bind("<Left>", izquierda)
    ventana.bind("<Right>", derecha)
    ventana.mainloop()

snake()