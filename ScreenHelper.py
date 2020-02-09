from MathHelper import MathHelper


class ScreenHelper:
    @staticmethod
    def draw_line(screen, x1, y1, x2, y2, value):
        if screen.point_is_valid(x1, y1) and screen.point_is_valid(x2, y2):
            points_to_draw = MathHelper.calculate_points_on_line(x1, y1, x2, y2)

            for point in points_to_draw:
                screen.set_point(point[0], point[1], value)
        else:
            raise IndexError("Coordinates not valid")
