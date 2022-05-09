from constants import *
import math
import random
import genericHelpers as gh
from dataItem import DataItem

finished_iteration_ant = False

def antDecisionDrop(matrix, current_ant, finished_iteration_ant):
  current_position_ant_x = current_ant['position'][0]
  current_position_ant_y = current_ant['position'][1]

  quantity_of_vision = 0
  quantity_of_items = 0
  cont_x = current_position_ant_x - 1

  while cont_x <= (current_position_ant_x + 1):
    cont_y = current_position_ant_y - 1
    while cont_y <= (current_position_ant_y + 1):
      if not (cont_x == current_position_ant_x and cont_y == current_position_ant_y):
        resultCheck = checkMatrixCelExists(matrix, cont_x, cont_y)
        if resultCheck == 2:
          quantity_of_vision += 1
        elif resultCheck == 1:
          quantity_of_vision += 1
          quantity_of_items += 1
        cont_y += 1
      else:
        cont_y += 1
    cont_x += 1

  resultDivision = quantity_of_items / quantity_of_vision 
  probability = random.random()
  
  print("ITEMS E VISÃO: ", quantity_of_items, quantity_of_vision)
  print("PROBABILIDADE E DIVISAO: ",probability, resultDivision)

  if probability <= resultDivision * resultDivision: # SOLTA
    print(f"#DEBUG -> Formiga decidiu largar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
    matrix[current_position_ant_x][current_position_ant_y] > 0 # SOLTA a formiguinha
    current_ant['state'] = EMPTY # Define seu estado como vazio
    finished_iteration_ant = True
  else:
    print(f"#DEBUG -> Formiga decidiu nao largar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
  return matrix, current_ant, finished_iteration_ant

def checkMatrixCelExists(matrix, x, y):
  if not (x < 0 or y < 0 or x >= MATRIX_LENGTH or y >= MATRIX_LENGTH): # Existe a celula
    if matrix[x][y] == 1: # Tem formiga morta
      return 1
    else: # Não tem formiga morta
      return 2
  else:
    return 0

def getValuePosition(matrix, current_x, current_y): # Pega retorna 0 se nao tiver nada ou um objeto dataItem caso tenha um dado
  new_x = current_x
  new_y = current_y

  if current_x >= MATRIX_LENGTH:
    new_x = current_x - MATRIX_LENGTH
  elif current_x <= 0: # -1
    new_x = MATRIX_LENGTH + current_x - 1
  
  if current_y >= MATRIX_LENGTH:
    new_y = current_y - MATRIX_LENGTH
  elif current_y <= 0:
    new_y = MATRIX_LENGTH + current_y - 1

  return matrix[new_x, new_y]

def euclidianDistance(currentData, targetData): # Retorna a distancia do dado da posicao atual e o a ser verificado
  return math.sqrt((currentData.x - targetData.x)**2 + (currentData.y - targetData.y)**2)

def antDecisionCatch(matrix, current_ant):
  current_position_ant_x = current_ant['position'][0]
  current_position_ant_y = current_ant['position'][1]
  current_data_item = matrix[current_position_ant_x][current_position_ant_y]
  cont_x = current_position_ant_x - ANT_VISION_RADIUS
  sum_distances = 0

  while cont_x <= (current_position_ant_x + ANT_VISION_RADIUS):
    cont_y = current_position_ant_y - ANT_VISION_RADIUS
    while cont_y <= (current_position_ant_y + 1):    
      targetDataItem = getValuePosition(matrix, cont_x, cont_y)
      if isinstance(targetDataItem, DataItem):
        sum_distances += euclidianDistance(current_data_item, targetDataItem)
      cont_y += 1
    cont_x += 1

  CONTINUAR AQUI: FORMULAS PARA PEGAR OU LARGAR

  # print("ITEMS E VISÃO: ", quantity_of_items, quantity_of_vision)
  # print("PROBABILIDADE E DIVISAO: ", probability, resultDivision)
  
  # if probability >= resultDivision: # PEGOU
  #   print(f"#DEBUG -> Formiga decidiu pegar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
  #   matrix[current_position_ant_x][current_position_ant_y] = EMPTY_CEL # Pega a formiguinha
  #   current_ant['state'] = FULL # Define seu estado como carregando/cheio
  # else:
  #   print(f"#DEBUG -> Formiga decidiu não pegar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
  #   # gh.writeMatrixInFile(matrix, 'matrix2_file')
  #   # exit(0)
  # print(f"#DEBUG -> MATRIZ NA posição: x({current_position_ant_x}) y({current_position_ant_y}) = {matrix[current_position_ant_x][current_position_ant_y]}")
  # return matrix, current_ant

def antWalk(current_ant, direction):
  if direction == 1: # avança em x
    afterMoveX = current_ant['position'][0] + 1
    if afterMoveX == MATRIX_LENGTH:
      current_ant['position'][0] = 0
    else: 
      current_ant['position'][0] = afterMoveX

  elif direction == 2: # avança em y
    afterMoveY = current_ant['position'][1] + 1
    if afterMoveY == MATRIX_LENGTH:
      current_ant['position'][1] = 0
    else: 
      current_ant['position'][1] = afterMoveY

  elif direction == 3: # volta em x
    afterMoveX = current_ant['position'][0] - 1
    if afterMoveX < 0:
      current_ant['position'][0] = MATRIX_LENGTH - 1
    else: 
      current_ant['position'][0] = afterMoveX

  elif direction == 4: # volta em y
    afterMoveY = current_ant['position'][1] - 1
    if afterMoveY < 0:
      current_ant['position'][1] = MATRIX_LENGTH - 1
    else: 
      current_ant['position'][1] = afterMoveY
  return current_ant

def antBrain(matrix, current_ant):
  finished_iteration_ant = False

  while not finished_iteration_ant:
    position_X = current_ant['position'][0]
    position_Y = current_ant['position'][1]
    state = current_ant['state']
    direction = random.randint(1, 4)

    print(f"#DEBUG -> Formiga na posição atual: x({position_X}) y({position_Y})")
    print("#DEBUG -> Formiga tentará andar na direção:", direction)

    current_ant = antWalk(current_ant, direction)
    print(f"#DEBUG -> Formiga andou para: x({current_ant['position'][0]}) y({current_ant['position'][1]})")

    if matrix[position_X][position_Y] == -1:
      print("#DEBUG -> Retirando formiga viva da posição anterior") 
      matrix[position_X][position_Y] = EMPTY_CEL

    current_position_ant_x = current_ant['position'][0]
    current_position_ant_y = current_ant['position'][1]

    print("#DEBUG -> Formiga está na posição:", current_position_ant_x, current_position_ant_y)

    # print("#DEBUG -> Matriz na posição", matrix[current_position_ant_x][current_position_ant_y])
    # print("#DEBUG -> Matriz na posição", type(matrix[current_position_ant_x][current_position_ant_y]))

    if matrix[current_position_ant_x][current_position_ant_y] == EMPTY_CEL and state == FULL:
      print(f"#DEBUG -> Formiga irá checar se solta o item na posição: x({current_position_ant_x}) y({current_position_ant_y})")
      matrix, current_ant, finished_iteration_ant = antDecisionDrop(matrix, current_ant, finished_iteration_ant)
    elif isinstance(matrix[current_position_ant_x][current_position_ant_y], DataItem) and state == EMPTY:
        print(f"#DEBUG -> Formiga irá checar se pega o item na posição: x({current_position_ant_x}) y({current_position_ant_y})")
        matrix, current_ant = antDecisionCatch(matrix, current_ant)

    exit(0)
    # gh.writeMatrixInFile(matrix, 'matrix2_file')
  return matrix, current_ant

def runAnts(alive_ants_map, matrix):
  cont = 0
  while cont < QUANTITY_OF_ITERATIONS:
    for a in range(ALIVE_ANTS):
      print("#DEBUG -> FORMIGA: ID", a, "CONTENT", alive_ants_map[a])
      matrix, alive_ants_map[a] = antBrain(matrix, alive_ants_map[a]) #Manda a formiga atual e a matriz para o cerebro
      gh.writeMatrixInFile(matrix, 'matrix2_file')
      exit(0)
      cont+=1
  
 
  
