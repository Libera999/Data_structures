def sublist(input_list):

    if input_list == []:
        return [[]]             ##add empty list
    else:
        s = sublist(input_list[1:])
        p= s + [[input_list[0]] + b for b in s]
        #print(s)
    return p

l=[12,2,3]

print("result: ",sublist(l))