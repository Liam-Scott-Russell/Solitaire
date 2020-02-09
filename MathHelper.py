def calculate_points_on_vertical_line(x_value, y0, y1):
    return [(x_value, y_value) for y_value in range(y0, y1+1)]


class MathHelper:
    @staticmethod
    def calculate_points_on_line(x0, y0, x1, y1):
        points_on_line = []

        y_gradient = 2 * (y1 - y0)
        x_gradient = x1 - x0

        if x_gradient == 0:
            return calculate_points_on_vertical_line(x0, y0, y1)

        slope_error = y_gradient - x_gradient
        current_y_value = y0

        for current_x_value in range(x0, x1 + 1):
            points_on_line.append((current_x_value, current_y_value))

            slope_error += y_gradient

            if slope_error >= 0:
                current_y_value += 1
                slope_error -= 2 * x_gradient

        if (x1, y1) not in points_on_line:
            points_on_line.append((x1, y1))

        return points_on_line
