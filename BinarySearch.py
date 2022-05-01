def binarySearch(liste,value):
    first_index = 0
    last_index = len(liste) - 1
    found = False

    while first_index <= last_index and not found:
        middle_index = int((first_index + last_index)/2)
        if(liste[middle_index] == value):
            found = True
        else:
            if(value < liste[middle_index]):
                last_index = middle_index - 1
                print("lower")
            else:
                first_index = middle_index + 1
                print("upper")
    return found
liste = [1,2,4,5,9,15,19,38,77]
state = binarySearch(liste,38)
print(state)

