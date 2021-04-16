

def statechange(tape, state, point):
    if state == "o":
        if tape[point] == "B":
            tape[point] = "B"
            state = "l"
            point += 1

    elif state == "l":
        if tape[point] == "1":
            tape[point] = "C"
            state = "l"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "v"
            point += 1

    elif state == "v":
        if tape[point] == "A":
            tape[point] = "A"
            state = "v"
            point += 1
        elif tape[point] == "1":
            tape[point] = "A"
            state = "x"
            point += 1

    elif state == "x":
        if tape[point] == "B":
            tape[point] = "B"
            state = "y"
            point += 1
        elif tape[point] == "1":
            tape[point] = "D"
            state = "h"
            point += 1

    elif state == "h":
        if tape[point] == "1":
            tape[point] = "D"
            state = "h"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "i"
            point -= 1

    elif state == "i":
        if tape[point] == "1":
            tape[point] = "1"
            state = "i"
            point -= 1
        elif tape[point] == "D":
            tape[point] = "1"
            state = "j"
            point += 1

    elif state == "j":
        if tape[point] == "1":
            tape[point] == "1"
            state = "j"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "a"
            point += 1

    elif state == "a":
        if tape[point] == "1":
            tape[point] = "E"
            state = "a"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "b"
            point -= 1

    elif state == "b":
        if tape[point] == "1":
            tape[point] = "1"
            state = "b"
            point -= 1
        elif tape[point] == "E":
            tape[point] = "1"
            state = "c"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "f"
            point -= 1

    elif state == "c":
        if tape[point] == "1":
            tape[point] = "1"
            state = "c"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "d"
            point += 1

    elif state == "d":
        if tape[point] == "1":
            tape[point] = "1"
            state = "d"
            point += 1
        elif tape[point] == "B":
            # TODO add a 1
            tape[point] = "1"
            tape.append("B")
            state = "e"
            point -= 1

    elif state == "e":
        if tape[point] == "1":
            tape[point] = "1"
            state = "e"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "b"
            point -= 1

    elif state == "f":
        if tape[point] == "1":
            tape[point] = "1"
            state = "f"
            point -= 1
        elif tape[point] == "A":
            tape[point] = "A"
            state = "g"
            point -= 1
        elif tape[point] == "D":
            tape[point] = "1"
            state = "j"
            point += 1

    elif state == "g":
        if tape[point] == "A":
            tape[point] == "A"
            state = "g"
            point -= 1
        elif tape[point] == "B":
            tape[point] == "B"
            state = "k"
            point -= 1

    elif state == "k":
        if tape[point] == "1":
            tape[point] = "1"
            state = "k"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "l"
            point += 1
        elif tape[point] == "C":
            tape[point] = "1"
            state = "m"
            point += 1

    elif state == "m":
        if tape[point] == "1":
            tape[point] = "1"
            state = "m"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "w"
            point += 1

    elif state == "w":
        if tape[point] == "A":
            tape[point] = "A"
            state  = "w"
            point += 1
        elif tape[point] == "1":
            tape[point] = "1"
            state = "n"
            point += 1

    elif state == "n":
        if tape[point] == "1":
            tape[point] = "1"
            state = "n"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "p"
            point += 1

    elif state == "p":
        if tape[point] == "1":
            tape[point] = "1"
            state = "p"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "q"
            point += 1

    elif state == "q":
        if tape[point] == "1":
            tape[point] = "1"
            state = "q"
            point += 1
        elif tape[point] == "B":
            tape[point] = "1"
            tape.append("B")
            state = "r"
            point -= 1

    elif state == "r":
        if tape[point] == "1":
            tape[point] = "1"
            state = "r"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "s"
            point -= 1

    elif state == "s":
        if tape[point] == "1":
            tape[point] = "1"
            state = "s"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "t"
            point -= 1

    elif state == "t":
        if tape[point] == "1":
            tape[point] = "1"
            state = "t"
            point -= 1
        elif tape[point] == "A":
            tape[point] = "A"
            state = "u"
            point -= 1

    elif state == "u":
        if tape[point] == "A":
            tape[point] == "A"
            state = "u"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "k"
            point -= 1

    elif state == "y":
        if tape[point] == "1":
            tape[point] = "B"
            state = "z"
            point += 1

    elif state == "z":
        if tape[point] == "1":
            tape[point] = "B"
            state = "z"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "aa"
            point -= 1

    elif state == "aa":
        if tape[point] == "B":
            tape[point] = "B"
            state = "aa"
            point -= 1
        elif tape[point] == "A":
            tape[point] = "B"
            state = "bb"
            point -= 1

    elif state == "bb":
        if tape[point] == "A":
            tape[point] = "B"
            state = "bb"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "cc"
            point -= 1

    elif state == "cc":
        if tape[point] == "C":
            tape[point] = "1"
            state = "dd"
            point += 1

    elif state == "dd":
        if tape[point] == "B":
            tape[point] = "B"
            state = "dd"
            point += 1
        elif tape[point] == "1":
            tape[point] = "1"
            state = "ee"
            point += 1

    elif state == "ee":
        if tape[point] == "1":
            tape[point] = "1"
            state = "ee"
            point += 1
        elif tape[point] == "B":
            tape[point] = "1"
            tape.append("B")
            state = "ff"
            point -= 1

    elif state == "ff":
        if tape[point] == "1":
            tape[point] = "1"
            state = "ff"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "gg"
            point -= 1

    elif state == "gg":
        if tape[point] == "B":
            tape[point] = "B"
            state = "gg"
            point -= 1
        elif tape[point] == "1":
            tape[point] = "1"
            state = "hh"
            point -= 1

    elif state == "hh":
        if tape[point] == "1":
            tape[point] = "1"
            state = "hh"
            point -= 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "kk"
            point += 1
        elif tape[point] == "C":
            tape[point] = "1"
            state = "ii"
            point += 1

    elif state == "ii":
        if tape[point] == "1":
            tape[point] = "1"
            state = "jj"
            point += 1

    elif state == "jj":
        if tape[point] == "1":
            tape[point] = "1"
            state = "jj"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "dd"
            point += 1

    elif state == "kk":
        if tape[point] == "1":
            tape[point] = "B"
            state = "kk"
            point += 1
        elif tape[point] == "B":
            tape[point] = "B"
            state = "ll"
            point += 1

    elif state == "ll":
        if tape[point] == "B":
            tape[point] = "B"
            state = "ll"
            point += 1
        elif tape[point] == "1":
            tape[point] = "1"
            state = "mm"
            point -= 1

    elif state == "mm":
        if tape[point] == "B":
            tape[point] = "B"
            state = "nn"
            point += 1

    return tape, state, point

