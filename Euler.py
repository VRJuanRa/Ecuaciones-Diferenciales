import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def euler_method():
    tabla.delete(*tabla.get_children())
    fig.clear()

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    try:
        # Lectura de datos
        f_str = entry_funcion.get()
        f_xy = sp.sympify(f_str)

        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        h = float(entry_h.get())
        iterations = int(entry_iter.get())

        f = sp.lambdify((x, y), f_xy, "numpy")

        xs = [x0]
        ys = [y0]

        xk = x0
        yk = y0

        for k in range(iterations):
            y_next = yk + h * f(xk, yk)
            x_next = xk + h

            tabla.insert("", "end", values=[
                k,
                f"{xk:.5f}",
                f"{yk:.5f}",
                f"{y_next:.5f}"
            ])

            xs.append(x_next)
            ys.append(y_next)

            xk = x_next
            yk = y_next

        # Graficar
        ax = fig.add_subplot(111)
        ax.plot(xs, ys, marker='o')
        ax.set_title("Solución con Método de Euler")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)

        canvas.draw()

    except Exception as e:
        print("Error:", e)


# Ventana principal
ventana = tk.Tk()
ventana.title("Método de Euler")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Método de Euler — Equipo 4",
         font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

# Frame de entrada
frame_entrada = tk.Frame(ventana, bg="#F2F2F2")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="f(x, y) =", bg="#F2F2F2").grid(row=0, column=0)
entry_funcion = ttk.Entry(frame_entrada, width=25)
entry_funcion.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="x0:", bg="#F2F2F2").grid(row=0, column=2)
entry_x0 = ttk.Entry(frame_entrada, width=10)
entry_x0.grid(row=0, column=3, padx=5)

tk.Label(frame_entrada, text="y0:", bg="#F2F2F2").grid(row=0, column=4)
entry_y0 = ttk.Entry(frame_entrada, width=10)
entry_y0.grid(row=0, column=5, padx=5)

tk.Label(frame_entrada, text="h:", bg="#F2F2F2").grid(row=0, column=6)
entry_h = ttk.Entry(frame_entrada, width=10)
entry_h.grid(row=0, column=7, padx=5)

tk.Label(frame_entrada, text="Iteraciones:", bg="#F2F2F2").grid(row=0, column=8)
entry_iter = ttk.Entry(frame_entrada, width=10)
entry_iter.grid(row=0, column=9, padx=5)

ttk.Button(frame_entrada, text="Calcular", command=euler_method).grid(row=0, column=10, padx=10)

# Frame inferior con tabla y gráfica
frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

# Tabla de resultados
frame_tabla = tk.LabelFrame(frame_inferior, text="Resultados",
                            font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_tabla.pack(side="left", fill="y", padx=10)

cols = ["Iter", "x_k", "y_k", "y_(k+1)"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=25)
for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=100, anchor="center")
tabla.pack(padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 9))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

# Gráfica
frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica",
                              font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
