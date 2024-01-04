n = int(input())
def get_pos(xxx,yyy,x,y):
    sum = 0
    if x == 0:
        sum = y
    elif y == yyy:
        sum = yyy + x
    elif x == xxx:
        sum = yyy + xxx + yyy - y
    elif y == 0:
        sum = 2*(xxx + yyy) - x 
    return sum

def get_next(xxx,yyy,x,y,t):
    temp1 = get_pos(xxx,yyy,x,y) + t 
    temp2 = 2*(xxx+yyy)
    next = temp1 % temp2
    return next
        
time = [0] * 4
pos = [0] * 4
mins = [0] * 4
ans = [0] * n
for j in range(n):
    xx,yy,tx,ty,wx,wy = map(int,input().split())
    time[0] =  wx
    pos[0] = wy 
    
    time[1] = yy - wy
    pos[1] = yy + wx
    
    time[2] = xx - wx
    pos[2] = 2*yy + xx -wy 
    
    time[3] = wy
    pos[3] = 2*(xx + yy) - wx
    for i in range(4):
        next_pos = get_next(xx,yy,tx,ty,time[i])
        if next_pos <=  pos[i]:
            mins[i] = time[i]  + pos[i] - next_pos
        else:
            mins[i] = time[i]  + pos[i] +(2*(xx+yy) - next_pos)
    ans[j] = min(mins)
for x in ans:
    print(x) 