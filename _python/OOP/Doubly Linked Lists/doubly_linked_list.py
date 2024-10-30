class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return self
    def add_to_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return self
    def delete(self, data):
        runner = self.head
        while runner:
            if runner.data == data:
                if runner.prev:
                    runner.prev.next = runner.next
                else:
                    self.head = runner.next
                if runner.next:
                    runner.next.prev = runner.prev
                else:
                    self.tail = runner.prev
                return  self
            runner = runner.next
    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if self.head is None:
            return new_node
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            return new_node
        runner = self.head
        count = 1
        while runner.next and count < position - 1:
            runner = runner.next
            count += 1
        new_node.next = runner.next
        new_node.prev = runner
        if runner.next is not None:
            runner.next.prev = new_node
        runner.next = new_node
        return self
    


# Questions

# 1: How would you know if you have a circular linked list?
# A: If the head's previous node or the tail's next node are not None.

# 2: How would you get to the middle of the linked list?
# A: Make two pointers that point to the head and one while loop. First pointer increments by 1 each time, the second by 2.
# Once the second becomes null, it means it's at the end of the linked list, and the first pointer should be in the middle.

# 3: How would you remove duplicate values from the list?
# A: Two ways. First way, to sort the list first, then make a pointer that points to the head and increments by one in a while loop.
# That pointer will keep checking if its value is the same as the one next to it. If True, remove the node.
# Second way, make a for loop through the whole list, a pointer to the head, and another loop for the list. We will loop once for every value and see if
# it's duplicated. After thr inner loop is finished, increment pointer by one. And re-initiate the inner loop for the next value.


# 4: How would you reverse the values in the list?
# A: Loop through the list, and swap the next and prev pointers of each node. Lastly, update the head to the last node processed and the tail to the first.