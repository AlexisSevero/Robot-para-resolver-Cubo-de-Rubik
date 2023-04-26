import tkinter as tk
import numpy as np

Cube = np.empty((6, 3, 3), dtype=dict)
Cube_solve = np.empty((6, 3, 3), dtype=dict)

ventana = tk.Tk()
ventana.geometry('1400x1200')
ventana.title('CUBO')

colors = ["white", "yellow", "green", "blue", "red", "orange"]
color_index_f = 0
color_index_b = 1
color_index_u = 2
color_index_d = 3
color_index_l = 4
color_index_r = 5

# Define las matrices de colores
color_matrix_f = [[colors[0] for i in range(3)] for j in range(3)]
color_matrix_b = [[colors[1] for i in range(3)] for j in range(3)]
color_matrix_u = [[colors[2] for i in range(3)] for j in range(3)]
color_matrix_d = [[colors[3] for i in range(3)] for j in range(3)]
color_matrix_l = [[colors[4] for i in range(3)] for j in range(3)]
color_matrix_r = [[colors[5] for i in range(3)] for j in range(3)]


def change_color(event, i, j, matrix):
    global color_index_f, color_index_b, color_index_u, color_index_d, color_index_l, color_index_r
    current_color = event.widget.cget("bg")  # obtener el color actual del cuadrado
    current_color_index = colors.index(current_color)  # obtener el índice del color actual
    next_color_index = (current_color_index + 1) % len(colors)  # obtener el índice del siguiente color
    next_color = colors[next_color_index]  # obtener el siguiente color
    event.widget.config(bg=next_color)  # actualizar el color del cuadrado
    matrix[i][j] = next_color  # actualizar la matriz de colores correspondiente
    if matrix is color_matrix_f:
        color_index_f = next_color_index
    elif matrix is color_matrix_b:
        color_index_b = next_color_index
    elif matrix is color_matrix_u:
        color_index_u = next_color_index
    elif matrix is color_matrix_d:
        color_index_d = next_color_index
    elif matrix is color_matrix_l:
        color_index_l = next_color_index
    else:
        color_index_r = next_color_index

    for i, letra in enumerate(['F', 'B', 'U', 'D', 'L', 'R']):
        for j in range(3):
            for k in range(3):
                key = letra + str((j * 3) + k + 1)
                if letra == 'F':
                    Cube[0][j][k] = {key: color_matrix_f[k][j]}
                    Cube_solve[0][j][k] = {key: color_matrix_f[1][1]}
                elif letra == 'B':
                    Cube[1][j][k] = {key: color_matrix_b[k][j]}
                    Cube_solve[1][j][k] = {key: color_matrix_b[1][1]}
                elif letra == 'U':
                    Cube[2][j][k] = {key: color_matrix_u[k][j]}
                    Cube_solve[2][j][k] = {key: color_matrix_u[1][1]}
                elif letra == 'D':
                    Cube[3][j][k] = {key: color_matrix_d[k][j]}
                    Cube_solve[3][j][k] = {key: color_matrix_d[1][1]}
                elif letra == 'L':
                    Cube[4][j][k] = {key: color_matrix_l[k][j]}
                    Cube_solve[4][j][k] = {key: color_matrix_l[1][1]}
                elif letra == 'R':
                    Cube[5][j][k] = {key: color_matrix_r[k][j]}
                    Cube_solve[5][j][k] = {key: color_matrix_r[1][1]}


squares = []  # Lista para almacenar los cuadrados
for i in range(3):
    for j in range(3):
        # Usa el color correspondiente de la matriz
        square_f = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_f[i][j])
        square_f.place(x=250 + 100 * (i + 1), y=250 + 100 * (j + 1))

        square_b = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_b[i][j])
        square_b.place(x=850 + 100 * (i + 1), y=250 + 100 * (j + 1))

        square_u = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_u[i][j])
        square_u.place(x=250 + 100 * (i + 1), y=-50 + 100 * (j + 1))

        square_d = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_d[i][j])
        square_d.place(x=250 + 100 * (i + 1), y=550 + 100 * (j + 1))

        square_l = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_l[i][j])
        square_l.place(x=-50 + 100 * (i + 1), y=250 + 100 * (j + 1))

        square_r = tk.Frame(ventana, width=105, height=105, borderwidth=6, relief="solid", bg=color_matrix_r[i][j])
        square_r.place(x=550 + 100 * (i + 1), y=250 + 100 * (j + 1))

        # Pasa las posiciones del cuadrado como argumentos a la función change_color
        square_f.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_f: change_color(event, i, j, matrix))
        square_b.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_b: change_color(event, i, j, matrix))
        square_u.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_u: change_color(event, i, j, matrix))
        square_d.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_d: change_color(event, i, j, matrix))
        square_l.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_l: change_color(event, i, j, matrix))
        square_r.bind("<Button-1>", lambda event, i=i, j=j, matrix=color_matrix_r: change_color(event, i, j, matrix))

        squares.append(square_f)
        squares.append(square_b)
        squares.append(square_u)
        squares.append(square_d)
        squares.append(square_l)
        squares.append(square_r)  # Agrega el cuadrado a la lista

Imprimir = tk.Button(ventana, text="IMPRIMIR CUBO", bg="grey", font=('Arial', 15), command=lambda: print(Cube))
Imprimir.place(x=1000, y=100)
Imprimir.config(width=15, height=3)


ventana.mainloop()

