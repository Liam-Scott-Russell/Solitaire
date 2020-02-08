class Screen:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__matrix = [[" " for j in range(self.__cols)] for i in range(self.__rows)]

    def get_point(self, x, y):
        x_is_valid = x >= 0 and x < self.__cols
        y_is_valid = y >= 0 and y < self.__rows

        if x_is_valid and y_is_valid:
            return self.__matrix[x][y]
        else:
            raise IndexError("Coordinates invalid")

    def set_point(self, x, y, value):
        x_is_valid = x >= 0 and x < self.__cols
        y_is_valid = y >= 0 and y < self.__rows

        if x_is_valid and y_is_valid:
            self.__matrix[x][y] = value
        else:
            raise IndexError("Coordinates invalid")

    def get_dimensions(self):
        return self.__rows, self.__cols

    def get_matrix(self):
        return self.__matrix
