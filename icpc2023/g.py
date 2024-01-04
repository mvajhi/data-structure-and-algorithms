class time:
    def __init__(self,s,e) -> None:
        self.start = s
        self.end = e
        self.count = 0

n, k = map(int,input().split())
lst = [time(0,0)] * n 
for i in range(n):
    st,en = map(int,input().split())
    lst[i] = time(st,en)
for w in range(k):
    for i in range(n):
        lst[i].count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                lst[i].count += 1
            if lst[i].start == lst[j].end or lst[i].end == lst[j].start:
                lst[i].count += 1
            elif (lst[i].start < lst[j].end and lst[i].start > lst[j].start) or (lst[i].end > lst[j].start and lst[i].end < lst[j].end):
                lst[i].count += 1
                
    gggg = max(lst,key=lambda ee:ee.count)
    for i in range(n):
        if lst[i] == gggg:
            lst.pop(i)
            break
    n = n-1

# lst.sort(key= lambda x: x.count)
# n = n-k
lst = lst[0:n]  
for i in range(n):
    lst[i].count = 0
    
for i in range(n):
    for j in range(n):
        if i == j:
            lst[i].count += 1
        if lst[i].start == lst[j].end or lst[i].end == lst[j].start:
            lst[i].count += 1
        elif (lst[i].start < lst[j].end and lst[i].start > lst[j].start) or (lst[i].end > lst[j].start and lst[i].end < lst[j].end):
            lst[i].count += 1
        
ans = [0] * n
for i in range(n):
    ans[i] = lst[i].count
    
res = max(ans)
print(res)
