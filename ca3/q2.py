class Bst:
    class Node:
        def __init__(self, value, parent, num) -> None:
            self.value = value
            self.parent = parent
            self.num = num
            self.L = None
            self.R = None
            if parent is None:
                self.way = [(value, num)]
            else:
                self.way = [(value, num)] + parent.way

    def __init__(self):
        self.counter = 0
        self.root = None

    def insert(self, key, n = None, p = None, side = '', first = True):
        if self.root == None:
            self.counter += 1
            self.root = self.Node(key, None, self.counter)
            return self.root.way
        if first == True:
            n = self.root
            
        if n == None:
            if side == 'L':
                self.counter += 1
                p.L = self.Node(key, p, self.counter)
                return p.L.way
            if side == 'R':
                self.counter += 1
                p.R = self.Node(key, p, self.counter)
                return p.R.way
        elif key < n.value:
            return self.insert(key, n.L, n, 'L', False)
        else:
            return self.insert(key, n.R, n, 'R', False)
        

def main():
    tree = Bst()
    inp = get_input()
    ways = list()
    for i in inp["bst"]:
        ways.append(tree.insert(i))
    fathers = list()
    for i in range(1, len(ways)):
        out = ways[i]
        fathers.append(out)
        if i != len(ways) - 1:
            print(out[1][0], end=' ')
        else:
            print(out[1][0])
            
    a = ways[inp["query"][0] - 1]
    b = ways[inp["query"][1] - 1]
    intersection_list = list(set(a).intersection(b))
    intersection_list.sort(key=lambda key : key[1])
    print(intersection_list[-1][1])
            
    
def get_input():
    output = dict()
    
    input()
    output["bst"] = [int(i) for i in input().split()]
    output["query"] = [int(i) for i in input().split()]
    
    return output
    
if __name__ == "__main__":
    main()
