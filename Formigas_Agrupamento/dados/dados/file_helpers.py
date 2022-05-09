def readAndConfigurateMap(file_mame):
    configDict = {} 
    with open(file_mame) as f:
        configDict['map_type'] = int(f.readline().strip())
        configDict['iterations'] = int(f.readline().strip())
        configDict['qtd_agents'] = int(f.readline().strip())
        configDict['vision'] = int(f.readline().strip())
        configDict['alpha'] = float(f.readline().strip())
    return configDict

def readDatabase(database_name):
    with open(database_name) as f:
        database_content = f.readlines()
    return database_content
