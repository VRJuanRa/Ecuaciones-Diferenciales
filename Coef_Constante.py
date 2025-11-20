import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
#----------------------------------------------------------------------
#                            FUNCIONES
#----------------------------------------------------------------------

def normalizar(expr: str) -> str:
    return expr.replace("^", "**").replace("sen", "sin")

def newton_find_root(f, df, x0, tol=1e-6, max_iter=50):
    for _ in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            return None
        x1 = x0 - fx/dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

def resolver():
    tabla.delete(*tabla.get_children())
    fig.clear()
    
    try:
        poly_input = entry_poly.get()
        poly_input = normalizar(poly_input)
        x = sp.Symbol('x')
        f_expr = sp.sympify(poly_input)
        df_expr = sp.diff(f_expr, x)

        f = sp.lambdify(x, f_expr, "numpy")
        df = sp.lambdify(x, df_expr, "numpy")
        
        #----------------------------------------------------------------------
        #                       BUSCA RAICES
        #----------------------------------------------------------------------

        roots = []
        for x0 in np.linspace(-10, 10, 40):
            r = newton_find_root(f, df, x0)
            if r is not None:
                r = np.round(r, 6)
                if r not in roots:
                    roots.append(r)
                    
        #----------------------------------------------------------------------
        #                       LLENAR TABLA 
        #----------------------------------------------------------------------

        for i, r in enumerate(roots, 1):
            tabla.insert("", "end", values=[i, r])

        # Mostrar solución general
        sol = " + ".join([f"C{i+1}*e^({r}x)" for i,r in enumerate(roots)])
        label_sol.config(text=f"Solución general: {sol}")

        # Graficar
        X = np.linspace(-10, 10, 400)
        Y = f(X)
        ax = fig.add_subplot(111)
        ax.plot(X, Y, label=f"f(x) = {poly_input}", linewidth=2)
        for r in roots:
            ax.plot(r, f(r), "ro")
            ax.text(r, f(r), f"{r}", fontsize=9)
        ax.axhline(0, color="black")
        ax.grid(True)
        ax.set_title("EcuaciON con Coeficiente - Newton-Raphson")
        ax.legend()
        canvas.draw()

    except Exception as e:
        print("Error:", e)

 #----------------------------------------------------------------------
 #                             INTERFAZ
 #----------------------------------------------------------------------
 
ventana = tk.Tk()
ventana.title("Newton-Raphson – Coeficiente Constante")
ventana.geometry("1000x600")

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Ecuación característica:").grid(row=0, column=0)
entry_poly = ttk.Entry(frame_entrada, width=40)
entry_poly.grid(row=0, column=1, padx=5)
ttk.Button(frame_entrada, text="Resolver", command=resolver).grid(row=0, column=2, padx=5)

label_sol = tk.Label(ventana, text="Solución general: ", font=("Segoe UI", 12, "bold"))
label_sol.pack(pady=5)

frame_inferior = tk.Frame(ventana)
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

# TABLA DE RAICES 
frame_tabla = tk.LabelFrame(frame_inferior, text="Raíces", font=("Segoe UI", 12, "bold"))
frame_tabla.pack(side="left", fill="y", padx=10)
cols = ["#", "Raíz"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=25)
for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=80, anchor="center")
tabla.pack(padx=10, pady=10)

# GRAFICA
frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica", font=("Segoe UI", 12, "bold"))
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)
fig = plt.Figure(figsize=(6,4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
