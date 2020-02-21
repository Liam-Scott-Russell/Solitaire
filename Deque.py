class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items = [item] + self.items

    def remove_front(self):
        if self.size() == 0:
            raise IndexError("No items in Deque")
        else:
            return self.items.pop()

    def remove_rear(self):
        if self.size() == 0:
            raise IndexError("No items in Deque")
        else:
            current_rear_item = self.items[0]
            self.items = self.items[1:]
            return current_rear_item

    def size(self):
        return len(self.items)

    def peek_front(self):
        if self.size() == 0:
            raise IndexError("No items in Deque")
        else:
            return self.items[-1]

    def peek_rear(self):
        if self.size() == 0:
            raise IndexError("No items in Deque")
        else:
            return self.items[0]
