class Screen:
    def __init__(self, cols, rows):
        self.__rows = rows
        self.__cols = cols
        self.__matrix = [[" " for j in range(self.__cols)] for i in range(self.__rows)]

    def point_is_valid(self, x, y):
        x_is_valid = 0 <= x < self.__cols
        y_is_valid = 0 <= y < self.__rows
        return x_is_valid and y_is_valid

    def get_point(self, x, y):
        if self.point_is_valid(x, y):
            return self.__matrix[x][y]
        else:
            raise IndexError("Coordinates invalid")

    def set_point(self, x, y, value):

        if self.point_is_valid(x, y):
            self.__matrix[x][y] = value
        else:
            raise IndexError("Coordinates invalid")

    def get_dimensions(self):
        return self.__cols, self.__rows

    def get_matrix(self):
        return self.__matrix
