from random import random, randint
import formula_helpers as fh

class Agent():
    def __init__(self, num, alpha, N, items, vision):
        self.num = num
        self.x = int(random() * N)
        self.y = int(random() * N)
        self.full = None
        self.alpha = alpha
        self.count_fails = 0
        self.items = items
        self.vision = vision
        self.N = N

    def move(self):
        self.x = (self.x + randint(-1,1)) % self.N
        self.y = (self.y + randint(-1,1)) % self.N
        
    def walkAndInteract(self):
        while(True):
            self.move()
            item = self.items[self.x][self.y]
            if item and not self.full:
                if fh.pick(fh.similarity(self.x, self.y, item, self.items, self.alpha, self.vision, self.N)) > random():
                    self.full = self.items[self.x][self.y]
                    self.items[self.x][self.y] = []
                    break
                else:
                    self.count_fails += 1
            elif not item and self.full:
                if fh.drop(fh.similarity(self.x, self.y, self.full, self.items, self.alpha, self.vision, self.N)) > random():
                    self.items[self.x][self.y] = self.full
                    self.full = []
                    break
                else:
                    self.count_fails += 1

    def updatealpha(self):
        if self.count_fails / 10 > 0.99:
            self.alpha += 0.01
        else:
            self.alpha -= 0.01
        self.count_fails = 0
