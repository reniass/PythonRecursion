
# function printing print in one row numbers from one to n
def printing(n):
    if n == 1:
        s =  str(n) + " "
        print(s, end="")
    else:
        printing(n-1)
        s = str(n) + " "
        print(s, end="")


printing(89)