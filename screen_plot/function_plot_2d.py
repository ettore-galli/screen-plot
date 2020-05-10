class FunctionPlot2d(object):
    class FunctionPlot2dException(Exception):
        pass

    def __init__(self, x_values, y_values, screen_height=40, function_of_x=None):
        self.x_values = x_values
        self.y_values = y_values
        if function_of_x is not None:
            self.y_values = [function_of_x(x) for x in x_values]
        self.screen_height = screen_height
        self.n_x = len(self.x_values)
        self.n_y = 2 * self.screen_height

    def calc_plot_box_draw(self):
        """
        Calc plot box only

        Render in unicode box plot chars

                0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
        U+250x	─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
        U+251x	┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
        U+252x	┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
        U+253x	┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
        U+254x	╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
        U+255x	═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
        U+256x	╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
        U+257x	╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿

        :param x_values: x axis
        :param y_values: y axis
        :return:
        """

        hline = "\u2500"  # ─
        vline = "\u2502"  # │
        right_up = "\u2518"  # ┘
        right_down = "\u2510"  # ┐
        down_right = "\u2514"  # └
        up_right = "\u250c"  # ┌
        if len(self.x_values) != len(self.y_values):
            raise FunctionPlot2d.FunctionPlot2dException("Incompatible vectors")

        y_min = min(self.y_values)
        y_max = max(self.y_values)

        y_range = y_max - y_min

        box_y_heights = []  # plot point heights in "array index" units

        # Heights
        for y_value in self.y_values:
            y_height = self.n_y - int(1.0 * (self.n_y - 1) * (y_value - y_min) / y_range) - 1
            box_y_heights.append(y_height)

        # Base render
        plot_box = [[" "] * self.n_x for _ in range(self.n_y)]

        for nx in range(self.n_x):
            if nx == 0:
                plot_box[box_y_heights[nx]][nx] = hline
            else:
                if box_y_heights[nx] == box_y_heights[nx - 1]:
                    plot_box[box_y_heights[nx]][nx] = hline
                elif box_y_heights[nx] < box_y_heights[nx - 1]:
                    plot_box[box_y_heights[nx - 1]][nx] = right_up
                    plot_box[box_y_heights[nx]][nx] = up_right
                    for y in range(box_y_heights[nx] + 1, box_y_heights[nx - 1]):
                        plot_box[y][nx] = vline
                else:
                    plot_box[box_y_heights[nx - 1]][nx] = right_down
                    plot_box[box_y_heights[nx]][nx] = down_right

                    for y in range(box_y_heights[nx - 1] + 1, box_y_heights[nx]):
                        plot_box[y][nx] = vline

        return plot_box

    def render(self, plot_box):
        """
        Render box matrix to printable lines.

        :param plot_box: Matrix
        :return: Printable render
        """

        plot_data = plot_box

        plot_draw = "\n".join(["".join([c for c in line]) for line in plot_data])

        render = plot_draw
        return render

    def plot(self):
        """
        Plots pre-calculated series

        :param x_values:
        :param y_values:
        :param render_type:
        :return:
        """
        plot_box_render = self.render(self.calc_plot_box_draw())
        return plot_box_render
