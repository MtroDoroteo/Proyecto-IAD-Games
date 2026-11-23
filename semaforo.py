import tkinter as tk

class SemaforoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semaforo en Tkinter")
        self.root.geometry("250x420")
        self.root.config(bg="#2c3e50")

        # Variable para controlar la secuencia automática
        self.automatico = False
        self.estado_actual = 0  # 0: Rojo, 1: Verde, 2: Amarillo
        self.timer_id = None

        # Canvas para dibujar el semáforo
        self.canvas = tk.Canvas(root, width=140, height=280, bg="#34495e", highlightthickness=2, highlightbackground="#1a252f")
        self.canvas.pack(pady=15)

        # Dibujar las luces (apagadas por defecto con un color oscuro)
        self.luz_roja = self.canvas.create_oval(20, 20, 120, 90, fill="#4a0000", outline="")
        self.luz_amarilla = self.canvas.create_oval(20, 105, 120, 175, fill="#4a4a00", outline="")
        self.luz_verde = self.canvas.create_oval(20, 190, 120, 260, fill="#004a00", outline="")

        # Panel de controles
        frame_botones = tk.Frame(root, bg="#2c3e50")
        frame_botones.pack(pady=5)

        # Botones de cambio manual
        btn_rojo = tk.Button(frame_botones, text="Rojo", bg="#e74c3c", fg="white", font=("Arial", 9, "bold"), width=6, command=lambda: self.cambiar_luz("rojo"))
        btn_rojo.grid(row=0, column=0, padx=3, pady=2)

        btn_amarillo = tk.Button(frame_botones, text="Amarillo", bg="#f1c40f", fg="black", font=("Arial", 9, "bold"), width=6, command=lambda: self.cambiar_luz("amarillo"))
        btn_amarillo.grid(row=0, column=1, padx=3, pady=2)

        btn_verde = tk.Button(frame_botones, text="Verde", bg="#2ecc71", fg="white", font=("Arial", 9, "bold"), width=6, command=lambda: self.cambiar_luz("verde"))
        btn_verde.grid(row=0, column=2, padx=3, pady=2)

        # Botón para activar/desactivar modo automático
        self.btn_auto = tk.Button(root, text="Iniciar Automático", bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=self.toggle_automatico)
        self.btn_auto.pack(pady=10)

        # Encender la luz roja por defecto al iniciar
        self.cambiar_luz("rojo")

    def apagar_luces(self):
        """Restablece todas las luces a su tono apagado."""
        self.canvas.itemconfig(self.luz_roja, fill="#4a0000")
        self.canvas.itemconfig(self.luz_amarilla, fill="#4a4a00")
        self.canvas.itemconfig(self.luz_verde, fill="#004a00")

    def cambiar_luz(self, color):
        """Enciende la luz seleccionada y apaga las demás."""
        self.apagar_luces()
        if color == "rojo":
            self.canvas.itemconfig(self.luz_roja, fill="#ff0000")
            self.estado_actual = 0
        elif color == "amarillo":
            self.canvas.itemconfig(self.luz_amarilla, fill="#ffff00")
            self.estado_actual = 2
        elif color == "verde":
            self.canvas.itemconfig(self.luz_verde, fill="#00ff00")
            self.estado_actual = 1

    def secuencia_automatica(self):
        """Maneja la transición de luces en modo automático."""
        if not self.automatico:
            return

        # Secuencia típica: Rojo (3s) -> Verde (3s) -> Amarillo (1.5s)
        if self.estado_actual == 0:  # Esta en Rojo -> Pasa a Verde
            self.cambiar_luz("verde")
            self.timer_id = self.root.after(3000, self.secuencia_automatica)
        elif self.estado_actual == 1:  # Esta en Verde -> Pasa a Amarillo
            self.cambiar_luz("amarillo")
            self.timer_id = self.root.after(1500, self.secuencia_automatica)
        elif self.estado_actual == 2:  # Esta en Amarillo -> Pasa a Rojo
            self.cambiar_luz("rojo")
            self.timer_id = self.root.after(3000, self.secuencia_automatica)

    def toggle_automatico(self):
        """Activa o desactiva la secuencia automática."""
        self.automatico = not self.automatico
        if self.automatico:
            self.btn_auto.config(text="Detener Automático", bg="#e67e22")
            self.secuencia_automatica()
        else:
            self.btn_auto.config(text="Iniciar Automático", bg="#3498db")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoApp(root)
    root.mainloop()