class per:
    def __init__(self,a,time) -> None:
        self.a = a
        self.time = time

n = int(input())
sum = 0
maxx = 0
lst = [per(0,0)] * n
for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    lst[i] = per(x,y)

pre = 0
lst.sort(key =lambda g: g.time)
for z in lst:
    if z.time != pre:
        maxx = max(maxx,sum)
    sum += z.a
    pre = z.time
print(maxx)  