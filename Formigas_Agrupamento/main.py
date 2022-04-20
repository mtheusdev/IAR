import random

def generateRandomNumbers(finalRange, qtd):
  return random.sample(range(0, finalRange), qtd) 

def generateMatrix(matrixLen):
  matrix = [[' ' for j in range(matrixLen)] for i in range (matrixLen)]
  return matrix

def setDeadAnts(matrixLen, matrix, deadAntsList):
  cont = 0
  for i in range(matrixLen):
    for j in range(matrixLen):    
      try:
        deadAntsList.index(cont)
        matrix[i][j] = '°'
      except:
        pass
      cont += 1
  return matrix

deadAntsList = generateRandomNumbers(100, 30)
matrix = generateMatrix(10)
matrix = setDeadAnts(10, matrix, deadAntsList)

print('')
print(' --------------------------------------------------')
for i in range(10):
    print('|', end='')
    for j in range(10):
      print(f'  {matrix[i][j]}  ', end='')
    print('|\n|', end='')
    print('                                                  |')
    
print(' --------------------------------------------------')