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

    @staticmethod
    def draw_card(screen, x, y, card):
        representation = card.get_representation()
        representation_as_rows = representation.split("\n")

        for y_offset in range(len(representation_as_rows)):
            current_y_coordinate = y + y_offset
            current_row = representation_as_rows[y_offset]

            for x_offset in range(len(current_row)):
                current_x_coordinate = x + x_offset
                current_symbol = current_row[x_offset]
                screen.set_point(current_x_coordinate, current_y_coordinate, current_symbol)