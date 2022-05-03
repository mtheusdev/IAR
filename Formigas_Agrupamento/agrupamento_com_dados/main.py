# import random
# from constants import *
import genericHelpers as gh
import antsHelpers as ah
import time

initial = time.time() # em segundos

alive_ants_map = {}

data_positions_list = gh.generateRandomDataPosition()
# print(data_positions_list)
alive_ants_list = gh.generateRandomAlives(data_positions_list)
# print(alive_ants_list)
matrix = gh.generateMatrix()
# print(matrix)
matrix = gh.setDataInMatrix(matrix, data_positions_list)
# print(matrix)
matrix = gh.setAliveAnts(matrix, alive_ants_list)
# print(matrix)
alive_ants_map = gh.makeListPostionAliveAnts(matrix)

# print(alive_ants_map)

gh.writeMatrixInFile(matrix, 'matrix_file')
ah.runAnts(alive_ants_map, matrix);

# final = time.time()

# gh.showFinalReport(final-initial)

