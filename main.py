import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys

# -------------------------------
#   EJECUTAR EL ARCHIVOS
# -------------------------------
def lanzar_archivo(nombre_archivo):
    try:
        subprocess.Popen([sys.executable, nombre_archivo])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir {nombre_archivo}\n{e}")


# -------------------------------
#        DISEÑO VENTANA 
# -------------------------------
ventana = tk.Tk()
ventana.title("Herramientas Matemáticas - Equipo 4")
ventana.attributes("-fullscreen", True)
ventana.configure(bg="#F2F2F2")


titulo = tk.Label(
    ventana,
    text="Herramientas Matemáticas — Métodos Numéricos",
    font=("Segoe UI", 28, "bold"),
    bg="#F2F2F2",
    fg="#333333"
)
titulo.pack(pady=30)


frame = tk.Frame(ventana, bg="#F2F2F2")
frame.pack()


style = ttk.Style()
style.configure(
    "TButton",
    font=("Segoe UI", 14, "bold"),
    padding=10
)


botones = [
    ("Regla del Trapecio", "ReglaDeTrapecio.py"),
    ("Newton-Raphson", "Newton_Raphson.py"),
    ("Euler", "Euler.py"),
    ("Euler Mejorado", "Euler_Mejorado.py"),
    ("Runge-Kutta 4", "Runge-Kutta-4.py"),
    ("Coeficiente Constante", "Coef_Constante.py"),
]

fila = 0
col = 0

for texto, archivo in botones:
    btn = ttk.Button(
        frame,
        text=texto,
        width=25,
        command=lambda a=archivo: lanzar_archivo(a)
    )
    btn.grid(row=fila, column=col, padx=40, pady=25)

    col += 1
    if col == 2:  # 2 columnas
        col = 0
        fila += 1


def salir():
    ventana.destroy()

btn_salir = ttk.Button(
    ventana,
    text="Salir",
    command=salir
)
btn_salir.pack(pady=20)


footer = tk.Label(
    ventana,
    text="Proyecto Ecuaciones Diferenciales — Equipo 4",
    font=("Segoe UI", 12),
    fg="#666666",
    bg="#F2F2F2"
)
footer.pack(side="bottom", pady=20)

ventana.mainloop()
