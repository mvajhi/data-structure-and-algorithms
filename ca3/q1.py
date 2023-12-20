import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    def __init__(self):
        self.heap = list()
        self.len = 0

    # def check_index(self, index = 0, check_size = True, check_type = True, check_value = True):
    #     if check_type and type(index) != int:
    #         raise Exception("invalid index")
    #     if check_value and (index >= self.len or index < 0):
    #         raise Exception("out of range index")
    #     if check_size and self.len == 0:
    #         raise Exception("empty")

    def bubble_up(self, index):
        if  type(index) != int:
            raise Exception("invalid index")
        if  (index >= self.len or index < 0):
            raise Exception("out of range index")
        if  self.len == 0:
            raise Exception("empty")
        while index > 0:
            p = (index + 1) // 2 - 1
            if p >= 0 and self.heap[index] < self.heap[p]:
                self.heap[index] , self.heap[p] = self.heap[p] , self.heap[index]
                
            else:
                break
            index = p

    def bubble_down(self, index):
        if  type(index) != int:
            raise Exception("invalid index")
        if  (index >= self.len or index < 0):
            raise Exception("out of range index")
        if  self.len == 0:
            raise Exception("empty")

        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        min_in = index
        while l <= self.len:
            l = (index + 1) * 2 - 1
            r = (index + 1) * 2
            if l < self.len and self.heap[min_in] > self.heap[l]:
                min_in = l
            if r < self.len and self.heap[min_in] > self.heap[r]:
                min_in = r

            if min_in != index:
                self.heap[index] , self.heap[min_in] = self.heap[min_in] , self.heap[index]
                index = min_in
            else:
                break

    def heap_push(self, value):
        self.heap.append(value)
        self.len += 1
        self.bubble_up(self.len - 1)
    
    def heap_pop(self):
        if  self.len == 0:
            raise Exception("empty")
        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
        val = self.heap.pop()
        self.len -= 1
        if self.len != 0:
            self.bubble_down(0)
        return val

    def find_min_child(self, index):
        if  type(index) != int:
            raise Exception("invalid index")
        if  (index >= self.len or index < 0):
            raise Exception("out of range index")
        if  self.len == 0:
            raise Exception("empty")
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        if r >= self.len:
            if l < self.len:
                return l
        if l >= self.len:
            if r < self.len:
                return r
        else:
            return r if self.heap[r] < self.heap[l] else l

    def find_max_child(self, index):
        l = (index + 1) * 2 - 1
        r = (index + 1) * 2
        if r >= self.len:
            if l < self.len:
                return l
        if l >= self.len:
            if r < self.len:
                return r
        else:
            return r if self.heap[r] > self.heap[l] else l
    
    def heapify(self, *args):
        for new_node in args:
            self.heap_push(new_node)


class HuffmanTree:
    class Node:
        def __init__(self, value, char=None, p=None, l=None, r=None) -> None:
            self.value = value
            self.char = char
            self.parent = p
            self.L = l
            self.R = r

    def __init__(self):
        self.letters = list()
        self.repetitions = list()

    def set_letters(self, *args):
        self.letters.extend(list(args))

    def set_repetitions(self, *args):
        self.repetitions.extend(list(args))

    def build_huffman_tree(self):
        chars = list(zip(self.letters, self.repetitions))
        chars.sort(key = lambda key : key[1],reverse=True)
        nodes = [self.Node(val, c) for c, val in chars]
        while len(nodes) >= 2:
            l = nodes.pop()
            r = nodes.pop()
            new_node = self.Node(l.value + r.value, l=l, r=r)
            l.parent = r.parent = new_node
            
            for i in range(len(nodes)):
                if nodes[i].value < new_node.value:
                    nodes = nodes[:i] + [new_node] + nodes[i:]
                    break
                if i >= len(nodes) - 1:
                    nodes += [new_node]
            if len(nodes) == 0:
                nodes = [new_node]
        
        self.code = dict()
        self.save_code(nodes[0])

    def save_code(self, tree, pre_str = ''):
        if tree == None:
            return
        if tree.char != None:
            self.code[tree.char] = pre_str
            return

        self.save_code(tree.L, pre_str + "0")
        self.save_code(tree.R, pre_str + "1")
        

    def get_huffman_code_cost(self):
        chars = dict(zip(self.letters, self.repetitions))
        output = 0
        for i in chars.keys():
            output += chars[i] * len(self.code[i])
        return output

    def text_encoding(self, text):
        # ! time
        letter_count = {}

        for letter in text:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        self.letters = list(letter_count.keys())
        self.repetitions = list(letter_count.values())
        self.build_huffman_tree()



class Bst:
    class Node:
        def __init__(self, value, parent) -> None:
            self.value = value
            self.parent = parent
            self.L = None
            self.R = None

    def __init__(self):
        self.root = None

    def insert(self, key, n = None, p = None, side = '', first = True):
        if self.root == None:
            self.root = self.Node(key, None)
            return
        if first == True:
            n = self.root
            
        if n == None:
            if side == 'L':
                p.L = self.Node(key, p)
            if side == 'R':
                p.R = self.Node(key, p)
            return
        if key < n.value:
            self.insert(key, n.L, n, 'L', False)
        else:
            self.insert(key, n.R, n, 'R', False)

    def inorder(self, n = None, first = True):
        if first == True:
            self.out = ''
            n = self.root
        if n == None:
            return
        self.inorder(n.L, False)
        self.out += str(n.value) + ' '
        self.inorder(n.R, False)
        
        if first:
            print(self.out[:-1])
        


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
