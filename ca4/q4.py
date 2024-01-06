class Node:
    def __init__(self, pos) -> None:
        self.h = -1
        self.pos = pos
        self.seen = False
        self.light = [0, -1]

def main():
    inp = get_input()
    print(inp)
    out = solve(inp)
    print(out)

def solve(inp):
    nodes = create_nodes(inp)

    return recursion_solve([inp['n'], inp['m']], [nodes[inp['initial']]],
                           inp['final'], inp['e'], nodes)

def create_nodes(inp):
    nodes = dict()
    for i in range(inp['n']):
        for j in range(inp['m']):
            nodes[(i, j)] = Node((i,j))
    nodes[inp['initial']].h = 0
    return nodes

def recursion_solve(size, queue, final_pos, light_edges, nodes):
    if len(queue) == 0:
        return -1
    node = queue.pop(0)
    if node.pos == final_pos:
        return node.h
    
    neighbor_pos = get_neighbor_pos(size, node.pos)

    for p in neighbor_pos:
        if nodes[p].seen:
            continue
        
        nodes[p].h = node.h
        if p in light_edges :
            light_edges.pop()
        elif is_light_ok(p, node.light):
            pass
        else:
            nodes[p].h += 1

        nodes[p].seen = True
        queue.append(nodes[p])
    
    return recursion_solve(size, queue, final_pos,
                           light_edges, nodes)

def get_neighbor_pos(size, pos):
    output = list()
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            new_pos = (pos[0]+i, pos[1]+j)
            if is_ok_pos(size, new_pos, pos):
                output.append(new_pos)
    return output

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