import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def euler_constante():
    tabla.delete(*tabla.get_children())
    fig.clear()

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    try:
        #----------------------------------------------------------------------
        #                  LO QUE PUSO EL USUARIO
        #----------------------------------------------------------------------
        a = float(entry_a.get())
        b = float(entry_b.get())

        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        h = float(entry_h.get())
        iterations = int(entry_iter.get())

       
        #FUNCION DE LA EDO
        def f(xk, yk):
            return a * yk + b

        xs = [x0]
        ys = [y0]

        xk = x0
        yk = y0
        
        #----------------------------------------------------------------------
        #                   LO DE COEFICIENTE CONSTANTE
        #----------------------------------------------------------------------

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
        #----------------------------------------------------------------------
        #                EL HACENDOR DE LA GRÁFICA
        #----------------------------------------------------------------------
        ax = fig.add_subplot(111) #UNA COLUMNA UNA FILA UNA POSICION ES LO DE 111
        ax.plot(xs, ys, marker="o")
        ax.set_title("Método de Euler — Coeficiente Constante")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)

        canvas.draw()

    except Exception as e:
        print("Error:", e)


# ----------------------------
#           INTERFAZ
# ----------------------------
ventana = tk.Tk()
ventana.title("Euler — Ecuación con Coeficientes Constantes")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Método de Euler — a·y + b (Coeficientes Constantes)",
         font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

frame_entrada = tk.Frame(ventana, bg="#F2F2F2")
frame_entrada.pack(pady=10)

# COEFICIENTE a
tk.Label(frame_entrada, text="a:", bg="#F2F2F2").grid(row=0, column=0)
entry_a = ttk.Entry(frame_entrada, width=10)
entry_a.grid(row=0, column=1, padx=5)

# COEFICIENTE b
tk.Label(frame_entrada, text="b:", bg="#F2F2F2").grid(row=0, column=2)
entry_b = ttk.Entry(frame_entrada, width=10)
entry_b.grid(row=0, column=3, padx=5)

# x0 EL QUE LE INGRESAS
tk.Label(frame_entrada, text="x0:", bg="#F2F2F2").grid(row=0, column=4)
entry_x0 = ttk.Entry(frame_entrada, width=10)
entry_x0.grid(row=0, column=5, padx=5)

# y0 EL QUE LE INGRESAS
tk.Label(frame_entrada, text="y0:", bg="#F2F2F2").grid(row=0, column=6)
entry_y0 = ttk.Entry(frame_entrada, width=10)
entry_y0.grid(row=0, column=7, padx=5)

# h EL QUE LE INGRESAS
tk.Label(frame_entrada, text="h:", bg="#F2F2F2").grid(row=0, column=8)
entry_h = ttk.Entry(frame_entrada, width=10)
entry_h.grid(row=0, column=9, padx=5)

# INTERACIONES EL QUE LE INGRESAS
tk.Label(frame_entrada, text="Iteraciones:", bg="#F2F2F2").grid(row=0, column=10)
entry_iter = ttk.Entry(frame_entrada, width=10)
entry_iter.grid(row=0, column=11, padx=5)
 
ttk.Button(frame_entrada, text="Calcular", command=euler_constante).grid(row=0, column=12, padx=10) #BOTON QUE CALCULA

frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

# TABLA
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

# GRAFICA
frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica",
                              font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
