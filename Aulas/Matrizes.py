import numpy as np
print('#----------Matrizes----------#')
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matriz)
print('---')
print(matriz[0])
print('---')
print(matriz[0][0])
print('---')
print(matriz.shape)  # Como se fosse o 'len'
print('---')
for i in range(matriz.shape[0]):
    print(matriz[i])
print('---')
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
