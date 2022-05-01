liste1 = [2,3,5,1,2,5,8,45,12,3]
def sequentialSearch(liste,value):
    index = 0
    found = False

    while index < len(liste) and not found:
        if liste[index] == value:
            found = True
            print("{}. indexte bulundu!".format(index))
        else:
            index += 1
            if(index == len(liste)):
                print("Bu listede bulunamadi")
sequentialSearch(liste1,4)


