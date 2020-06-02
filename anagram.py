def anagram(string):
    if string == '':
        return [string]
    else:
        result = []
        for i in anagram(string[1:]):
            for j in range(len(i) + 1):
                result.append(i[:j] + string[0] + i[j:])
        return result

print(len(anagram("abcd")))
