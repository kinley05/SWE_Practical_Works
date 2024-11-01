class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        current = self.head
        previous = None
        seen_data = set()
        while current:
            if current.data in seen_data:
                previous.next = current.next
            else:
                seen_data.add(current.data)
                previous = current
            current = current.next

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        l1, l2 = self.head, other.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        self.head = dummy.next

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("Original List 1:")
ll1.display()
print("Original List 2:")
ll2.display()

print("Middle element of ll1:", ll1.find_middle())

ll1.merge_sorted(ll2)
print("Merged Sorted List:")
ll1.display()

ll1.head.next.next.next.next.next = ll1.head.next.next
print("Cycle present:", ll1.has_cycle())

ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(2)
ll3.append(3)
print("List with duplicates:")
ll3.display()
ll3.remove_duplicates()
print("List after removing duplicates:")
ll3.display()
