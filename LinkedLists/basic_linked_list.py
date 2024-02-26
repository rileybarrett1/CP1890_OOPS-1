from dataclasses import dataclass


@dataclass
class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'

test1 = Node(2)
print(test1)

@dataclass
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nextNode
        nodes.append('None')
        return '->'.join(nodes)

llist = LinkedList()
print(llist)

firstNode = Node('a')
llist.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(llist)