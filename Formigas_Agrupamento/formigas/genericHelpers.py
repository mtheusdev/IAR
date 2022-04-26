import random
from constants import *

def generateMatrix():
  matrix = [[0 for j in range(MATRIX_LENGTH)] for i in range (MATRIX_LENGTH)]

  return matrix

def writeMatrixInFile(matrix, filename):
  line = '-'
  file = open(filename+'.txt','w')
  file.write(f' {line*MATRIX_LENGTH*3}\n')
  for i in range(MATRIX_LENGTH):
    file.write(f'|')
    for j in range(MATRIX_LENGTH):
        if matrix[i][j] == 0 or matrix[i][j] == 2:
          file.write(f'   ')
        elif matrix[i][j] == 1:
          file.write(f' o ')
        else:
          file.write(f' {matrix[i][j]} ')
    file.write("|\n")
  file.write(f' {line*MATRIX_LENGTH*3}\n')
  file.close()
  
def generateRandomDeads():
  return random.sample(range(0, TOTAL_MATRIX_CELS), DEAD_ANTS)

def generateRandomAlives(dead_ants_list):
    cont = 0
    alive_ants_list = []

    while cont < ALIVE_ANTS:
        ant_alive = random.randint(ALIVE_ANTS, TOTAL_MATRIX_CELS)
        try:
            dead_ants_list.index(ant_alive)
        except:
            try:
                alive_ants_list.index(ant_alive)
            except:
                alive_ants_list.append(ant_alive)
                cont += 1

    return alive_ants_list

def setDeadAnts(matrix,dead_ants_list):
  cont = 0

  for i in range(MATRIX_LENGTH):
    for j in range(MATRIX_LENGTH):    
      try:
        dead_ants_list.index(cont)
        matrix[i][j] = 1
      except:
        pass
      cont += 1

  return matrix


def setAliveAnts(matrix, alive_ants_list):
  cont = 0
  alive_ants_map = {}

  for i in range(MATRIX_LENGTH):
    for j in range(MATRIX_LENGTH):    
      try:
        alive_ants_list.index(cont)
        matrix[i][j] = 2
        alive_ants_map[cont] = [i, j]
      except:
        pass
      cont += 1

  return matrix
 
def makeListPostionAliveAnts(matrix):
    count = 0
    alive_ants_map = {}

    for i in range(MATRIX_LENGTH):
        for j in range(MATRIX_LENGTH):
            if matrix[i][j] == 2:
                alive_ants_map[count] = {'position': [i, j], 'state': EMPTY}
                count += 1

    return alive_ants_map

def showFinalReport(time):
  print('\n')
  print("Total de células da matriz:",TOTAL_MATRIX_CELS)
  print("Total de formigas mortas:",DEAD_ANTS)
  print("Total de formigas vivas:",ALIVE_ANTS)
  print("Total iterações:",QUANTITY_OF_ITERATIONS)
  print(f"Tempo total de execução: {time:.2f}s")
  print('\n')