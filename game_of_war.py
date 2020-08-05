WIN_A = 1
WIN_B = 2

END_A = 3
END_B = 4
END_OF_CARDS = 5

def play_a_first(hA, hB):
    if not hA and not hB:
        hA = []
        hB = []
        return END_OF_CARDS
    if not hA:
        return END_B
    if not hB:
        return END_A

    a = hA.pop(0)
    b = hB.pop(0)
    if a > b:
        hA.append(a)
        hA.append(b)
        return WIN_A
    if a < b :
        hB.append(a)
        hB.append(b)
        return WIN_B
    if a==b:
        if not hA:
            return END_B
        if not hB:
            return END_A

        h1 = hA.pop(0)
        h2 = hB.pop(0)
        res = play_a_first(hA, hB)
        if res == WIN_A:
            hA.append(h1)
            hA.append(h2)
            hA.append(a)
            hA.append(b)
            pass
        else:
            hB.append(h1)
            hB.append(h2)
            hB.append(a)
            hB.append(b)
            pass
        return res


def play_b_first(hA, hB):
    if not hA and not hB:
        hA = []
        hB = []
        return END_OF_CARDS
    if not hA:
        return END_B
    if not hB:
        return END_A

    a = hA.pop(0)
    b = hB.pop(0)
    if a > b:
        hA.append(b)
        hA.append(a)
        return WIN_A
    if a < b :
        hB.append(b)
        hB.append(a)
        return WIN_B
    if a==b:
        if not hA:
            return END_B
        if not hB:
            return END_A

        h1 = hA.pop(0)
        h2 = hB.pop(0)
        res = play_b_first(hA, hB)
        if res == WIN_A:
            hA.append(h2)
            hA.append(h1)
            hA.append(b)
            hA.append(a)
            pass
        else:
            hB.append(h2)
            hB.append(h1)
            hB.append(b)
            hB.append(a)
            pass
        return res

def play_winner_first(hA, hB):
    if not hA and not hB:
        hA = []
        hB = []
        return END_OF_CARDS
    if not hA:
        return END_B
    if not hB:
        return END_A

    a = hA.pop(0)
    b = hB.pop(0)
    if a > b:
        hA.append(a)
        hA.append(b)
        return WIN_A
    if a < b :
        hB.append(b)
        hB.append(a)
        return WIN_B
    if a==b:
        if not hA:
            return END_B
        if not hB:
            return END_A

        h1 = hA.pop(0)
        h2 = hB.pop(0)
        res = play_b_first(hA, hB)
        if res == WIN_A:
            hA.append(h1)
            hA.append(h2)
            hA.append(a)
            hA.append(b)
            pass
        else:
            hB.append(h2)
            hB.append(h1)
            hB.append(b)
            hB.append(a)
            pass
        return res
