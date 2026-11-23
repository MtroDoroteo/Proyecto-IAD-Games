#IMPORTACIÓN DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox

import random as r

#VARIABLES GLOBALES
tablero=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

vivo = True

head = {
    'x':2,
    'y':5
}

#FUNCIONES PRINCIPALES

def generar_manzana():
    m_x = r.randint(0,4)
    m_y = r.randint(0,9)

    while tablero[m_x][m_y] == 1:
        m_x = r.randint(0,4)
        m_y = r.randint(0,9)
    global manzana
    manzana = {
        'x': m_x,
        'y': m_y
    }

    cambiar_tablero(manzana["x"], manzana["y"], 2)

def reiniciar_todo():
    global vivo
    limpiar_tablero(head["x"], head["y"])
    quitar_manzanas(manzana["x"], manzana["y"])
    head["x"] = 2
    head["y"] = 5
    tablero[head["x"]][head["y"]] = 1
    vivo = True
    generar_manzana()
    dibujar_tablero()

def arriba():
    global vivo
    if vivo:
        if head["x"] > 0:
            limpiar_tablero(head["x"], head["y"])
            cambiar_tablero(head["x"]-1,head["y"], 1)

            head["x"] -= 1

            comprobar_comer()

            dibujar_tablero()
        else:
            messagebox.showerror("","GAME OVER")
            vivo = False

def abajo():
    global vivo
    if vivo:
        if head["x"]+1 < 5:
            limpiar_tablero(head["x"], head["y"])
            cambiar_tablero(head["x"]+1, head["y"], 1)
            head["x"] += 1
            
            comprobar_comer()
            
            dibujar_tablero()
        else:
            vivo = False
            messagebox.showerror("","GAME OVER")

def izquierda():
    global vivo
    if vivo:
        if head["y"] > 0:
            limpiar_tablero(head["x"], head["y"])
            cambiar_tablero(head["x"], head["y"]-1, 1)
            head["y"] -= 1
            
            comprobar_comer()
            
            dibujar_tablero()
        else:
            vivo = False
            messagebox.showerror("","GAME OVER")

def derecha():
    global vivo
    if vivo:
        if head["y"] < 9:
            limpiar_tablero(head["x"], head["y"])
            cambiar_tablero(head["x"], head["y"]+1, 1)
            head["y"] += 1
            
            comprobar_comer()
            
            dibujar_tablero()
        else:
            vivo = False
            messagebox.showerror("","GAME OVER")

#FUNCIONES AUXILIARES
def comprobar_comer():
    if head["x"] == manzana["x"] and head["y"] == manzana["y"]:
        generar_manzana()

def cambiar_tablero(x,y,valor):
    tablero[x][y] = valor

def quitar_manzanas(x,y):
    tablero[x][y] = 0

def limpiar_tablero(x,y):
    global tablero
    tablero[x][y] = 0
    canva.delete("all")

def dibujar_tablero():
    for fila in range(5):
            for columna in range(10):
                #DIBUJAMOS LA CUADRICULA
                canva.create_rectangle(
                            (columna * 75) + 2, (fila * 75) + 2,
                            (columna * 75) + 77, (fila * 75) + 77,
                            outline="#000000"
                            )
                #COLOCAMOS UN CIRCULO VERDE DONDE HAYA UN 1 EN EL ARREGLO
                if tablero[fila][columna] == 1:
                    canva.create_oval(
                        (columna * 75) + 7, (fila * 75) + 7,
                        (columna * 75) + 72, (fila * 75) + 72,
                        fill="#00FF00"
                    )
                
                if tablero[fila][columna] == 2:
                    canva.create_oval(
                        (columna * 75) + 15, (fila * 75) + 15,
                        (columna * 75) + 61, (fila * 75) + 61,
                        fill="#FF0000"
                    )

#MAIN
def main():
    ventana = tk.Tk()
    ventana.geometry("1000x600")
    ventana.title("Snake")
    ventana.resizable(False,False)

    global canva
    canva = tk.Canvas(
        ventana,
        width=800,
        height=400,
        bg= "#FFFFFF"
    )
    canva.pack()

    generar_manzana()
    dibujar_tablero()

    reiniciar = tk.Button(
        ventana,
        text="Reiniciar",
        command= lambda: reiniciar_todo()
    )
    reiniciar.pack()
                
    ventana.bind("<Up>", lambda event: arriba())
    ventana.bind("<Down>", lambda event: abajo())
    ventana.bind("<Left>", lambda event: izquierda())
    ventana.bind("<Right>", lambda event: derecha())
    ventana.bind("<r>", lambda event: reiniciar_todo())
    ventana.mainloop()

main()