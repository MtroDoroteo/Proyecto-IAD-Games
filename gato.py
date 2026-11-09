import tkinter as tk

global tablero
tablero = [
    ['','',''],
    ['','',''],
    ['','','']
]

global turno
turno = 'X'

global no_turno
no_turno = 0

def reiniciar_juego(boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9):
    global tablero, turno, label
    tablero = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    turno = 'X'
    label.config(text="Turno de: " + turno, fg="#FF0000")
    boton1.config(text='', state='normal')
    boton2.config(text='', state='normal')
    boton3.config(text='', state='normal')
    boton4.config(text='', state='normal')
    boton5.config(text='', state='normal')
    boton6.config(text='', state='normal')
    boton7.config(text='', state='normal')
    boton8.config(text='', state='normal')
    boton9.config(text='', state='normal')

def comprobar_ganador():
    global tablero
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return tablero[0][i]
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return tablero[0][2]
    
    return None

def presionar_boton(boton, fila, columna):
    if turno == 'X':
        color = '#FF0000'
    else:
        color = '#0000FF'
    boton.config(text=turno, disabledforeground=color, state='disabled')

    tablero[fila][columna] = turno
    print(tablero)

    ganador = comprobar_ganador()
    if ganador:
        label.config(text="Ganador: " + ganador, fg="#00FF00")
        return

    cambiar_turno()

def cambiar_turno():
    global turno, label, no_turno
    if turno == 'X':
        turno = 'O'
        color = '#0000FF'
    else:
        turno = 'X'
        color = '#FF0000'

    label.config(text="Turno de: " + turno, fg= color)

def main():
    ventana = tk.Tk()
    ventana.title("Gato")
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    
    global label
    label = tk.Label(
        ventana,
        text="Turno de: " + turno,
        font=("Arial", 20),
        fg="#FF0000"
    )
    label.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    boton00 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton00,0,0)
    )
    boton00.grid(row = 0, column = 0,padx=(125,0), pady=(20, 0))

    boton01 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton01,0,1)
    )
    boton01.grid(row = 0, column = 1,padx=(0,0), pady=(20, 0))

    boton02 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton02,0,2)
    )
    boton02.grid(row = 0, column = 2,padx=(0,0), pady=(20, 0))

    boton10 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton10,1,0)
    )
    boton10.grid(row = 1, column = 0,padx=(125,0), pady=(0, 0))

    boton11 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton11,1,1)
    )
    boton11.grid(row = 1, column = 1,padx=(0,0), pady=(0, 0))

    boton12 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton12,1,2)
    )
    boton12.grid(row = 1, column = 2,padx=(0,0), pady=(0, 0))

    boton20 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton20,2,0)
    )
    boton20.grid(row = 2, column = 0,padx=(125,0), pady=(0, 0))

    boton21 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton21,2,1)
    )
    boton21.grid(row = 2, column = 1,padx=(0,0), pady=(0, 0))

    boton22 = tk.Button(
        ventana,
        width=11,
        height=5,
        command=lambda: presionar_boton(boton22,2,2)
    )
    boton22.grid(row = 2, column = 2,padx=(0,0), pady=(0, 0))
    
    botonreinicio = tk.Button(
        ventana,
        text="Reiniciar",
        width=10,
        height=2,
        command=lambda: reiniciar_juego(boton00, boton01, boton02, boton10, boton11, boton12, boton20, boton21, boton22)
    )
    botonreinicio.grid(row=4, column=1, pady=(20, 0))

    ventana.mainloop()

main()