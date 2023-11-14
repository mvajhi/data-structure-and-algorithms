import sys
import re


class Queue:
    def __init__(self):
        self.queue = list()

    def getSize(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.getSize() == 0

    def getInOneLine(self):
        out = ""
        for i in self.queue:
            out += str(i) + " "
        if self.isEmpty():
            return ""
        return out[:-1]


class Stack:
    def __init__(self, size=10):
        self.stack = [0 for i in range(size)]
        self.top = -1

    def isEmpty(self):
        return self.top < 0

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        self.top -= 1
        return self.stack[self.top + 1]

    def put(self, value):
        self.pop()
        self.push(value)

    def peek(self):
        return self.stack[self.top]

    def expand(self):
        self.stack = [*self.stack, *[0 for i in range(len(self.stack))]]

    def getInOneLine(self):
        out = ""
        for i in range(self.top + 1):
            out += str(self.stack[i]) + " "
        if self.isEmpty():
            return ""
        return out[:-1]

    def getSize(self):
        return self.top + 1

    def getCapacity(self):
        return len(self.stack)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def getList(self):
        tmp = self.head
        out = ""
        while tmp is not None:
            out += str(tmp.val) + " "
            tmp = tmp.next
        return out[:-1]
        pass

    def insertFront(self, new_data):
        new = Node(new_data)
        new.next = self.head
        self.head = new
        pass

    def insertEnd(self, new_data):
        new = Node(new_data)
        if self.head is None:
            self.head = new
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = new
        pass

    def reverse(self):
        pre = None
        cur = self.head

        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        self.head = pre
        pass


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
