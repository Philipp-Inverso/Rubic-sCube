class Printer:
    from colorama import Fore, Back, Style

    __RESET = Fore.RESET + Back.RESET + Style.NORMAL
    __YELLOW = Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + '  ' + __RESET
    __RED = Fore.RED + Back.RED + '  ' + __RESET
    __GREEN = Fore.GREEN + Back.GREEN + '  ' + __RESET
    __BLUE = Fore.BLUE + Back.BLUE + '  ' + __RESET
    __WHITE = Fore.WHITE + Back.WHITE + '  ' + __RESET
    __ORANGE = Fore.YELLOW + Style.DIM + Back.YELLOW + '  ' + __RESET
    __colors = {'w': __WHITE, 'r': __RED, 'o': __ORANGE, 'y': __YELLOW, 'b': __BLUE, 'g': __GREEN}

    def printout(self, ccolors):
        colors = []
        print('       ╔══════╗')
        side = 0

        ##########   Side 1   ##########
        for i in range(3):
            colors.append(ccolors[side][i])
        self.__printline(colors)
        colors = []

        colors.append(ccolors[side][7])
        colors.append(ccolors[side][8])
        colors.append(ccolors[side][3])
        self.__printline(colors)
        colors = []

        for i in range(6,3,-1):
            colors.append(ccolors[side][i])
        self.__printline(colors)
        colors = []

        ##########   Sides 2-4   ##########
        print('╔══════╬══════╬══════╗')
        side += 1
        for i in range(3):
            colors.append(ccolors[side][i])
        for i in range(3):
            colors.append(ccolors[side+1][i])
        for i in range(3):
            colors.append(ccolors[side+2][i])
        self.__printlargeline(colors)
        colors = []

        colors.append(ccolors[side][7])
        colors.append(ccolors[side][8])
        colors.append(ccolors[side][3])
        colors.append(ccolors[side+1][7])
        colors.append(ccolors[side+1][8])
        colors.append(ccolors[side+1][3])
        colors.append(ccolors[side+2][7])
        colors.append(ccolors[side+2][8])
        colors.append(ccolors[side+2][3])
        self.__printlargeline(colors)
        colors = []

        for i in range(6,3,-1):
            colors.append(ccolors[side][i])
        for i in range(6,3,-1):
            colors.append(ccolors[side+1][i])
        for i in range(6,3,-1):
            colors.append(ccolors[side+2][i])
        self.__printlargeline(colors)
        colors = []

        ##########   Sides 5-6   ##########
        print('╚══════╬══════╬══════╣')
        side = 4

        for i in range(3):
            colors.append(ccolors[side][i])
        for i in range(2,-1,-1):
            colors.append(ccolors[side+1][i])
        self.__printmidline(colors)
        colors = []

        colors.append(ccolors[side][7])
        colors.append(ccolors[side][8])
        colors.append(ccolors[side][3])
        colors.append(ccolors[side+1][3])
        colors.append(ccolors[side+1][8])
        colors.append(ccolors[side+1][7])
        self.__printmidline(colors)
        colors = []

        for i in range(6, 3, -1):
            colors.append(ccolors[side][i])
        for i in range(4, 7):
            colors.append(ccolors[side+1][i])
        self.__printmidline(colors)

        print('       ╚══════╩══════╝')

    def __printline(self, colors):
        print('       ║', end='')
        for color in colors:
            print(self.__colors[color], end='')
        print('║')

    def __printlargeline(self, colors):
        print('║', end='')
        for index, color in enumerate(colors):
            print(self.__colors[color], end='')
            if index == 2 or index == 5:
                print('║', end='')
        print('║')

    def __printmidline(self, colors):
        print('       ║', end='')
        for index, color in enumerate(colors):
            print(self.__colors[color], end='')
            if index == 2:
                print('║', end='')
        print('║')
