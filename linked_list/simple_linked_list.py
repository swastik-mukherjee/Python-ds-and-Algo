class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def search(head, key):
    current = head
    index = 0
    while(current):

        if(current.key == key):
            return index
        else:
            current = current.next
            index = index + 1


# driver code
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
x = 20

print(search(head, 40))
