import math
import file_helpers as fh
import generic_helpers as gh
from constants import *
from agent import Agent
from classMap import ClassMap

# Start steps for configuration
configurations_map = fh.readAndConfigurateMap('configuration.txt')
database_content = fh.readDatabase('database' + str(configurations_map['map_type']) + '.txt')
database_content = [list(map(float, x.strip().split())) for x in database_content]
N = int(math.sqrt((len(database_content))/0.10))
WIDTH = 800 / N - MARGIN
HEIGHT = 800 / N - MARGIN
## End steps for configuration

# Instantiate map object and operate
mapObject = ClassMap(N)
mapObject.setMap()
items = mapObject.getMap()
items = gh.setRandomPostitionItems(database_content, items, N)
mapObject.show(items)

# Instantiate agents
agents = [Agent(num, configurations_map['alpha'], N, items, configurations_map['vision']) for num in range(configurations_map['qtd_agents'])]

# Run
gh.run(configurations_map['iterations'], configurations_map['map_type'], agents, WIDTH, HEIGHT, items, N)
