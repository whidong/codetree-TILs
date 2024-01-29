def printhi(n):
    if n == 0:
        return
    n = n-1
    print("HelloWorld")
    printhi(n)

k = int(input())
printhi(k)