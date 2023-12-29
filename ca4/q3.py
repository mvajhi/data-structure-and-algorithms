class Tree:
    class Node:
        def __init__(self, value, parent) -> None:
            self.value = value
            self.parent = parent
            self.child = list()
            if parent is None:
                self.way = None
            else:
                self.way = [parent.value] + parent.way

    def __init__(self):
        self.root = None
        self.hash = dict()

    def insert(self, key, p = None):
        if p is None:
            new_node = self.Node(key, None)
            self.root = new_node
            self.hash[key] = new_node
        new_node = self.Node(key, self.hash[p])
        self.hash[p].child.append(new_node)

def main():
    e, query = get_input()
    tree = create_tree(e)
    print(solve(tree, query))

def solve(tree, query):
    intersection_list = list(set(a).intersection(b))
    intersection_list.sort(key=lambda key : key[1])
    print(intersection_list[-1][1])

def create_tree(e):
    tree = Tree()
    for i in e:
        if tree.root == None:
            tree.insert(i[0])
        tree.insert(i[0], i[1])
    return tree

def get_input():
    n = int(input())
    e = list()
    for _ in range(n - 1):
        e.append(list(map(int, input().split())))
    query = list(int, input().split())
    return e, query
    