n = int(input())
ddate = None
dk, dt, dp = None, None, None
for i in range(n):
    k, t, p = map(str, input().split())
    if p =="Rain":
        date = list(map(int, k.split("-")))
        if ddate != None:
            for i in range(3):
                if ddate[i] > date[i]:
                    ddate = date
                    dk, dt, dp = k, t, p
                    break
                elif ddate[i] == date[i]:
                    pass
                else:
                    break
        else:
            ddate = date
            dk, dt, dp = k, t, p
print(dk, dt, dp)