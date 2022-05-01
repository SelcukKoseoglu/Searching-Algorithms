import math
def jumpSearch(liste,value):
    n = len(liste)
    step = math.sqrt(n)
    prev = 0

    while liste[int(min(step,n)-1)] <= value:
        prev = step
        step += math.sqrt(n)

        if prev >= n:
            return -1
    while liste[int(prev)] < value:
        prev += 1

        if prev == min(step,n):
            return -1

    if liste[int(prev)] == value:
        return int(prev)

    return -1
liste = [1,2,5,8,9,12,14,78,96,105]

print(jumpSearch(liste,78))