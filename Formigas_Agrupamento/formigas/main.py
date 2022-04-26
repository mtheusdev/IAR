# import random
# from constants import *
import genericHelpers as gh
import antsHelpers as ah
import time

initial = time.time() # em segundos

alive_ants_map = {}

dead_ants_list = gh.generateRandomDeads()
alive_ants_list = gh.generateRandomAlives(dead_ants_list)

matrix = gh.generateMatrix()
matrix = gh.setDeadAnts(matrix, dead_ants_list)
matrix = gh.setAliveAnts(matrix, alive_ants_list)
alive_ants_map = gh.makeListPostionAliveAnts(matrix)

# print(alive_ants_map)

gh.writeMatrixInFile(matrix, 'matrix_file')
ah.runAnts(alive_ants_map, matrix);

final = time.time()

gh.showFinalReport(final-initial)

