class ClassMap():
    def __init__(self, N):
        self.map = []
        self.N = N

    def setMap(self):
        self.map = [[[] for _ in range(self.N)] for _ in range(self.N)]

    def getMap(self):
        return self.map

    def show(self, items):
        print('####################')
        for x in items:
            for y in x:
                if y != []:
                    print(int(y[2]), end=' ')
                else:
                    print(end = ' ')
            print()
        print('####################')
