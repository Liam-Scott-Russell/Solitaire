class ScreenHelper:
    @staticmethod
    def draw_line(screen, x1, y1, x2, y2, value):
        if screen.point_is_valid(x1, y1) and screen.point_is_valid(x2+1, y2+1):
            for row in range(x1, x2+1):
                for col in range(y1, y2+1):
                    screen.set_point(row, col, value)
        else:
            raise IndexError("Coordinates not valid")
