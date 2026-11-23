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

# PALETA NEON ARCADE
FONDO = "#071B33"
AZUL = "#00BFFF"
VERDE = "#39FF14"
NARANJA = "#FF7900"
BLANCO = "#FFFFFF"
CASILLA = "#102D4D"

def reiniciar_juego(boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9):
    global tablero, turno, label
    tablero = [
        ['','',''],
        ['','',''],
        ['','','']
    ]
    turno = 'X'
    label.config(text="TURNO DE: " + turno, fg=NARANJA)
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
        color = NARANJA
    else:
        color = AZUL
    boton.config(text=turno, disabledforeground=color, state='disabled')

    tablero[fila][columna] = turno
    print(tablero)

    ganador = comprobar_ganador()
    if ganador:
        label.config(text="GANADOR: " + ganador, fg=VERDE)
        return

    cambiar_turno()

def cambiar_turno():
    global turno, label, no_turno
    if turno == 'X':
        turno = 'O'
        color = AZUL
    else:
        turno = 'X'
        color = NARANJA

    label.config(text="TURNO DE: " + turno, fg= color)

def main():
    ventana = tk.Tk()
    ventana.title("NEON ARCADE | GATO")
    ventana.geometry("1000x1000")
    ventana.resizable(False, False)
    ventana.configure(bg=FONDO)

    global label
    label = tk.Label(
        ventana,
        text="TURNO DE: " + turno,
        font=("Arial", 20, "bold"),
        fg=NARANJA,
        bg=FONDO
    )
    label.grid(row=3, column=0, columnspan=3, pady=(20, 0))

    boton00 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=AZUL,
        command=lambda: presionar_boton(boton00,0,0)
    )
    boton00.grid(row = 0, column = 0,padx=(65,4), pady=(30, 4))

    boton01 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=VERDE,
        command=lambda: presionar_boton(boton01,0,1)
    )
    boton01.grid(row = 0, column = 1,padx=4, pady=(30, 4))

    boton02 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=NARANJA,
        command=lambda: presionar_boton(boton02,0,2)
    )
    boton02.grid(row = 0, column = 2,padx=4, pady=(30, 4))

    boton10 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=NARANJA,
        command=lambda: presionar_boton(boton10,1,0)
    )
    boton10.grid(row = 1, column = 0,padx=(65,4), pady=4)

    boton11 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=AZUL,
        command=lambda: presionar_boton(boton11,1,1)
    )
    boton11.grid(row = 1, column = 1,padx=4, pady=4)

    boton12 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=VERDE,
        command=lambda: presionar_boton(boton12,1,2)
    )
    boton12.grid(row = 1, column = 2,padx=4, pady=4)

    boton20 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=VERDE,
        command=lambda: presionar_boton(boton20,2,0)
    )
    boton20.grid(row = 2, column = 0,padx=(65,4), pady=4)

    boton21 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=NARANJA,
        command=lambda: presionar_boton(boton21,2,1)
    )
    boton21.grid(row = 2, column = 1,padx=4, pady=4)

    boton22 = tk.Button(
        ventana,
        width=11,
        height=5,
        bg=CASILLA,
        activebackground=AZUL,
        fg=BLANCO,
        font=("Arial", 20, "bold"),
        relief="flat",
        bd=3,
        highlightthickness=2,
        highlightbackground=AZUL,
        command=lambda: presionar_boton(boton22,2,2)
    )
    boton22.grid(row = 2, column = 2,padx=4, pady=4)
    
    botonreinicio = tk.Button(
        ventana,
        text="REINICIAR",
        width=15,
        height=2,
        bg=NARANJA,
        fg=FONDO,
        activebackground=VERDE,
        activeforeground=FONDO,
        font=("Arial", 11, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        command=lambda: reiniciar_juego(boton00, boton01, boton02, boton10, boton11, boton12, boton20, boton21, boton22)
    )
    botonreinicio.grid(row=4, column=1, pady=(20, 0))

    ventana.mainloop()

main()
