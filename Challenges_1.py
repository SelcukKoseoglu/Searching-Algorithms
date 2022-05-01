def rec_binary_search(arr,ele):

    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr)/2)
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid],ele)
            else:
                return rec_binary_search(arr[mid + 1:],ele)
liste = [1,2,3,4,5,6,7,8,10,15,17]
print(rec_binary_search(liste,16))