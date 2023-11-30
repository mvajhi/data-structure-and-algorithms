class Stack:
    def __init__(self, size=10):
        self.stack = [0 for i in range(size)]
        self.top = -1

    def isEmpty(self):
        return self.top < 0

    def push(self, value):
        self.top += 1
        self.stack.append(value)

    def pop(self):
        self.top -= 1
        return self.stack.pop()

n = int(input())
pos = dict()
inp = [int(i) for i in input().split(" ")]
for i in range(1, n + 1):
    y = inp[i - 1]
    pos[y] = i

prev_stack = Stack()
prev_pos = dict()
for i in range(n, 0, -1):
    while(not prev_stack.isEmpty() or prev_stack.top > i):
        prev_stack.pop()
    
    if not prev_stack.isEmpty():
        prev_pos[pos[i]] = prev_stack.top
    
    prev_stack.push(pos[i])

stack = Stack()
ans = 0
for i in range(1, n + 1):
    if pos[i] in prev_pos.keys():
        if stack.isEmpty() or prev_pos[pos[i]] != prev_pos[stack.top]:
            ans += 1
    stack.push(pos[i])

print(ans)
    