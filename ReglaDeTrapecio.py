import numpy as np      
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
import tkinter as tk
from tkinter import messagebox

# --- Función para calcular la integral y graficar ---
def calcular():
    try:
        # Obtener valores de la interfaz
        funcion_str = entrada_funcion.get()     # Función como cadena respetando sintaxis
        a = float(entrada_a.get())              # Límite inferior
        b = float(entrada_b.get())              # Límite superior
        n = int(entrada_n.get())                # Número de particiones

        # Procesar la función
        x = symbols('x')
        f_sym = sympify(funcion_str)
        f = lambdify(x, f_sym, 'numpy')

        # Regla del trapecio
        h = (b - a) / n                                                             # Ancho de cada subintervalo
        x_vals = np.linspace(a, b, n + 1)                                           # Puntos de evaluación
        y_vals = f(x_vals)                                                          # Valores de la función en esos puntos 
        area = (h / 2) * (y_vals[0] + 2 * np.sum(y_vals[1:-1]) + y_vals[-1])        # Cálculo del área  

        # Mostrar resultado
        resultado.set(f"Aproximación de la integral = {area:.6f}")

        # --- Gráfica ---
        x_plot = np.linspace(a, b, 1000)                                      # Puntos para la gráfica
        y_plot = f(x_plot)                                                    # Valores de la función para la gráfica

        plt.figure(figsize=(10, 6))                                           # Crear figura
        plt.plot(x_plot, y_plot, 'b', label=f"f(x) = {funcion_str}")          # Graficar la función
        plt.title("Regla del Trapecio")                                       # Título de la gráfica    
        plt.xlabel("x")                                                       # Etiqueta eje x
        plt.ylabel("f(x)")                                                    # Etiqueta eje y
        plt.grid(True)
        plt.fill_between(x_plot, y_plot, color='lightblue', alpha=0.5, label=f"Integral ≈ {area:.6f}") # Área bajo la curva

        # Dibujar trapecios
        for i in range(n):
            xs = [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]]                # Coordenadas x del trapecio
            ys = [0, y_vals[i], y_vals[i+1], 0]                                  # Coordenadas y del trapecio
            plt.fill(xs, ys, 'lightblue', alpha=0.3, edgecolor='red')            # Rellenado de trapecio (color y borde)

        plt.scatter(x_vals, y_vals, color='red', zorder=5)                       # Puntos de evaluación
        plt.legend()                                                         
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")                  # Manejo de errores 

# ======== Crear la ventana principal =========
ventana = tk.Tk()                                                               # Crear ventana
ventana.title("Calculadora de Integrales - Regla del Trapecio")                 # Título de la ventana
ventana.geometry("400x350")                                                     # Tamaño de la ventana
ventana.resizable(False, False)                                                 # No redimensionable

# --- Etiquetas y campos de entrada ---
tk.Label(ventana, text="Ingrese la función f(x):").pack(pady=5)                 # Etiqueta para la función
entrada_funcion = tk.Entry(ventana, width=30)                                   # Campo de entrada para la función
entrada_funcion.pack()                                                          # Empaquetar el campo para mostrarlo

tk.Label(ventana, text="Límite inferior (a):").pack(pady=5)                     # Etiqueta para límite inferior
entrada_a = tk.Entry(ventana, width=15)                                         # Campo de entrada para límite inferior                 
entrada_a.pack()                                                                # Empaquetar el campo para mostrarlo            

tk.Label(ventana, text="Límite superior (b):").pack(pady=5)                     # Etiqueta para límite superior
entrada_b = tk.Entry(ventana, width=15)
entrada_b.pack()

#-Muestra etiqueta y campo de entrada para el número de particiones-
tk.Label(ventana, text="Número de particiones (n):").pack(pady=5)               # Etiqueta para número de particiones
entrada_n = tk.Entry(ventana, width=15)                                         # Campo de entrada para número de particiones
entrada_n.pack()

# --- Botón para calcular ---
tk.Button(ventana, text="Calcular Integral", command=calcular, bg="lightblue").pack(pady=15)

# --- Etiqueta para mostrar el resultado ---
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, fg="green", font=("Arial", 10, "bold")).pack(pady=10)
ventana.mainloop()

