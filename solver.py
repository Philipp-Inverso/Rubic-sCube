def solveWhite(cube):
    correct = []
    args = ""
    for index, color in enumerate(cube[0]):
        if index % 2 != 0 and color == 'w':
            if index == 1 and cube[5][1] == 'b':
                correct.append(['w', 'b'])
            if index == 3 and cube[3][1] == 'o':
                correct.append(['w', 'o'])
            if index == 5 and cube[2][1] == 'g':
                correct.append(['w', 'g'])
            if index == 7 and cube[1][1] == 'r':
                correct.append(['w', 'r'])

    if all([['w', 'r'], ['w', 'g'], ['w', 'o'], ['w', 'b']]) in correct:
        pass
    elif all([['w', 'g'], ['w', 'o'], ['w', 'b']]) in correct:
        for index, color in enumerate(cube[1]):
            if index % 2 != 0 and color == 'w':
                if index == 1:
                    args += "l' u b' u'"
                    break
                elif index == 3:
                    args += "u' f u"
                    break
                elif index == 5:
                    args += "l' u' f u"
                    break
                elif index == 7:
                    args += "u b' u'"
                    break
        else:
            for index, color in enumerate(cube[2]):
                if index % 2 != 0 and color == 'w':
                    if index == 3:
                        args += "l f f l' f f"
                        break
                    elif index == 5:
                        args += "d' u' l' f u"
                        break
                    elif index == 7:
                        args += "u b' u'"
                        break
            else:
                for index, color in enumerate(cube[3]):
                    if index % 2 != 0 and color == 'w':
                        if index == 3:
                            args += "u b u'"
                            break
                        elif index == 5:
                            args += "u' l f' l' u"
                            break
                        elif index == 7:
                            args += "u f' u'"
                            break
                else:
                    for index, color in enumerate(cube[4]):
                        if index % 2 != 0 and color == 'w':
                            if index == 1:
                                args += "u' f f u"
                                break
                            elif index == 3:
                                args += "d d r r"
                                break
                            elif index == 5:
                                args += "d r r"
                                break
                            elif index == 7:
                                args += "r r"
                                break
                    else:
                        for index, color in enumerate(cube[5]):
                            if index % 2 != 0 and color == 'w':
                                if index == 3:
                                    args += "r"
                                    break
                                elif index == 5:
                                    args += "b' r b"
                                    break
                                elif index == 7:
                                    args += "u u l' u u"
                                    break
    elif all([['w', 'r'], ['w', 'o'], ['w', 'b']]) in correct:
        for index, color in enumerate(cube[1]):
            if index % 2 != 0 and color == 'w':
                if index == 3:
                    args += "f "
                    break
                elif index == 5:
                    args += "u' r' u f"
                    break
                elif index == 7:
                    args += "u u b' u u"
                    break
        else:
            for index, color in enumerate(cube[2]):
                if index % 2 != 0 and color == 'w':
                    if index == 1:
                        args += "f u l u'"
                        break
                    elif index == 3:
                        args += "u l u'"
                        break
                    elif index == 5:
                        args += "f' u l u'"
                        break
                    elif index == 7:
                        args += "u' r' u"
                        break
            else:
                for index, color in enumerate(cube[3]):
                    if index % 2 != 0 and color == 'w':
                        if index == 3:
                            args += "u u b u u"
                            break
                        elif index == 5:
                            args += "l f' l'"
                            break
                        elif index == 7:
                            args += "f'"
                            break
                else:
                    for index, color in enumerate(cube[4]):
                        if index % 2 != 0 and color == 'w':
                            if index == 1:
                                args += "f f"
                                break
                            elif index == 3:
                                args += "d' f f"
                                break
                            elif index == 5:
                                args += "d d f f"
                                break
                            elif index == 7:
                                args += "d f f"
                                break
                    else:
                        for index, color in enumerate(cube[5]):
                            if index % 2 != 0 and color == 'w':
                                if index == 3:
                                    args += "u r u'"
                                    break
                                elif index == 5:
                                    args += "b' u r u' b"
                                    break
                                elif index == 7:
                                    args += "u' l' u"
                                    break
    elif all([['w', 'r'], ['w', 'g'], ['w', 'b']]) in correct:
        for index, color in enumerate(cube[1]):
            if index % 2 != 0 and color == 'w':
                if index == 3:
                    args += "u f u'"
                    break
                elif index == 5:
                    args += "u u  r' u' f u'"
                    break
                elif index == 7:
                    args += "u' b' u"
                    break
        else:
            for index, color in enumerate(cube[2]):
                if index % 2 != 0 and color == 'w':
                    if index == 3:
                        args += "l"
                        break
                    elif index == 5:
                        args += "f' l f"
                        break
                    elif index == 7:
                        args += "f f l f f"
                        break
            else:
                for index, color in enumerate(cube[3]):
                    if index % 2 != 0 and color == 'w':
                        if index == 1:
                            args += "l u' b' u"
                            break
                        elif index == 3:
                            args += "u' b' u"
                            break
                        elif index == 5:
                            args += "l u f' u'"
                            break
                        elif index == 7:
                            args += "u f' u'"
                            break
                else:
                    for index, color in enumerate(cube[4]):
                        if index % 2 != 0 and color == 'w':
                            if index == 1:
                                args += "d l l"
                                break
                            elif index == 3:
                                args += "l l"
                                break
                            elif index == 5:
                                args += "d' l l"
                                break
                            elif index == 7:
                                args += "d d l l"
                                break
                    else:
                        for index, color in enumerate(cube[5]):
                            if index % 2 != 0 and color == 'w':
                                if index == 3:
                                    args += "u' b' u"
                                    break
                                elif index == 5:
                                    args += "b' u' b' u"
                                    break
                                elif index == 7:
                                    args += "u' b' u"
                                    break
    elif all([['w', 'r'], ['w', 'g'], ['w', 'o']]) in correct:
        for index, color in enumerate(cube[1]):
            if index % 2 != 0 and color == 'w':
                if index == 3:
                    args += "u u f u u"
                    break
                elif index == 5:
                    args += "u' r' u' f u u"
                    break
                elif index == 7:
                    args += "b'"
                    break
        else:
            for index, color in enumerate(cube[2]):
                if index % 2 != 0 and color == 'w':
                    if index == 3:
                        args += "u l u'"
                        break
                    elif index == 5:
                        args += "f' u l u' f"
                        break
                    elif index == 7:
                        args += "u r' u'"
                        break
            else:
                for index, color in enumerate(cube[3]):
                    if index % 2 != 0 and color == 'w':
                        if index == 3:
                            args += "b"
                            break
                        elif index == 5:
                            args += "l' b l"
                            break
                        elif index == 7:
                            args += "u' l u"
                            break
                else:
                    for index, color in enumerate(cube[4]):
                        if index % 2 != 0 and color == 'w':
                            if index == 1:
                                args += "d d b b"
                                break
                            elif index == 3:
                                args += "d b b"
                                break
                            elif index == 5:
                                args += "b b"
                                break
                            elif index == 7:
                                args += "d' b b"
                                break
                    else:
                        for index, color in enumerate(cube[5]):
                            if index % 2 != 0 and color == 'w':
                                if index == 1:
                                    args += "b' u l' u'"
                                elif index == 3:
                                    args += "u' r u"
                                    break
                                elif index == 5:
                                    args += "b' u' r u"
                                    break
                                elif index == 7:
                                    args += "u l' u'"
                                    break
    elif all([['w', 'g'], ['w', 'o']]) in correct:
        pass
    elif all([['w', 'r'], ['w', 'o']]) in correct:
        pass
    elif all([['w', 'r'], ['w', 'g']]) in correct:
        pass
    return args
