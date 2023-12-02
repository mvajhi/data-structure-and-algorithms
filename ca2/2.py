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
for i in range(0, n):
    y = inp[i]
    pos[y] = i
# print(pos)

prev_stack = list()
prev_pos = dict()
for i in range(n, 0, -1):
    while(True):
        if len(prev_stack) == 0 or prev_stack[-1] < pos[i]:
            break
        prev_stack.pop()
    
    if len(prev_stack) != 0:
        prev_pos[i] = prev_stack[-1]
    else:
        prev_pos[i] = -1
    
    prev_stack.append(pos[i])

# print(prev_pos)
stack = list()
ans = 0
print("0")
for i in range(1, n + 1):
    while(True):
        if prev_pos[i] == -1:
            stack.clear()
            print(len(stack))
            break
        elif len(stack) == 0:
            stack.append(pos[i])
            print(len(stack))
            break
        else:
            if stack[-1] == prev_pos[i]:
                print(len(stack))
                break
            elif stack[-1] < prev_pos[i]:
                stack.append(prev_pos[i])
                print(len(stack))
                break
            elif stack[-1] > prev_pos[i]:
                stack.pop()