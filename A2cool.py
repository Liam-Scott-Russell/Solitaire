from screen import Screen, Message, Card, Column, get_current_screen_size
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

    def return_all(self, index):
        # prints the data stored within the deque
        if self.size() == 0:
            return []
        elif index == 0:
            # returns the first item, followed by '*' characters
            return [str(self.items[0])] + ['*'] * (len(self.items) - 1)
        else:
            # necessary to use the list comprehension,
            # as string objects are expected
            output = [str(x) for x in self.items]
            if output is not None:
                return output
            return []


class Solitaire:
    def __init__(self, ncards, screen):
        # implemented as specified in the handout/coderunner
        self.card_deques = []
        self.__CardNo = len(ncards)
        self.__ColNo = (self.__CardNo // 8) + 3
        self.__ChanceNo = self.__CardNo * 2
        for i in range(self.__ColNo):
            self.card_deques.append(Deque())
        for i in range(self.__CardNo):
            self.card_deques[0].add_front(ncards[i])
        self.screen = screen
        self.columns = []

    def display(self):
        # sets the heigh of all columns based on the largest number of cards
        height = 2 * max([len(j.items) for j in self.card_deques]) + 6
        for i in range(len(self.card_deques)):
            # Gets the deck of cards, and we reverse it as we want the top card at the back
            deck = [Card(j, self.screen) for j in self.card_deques[i].return_all(i)]
            self.columns.append(Column(f"Col #{i}", self.screen, 1+(10*i), 9+(10*i), 1, height, deck[::-1]))

        for col in self.columns:
            col.display()
        self.screen.display()


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
        sleep(2)  # Wait a little bit
        rows, cols = get_current_screen_size()


if __name__ == "__main__":
    main()
    input("...")
