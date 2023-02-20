## table_ball_loops

import numpy as np
v0 = eval(input('initial velocity:'))
n = eval(input('n value:'))
g = 9.8
step = ((2 * v0)/g)/(n + 1)
ty1 = []
t_values = np.arange(0, (2 * v0)/g, step)
y_values = []
for t in t_values:
    y = v0 * t - (1/2) * g * t**2
    y_values.append(y)
    # print(t, y)
ty1.append(t_values)
ty1.append(y_values)
# print(ty1)
for i in ty1:
    for j in ty1:
        print(f'{i[j]}, {i[j]}')


