def printnum(n, i):
    i += 1
    if n == 0:
        print()
        return
    print(i, end = " ")    
    printnum(n - 1, i)
    print(i, end = " ")

i = 0
k = int(input())
printnum(k, i)