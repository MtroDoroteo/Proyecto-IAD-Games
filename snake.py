#IMPORTACIÓN DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox
import random as r

#VARIABLES GLOBALES

def generar_manzana():
    global manzana
    manzana = {
        "x": r.randint(0,4),
        "y": r.randint(0,9)
    }

def cambiar_tablero():
    global tablero, manzana
    tablero = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    tablero[head["x"]][head["y"]] = 1
    tablero[manzana["x"]][manzana["y"]] = 2

colores = {
    "COLOR_FONDO" : "#6e85d4"
}

head = {
    "x":2,
    "y":5
}

vivo = True

generar_manzana()
cambiar_tablero()

#FUNCIONES
def reiniciar_todo():
    global vivo
    borrar_tablero()
    head["x"] = 2
    head["y"] = 5
    generar_manzana()
    cambiar_tablero()
    dibujar_tablero()
    vivo = True

def mover(operacion, comparacion, letra):
    global vivo
    if vivo:
        head[letra] += operacion
        if comparacion:
            cambiar_tablero()
            borrar_tablero()
            dibujar_tablero()
        else:
            vivo = False
            messagebox.showerror("GAMGE OVER", "GAME OVER")

def arriba():
    mover(-1, head["x"] > 0, "x")

def abajo():
    mover(1, head["x"] < 4, "x")

def izquierda():
    mover(-1, head["y"] > 0, "y")

def derecha():
    mover(1, head["y"] < 9, "y")

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
                
            if tablero[fila][columna] == 2:
                canva.create_oval(
                    x1+15, y1+15,
                    x2-15, y2-15,
                    fill="#ff0000",
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

    reiniciar = tk.Button(
        ventana,
        text="Reiniciar",
        font=("Arial", 20),
        command=lambda:reiniciar_todo()
    )
    reiniciar.pack()

    ventana.bind("r",lambda event:reiniciar_todo())
    ventana.bind("<Up>", lambda event: arriba())
    ventana.bind("<Down>",lambda event: abajo())
    ventana.bind("<Left>", lambda event: izquierda())
    ventana.bind("<Right>", lambda event: derecha())
    ventana.mainloop()

snake()