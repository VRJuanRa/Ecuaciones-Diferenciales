import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys

# -------------------------------
#   FUNCIÓN PARA EJECUTAR ARCHIVOS
# -------------------------------
def lanzar_archivo(nombre_archivo):
    try:
        subprocess.Popen([sys.executable, nombre_archivo])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir {nombre_archivo}\n{e}")


# -------------------------------
#        VENTANA PRINCIPAL
# -------------------------------
ventana = tk.Tk()
ventana.title("Herramientas Matemáticas")
ventana.geometry("600x400")
ventana.configure(bg="#1e1e2f")   # Fondo oscuro elegante


# -------------------------------
#          TÍTULO
# -------------------------------
titulo = tk.Label(
    ventana,
    text="Herramientas Matemáticas",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
titulo.pack(pady=20)


# -------------------------------
#   FRAME PRINCIPAL DE BOTONES
# -------------------------------
frame = tk.Frame(ventana, bg="#1e1e2f")
frame.pack(pady=10)


# Estilo de botones
style = ttk.Style()
style.configure(
    "TButton",
    font=("Segoe UI", 14, "bold", ),
    padding=10
)

# -------------------------------
#      BOTONES DEL MENÚ
# -------------------------------
btn1 = ttk.Button(
    frame,
    text="Regla del Trapecio",
    command=lambda: lanzar_archivo("ReglaDeTrapecio.py")
)
btn1.grid(row=0, column=0, padx=20, pady=20)


btn2 = ttk.Button(
    frame,
    text="Newton-Raphson",
    command=lambda: lanzar_archivo("Newton_Raphson.py")
)
btn2.grid(row=0, column=1, padx=20, pady=20)


# -------------------------------
# PIE DE PÁGINA
# -------------------------------
footer = tk.Label(
    ventana,
    text="Proyecto Ecuaciones Diferenciales - Equipo 4",
    font=("Segoe UI", 10),
    fg="lightgray",
    bg="#1e1e2f"
)
footer.pack(side="bottom", pady=15)


# -------------------------------
#     EJECUTAR INTERFAZ
# -------------------------------
ventana.mainloop()
