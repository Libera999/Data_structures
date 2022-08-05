def subsets(in_set):
    
    allsubsets = []
 
    max_edge = 1<<len(in_set)      ##2^n

    for i in range(0,max_edge):
        subset= binary_to_set(i,in_set)
        allsubsets.append(subset)

    return allsubsets


def binary_to_set(iteration, input_set):

    subset=[]
    i = 0
    index=iteration

    while index>0:
        if (index & 1) == 1:
            subset.append(input_set[i])
        i+=1
        index>>=1

    return subset

set_1=[12,2,3,1]
print(subsets(set_1))

##b1=8
##print(b1&1)
