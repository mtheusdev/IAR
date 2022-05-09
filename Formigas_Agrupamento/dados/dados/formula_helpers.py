import math

def euclidianDistance(current_item, target_item):
    #print(current_item, target_item)
    return math.sqrt((current_item[0] - target_item[0])**2 + (current_item[1] - target_item[1])**2)

def similarity(x, y, item, items, alpha, vision, N):
    x = [*range(x - vision, x + vision)]
    y = [*range(y - vision, y + vision)]
    f = 0.0
    for posx in x:
        for posy in y:
            x_ = posx % N
            y_ = posy % N
            if items[x_][y_] != [] and items[x_][y_] != item:
                f += (1 - euclidianDistance(item, items[x_][y_])/ alpha)
    return max(0,f/4)

def pick(similarity):
    if similarity <= 1:
        return 1.0
    return 1/(similarity**2)

def drop(similarity):
    if similarity >= 1:
        return 1.0
    return similarity**4

