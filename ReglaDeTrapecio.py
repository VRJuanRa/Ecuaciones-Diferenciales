import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
import tkinter as tk
from tkinter import messagebox

# --- Función para calcular la integral y graficar ---
def calcular():
    try:
        # Obtener valores de la interfaz
        funcion_str = entrada_funcion.get()
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        n = int(entrada_n.get())

        # Procesar la función
        x = symbols('x')
        f_sym = sympify(funcion_str)
        f = lambdify(x, f_sym, 'numpy')

        # Regla del trapecio
        h = (b - a) / n
        x_vals = np.linspace(a, b, n + 1)
        y_vals = f(x_vals)
        area = (h / 2) * (y_vals[0] + 2 * np.sum(y_vals[1:-1]) + y_vals[-1])

        # Mostrar resultado
        resultado.set(f"Aproximación de la integral = {area:.6f}")

        # --- Gráfica ---
        x_plot = np.linspace(a, b, 1000)
        y_plot = f(x_plot)

        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, y_plot, 'b', label=f"f(x) = {funcion_str}")
        plt.title("Regla del Trapecio")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.fill_between(x_plot, y_plot, color='lightblue', alpha=0.5, label=f"Integral ≈ {area:.6f}")

        # Dibujar trapecios
        for i in range(n):
            xs = [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]]
            ys = [0, y_vals[i], y_vals[i+1], 0]
            plt.fill(xs, ys, 'orange', alpha=0.3, edgecolor='red')

        plt.scatter(x_vals, y_vals, color='red', zorder=5)
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# --- Crear la ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora de Integrales - Regla del Trapecio")
ventana.geometry("400x350")
ventana.resizable(False, False)

# --- Etiquetas y campos de entrada ---
tk.Label(ventana, text="Ingrese la función f(x):").pack(pady=5)
entrada_funcion = tk.Entry(ventana, width=30)
entrada_funcion.pack()

tk.Label(ventana, text="Límite inferior (a):").pack(pady=5)
entrada_a = tk.Entry(ventana, width=15)
entrada_a.pack()

tk.Label(ventana, text="Límite superior (b):").pack(pady=5)
entrada_b = tk.Entry(ventana, width=15)
entrada_b.pack()

tk.Label(ventana, text="Número de particiones (n):").pack(pady=5)
entrada_n = tk.Entry(ventana, width=15)
entrada_n.pack()

# --- Botón para calcular ---
tk.Button(ventana, text="Calcular Integral", command=calcular, bg="lightblue").pack(pady=15)

# --- Etiqueta para mostrar el resultado ---
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, fg="green", font=("Arial", 10, "bold")).pack(pady=10)

# --- Iniciar la interfaz ---
ventana.mainloop()
