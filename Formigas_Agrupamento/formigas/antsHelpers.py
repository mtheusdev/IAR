from constants import *
import random
import genericHelpers as gh
finished_iteration_ant = False

def checkMatrixCelExists(matrix, x, y):
  if not (x < 0 or y < 0 or x >= MATRIX_LENGTH or y >= MATRIX_LENGTH): # Existe a celula
    if matrix[x][y] == 1: # Tem formiga morta
      return 1
    else: # Não tem formiga morta
      return 2
  else:
    return 0

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
    matrix[current_position_ant_x][current_position_ant_y] = DEAD_ANT_CEL # SOLTA a formiguinha
    current_ant['state'] = EMPTY # Define seu estado como vazio
    finished_iteration_ant = True
  else:
    print(f"#DEBUG -> Formiga decidiu nao largar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
  return matrix, current_ant, finished_iteration_ant

def canWalk(x, y):
  if x >= MATRIX_LENGTH or y >= MATRIX_LENGTH or x < 0 or y < 0:
    return False
  else:
    return True


def antDecisionCatch(matrix, current_ant):
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

  resultDivision = quantity_of_items / quantity_of_vision #DIGAMOS 2/8 = 0.25 
  probability = random.random() #DIGAMOS 0.7

  print("ITEMS E VISÃO: ", quantity_of_items, quantity_of_vision)
  print("PROBABILIDADE E DIVISAO: ", probability, resultDivision)
  
  if probability >= resultDivision * resultDivision: # PEGOU
    print(f"#DEBUG -> Formiga decidiu pegar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
    matrix[current_position_ant_x][current_position_ant_y] = EMPTY_CEL # Pega a formiguinha
    current_ant['state'] = FULL # Define seu estado como carregando/cheio
  else:
    print(f"#DEBUG -> Formiga decidiu não pegar o item na posição x({current_position_ant_x}) y({current_position_ant_y})")
    # gh.writeMatrixInFile(matrix, 'matrix2_file')
    # exit(0)
  print(f"#DEBUG -> MATRIZ NA posição: x({current_position_ant_x}) y({current_position_ant_y}) = {matrix[current_position_ant_x][current_position_ant_y]}")
  return matrix, current_ant

def antBrain(matrix, current_ant):
  finished_iteration_ant = False

  while not finished_iteration_ant:
    position_X = current_ant['position'][0]
    position_Y = current_ant['position'][1]
    state = current_ant['state']
    direction = random.randint(1, 4)
    walked = False

    print(f"#DEBUG -> Formiga na posição atual: x({position_X}) y({position_Y})")
    print("#DEBUG -> Formiga tentará andar na direção:", direction)
    
    if direction == 1: # avança em x
      if canWalk(position_X + 1, position_Y):
        current_ant['position'][0] = position_X + 1
        current_ant['position'][1] = position_Y
        walked = True

    elif direction == 2: # avança em y
      if canWalk(position_X, position_Y + 1):
        current_ant['position'][0] = position_X
        current_ant['position'][1] = position_Y + 1
        walked = True

    elif direction == 3: # volta em x
      if canWalk(position_X - 1, position_Y):
        current_ant['position'][0] = position_X - 1
        current_ant['position'][1] = position_Y
        walked = True

    elif direction == 4: # volta em y
      if canWalk(position_X, position_Y - 1):
        current_ant['position'][0] = position_X
        current_ant['position'][1] = position_Y - 1
        walked = True

    if walked:
      print("#DEBUG -> formiga viva andou na direção:", direction)
      if matrix[position_X][position_Y] == 2:
        print("#DEBUG -> Retirando formiga viva da posição anterior") 
        matrix[position_X][position_Y] = EMPTY_CEL
  
      current_position_ant_x = current_ant['position'][0]
      current_position_ant_y = current_ant['position'][1]
      print("#DEBUG -> Formiga está na posição:", current_position_ant_x, current_position_ant_y)

      if matrix[current_position_ant_x][current_position_ant_y] == EMPTY_CEL and state == FULL:
        print(f"#DEBUG -> Formiga irá checar se solta o item na posição: x({current_position_ant_x}) y({current_position_ant_y})")
        matrix, current_ant, finished_iteration_ant = antDecisionDrop(matrix, current_ant, finished_iteration_ant)
      elif matrix[current_position_ant_x][current_position_ant_y] == DEAD_ANT_CEL and state == EMPTY:
        print(f"#DEBUG -> Formiga irá checar se pega o item na posição: x({current_position_ant_x}) y({current_position_ant_y})")
        matrix, current_ant = antDecisionCatch(matrix, current_ant)
    else:
      print("#DEBUG -> Não foi possivel andar por esse caminho:", direction)
    
    # gh.writeMatrixInFile(matrix, 'matrix2_file')
  return matrix, current_ant

def runAnts(alive_ants_map, matrix):
  cont = 0
  print(QUANTITY_OF_ITERATIONS)
  while cont < QUANTITY_OF_ITERATIONS:
    for a in range(ALIVE_ANTS):
      print("#DEBUG -> FORMIGA: ID", a, "CONTENT", alive_ants_map[a])
      matrix, alive_ants_map[a] = antBrain(matrix, alive_ants_map[a]) #Manda a formiga atual e a matriz para o cerebro
      gh.writeMatrixInFile(matrix, 'matrix2_file')
      # exit(0)
      cont+=1
  
 
  
