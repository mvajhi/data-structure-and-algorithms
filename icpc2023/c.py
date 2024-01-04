m, n = map(int, input().split())
mat = list()
for i in range(m):
    mat.append(list(map(int, input().split())))
    
mat_t = []
for i in range(n):
    tmp = set()
    for j in range(m):
        tmp.add(mat[j][i])
    mat_t.append(tmp)

mat = [set(i) for i in mat]

output_2 = []
while(True):
    output = []
    end = True
    for i in range(len(mat)):
        if len(mat[i]) == 1:
            color, = mat[i]
            flag = 0
            for j in mat:
                if color in j:
                    flag += 1
            if flag == 1:
                end = False
                color = mat[i].pop()
                output.append(color)
                for j in range(len(mat_t)):
                    if color in mat_t[j]:
                        mat_t[j].remove(color)
                    
    output.sort(reverse=True)
    for i in output:
        output_2.append(i)
        
    output = []
    for i in range(len(mat_t)):
        if len(mat_t[i]) == 1:
            color, = mat_t[i]
            flag = 0
            for j in mat_t:
                if color in j:
                    flag += 1
            if flag == 1:
                end = False
                color = mat_t[i].pop()
                output.append(color)
                for j in range(len(mat)):
                    if color in mat[j]:
                        mat[j].remove(color)
    
    output.sort(reverse=True)
    for i in output:
        output_2.append(i)
    
    
    if end:
        break
output_2.reverse()
print(*output_2)
