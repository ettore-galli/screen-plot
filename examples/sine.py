from screen_plot.function_plot_2d import FunctionPlot2d

from screen_plot.float_range_utils import float_range
import math

if __name__ == "__main__":
    x_values = float_range(0, 3 * 3.14159, 80)

    p = FunctionPlot2d(x_values, y_values=None, screen_height=24, function_of_x=lambda x: math.sin(x))
    print(p.plot())
