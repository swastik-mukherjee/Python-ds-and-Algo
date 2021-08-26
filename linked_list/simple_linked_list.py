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


def display(head):
    while(head):
        print(head.key)
        head = head.next


# driver code
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)


#print(search(head, 40))
display(head)
