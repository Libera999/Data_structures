def binary_search(list,item,begin,end):

        if begin > end:
            return False

        mid = (begin + end) // 2

        if item == list[mid]:
            return mid

        elif item > list[mid]:
            return binary_search(list, item, mid + 1, end)

        else:
            return binary_search(list, item, begin, mid - 1)


array=[3,12,21,87,130,211,1022]
result=binary_search(array,212,0,len(array)-1)

if result==False:
    print("Not found")
else:
    print("Position of the item:",result)