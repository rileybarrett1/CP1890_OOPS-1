class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertatbegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node


# Indexing starts from 0.
def insertAtIndex(self, data, index):
    new_node = Node(data)
    current_node = self.head
    position = 0
    if position == index:
        self.insertAtBegin(data)
    else:
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:

            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

# inserting at the end
def insertAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while current_node.next:
        current_node = current_node.next

    current_node.next = new_node


# Update node of a linked list
# at given position
def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
        current_node.data = val
    else:
        while (current_node != None and position != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            current_node.data = val
        else:
            print("Index not present")


def remove_first_node(self):
    if (self.head == None):
        return

    self.head = self.head.next


def remove_last_node(self):
    if self.head is None:
        return
    current_node = self.head
    while(current_node.next.next):
        current_node = current_node.next

    current_node.next = None


# Method to remove at given index
def remove_at_index(self, index):
    if self.head == None:
        return

    current_node = self.head
    position = 0
    if position == index:
        self.remove_first_node()
    else:
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")