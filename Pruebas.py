p_d_color = [('white', 'blue'), ('white', 'green'), ('white', 'red'), ('white', 'orange'), ('yellow', 'blue'), ('yellow', 'green'), ('yellow', 'red'), ('yellow', 'orange'), ('blue', 'red'), ('blue', 'orange'), ('green', 'red'), ('green', 'orange')]
#p_d_lugar = [('F2', 'U8'), ('F4', 'L6'), ('F6', 'R4'), ('F8', 'D2'), ('B2', 'U2'), ('B4', 'R6'), ('B6', 'L4'), ('B8', 'D8'), ('U4', 'L2'), ('U6', 'R2'), ('D4', 'L8'), ('D6', 'R8')]

from Cubo import *
Pos_d = []
P_dif = []
for i in range(6):
    pos = [(i, 0, 1), (i, 1, 0), (i, 1, 2), (i, 2, 1)]
    Pos_d.append(pos)
for n in Pos_d[0]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])
for n in Pos_d[1]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])
for n in Pos_d[2]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])
for n in Pos_d[3]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])
for n in Pos_d[4]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])
for n in Pos_d[5]:
    P_dif.append(Cube[n[0]][n[1]][n[2]])

for i in range(12):
    for j in range(2):
        if (P_dif[1]['F4'] != p_d_color[i][j]) and (P_dif[18]['L6'] != p_d_color[i][j]):
            print(p_d_color[i][j])

#for pos in [(0,0,1), (0,1,0), (0,1,2), (0,2,1)]:
#    print(Cube[pos[0]][pos[1]][pos[2]])
#blanco azul
#blanco verde
#blanco rojo
#blanco naranja
#amarrillo azul
#amarrillo verde
#amarrillo rojo
#amarrillo naranja
#azul rojo
#azul naranja
#verde rojo
#verde naranja

# 'F2', 'U8'
# 'F6', 'R4'
# 'F8', 'D2'
# 'F4', 'L6'
# 'B2', 'U2'
# 'B6', 'L4'
# 'B8', 'D8'
# 'B4', 'R6'
# 'U6', 'R2'
# 'U4', 'L2'
# 'D6', 'R8'
# 'D4', 'L8'
