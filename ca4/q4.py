from collections import deque

def main():
    inp = get_input()
    out = solve(inp)
    print(out)

def solve(inp):
    return bfs((0, (0,0)), inp)

def bfs(start, inp):
    queue = deque()
    queue.append(start)
    inp['e'].append(start[1])
    
    end_have_light = inp['final'] in inp['e']
    while len(queue) != 0:
        cost, pos = queue.popleft()
        inp['e'].remove(pos)
        neighbor_with_cost = get_neighbor_with_cost(cost, pos, inp)
        push_all(cost, neighbor_with_cost, queue)
        
        flag, out = check_state(cost, pos, inp['final'],
                                end_have_light)
        if flag:
            return out

    return -1

def get_neighbor_with_cost(cost, pos, inp):
    close_neighbor = get_close_neighbor(pos, inp)
    neighbor_with_cost = [(cost,i) for i in close_neighbor]
    far_neighbor = get_far_neighbor(close_neighbor + [pos], inp)
    neighbor_with_cost += [(cost + 1,i) for i in far_neighbor]
    return neighbor_with_cost
    
def get_far_neighbor(queue, inp):
    far_neighbor = list()
    while True:
        state = queue.pop()
        new_neighbor = get_far(state, inp)
        # inp['e'] = remove_neighbor(inp['e'], new_neighbor)
        far_neighbor.extend(new_neighbor)
        if len(queue) == 0:
            break
    return far_neighbor

def get_far(pos, inp):
    out = list()
    for p in inp['e']:
        if is_neighbor2(pos, p):
            out.append(p)
    return out

def get_close_neighbor(pos, inp):
    queue = [pos]
    close_neighbor = list()
    while True:
        state = queue.pop()
        new_neighbor = get_close(state, inp)
        # inp['e'] = remove_neighbor(inp['e'], new_neighbor)
        close_neighbor.extend(new_neighbor)
        queue.extend(new_neighbor)
        if len(queue) == 0:
            break
    
    return close_neighbor

def get_close(pos, inp):
    out = list()
    for p in inp['e']:
        if is_adjacent(pos, p):
            out.append(p)
    return out

def is_neighbor2(p1, p2):
    for i in [0,1]:
        if abs(p1[i] - p2[i]) <= 2:
            return True
    return False
    

def check_state(cost, pos, end, end_have_light):
    if end_have_light:
        if pos == end:
            return True, cost
    else:
        if is_neighbor(pos, end):
            return True, cost + 1
            
    return False, None

# bug??
def is_neighbor(p1, p2):
    for i in [0,1]:
        if abs(p1[i] - p2[i]) <= 1:
            return True
    return False

def push_all(cost, l, queue: deque):
    for i in l:
        if cost == i[0]:
            queue.appendleft(i)
        else:
            queue.append(i)

def calculate_cost(pre_cost, pos, neighbor):
    output = list()
    for n in neighbor:
        cost = pre_cost
        if not is_adjacent(pos, n):
            cost += 1
        output.append((cost, n))
    return output

def is_adjacent(pos, n):
    count = 0
    for i in [0,1]:
        if abs(pos[i] - n[i]) == 1:
            count += 1
    if count == 2:
        return True
    return False

def remove_neighbor(edge, neighbor):
    return list(filter(lambda x: x not in neighbor, edge))
    
def get_neighbor(pos, edge):
    neighbor = list()
    for i in [0,1]:
        for j in [-2,-1,0,1,2]:
            neighbor.extend(list(filter(
                lambda p: p[i] == j + pos[i], edge)))

    return list(set(neighbor))

def get_input():
    n, m, k = map(int, input().split())
    edge = list()
    for _ in range(k):
        edge.append(tuple(map(
            lambda p: int(p) - 1, input().split())))
    edge.remove((0,0))
    return {
        'n':n,
        'm':m,
        'k':k,
        'e':edge,
        'initial':(0,0),
        'final':(n-1, m-1)
    }

if __name__ == "__main__":
    main()