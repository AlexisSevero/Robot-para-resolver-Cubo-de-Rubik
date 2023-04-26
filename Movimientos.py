import tkinter
import serial
from Cubo import Cube
import copy
from time import sleep

def move_cube(move):
    Cube_old = copy.deepcopy(Cube)
    if move == 'F':
        for j in range(3):
            for k in range(3):
                Cube[0][j][(k-2)*(-1)] = Cube_old[0][k][j]
        for n in range(3):
            Cube[2][2][n] = Cube_old[4][(n - 2) * (-1)][2]
            Cube[5][n][0] = Cube_old[2][2][n]
            Cube[3][0][n] = Cube_old[5][(n - 2) * (-1)][0]
            Cube[4][n][2] = Cube_old[3][0][n]
        ser.write(b'F')

    elif move == 'f':
        for j in range(3):
            for k in range(3):
                Cube[0][(k-2)*(-1)][j] = Cube_old[0][j][k]
        for n in range(3):
            Cube[2][2][n] = Cube_old[5][n][0]
            Cube[5][n][0] = Cube_old[3][0][(n - 2) * (-1)]
            Cube[3][0][n] = Cube_old[4][n][2]
            Cube[4][n][2] = Cube_old[2][2][(n - 2) * (-1)]
        ser.write(b'f')

    elif move == 'B':
        for j in range(3):
            for k in range(3):
                Cube[1][j][(k-2)*(-1)] = Cube_old[1][k][j]
        for n in range(3):
            Cube[2][0][n] = Cube_old[5][n][2]
            Cube[4][n][0] = Cube_old[2][0][(n - 2) * (-1)]
            Cube[3][2][n] = Cube_old[4][n][0]
            Cube[5][n][2] = Cube_old[3][2][(n - 2) * (-1)]
        ser.write(b'B')

    elif move == 'b':
        for j in range(3):
            for k in range(3):
                Cube[1][(k-2)*(-1)][j] = Cube_old[1][j][k]
        for n in range(3):
            Cube[2][0][n] = Cube_old[4][(n - 2) * (-1)][0]
            Cube[4][n][0] = Cube_old[3][2][n]
            Cube[3][2][n] = Cube_old[5][(n - 2) * (-1)][2]
            Cube[5][n][2] = Cube_old[2][0][n]
        ser.write(b'b')

    elif move == 'U':
        for j in range(3):
            for k in range(3):
                Cube[2][j][(k-2)*(-1)] = Cube_old[2][k][j]
        for n in range(3):
            Cube[0][0][n] = Cube_old[5][0][n]
            Cube[4][0][n] = Cube_old[0][0][n]
            Cube[1][0][n] = Cube_old[4][0][n]
            Cube[5][0][n] = Cube_old[1][0][n]
        ser.write(b'U')

    elif move == 'u':
        for j in range(3):
            for k in range(3):
                Cube[2][(k-2)*(-1)][j] = Cube_old[2][j][k]
        for n in range(3):
            Cube[0][0][n] = Cube_old[4][0][n]
            Cube[4][0][n] = Cube_old[1][0][n]
            Cube[1][0][n] = Cube_old[5][0][n]
            Cube[5][0][n] = Cube_old[0][0][n]
        ser.write(b'u')

    elif move == 'D':
        for j in range(3):
            for k in range(3):
                Cube[3][j][(k-2)*(-1)] = Cube_old[3][k][j]
        for n in range(3):
            Cube[0][2][n] = Cube_old[4][2][n]
            Cube[4][2][n] = Cube_old[1][2][n]
            Cube[1][2][n] = Cube_old[5][2][n]
            Cube[5][2][n] = Cube_old[0][2][n]
        ser.write(b'D')

    elif move == 'd':
        for j in range(3):
            for k in range(3):
                Cube[3][(k-2)*(-1)][j] = Cube_old[3][j][k]
        for n in range(3):
            Cube[0][2][n] = Cube_old[5][2][n]
            Cube[4][2][n] = Cube_old[0][2][n]
            Cube[1][2][n] = Cube_old[4][2][n]
            Cube[5][2][n] = Cube_old[1][2][n]
        ser.write(b'd')

    elif move == 'L':
        for j in range(3):
            for k in range(3):
                Cube[4][j][(k-2)*(-1)] = Cube_old[4][k][j]
        for n in range(3):
            Cube[2][n][0] = Cube_old[1][(n - 2) * (-1)][2]
            Cube[0][n][0] = Cube_old[2][n][0]
            Cube[3][n][0] = Cube_old[0][n][0]
            Cube[1][n][2] = Cube_old[3][(n - 2) * (-1)][0]
        ser.write(b'L')

    elif move == 'l':
        for j in range(3):
            for k in range(3):
                Cube[4][(k-2)*(-1)][j] = Cube_old[4][j][k]
        for n in range(3):
            Cube[2][n][0] = Cube_old[0][n][0]
            Cube[0][n][0] = Cube_old[3][n][0]
            Cube[3][n][0] = Cube_old[1][(n - 2) * (-1)][2]
            Cube[1][n][2] = Cube_old[2][(n - 2) * (-1)][0]
        ser.write(b'l')

    elif move == 'R':
        for j in range(3):
            for k in range(3):
                Cube[5][j][(k-2)*(-1)] = Cube_old[5][k][j]
        for n in range(3):
            Cube[2][n][2] = Cube_old[0][n][2]
            Cube[1][n][0] = Cube_old[2][(n - 2) * (-1)][2]
            Cube[3][n][2] = Cube_old[1][(n - 2) * (-1)][0]
            Cube[0][n][2] = Cube_old[3][n][2]
        ser.write(b'R')

    elif move == 'r':
        for j in range(3):
            for k in range(3):
                Cube[5][(k-2)*(-1)][j] = Cube_old[5][j][k]
        for n in range(3):
            Cube[2][n][2] = Cube_old[1][(n - 2) * (-1)][0]
            Cube[1][n][0] = Cube_old[3][(n - 2) * (-1)][2]
            Cube[3][n][2] = Cube_old[0][n][2]
            Cube[0][n][2] = Cube_old[2][n][2]
        ser.write(b'r')

    elif move == 'M':
        for j in range(3):
            for k in range(3):
                Cube[5][j][k] = Cube_old[5][(j-2)*(-1)][(k-2)*(-1)]
        for j in range(3):
            for k in range(3):
                Cube[4][j][k] = Cube_old[4][(j-2)*(-1)][(k-2)*(-1)]

        for n in range(3):
            Cube[2][n][2] = Cube_old[3][n][2]
            Cube[1][n][0] = Cube_old[0][(n - 2) * (-1)][2]
            Cube[3][n][2] = Cube_old[2][n][2]
            Cube[0][n][2] = Cube_old[1][(n - 2) * (-1)][0]

        for n in range(3):
            Cube[2][n][0] = Cube_old[3][n][0]
            Cube[1][n][2] = Cube_old[0][(n - 2) * (-1)][0]
            Cube[3][n][0] = Cube_old[2][n][0]
            Cube[0][n][0] = Cube_old[1][(n - 2) * (-1)][2]
        ser.write(b'M')

    return Cube
    PLL(Cube)

