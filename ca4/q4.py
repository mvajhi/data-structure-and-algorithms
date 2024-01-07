from heapq import heapify, heappush, heappop

def main():
    inp = get_input()
    out = solve(inp)
    print(out)

def solve(inp):
    return bfs([(0, (0,0))], inp)

def bfs(queue, inp):
    end_have_light = inp['final'] in inp['e']
    while len(queue) != 0:
        cost, pos = heappop(queue)
        neighbor = get_neighbor(pos, inp['e'])
        inp['e'] = remove_neighbor(inp['e'], neighbor)
        neighbor_with_cost = calculate_cost(cost, pos, neighbor)
        push_all(neighbor_with_cost, queue)
        
        flag, out = check_state(cost, pos, inp['final'],
                                end_have_light)
        if flag:
            return out

    return -1

def check_state(cost, pos, end, end_have_light):
    if end_have_light:
        if pos == end:
            return True, cost
    else:
        if is_neighbor(pos, end):
            return True, cost + 1
            
    return False, None

def is_neighbor(p1, p2):
    for i in [0,1]:
        if abs(p1[i] - p2[i]) <= 1:
            return True
    return False

def push_all(l, heap):
    for i in l:
        heappush(heap, i)

def calculate_cost(pre_cost, pos, neighbor):
    output = list()
    for n in neighbor:
        cost = pre_cost
        if not is_adjacent(pos, n):
            cost += 1
        output.append((cost, n))
    return output

def is_adjacent(pos, n):
    out = False
    for i in [0,1]:
        if abs(pos[i] - n[i]) == 1:
            out = not out
    return out

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