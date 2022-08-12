# determine if a string has all unique characters
def uniqcharacters(string):

    list = [*string]
    uni = []

    for i in list:
        if i in uni:
            return False
        else:
            uni.append(i)

    return True


s = input("Type the string ")
print("Does string has all unique characters: ", uniqcharacters(s))