def PLL():
    if ('B2' in Cube[0][0][1]) & ('L2' in Cube[5][0][1]) & ('F2' in Cube[1][0][1]) & ('R2' in Cube[4][0][1]):
        print('entro')
        movimientos = ['M', 'u', 'u', 'M', 'u', 'M', 'u', 'u', 'M', 'U']
        for movimiento in movimientos:
            move_cube(movimiento)
            sleep(0.2)
    elif (('R2' in Cube[4][0][1]) & ('B2' in Cube[5][0][1]) & ('L2' in Cube[1][0][1])):
        movimientos = ['R', 'U', 'r', 'U', 'r', 'u', 'R', 'R', 'u', 'r', 'U', 'r', 'U', 'R']
        for movimiento in movimientos:
            move_cube(movimiento)
            sleep(0.2)


ser = serial.Serial('COM3', 9600, timeout = 1)

move = ''

ventana = tkinter.Tk()

ventana.geometry("800x800")

etiqueta = tkinter.Label(ventana, text = "CONTROL DE MOTORES", bg = "grey", font = ("Arial", 20))
etiqueta.pack(fill = tkinter.X)

b_f = tkinter.Button(ventana, text = "FRONT", bg = "white",font = ('Arial', 15), command = lambda: [move := 'F', move_cube(move)])

b_f.place(x=350, y=150)

b_b = tkinter.Button(ventana, text = "BACK", bg = "yellow",font = ('Arial', 15),command = lambda: [move := 'B', move_cube(move)])
b_b.place(x=350, y=250)

b_u = tkinter.Button(ventana, text = "UP", bg = "blue",font = ('Arial', 15),command = lambda: [move := 'U', move_cube(move)])
b_u.place(x=350, y=350)

b_d = tkinter.Button(ventana, text = "DOWN", bg = "green",font = ('Arial', 15),command = lambda: [move := 'D', move_cube(move)])
b_d.place(x=350, y=450)

b_l = tkinter.Button(ventana, text = "LEFT", bg = "orange",font = ('Arial', 15),command = lambda: [move := 'L', move_cube(move)])
b_l.place(x=350, y=550)

b_r = tkinter.Button(ventana, text = "RIGHT", bg = "red",font = ('Arial', 15),command = lambda: [move := 'R', move_cube(move)])
b_r.place(x=350, y=650)

imprimir = tkinter.Button(ventana, text = "Print", bg = "red",font = ('Arial', 15),command = lambda: print(Cube))
imprimir.place(x=500, y=550)

cruz = tkinter.Button(ventana, text = "PLL", bg = "pink",font = ('Arial', 15),command = lambda:  [PLL()])
cruz.place(x=500, y=650)

ventana.mainloop()



