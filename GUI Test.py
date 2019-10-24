from os import system, name, get_terminal_size
from sys import modules
from time import sleep
import sys


def clear():
    pass

    # for windows
    if 'idlelib.run' in modules:
        print("Please run this program outside of Python IDLE.\n To do this, double click the A2cool.py file.")
    # print('Running IDLE' if 'idlelib.run' in sys.modules else 'Out of IDLE')

    print("Current screen size is {} by {}".format(
        get_terminal_size().columns, get_terminal_size().columns))
    print("Setting screen size to 200 by 100")
    sleep(2)
    system("mode con cols=200 lines=100")

    print("New screen size is {} by {}".format(
        get_terminal_size().columns, get_terminal_size().columns))
    sleep(5)

    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


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

    def display(self):
        """
        Prints the screen matrix.
        """
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
        return self.__matrix.copy()

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
        self.previous_screen = self.screen.get_matrix()

        # create the border
        # the top and bottom border
        tb_border = border * self.max_length
        # makes the first and last lines the border
        self.lines = [tb_border] + self.lines + [tb_border]
        for i in range(len(self.lines)):
            # adds the side border
            self.lines[i] = border + self.lines[i] + border

        # account for adding the border, even if the border is blank
        self.max_length += 2 * len(border)

    def display_centre(self):
        """
        Displays the message contents in the centre of the screen.
        This method is best for printing warnings and alerts.
        """
        max_rows = self.screen.get_dimensions()[0]
        max_cols = self.screen.get_dimensions()[1]

        # check if we can display our message, accounting for the border
        cols_fit = (2 + self.max_length) <= max_cols
        rows_fit = (2 + len(self.lines)) <= max_rows
        if rows_fit and cols_fit:

            # top left corner of the message box (for message)
            start_col = (max_cols - self.max_length) // 2
            start_row = (max_rows - len(self.lines)) // 2

            # testing
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

        else:
            raise Exception("Message does not fit on the screen")


def get_number_of_columns():
    """
    Returns the current number of columns being displayed by the terminal.
    """
    try:
        # This works on windows, sometimes on Linux/mac
        columns = get_terminal_size().columns
    except Exception as e:
        print(e)
        return None
    else:
        return columns


if __name__ == "__main__":
    sleep(5)
    number_of_cols = get_number_of_columns() - 1
    # Doing floor division by 4 gives a good ratio of height to width
    number_of_rows = number_of_cols // 4
    screen = Screen(number_of_rows, number_of_cols)
    # screen.draw_vertical_line(0, '#')
    # screen.draw_vertical_line(number_of_cols - 1, '#')
    # screen.draw_horizontal_line(0, '#')
    # screen.draw_horizontal_line(number_of_rows - 1, '#')
    # screen.display()
    delay = 0.005
    while True:
        my_message = Message(
            "Hello and welcome to:\n      Solitaire!", screen, border='-')
        my_message.display_centre()
        screen.draw_vertical_line(0, '-')
        screen.draw_vertical_line(number_of_cols - 1, '-')
        screen.draw_horizontal_line(0, '-')
        screen.draw_horizontal_line(number_of_rows - 1, '-')
        screen.clear()
        screen.display()
        sleep(delay)

        my_message = Message(
            "Hello and welcome to:\n      Solitaire!", screen, border='\\')
        screen.clear()
        my_message.display_centre()
        screen.display()
        screen.draw_vertical_line(0, '\\')
        screen.draw_vertical_line(number_of_cols - 1, '\\')
        screen.draw_horizontal_line(0, '\\')
        screen.draw_horizontal_line(number_of_rows - 1, '\\')
        sleep(delay)

        my_message = Message(
            "Hello and welcome to:\n      Solitaire!", screen, border='|')
        screen.clear()
        my_message.display_centre()
        screen.draw_vertical_line(0, '|')
        screen.draw_vertical_line(number_of_cols - 1, '|')
        screen.draw_horizontal_line(0, '|')
        screen.draw_horizontal_line(number_of_rows - 1, '|')
        screen.display()
        sleep(delay)

        my_message = Message(
            "Hello and welcome to:\n      Solitaire!", screen, border='/')
        screen.clear()
        my_message.display_centre()
        screen.draw_vertical_line(0, '/')
        screen.draw_vertical_line(number_of_cols - 1, '/')
        screen.draw_horizontal_line(0, '/')
        screen.draw_horizontal_line(number_of_rows - 1, '/')
        screen.display()
        sleep(delay)
    input('...')
