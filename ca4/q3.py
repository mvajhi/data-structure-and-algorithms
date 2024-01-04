class Tree:
    class Node:
        def __init__(self, value, parent):
            self.value = value
            self.parent = parent
            self.child = list()
            if parent is None:
                self.way = [value]
            else:
                self.way = [value] + parent.way

    def __init__(self):
        self.root = None
        self.hash = dict()

    def insert(self, key, p = None):
        if p is None:
            new_node = self.Node(key, None)
            self.root = new_node
            self.hash[key] = new_node
            return
        new_node = self.Node(key, self.hash[p])
        self.hash[p].child.append(new_node)
        self.hash[key] = new_node

def main():
    e, query, n = get_input()
    # print(-1)
    tree = create_tree(e)
    out = solve(tree, query, n)
    if out == -1:
        print(-1)
    else:
        print(*out)

def solve(tree, query, n):
    way = list()
    for i in range(len(query) - 1):
        small_query = [query[i], query[i+1]]
        small_way = find_way(tree, small_query)
        if i == 0:
            way = small_way
        else:
            way += small_way[1:]
        if len(way) > 2 * n - 1:
            return -1
    way.pop()
    return way

def find_way(tree, query):
    joint_father = find_joint_father([tree.hash[query[0]].way,
                                     tree.hash[query[1]].way])
    way = list()
    for i in query:
        way.append(get_way_to_father(joint_father, tree.hash[i].way))

    full_way = get_full_way(way[0], way[1], joint_father)
    # print(full_way)
    return full_way

def get_full_way(initial, final, father):
    return initial + [father] + list(reversed(final))

def get_way_to_father(father, child_way):
    '''output without father'''
    for i in range(len(child_way)):
        if father == child_way[i]:
            return child_way[:i]

def find_joint_father(way):
        for i in range(1, min(len(way[0]), len(way[1])) + 1):
            
            if way[0][-i] != way[1][-i]:
                return way[0][-i + 1]
        if len(way[0]) > len(way[1]):
            return way[1][0]
        else:
            return way[0][0]

def create_tree(e):
    tree = Tree()
    for i in e:
        if tree.root == None:
            tree.insert(i[0])
        tree.insert(i[1], i[0])
    return tree

def get_input():
    n = int(input())
    e = list()
    for _ in range(n - 1):
        e.append(list(map(int, input().split())))
    query = list(map(int, input().split()))
    query = [1] + query + [1]
    return e, query, n
    
if __name__ == "__main__":
    main()