from screen_plot.function_plot_2d import FunctionPlot2d

from screen_plot.float_range_utils import float_range
import math

if __name__ == "__main__":
    # FUNCTION

    x_values = float_range(0, 2 * 3.14159, 80)

    p = FunctionPlot2d(x_values, y_values=None, screen_height=40, function_of_x=lambda x: math.sin(x))
    print(p.plot())

    # VALUES
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_values = [8, 9, 10, 11, 9, 7, 5, 7, 9, 10]

    p2 = FunctionPlot2d(x_values, y_values, screen_height=7)
    print(p2.plot())

"""

"""
