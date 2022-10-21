def cant_see_game(matrix):
     positions = []
     for i in range(1, len(matrix) - 1):
         for j in range(0, len(matrix[i]) - 1):
             if matrix[i][j] < matrix[i - 1][j]:
                 positions.append((i, j))

     return positions

stadium =     [[1, 2, 3, 2, 1, 1],

               [2, 4, 4, 3, 7, 2],

               [5, 5, 2, 5, 6, 4],

               [6, 6, 7, 6, 7, 5]]

print(cant_see_game(stadium))