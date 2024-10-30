class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
        runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value
    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.remove_from_front()
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value
    def remove_val(self, val):
        if self.head is None:
            return False
        if self.head.value == val:
            self.head = self.head.next
            return True
        runner = self.head
        while runner.next != None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return True
            runner = runner.next
        return False
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        count = 0
        while runner != None and count < n - 1:
            runner = runner.next
            count += 1
        if runner is None:
            return False
        new_node.next = runner.next
        runner.next = new_node
        return self