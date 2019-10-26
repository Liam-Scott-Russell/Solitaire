"""
Name: Liam Scott-Russell
UPI: hsco139
ID: 980268500
"""
from os import system, name, get_terminal_size
from sys import modules
from time import sleep
import copy


class Screen:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        # creates an ixj matrix of ' ' characters that we can use as the screen
        self.__matrix = [
            [' ' for i in range(self.__cols)] for j in range(self.__rows)]

    def is_running_in_IDLE(self):
        """
        Returns true if the program is running within Python IDLE.
        Terminal commands won't work within IDLE.
        """
        return 'idlelib.run' in modules

    def clear(self):
        """
        Clears the screen by wiping the standard output.
        """
        # this is when running on windows
        if name == 'nt':
            _ = system('cls')  # the '_' character suppresses the system output
        else:  # if we are running on mac or linux
            _ = system('clear')

    def display(self, clear=True):
        """
        Prints the screen matrix.
        If clear is set to True, then the screen is cleared beforehand.
        """
        if clear:
            self.clear()
        for row in self.__matrix:
            print("".join(row))

    def get_dimensions(self):
        """
        Returns the dimensions of the screen object,
        as the tuple (rows, columns).
        """
        return (self.__rows, self.__cols)

    def get_matrix(self):
        """
        Returns the current screen matrix as a 2D array.
        Useful for saving the previous screen when displaying a message.
        """
        # We return a copy of the list, not a reference because
        #   if we update the matrix, we want this copy to stay the same.
        return copy.deepcopy(self.__matrix)

    def set_matrix(self, new_matrix):
        """
        Replaces the current screen matrix with new_matrix, if it is valid.
        The dimensions of the new matrix must match those of the old one.
        """
        # checks if the two matrices have the same number of rows
        rows_match = len(new_matrix) == len(self.__matrix)

        # for the rows, we assume all rows of the new matrix are the same length
        # if both matrices have the same number of elements in each column,
        #   then they must have the same number of columns
        cols_match = len(new_matrix[0]) == len(self.__matrix[0])

        if rows_match and cols_match:
            self.__matrix = new_matrix
            return True  # so the caller program knows that the matrix was set
        else:
            raise Exception(
                "New matrix dimensions don't match existing dimensions.")

    def get_point(self, i, j):
        """
        Returns the point in the i'th row and j'th column, if it exists.
        (0,0) is the top left point.
        """
        if 0 <= i and i < self.__rows and 0 <= j and j < self.__cols:
            return self.__matrix[i][j]
        else:
            return None

    def set_point(self, i, j, new_value):
        """
        Sets the point in the i'th row and j'th column, to new_value, if the point exists.
        (0,0) is the top left point.
        """
        if 0 <= i and i < self.__rows and 0 <= j and j < self.__cols:
            self.__matrix[i][j] = new_value
            return True  # so the caller program knows that the matrix was set
        else:
            raise Exception("The value ({}, {}) is not valid".format(i, j))

    def set_screen(self, rows, cols):
        """
        Creates and returns a new screen object.
        Attempts to transfer the old screen matrix over
        """
        new_screen = Screen(rows, cols)
        try:
            new_screen.set_matrix(self.get_matrix())
        except:
            print("Couldn't transfer the matrix. Previous screen lost.")
        return new_screen

    def draw_horizontal_line(self, row, value, lower=0, upper=None):
        """
        Draws a horizontal line of a custom value along a row, from lower to upper.
        Values must be valid, i.e. within the range of the matrix.
        lower and upper are inclusive
        """
        if upper is None:
            # sets the default value of upper to be the entire horizontal screen
            upper = self.__cols

        # checks if the row value is valid
        if 0 <= row and row < self.__rows:
            for j in range(lower, upper):
                # changes all the values from lower to upper
                self.set_point(row, j, value)
        else:
            raise Exception("The row value is not valid")

    def draw_vertical_line(self, col, value, lower=0, upper=None):
        """
        Draws a vertical line of a custom value along a column, from lower to upper.
        Values must be valid, i.e. within the range of the matrix.
        lower and upper are inclusive
        """
        if upper is None:
            # sets the default value of upper to be the entire vertical screen
            upper = self.__rows

        # checks if the col value is valid
        if 0 <= col and col < self.__cols:
            for i in range(lower, upper):
                # sets all the values from lower to upper
                self.set_point(i, col, value)
        else:
            raise Exception("The column value is not valid")


