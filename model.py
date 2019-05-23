class Cube:
    colors = [[], [], [], [], [], []]

    def __init__(self):
        self.colors = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                       ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                       ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

    def iscorrect(self):
        correct = True
        for i, c in enumerate(self.colors):
            if correct:
                for color in self.colors[i]:
                    if color == self.colors[i][-1]:
                        correct = True
                    else:
                        correct = False
                        break
        print('correct = ', correct)

    def __turnclockwise(self, side):
        merke = []
        for i in range(8):
            merke.append(self.colors[side][i])
        for i in range(8):
            self.colors[side][i] = merke[i - 2]

    def turnleft(self):
        self.__turnclockwise(1)

        merke = []
        merke.append(self.colors[0][0])
        merke.append(self.colors[0][7])
        merke.append(self.colors[0][6])

        self.colors[0][0] = self.colors[5][4]
        self.colors[0][7] = self.colors[5][3]
        self.colors[0][6] = self.colors[5][2]
        self.colors[5][4] = self.colors[4][0]
        self.colors[5][3] = self.colors[4][7]
        self.colors[5][2] = self.colors[4][6]

        self.colors[4][0] = self.colors[2][0]
        self.colors[4][7] = self.colors[2][7]
        self.colors[4][6] = self.colors[2][6]

        self.colors[2][0] = merke[0]
        self.colors[2][7] = merke[1]
        self.colors[2][6] = merke[2]

    def turnright(self):
        self.__turnclockwise(3)

        merke = []
        for i in range(2, 5):
            merke.append(self.colors[0][i])
            self.colors[0][i] = self.colors[2][i]
            self.colors[2][i] = self.colors[4][i]
        self.colors[4][2] = self.colors[5][6]
        self.colors[4][3] = self.colors[5][7]
        self.colors[4][4] = self.colors[5][0]

        self.colors[5][6] = merke[0]
        self.colors[5][7] = merke[1]
        self.colors[5][0] = merke[2]

    def turnup(self):
        self.__turnclockwise(0)

        merke = []
        for i in range(3):
            merke.append(self.colors[2][i])
        for i in range(3):
            self.colors[2][i] = self.colors[3][i]
            self.colors[3][i] = self.colors[5][i]
            self.colors[5][i] = self.colors[1][i]
            self.colors[1][i] = merke[i]

    def turndown(self):
        self.__turnclockwise(4)

        merke = []
        for i in range(6,3,-1):
            merke.append(self.colors[2][i])
            self.colors[2][i] = self.colors[1][i]
            self.colors[1][i] = self.colors[5][i]
            self.colors[5][i] = self.colors[3][i]
        self.colors[3][6] = merke[0]
        self.colors[3][5] = merke[1]
        self.colors[3][4] = merke[2]

    def turnfront(self):
        self.__turnclockwise(2)

        merke = []
        for i in range(6, 3, -1):
            merke.append(self.colors[0][i])
        self.colors[0][6] = self.colors[1][4]
        self.colors[0][5] = self.colors[1][3]
        self.colors[0][4] = self.colors[1][2]

        self.colors[1][4] = self.colors[4][2]
        self.colors[1][3] = self.colors[4][1]
        self.colors[1][2] = self.colors[4][0]

        self.colors[4][2] = self.colors[3][0]
        self.colors[4][1] = self.colors[3][7]
        self.colors[4][0] = self.colors[3][6]

        self.colors[3][0] = merke[0]
        self.colors[3][7] = merke[1]
        self.colors[3][6] = merke[2]

    def turnback(self):
        self.__turnclockwise(5)

        merke = []
        for i in range(3):
            merke.append(self.colors[0][i])
        self.colors[0][0] = self.colors[3][2]
        self.colors[0][1] = self.colors[3][3]
        self.colors[0][2] = self.colors[3][4]

        self.colors[3][2] = self.colors[4][4]
        self.colors[3][3] = self.colors[4][5]
        self.colors[3][4] = self.colors[4][6]

        self.colors[4][4] = self.colors[1][6]
        self.colors[4][5] = self.colors[1][7]
        self.colors[4][6] = self.colors[1][0]

        self.colors[1][6] = merke[0]
        self.colors[1][7] = merke[1]
        self.colors[1][0] = merke[2]
