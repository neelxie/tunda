def selection_sort(mylist):

    for i in range(len(mylist)):
        min = i  # consider it mininmum
        for k in range(i+1, len(mylist)):
            if mylist[min] > mylist[k]:
                min = k

        temp = mylist[i]  # swapping
        mylist[i] = mylist[min]
        mylist[min] = temp
    return mylist


def bubble_Sort(mylist):

    for i in range(len(mylist)-1, 0, -1):
        for k in range(i):
            if mylist[k] > mylist[k+1]:  # compare with next neighbor
                temp = mylist[k]  # begin swap
                mylist[k] = mylist[k+1]
                mylist[k+1] = temp
    return mylist


def merge_sort(mylist):

    if len(mylist) > 1:
        mid = len(mylist)//2
        lhalf = mylist[:mid]
        rhalf = mylist[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)
        i, j, k = 0, 0, 0
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                mylist[k] = lhalf[i]
                i = i+1
            else:
                mylist[k] = rhalf[j]
                j = j+1
            k = k+1

        while i < len(lhalf):
            mylist[k] = lhalf[i]
            i = i+1
            k = k+1

        while j < len(rhalf):
            mylist[k] = rhalf[j]
            j = j+1
            k = k+1
    return mylist


if __name__ == '__main__':
    mylis = [88, 3, 48, 57, 26, 56, 5, 67, 49, 96, 75, 6, 90, 400, 9]
    myli = [88, 3, 48, 57, 26, 56, 5, 67, 49, 96, 75, 6, 90, 400, 9]
    myl = [88, 3, 48, 57, 26, 56, 5, 67, 49, 96, 75, 6, 90, 400, 9]
    print(mylis)
    print("Bubble sort\n")
    print(bubble_Sort(mylis))
    print('selection sort\n')
    print(selection_sort(myli))
    print('merge sort\n')
    print(merge_sort(myl))
