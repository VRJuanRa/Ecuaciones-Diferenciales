import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#----------------------------------------------------------------------    
#                           METODO RK4 
# ----------------------------------------------------------------------
def runge_kutta_4():

    tabla.delete(*tabla.get_children())  # LIMPIA TABLA 
    fig.clear()  # LIMPIA GRAFICA

    t = sp.Symbol('t')
    x = sp.Symbol('x')

    try:
        #----------------------------------------------------------------------
        #               LO QUE EL USUARIO ESCRIBE
        #----------------------------------------------------------------------
        f_str = entry_funcion.get()
        f_tx = sp.sympify(f_str)

        t0 = float(entry_t0.get())      
        x0 = float(entry_x0.get())      
        h = float(entry_h.get())
        tf = x0   #LO QUE PIDIO EL PROFE 

        if h == 0:
            raise ValueError("El paso h no puede ser cero.")
        
        # ----------------------------------------------------
        # CONVERTIR A FUNCIÓN PARA QUE LA ENTIENDA EL PYTHON
        # ----------------------------------------------------
        f = sp.lambdify((t, x), f_tx, "numpy")

        ts = [t0]
        xs = [x0]

        tk_ = t0
        xk = x0
        k = 0
        
        # ----------------------------------------------------
        # RK4 
        # ----------------------------------------------------
        while (h > 0 and tk_ < tf) or (h < 0 and tk_ > tf):

            k1 = h * f(tk_, xk)
            k2 = h * f(tk_ + h/2, xk + k1/2)
            k3 = h * f(tk_ + h/2, xk + k2/2)
            k4 = h * f(tk_ + h, xk + k3)

            x_next = xk + (k1 + 2*k2 + 2*k3 + k4) / 6
            t_next = tk_ + h
            
            # ----------------------------------------------------
            # HACENDOR DE TABLA
            # ----------------------------------------------------
            
            tabla.insert("", "end", values=[
                k,
                f"{tk_:.5f}",
                f"{xk:.5f}",
                f"{k1:.5f}",
                f"{k2:.5f}",
                f"{k3:.5f}",
                f"{k4:.5f}",
                f"{x_next:.5f}"
            ])

            ts.append(t_next)
            xs.append(x_next)

            tk_ = t_next
            xk = x_next
            k += 1

        # ----------------------------------------------------
        #                     GRAFICA
        # ----------------------------------------------------
        ax = fig.add_subplot(111)
        ax.plot(ts, xs, marker="o", linestyle="-", label="RK4")

        ax.set_title("Solucion de Runge–Kutta 4", fontsize=12)
        ax.set_xlabel("t")
        ax.set_ylabel("x")
        ax.grid(True)

        canvas.draw()

    except Exception as e:
        print("Error:", e)


# ----------------------------------------------------
#              INTERFAZ GRÁFICA 
# ----------------------------------------------------
ventana = tk.Tk()
ventana.title("Runge-Kutta 4 — Equipo 4")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Método Runge-Kutta — Equipo 4",
         font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

# ENTRADAS
frame_entrada = tk.Frame(ventana, bg="#F2F2F2")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="f(t, x) =", bg="#F2F2F2").grid(row=0, column=0)
entry_funcion = ttk.Entry(frame_entrada, width=25)
entry_funcion.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="t0:", bg="#F2F2F2").grid(row=0, column=2)
entry_t0 = ttk.Entry(frame_entrada, width=10)
entry_t0.grid(row=0, column=3, padx=5)

tk.Label(frame_entrada, text="x0:", bg="#F2F2F2").grid(row=0, column=4)
entry_x0 = ttk.Entry(frame_entrada, width=10)
entry_x0.grid(row=0, column=5, padx=5)

tk.Label(frame_entrada, text="h:", bg="#F2F2F2").grid(row=0, column=6)
entry_h = ttk.Entry(frame_entrada, width=10)
entry_h.grid(row=0, column=7, padx=5)

ttk.Button(frame_entrada, text="Calcular", command=runge_kutta_4).grid(row=0, column=8, padx=10)

# TABLA
frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

frame_tabla = tk.LabelFrame(frame_inferior, text="Resultados",
                            font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_tabla.pack(side="left", fill="y", padx=10)

cols = ["Iter", "t_k", "x_k", "k1", "k2", "k3", "k4", "x_(k+1)"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=25)

for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=90, anchor="center")

tabla.pack(padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 9))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

# GRÁFICA
frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica",
                              font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
