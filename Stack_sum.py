def stack_sum(n): ##O(n) time complexity, O(1) space complexity
    sum=0
    for i in range(n):
        sum+= pair(i, i + 1)
    return sum

def pair(a,b):
    return a + b

n = int(input('Input N: '))
print(stack_sum(n))