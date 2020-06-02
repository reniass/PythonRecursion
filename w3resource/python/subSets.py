def subSets(L):

    if len(L) == 0:
        return [[]]
    else:
        result = []
        first_element = L[0]
        result = result + subSets(L[1:])
        for el in subSets(L[1:]):
            result = result + ([[first_element] + el])
        return result

print(subSets([1,2,3]))
