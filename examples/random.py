from screen_plot.function_plot_2d import FunctionPlot2d

from screen_plot.float_range_utils import float_range
import math

if __name__ == "__main__":
    x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    p = FunctionPlot2d(x_values, y_values=y_values, screen_height=24, function_of_x=None)
    print(p.plot())
