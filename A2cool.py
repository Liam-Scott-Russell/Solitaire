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
        self.columns = []
        # sets the heigh of all columns based on the largest number of cards
        height = self.screen.get_dimensions()[0] - 1
        for i in range(len(self.card_deques)):
            # Gets the deck of cards, and we reverse it as we want the top card at the back
            deck = [Card(j, self.screen)
                    for j in self.card_deques[i].return_all(i)]
            self.columns.append(
                Column(f"Col #{i}", self.screen, 1+(10*i), 9+(10*i), 1, height, deck[::-1]))

        for col in self.columns:
            col.display()
        self.screen.display()

    def move(self, c1, c2):
        if c1 == 0 and c2 == 0:  # condition 1
            card = self.card_deques[0].remove_rear()
            self.card_deques[0].add_front(card)
            return True  # successfully moved

        elif c1 == 0 and c2 > 0:  # condition 2
            # first if statement checks that there are items within the deques
            if self.card_deques[0].size() != 0 and self.card_deques[c2].size() != 0:

                # checks if the move is valid, so we move the card
                if self.card_deques[0].peeklast() == (self.card_deques[c2].peeklast() - 1):

                    # select the card to move
                    card_to_move = self.columns[c1].cards[-1]
                    popped_card = self.card_deques[0].remove_rear()

                    # clear the removed card off the scree
                    card_to_move.wipe()
                    self.display()

                    # calculate the destination address
                    destination_row, destination_col = self.columns[c2].current_starting_position

                    # move the card along the screen, and then remove it
                    card_to_move.move(destination_row, destination_col)
                    card_to_move.wipe()

                    # actually "add" the card to the deque
                    self.card_deques[c2].add_rear(popped_card)
                    self.display()

                    return True

                else:
                    self.invalid_move_warning()
                    return False

            # the target column is empty, so we can move there
            elif self.card_deques[0].size() != 0:

                # select the card to move
                card_to_move = self.columns[c1].cards[-1]
                popped_card = self.card_deques[0].remove_rear()

                # clear the removed card off the scree
                card_to_move.wipe()
                self.display()

                # calculate the destination address
                destination_row, destination_col = self.columns[c2].current_starting_position

                # move the card along the screen, and then remove it
                card_to_move.move(destination_row, destination_col)
                card_to_move.wipe()

                # actually "add" the card to the deque
                self.card_deques[c2].add_rear(popped_card)
                self.display()

                return True
            else:
                self.invalid_move_warning()
                return False

        elif c1 > 0 and c2 > 0:
            # first if statement checks that there are items within the deques
            if self.card_deques[c1].size() != 0 and self.card_deques[c2].size() != 0:
                if self.card_deques[c1].peeklast() == (self.card_deques[c2].peek() - 1):
                    # the move is valid, so move the cards
                    for i in range(self.card_deques[c1].size()):
                        self.card_deques[c2].add_front(self.card_deques[c1].remove_rear())
                        self.display()
                    return True

            elif self.card_deques[0].size() != 0:
                # the target column is empty, so we can move there
                for i in range(self.card_deques[c1].size()):
                    self.card_deques[c2].add_front(self.card_deques[c1].remove_rear())
                    self.display()
                return True

            else:
                self.invalid_move_warning()
                return False
        else:
            self.invalid_move_warning()
            return False

    def invalid_move_warning(self):
        error = Message(
            "Your move is invalid!\nPress ENTER to try again.", self.screen, border="#")
        error.display_centre()
        self.screen.display()
        input("...")
        error.wipe()
        self.screen.display()

    def IsComplete(self):
        if self.card_deques[0].size() != 0:
            # fails condition 1 (cards are still in the first pile)
            return False

        # this list holds the size of the piles of cards
        sizes = [self.card_deques[i].size() for i in range(len(self.card_deques))]

        # this is true if the cards aren't all in the same pile,
        # as only one pile should have a non-zero length (condition 2)
        if sizes.count(0) != (len(self.card_deques) - 1):
            return False

        # we don't need to check condition 3, as it should always
        # be true, unless there was an illegal move somewhere
        return True

    def play(self):

        game_iter = 0
        for i in range(self.__ChanceNo):

            self.display()

            status = Message(f"Round { game_iter } out of { self.__ChanceNo }", self.screen)
            status.display_centre()
            self.screen.display()
            col1 = input('Source Column?\t')
            col2 = input('Destination Column?\t')
            status.wipe()
            # Try and convert the moves to integers
            try:
                col1 = int(col1)
                col2 = int(col2)
            except:
                self.invalid_move_warning()
                continue

            if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:
                
                if self.move(col1, col2):
                    game_iter += 1
            
            else:
                self.invalid_move_warning()

            if self.IsComplete():
                
                
                win = Message(f"You Win in {game_iter+1} steps!", self.screen)
                win.display_centre()
                self.screen.display()

                input("Press ENTER to exit ...")
                break

            else:

                if game_iter+1 == self.__ChanceNo:
                    
                    lose = Message("You LOSE!", self.screen)
                    lose.display_centre()
                    self.screen.display()
                    input("Press ENTER to exit ...")
                    break


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

    screen = Screen(rows, cols)
    screen.clear()
    welcome_message = Message(
        "Welcome to Solitaire!\nPress ENTER to start.", screen)
    welcome_message.display_centre()
    screen.display()
    input('...')
    welcome_message.wipe()
    game=Solitaire([i for i in range(2, -1, -1)], screen)
    game.display()
    game.play()


if __name__ == "__main__":
    main()