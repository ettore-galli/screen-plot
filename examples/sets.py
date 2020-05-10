from screen_plot.function_plot_2d import FunctionPlot2d

from screen_plot.float_range_utils import float_range
import math

if __name__ == "__main__":
    x_values = float_range(0, 7 * 3.14159, 70)

    for render_set in FunctionPlot2d.RENDER_SET_LIST:
        print("-" * 80)
        print(render_set + " " + "-" * (80 - len(render_set) - 1))
        print("-" * 80)
        p = FunctionPlot2d(x_values, y_values=None, screen_height=20, function_of_x=lambda x: math.sin(x),
                           use_render_set=render_set)
        print(p.plot())
