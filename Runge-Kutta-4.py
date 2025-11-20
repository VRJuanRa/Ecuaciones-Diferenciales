import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------------------------
# MÉTODO RUNGE-KUTTA 4
# ----------------------------
def runge_kutta_4():
    tabla.delete(*tabla.get_children())
    fig.clear()

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    try:
        # Obtener datos
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
            k1 = h * f(xk, yk)
            k2 = h * f(xk + h/2, yk + k1/2)
            k3 = h * f(xk + h/2, yk + k2/2)
            k4 = h * f(xk + h, yk + k3)

            y_next = yk + (k1 + 2*k2 + 2*k3 + k4) / 6
            x_next = xk + h

            tabla.insert("", "end", values=[
                k,
                f"{xk:.5f}",
                f"{yk:.5f}",
                f"{k1:.5f}",
                f"{k2:.5f}",
                f"{k3:.5f}",
                f"{k4:.5f}",
                f"{y_next:.5f}"
            ])

            xs.append(x_next)
            ys.append(y_next)

            xk = x_next
            yk = y_next

        # Graficar
        ax = fig.add_subplot(111)
        ax.plot(xs, ys, marker="o")
        ax.set_title("Solución con Runge-Kutta 4")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)

        canvas.draw()

    except Exception as e:
        print("Error:", e)


# ----------------------------
# INTERFAZ TKINTER
# ----------------------------
ventana = tk.Tk()
ventana.title("Runge-Kutta de Orden 4")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Método Runge-Kutta 4° — Equipo 4",
         font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

# ----------------------------
# ENTRADAS
# ----------------------------
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

ttk.Button(frame_entrada, text="Calcular", command=runge_kutta_4).grid(row=0, column=10, padx=10)

# ----------------------------
# TABLA + GRÁFICA
# ----------------------------
frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

# Tabla
frame_tabla = tk.LabelFrame(frame_inferior, text="Resultados",
                            font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_tabla.pack(side="left", fill="y", padx=10)

cols = ["Iter", "x_k", "y_k", "k1", "k2", "k3", "k4", "y_(k+1)"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=25)
for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=80, anchor="center")
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