class Message:
    def __init__(self, message, screen, border='*'):
        """
        Displays the input message on the input screen object.
        The length of each line must be 2 less then the width of the screen (for border).
        The number of lines must be 2 less than the height of the screen (for border)
        The message is passed as a single string, using '\n' for line breaks.
        The border must be a single character, or an empty string.
        """

        # TODO: make this a matrix so that the whitespace and borders display correctly
        self.lines = message.split("\n")
        self.max_length = max([len(i) for i in self.lines])
        self.screen = screen
        self.previous_screen = None
        self.border_char = border

    def display_centre(self):
        """
        Displays the message contents in the centre of the screen.
        This method is best for printing warnings and alerts.
        """
        self.previous_screen = self.screen.get_matrix()
        max_rows = self.screen.get_dimensions()[0]
        max_cols = self.screen.get_dimensions()[1]

        # check if we can display our message, accounting for the border
        cols_fit = (2 + self.max_length) <= max_cols
        rows_fit = (2 + len(self.lines)) <= max_rows
        if rows_fit and cols_fit:

            # top left corner of the message box (for message)
            start_col = (max_cols - self.max_length) // 2
            start_row = (max_rows - len(self.lines)) // 2

            # draws the message
            for i in range(len(self.lines)):
                for j in range(self.max_length):
                    try:
                        # trys to plot the message's character at a point
                        self.screen.set_point(
                            start_row + i, start_col + j, self.lines[i][j])
                    except:
                        # there isn't a character there, so we print a ' '
                        self.screen.set_point(
                            start_row + i, start_col + j, ' ')

            # define the corners of the border
            top_row = start_row - 1
            bottom_row = start_row + len(self.lines) + 1
            left_col = start_col - 1
            right_col = start_col + self.max_length

            # draw the border lines
            self.screen.draw_vertical_line(
                left_col, self.border_char, lower=top_row, upper=bottom_row)
            self.screen.draw_vertical_line(
                right_col, self.border_char, lower=top_row, upper=bottom_row)
            self.screen.draw_horizontal_line(
                top_row, self.border_char, lower=left_col, upper=right_col)
            self.screen.draw_horizontal_line(
                bottom_row-1, self.border_char, lower=left_col, upper=right_col)

        else:
            raise Exception("Message does not fit on the screen")

    def wipe(self):
        """
        Restores the previous screen (if there is one) prior to
        displaying the message on the screen.
        WARNING: Any screen changes between display_centre() and wipe aren't saved
        """
        if self.previous_screen is None:
            return False  # The wipe failed
        self.screen.set_matrix(self.previous_screen)
        return True  # the wipe was successful


class Card:
    def __init__(self, number, screen):
        """
        Creates a card with the number specified.
        Cards are 5x5.
        """
        self.number = number
        self.screen = screen
        self.__string = " ____\n|   {}|\n|    |\n|    |\n|____|".format(
            str(self.number))
        self.previous_screen = None
        self.current_row = None
        self.current_col = None

    def __str__(self):
        return self.__string

    def display(self, row, col):
        """
        Prints the card, with its top left corner at the specified
        row and col. Will overwrite whatever is underneath it.
        """
        # Saves the previous screen, so we can restore it later
        self.previous_screen = self.screen.get_matrix()

        rows = self.__string.split('\n')
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.screen.set_point(row + i, col + j, rows[i][j])

        # update the cards's current location
        self.current_row = row
        self.current_col = col

    def wipe(self):
        """
        Restores the previous screen (if there is one) prior to
        displaying the card on the screen.
        WARNING: Any screen changes between display() and wipe aren't saved
        """
        if self.previous_screen is None:
            return False  # The wipe failed
        self.screen.set_matrix(self.previous_screen)
        return True  # the wipe was successful

    def move(self, row, col):
        """
        Moves the card to the specified row and column.
        Displays the card moving along the screen to its destination.
        Card must have been displayed using display() first.
        """
        # sets the delay for how long to sleep between printing cards
        delay = 0.1

        # the difference between the initial and final destination
        row_change = row - self.current_row
        col_change = col - self.current_col

        # hold the sign of the change, i.e. is it negative or positive
        row_change_sign = 1
        col_change_sign = 1

        # sets the signs, and then makes them positive
        if row_change < 0:
            row_change_sign = -1
            row_change *= -1
        if col_change < 0:
            col_change_sign = -1
            col_change *= -1

        while row_change > 0 and col_change > 0:
            sleep(delay)
            self.wipe()  # clear the card off the screen
            new_row = self.current_row + (1 * row_change_sign)
            new_col = self.current_col + (1 * col_change_sign)
            self.display(new_row, new_col)
            self.screen.display()
            row_change -= 1
            col_change -= 1

        # handles remaining vertical movement
        while row_change > 0:
            sleep(delay)
            self.wipe()  # clear the card off the screen
            new_row = self.current_row + (1 * row_change_sign)
            self.display(new_row, self.current_col)
            self.screen.display()
            row_change -= 1

        # handles remaining horizontal movement
        while col_change > 0:
            sleep(delay)
            self.wipe()  # clear the card off the screen
            new_col = self.current_col + (1 * col_change_sign)
            self.display(self.current_row, new_col)
            self.screen.display()
            col_change -= 1


class Column:
    def __init__(self, name, screen, start_col, end_col, start_row, end_row, cards):
        self.screen = screen
        self.start_col = start_col
        self.end_col = end_col
        self.start_row = start_row
        self.end_row = end_row
        self.cards = cards
        self.current_starting_position = [start_row, start_col+1]
        if self.start_col > self.end_col or self.start_row > self.end_row:
            raise Exception("The row or column is invalid.")

    def display(self):
        # draw the vertical lines at the edges of the column
        # self.screen.draw_vertical_line(self.start_col, '#', upper=self.end_row, lower=self.start_row)
        self.screen.draw_vertical_line(
            self.end_col, ':', upper=self.end_row, lower=self.start_row)

        for card in self.cards:
            if self.current_starting_position[0] + 5 > self.end_row:
                # The card wont fit on the screen
                continue
            else:
                card.display(
                    self.current_starting_position[0], self.current_starting_position[1])
                self.current_starting_position[0] += 2


def get_current_screen_size():
    """
    Returns the current number of rows and columns being displayed.
    """
    try:
        # This works on windows, sometimes on Linux/mac
        # The -1 is to prevent the columns/rows from going over the screen limit
        cols = get_terminal_size().columns - 1
        rows = get_terminal_size().lines - 1
    except Exception as e:
        print(e)
        return None
    else:
        return (rows, cols)
