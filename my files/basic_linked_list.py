from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


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

    def insert_at_head(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            return self.head


list1 = LinkedList()
print(list1)

firstnode = Node('a')
list1.head = firstnode

secondnode = Node('b')
thirdnode = Node('c')

firstnode.nextNode = secondnode
secondnode.nextNode = thirdnode

print(list1)
print(list1.head)
