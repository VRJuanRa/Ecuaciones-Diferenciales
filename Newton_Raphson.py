import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def newton_raphson():
    #----------------------------------------------------------------------
    #               DATOS DE ENTRADA
    #----------------------------------------------------------------------
    
    try:
        f_str = entry_funcion.get()
        df_str = entry_derivada.get()
        x0 = float(entry_x0.get())
        n_iter = int(entry_iter.get())

        # Símbolo
        x = sp.Symbol('x')

        # Convertir cadenas a funciones
        f = sp.sympify(f_str)
        df = sp.sympify(df_str)
        
        #----------------------------------------------------------------------
        #               COMPROBAR QUE LA DERIVADA       Si no se pone esto la funcion se resuleve con cualquier derivada.
        #----------------------------------------------------------------------
        derivada_correcta = sp.diff(f, x)

        # Simplificar ambas para comparar
        if not sp.simplify(derivada_correcta - df) == 0:
            messagebox.showerror(
            "Derivada incorrecta",
            "La derivada ingresada no coincide con la derivada real de la función."
        )
            return  # detener

        #----------------------------------------------------------------------
        #    CONVIERTE LAS FUNCIONES PARA QUE PUEDAN SER EVALUADAS CON NUMPY
        #----------------------------------------------------------------------
        f_num = sp.lambdify(x, f, 'numpy')
        df_num = sp.lambdify(x, df, 'numpy')

        datos = [] #GUARDA LOS RESULTADOS DE CADA ITERACIÓN
        x_values = [x0] #GUARDA LOS VALORES PAR PODER GRAFICAR 


        #----------------------------------------------------------------------
        #              PROCESO DE NEWTON-RAPHSON
        #----------------------------------------------------------------------
        for i in range(n_iter): #HACE EL PROCESO CON EL NUMEOR DE VECES QUE PUSISTE EN TUS INTERACIONES
            fx = f_num(x0)
            dfx = df_num(x0)

            if dfx == 0:
                messagebox.showerror("Error", "La derivada es cero. No se puede continuar.")
                break

            x1 = x0 - fx / dfx # FÓRMULA DE NEWTON RAPHSON
            error = abs(x1 - x0) 

            datos.append([i+1, round(x0, 6), round(fx, 6), 
                          round(dfx, 6), round(x1, 6), round(error, 6)]) #AGREGA LOS DATOS DE INTERACIONES EL LA TABLA QUE HICIMOS LLAMADA DATOS
            

            x_values.append(x1)

            if error < 1e-7:
                break #PARA ENCOTRAR LA RAIZ SI YA SE ENCOTRO LO DETIENE

            x0 = x1 #PARA PODER SEGUIR CON LA SIGUIENTE INTERACIÓN

      #----------------------------------------------------------------------
      # TABLA CON LOS RESULTADOS EN BASE A LA INTERACIONES QUE SE NECESITAN
      #----------------------------------------------------------------------
        for i in tabla.get_children():
            tabla.delete(i)
        for row in datos:
            tabla.insert("", "end", values=row)
            
            
        #----------------------------------------------------------------------
        #                GRAFICA LA FUNCION
        #----------------------------------------------------------------------

        x_min = min(x_values) - 2
        x_max = max(x_values) + 2 # LIMITA EL RANGO DE LA GRAFICA
        x_vals = np.linspace(x_min, x_max, 400)
        y_vals = f_num(x_vals)
        fig.clear() #lIMPIA LA GRAFICA POR SI HABIA UNA ANTES DE ESA
        
        ax = fig.add_subplot(111)
        #HACE LAS LINEAS DE LOS EJES PUNTEADAS
        ax.axhline(0, color='black', linestyle='--', linewidth=1)
        ax.axvline(0, color='black', linestyle='--', linewidth=1) 
        ax.plot(x_vals, y_vals, label=f"f(x) = {f_str}")

       
        for i, row in enumerate(datos):
            xi = row[1]
            yi = f_num(xi)
            slope = df_num(xi)
            tx = np.linspace(xi - 1, xi + 1, 50) #HACEMOS LOS VALORES PARA LA RECTA TANGENTE EN CADA PUNTO
            ty = slope * (tx - xi) + yi
            ax.plot(tx, ty, color='orange', linestyle='--', alpha=0.7) #HACE LA RECTA TANGENTE 
            ax.scatter(xi, yi, color='red') #HACE LOS PUNTITOS ROJOS EN LA GRAFICA 
            ax.text(xi, yi, f"x{i}", fontsize=8) #INDICA EL NUMERO DE INTERACION EN LA GRAFICA

        raiz = datos[-1][4]
        raiz_y = f_num(raiz)

        ax.scatter(raiz, raiz_y, color='green', s=80,
                   label=f"Raíz encontrada = {round(raiz, 6)}")

        ax.set_title("Newton-Raphson")
        ax.set_xlabel("x") #DEFINICON DEL EJE X
        ax.set_ylabel("f(x)")  #DEFINCION DEL EJE Y 
        ax.legend() #SIMBOLOGIA
        ax.grid(True) #CUADRICULA
        canvas.draw()#IMPRIME LA GRAFICA

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

#----------------------------------------------------------------------
#                           VENTANA PRINCIPAL
#----------------------------------------------------------------------

ventana = tk.Tk()
ventana.title("Newton-Raphson")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#F2F2F2")

tk.Label(ventana, text="Newton-Raphson Equipo 4", font=("Segoe UI", 16, "bold"), bg="#F2F2F2").pack(pady=10)

frame_entrada = tk.Frame(ventana, bg="#F2F2F2")
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Función f(x):", bg="#F2F2F2").grid(row=0, column=0)
entry_funcion = ttk.Entry(frame_entrada, width=25)
entry_funcion.grid(row=0, column=1, padx=5)

tk.Label(frame_entrada, text="Derivada f'(x):", bg="#F2F2F2").grid(row=0, column=2)
entry_derivada = ttk.Entry(frame_entrada, width=25)
entry_derivada.grid(row=0, column=3, padx=5)

tk.Label(frame_entrada, text="x0:", bg="#F2F2F2").grid(row=0, column=4)
entry_x0 = ttk.Entry(frame_entrada, width=10)
entry_x0.grid(row=0, column=5, padx=5)

tk.Label(frame_entrada, text="Iteraciones máx:", bg="#F2F2F2").grid(row=0, column=6)
entry_iter = ttk.Entry(frame_entrada, width=10)
entry_iter.grid(row=0, column=7, padx=5)

ttk.Button(frame_entrada, text="Calcular", command=newton_raphson).grid(row=0, column=8, padx=10)

# Tabla y gráfica
frame_inferior = tk.Frame(ventana, bg="#F2F2F2")
frame_inferior.pack(expand=True, fill="both", padx=10, pady=10)

frame_tabla = tk.LabelFrame(frame_inferior, text="Resultados", font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_tabla.pack(side="left", fill="y", padx=10)

cols = ["Iteración", "x_k", "f(x_k)", "f'(x_k)", "x_(k+1)", "Error"]
tabla = ttk.Treeview(frame_tabla, columns=cols, show="headings", height=20)
for col in cols:
    tabla.heading(col, text=col)
    tabla.column(col, width=80, anchor="center")
tabla.pack(padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 9))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

frame_grafica = tk.LabelFrame(frame_inferior, text="Gráfica", font=("Segoe UI", 14, "bold"), bg="#F2F2F2")
frame_grafica.pack(side="right", fill="both", expand=True, padx=10)

fig = plt.Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()