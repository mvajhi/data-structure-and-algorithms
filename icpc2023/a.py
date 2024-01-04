d, n = input().split()
n = int(n)

tmp = 0
for i in d:
    tmp += int(i)
d = tmp

def foo (res, n, i):
    if i > n:
        return res
    tmp = 0
    for j in str(i):
        tmp += int(j)
    out = res * 2 + tmp
    return foo(out, n, i + 1)

if n == 1:
    print(d)
else:
    out = foo(d, n, 2)
    print(out)