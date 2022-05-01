def seqSearchOrderedList(liste,value):
    index = 0
    found = False
    stop = False

    while index < len(liste) and not found and not stop:
        if liste[index] == value:
            found = True
        else:
            if(value < liste[index]):
                stop = True
            else:
                index += 1
    return (found,index)
liste = [1,2,3,4,5,6,10,15]
found, index = seqSearchOrderedList(liste,12)
print(index)
print(found)