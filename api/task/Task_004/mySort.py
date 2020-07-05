def mySort(List):
    newList=[]
    for i in range(len(List)):
        newList.append(min(List))
        List.remove(min(List))
    return newList
print(mySort([1,0,2,5,7]))
