from heapq import heapify, heappush, heappop
class Node:
    def __init__(self, pos) -> None:
        self.cost = -1
        self.pos = pos
        self.seen = False
        self.light = False

def main():
    inp = get_input()
    print(inp)
    out = solve(inp)
    print(out)

def solve(inp):
    nodes = create_nodes(inp)
    return bfs(nodes, [(0, (0,0))], inp)

def bfs(nodes, queue, inp):
    while len(queue) != 0:
        cost, pos = heappop(queue)
        neighbor = get_neighbor(pos, inp['e'])
        inp['e'] = remove_neighbor(inp['e'], neighbor)
        neighbor_with_cost = calculate_cost(cost, pos, neighbor)
        
    return -1

def calculate_cost(pre_cost, pos, neighbor):
    output = list()
    for n in neighbor:
        if calculate_distance(pos, n) == 1:
            pass

def remove_neighbor(edge, neighbor):
    return list(filter(lambda x: x not in neighbor, edge))
    
def create_nodes(inp):
    nodes = dict()
    for i in range(inp['n']):
        for j in range(inp['m']):
            nodes[(i, j)] = Node((i,j))
    nodes[inp['initial']].cost = 0
    
    for i in inp['e']:
        nodes[i].light = True
    
    return nodes

def get_neighbor(pos, edge):
    neighbor = list()
    for i in [0,1]:
        for j in [-2,-1,0,1,2]:
            neighbor.extend(list(filter(
                lambda p: p[i] == j + pos[i], edge)))

    return list(set(neighbor))

def is_ok_pos (size, new_pos, pos) -> bool:
    for i in range(2):
        if not (0 <= new_pos[i] and new_pos[i] < size[i]):
            return False
    if new_pos == pos:
        return False
    
    return True

def get_input():
    n, m, k = map(int, input().split())
    edge = list()
    for _ in range(k):
        edge.append(tuple(map(lambda p: int(p) - 1, input().split())))
    
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