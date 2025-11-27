import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def euler_method():

    # LIMPIA TABLA Y GRÁFICA
    tabla.delete(*tabla.get_children())
    fig.clear()

    # DEFINIENDO LOS SÍMBOLOS
    t = sp.Symbol('t')
    x = sp.Symbol('x')

    try:
        # ENTRADAS DEL USUARIO
        f_str = entry_funcion.get()
        f_tx = sp.sympify(f_str)

        t0 = float(entry_x0.get())     
        x0 = float(entry_y0.get())      
        h = float(entry_h.get())
        tf = x0   # LO QUE PIDIO EL PROFE  

        if h == 0:
            raise ValueError("El paso 'h' no puede ser cero.")

        # TRADUCTOR DE PYTHON EN POCAS PALABRAS
        f = sp.lambdify((t, x), f_tx, "numpy")

        # LISTAS PARA GRAFICAR
        ts = [t0]
        xs = [x0]

        tk_ = t0
        xk = x0
        k = 0

        # ----------------------------------------------------
        #          MÉTODO DE EULER
        # ----------------------------------------------------
        while (h > 0 and tk_ < tf) or (h < 0 and tk_ > tf):

            x_next = xk + h * f(tk_, xk)
            t_next = tk_ + h

            # HACENDOR DE TABLA
            tabla.insert("", "end", values=[
                k,
                f"{tk_:.5f}",
                f"{xk:.5f}",
                f"{x_next:.5f}"
            ])

            ts.append(t_next)
            xs.append(x_next)

            tk_ = t_next
            xk = x_next
            k += 1

        # ----------------------------------------------------
        #       GRAFICAR RESULTADOS
        # ----------------------------------------------------
        ax = fig.add_subplot(111)
        ax.plot(ts, xs, marker='o', linestyle='-', label="Euler")

        ax.set_title("Solución con Método de Euler\n" ,
                     fontsize=12)

        ax.set_xlabel("t")
        ax.set_ylabel("x")
        ax.grid(True)

        canvas.draw()

    except Exception as e:
        tabla.insert("", "end", values=["Error", "", "", str(e)])


# #----------------------------------------------------------------------
#              INTERFAZ GRÁFICA 
# #----------------------------------------------------------------------
ventana = tk.Tk()
ventana.title("Método de Euler — Intervalo [t0, tf]")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Método de Euler — Equipo 4",
         font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

frame_entrada = tk.Frame(ventana, bg="#F2F2F2")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="f(t, x) =", bg="#F2F2F2").grid(row=0, column=0)
entry_funcion = ttk.Entry(frame_entrada, width=25)
entry_funcion.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="t0:", bg="#F2F2F2").grid(row=0, column=2)
entry_x0 = ttk.Entry(frame_entrada, width=10)
entry_x0.grid(row=0, column=3, padx=5)

tk.Label(frame_entrada, text="x0:", bg="#F2F2F2").grid(row=0, column=4)
entry_y0 = ttk.Entry(frame_entrada, width=10)
entry_y0.grid(row=0, column=5, padx=5)

tk.Label(frame_entrada, text="h:", bg="#F2F2F2").grid(row=0, column=6)
entry_h = ttk.Entry(frame_entrada, width=10)
entry_h.grid(row=0, column=7, padx=5)

ttt_button = ttk.Button(frame_entrada, text="Calcular", command=euler_method)
ttt_button.grid(row=0, column=8, padx=10)

frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

frame_tabla = tk.LabelFrame(frame_inferior, text="Resultados",
                            font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_tabla.pack(side="left", fill="y", padx=10)

cols = ["Iter", "t_k", "x_k", "x_(k+1)"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=25)

for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=100, anchor="center")

tabla.pack(padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 9))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica",
                              font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
