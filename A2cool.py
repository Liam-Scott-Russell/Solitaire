from screen import Screen, Message, Card, get_current_screen_size
from time import sleep


class Deque:
    """
    Implements a deque class

    The front of the deque is stored in the last element of the list.
    The rear of the deque is stored in the first element of the list.

    Operations:

        add_front(item)
        add_read(item)
        remove_front()
        remove_rear()
        size()
        peek()
        peeklast()
        printall()
    """

    def __init__(self):
        # sets up the python list that holds the deque items
        self.items = []

    def add_front(self, item):
        # adds the item to the front of the deque, i.e. append
        self.items.append(item)

    def add_rear(self, item):
        # adds the item to the end of the deque, i.e. prepend
        self.items = [item] + self.items

    def remove_front(self):
        # removes and returns the item in the front of the deque
        if self.size() == 0:
            return None  # no data in deque
        else:
            return self.items.pop()

    def remove_rear(self):
        # removes and returns the item at the rear of the deque
        if self.size() == 0:
            return None  # no data in deque
        else:
            temp = self.items[0]
            self.items = self.items[1:]  # removes the first item
            return temp

    def size(self):
        # returns the size of the deque
        return len(self.items)

    def peek(self):
        # returns the item at the front of the deque, without removing it
        if self.size() == 0:
            return None  # no data in deque
        else:
            return self.items[-1]

    def peeklast(self):
        # returns the item at the rear of the deque, without removing it
        if self.size() == 0:
            return None  # no data in deque
        else:
            return self.items[0]

    def printall(self, index):
        # prints the data stored within the deque
        if self.size() == 0:
            print(' ')
        elif index == 0:
            # prints the first item, followed by '*' characters
            print(str(self.items[0]), ' *' * (len(self.items) - 1), sep="")
        else:
            # necessary to use the list comprehension,
            # as string objects are expected
            print(" ".join([str(x) for x in self.items]))


def main():
    try:
        rows, cols = get_current_screen_size()
    except:
        # We are probably running the code in IDLE, check this
        s = Screen(0, 0)
        if s.is_running_in_IDLE():
            print("You appear to be running this code in IDLE.")
            print("Please refer to the instructions in the PDF for how to run the file")
            input('Press ENTER to exit')

    # checks that the file is being run in fullscreen
    while rows < 50 or cols < 200:
        s = Screen(rows, cols)
        disp_string = "You don't appear to be running this file in fullscreen."
        disp_string += f"\nCurrent screen size: rows = {rows}, columns = {cols}"
        disp_string += "\nThe reccomended minimum screen size is 50 rows and 200 columns."
        disp_string += "\nPlease adjust the screen size to continue"
        message = Message(disp_string, s)
        message.display_centre()  # displays the message to the user
        s.display()
        sleep(2) # Wait a little bit
        rows, cols = get_current_screen_size()
    else:
        s.clear()


if __name__ == "__main__":
    main()
    input("...")
