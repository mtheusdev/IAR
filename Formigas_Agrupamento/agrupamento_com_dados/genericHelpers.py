import random
from constants import *
from ant import Ant

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
        if matrix[i][j] == 0:
          file.write(f'   ')
        elif matrix[i][j] == -1:
         file.write(f' {matrix[i][j]} ')
        else:
          file.write(f' {matrix[i][j].label} ')
    file.write("|\n")
  file.write(f' {line*MATRIX_LENGTH*3}\n')
  file.close()
  
def generateRandomDataPosition():
  return random.sample(range(0, TOTAL_MATRIX_CELS), QTD_ITEMS)

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

def setDataInMatrix(matrix, position_items_list):
  cont = 0
  database_array_position = 0
  database = []
  database_randon_index_list = random.sample(range(0, QTD_ITEMS), QTD_ITEMS)

  ref_file = open("database.txt","r")
  for i in range(6):
    line = ref_file.readline()

  while line:
    line = ref_file.readline().split()
    database.append(line)

  for i in range(MATRIX_LENGTH):
    for j in range(MATRIX_LENGTH):    
      if cont in position_items_list:
        current_data = database[database_randon_index_list[database_array_position]]
        # print(current_data)
        database_array_position +=1
        matrix[i][j] = Ant(current_data[0], current_data[1], current_data[2])
      cont += 1

  ref_file.close()
  return matrix

def setAliveAnts(matrix, alive_ants_list):
  cont = 0
  alive_ants_map = {}

  for i in range(MATRIX_LENGTH):
    for j in range(MATRIX_LENGTH):    
      try:
        alive_ants_list.index(cont)
        matrix[i][j] = -1
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
            if matrix[i][j] == -1:
                alive_ants_map[count] = {'position': [i, j], 'state': EMPTY}
                count += 1

    return alive_ants_map

def showFinalReport(time):
  print('\n')
  print("Total de células da matriz:",TOTAL_MATRIX_CELS)
  print("Total de formigas mortas:",QTD_ITEMS)
  print("Total de formigas vivas:",ALIVE_ANTS)
  print("Total iterações:",QUANTITY_OF_ITERATIONS)
  print(f"Tempo total de execução: {time:.2f}s")
  print('\n')