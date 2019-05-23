import model
import view
import random
import time
import solver


def randomize():
    r = random.randint(0, 11)
    if r == 0:
        return 'r'
    elif r == 1:
        return 'l'
    elif r == 2:
        return 'u'
    elif r == 3:
        return 'd'
    elif r == 4:
        return 'b'
    elif r == 5:
        return 'f'
    elif r == 6:
        return 'r'
    elif r == 7:
        return 'l'
    elif r == 8:
        return 'u'
    elif r == 9:
        return 'd'
    elif r == 10:
        return 'b'
    elif r == 11:
        return 'f'


def controller(cube, do):
    if do == "l":
        cube.turnleft()
    elif do == "r":
        cube.turnright()
    elif do == "u":
        cube.turnup()
    elif do == "d":
        cube.turndown()
    elif do == "f":
        cube.turnfront()
    elif do == "b":
        cube.turnback()
    elif do == "l'":
        cube.turnleft()
        cube.turnleft()
        cube.turnleft()
    elif do == "r'":
        cube.turnright()
        cube.turnright()
        cube.turnright()
    elif do == "u'":
        cube.turnup()
        cube.turnup()
        cube.turnup()
    elif do == "d'":
        cube.turndown()
        cube.turndown()
        cube.turndown()
    elif do == "f'":
        cube.turnfront()
        cube.turnfront()
        cube.turnfront()
    elif do == "b'":
        cube.turnback()
        cube.turnback()
        cube.turnback()
    elif do == "x":
        cube.__init__()
    out.printout(cube.colors)


if __name__=="__main__":
    cube = model.Cube()
    out = view.Printer()
    out.printout(cube.colors)
    while True:
        do = input("What to do?\n")
        if do == "e":
            break
        elif do == 'rand':
            for i in range(10):
                controller(cube, randomize())
                time.sleep(0.125)
        elif do == 'solve':
            do = solver.solveWhite(cube.colors)
            print(do)
            for item in do.split(' '):
                controller(cube, item)
                time.sleep(1 / 3)
        elif do == "c":
            cube.iscorrect()
            continue
        elif len(do) > 2:
            for item in do.split(' '):
                controller(cube, item)
                time.sleep(1/3)
        else:
            controller(cube, do)
