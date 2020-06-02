

def string_permutation(word):
    if len(word) == 1:
        return word
    else:
        for i in len(word):


        first_letter = word[0]

        string_permutation(word[1:])