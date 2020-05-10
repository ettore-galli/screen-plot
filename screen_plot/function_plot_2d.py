class FunctionPlot2d(object):

    """
                0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
        U+250x	─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
        U+251x	┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
        U+252x	┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
        U+253x	┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
        U+254x	╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
        U+255x	═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
        U+256x	╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
        U+257x	╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿

    """
    __render_sets_configuration = {
        "double_set": {
            "hline": "═",
            "vline": "║",
            "right_up": "╝",
            "right_down": "╗",
            "down_right": "╚",
            "up_right": "╔"
        },
        "ascii_set": {
            "hline": "-",
            "vline": "|",
            "right_up": "'",
            "right_down": ".",
            "down_right": "'",
            "up_right": "."
        },

        "bold_set": {
            "hline": "━",
            "vline": "┃",
            "right_up": "┛",
            "right_down": "┓",
            "down_right": "┗",
            "up_right": "┏"
        },

        "square_set": {
            "hline": "\u2500",  # ─
            "vline": "\u2502",  # │
            "right_up": "\u2518",  # ┘
            "right_down": "\u2510",  # ┐
            "down_right": "\u2514",  # └
            "up_right": "\u250c"  # ┌
        },

        "round_set": {
            "hline": "─",
            "vline": "│",
            "right_up": "╯",
            "right_down": "╮",
            "down_right": "╰",
            "up_right": "╭"
        }
    }

    RENDER_SET_LIST = __render_sets_configuration.keys()

    class FunctionPlot2dException(Exception):
        pass

    def __init__(self, x_values, y_values, screen_height=40, function_of_x=None, use_render_set=None):
        self.x_values = x_values
        self.y_values = y_values
        if function_of_x is not None:
            self.y_values = [function_of_x(x) for x in x_values]
        self.screen_height = screen_height
        self.n_x = len(self.x_values)
        self.n_y = self.screen_height
        self.use_render_set = use_render_set

    def calc_block_function_heights(self):
        y_min = min(self.y_values)
        y_max = max(self.y_values)

        y_range = y_max - y_min

        box_y_heights = []  # plot point heights in "array index" units

        # Heights
        for y_value in self.y_values:
            y_height = self.n_y - int(1.0 * (self.n_y - 1) * (y_value - y_min) / y_range) - 1
            box_y_heights.append(y_height)

        return box_y_heights

    def calc_plot_box_draw(self):
        """
        Calc plot box only

        Render in unicode box plot chars



        :param x_values: x axis
        :param y_values: y axis
        :return:
        """

        render_set = FunctionPlot2d.__render_sets_configuration["square_set"]
        if self.use_render_set is not None:
            render_set = FunctionPlot2d.__render_sets_configuration[self.use_render_set.lower()]

        if len(self.x_values) != len(self.y_values):
            raise FunctionPlot2d.FunctionPlot2dException("Incompatible vectors")

        box_y_heights = self.calc_block_function_heights()

        # Base render
        plot_box = [[" "] * self.n_x for _ in range(self.n_y)]

        for nx in range(self.n_x):
            if nx == 0:
                plot_box[box_y_heights[nx]][nx] = render_set["hline"]
            else:
                if box_y_heights[nx] == box_y_heights[nx - 1]:
                    plot_box[box_y_heights[nx]][nx] = render_set["hline"]
                elif box_y_heights[nx] < box_y_heights[nx - 1]:
                    plot_box[box_y_heights[nx - 1]][nx] = render_set["right_up"]
                    plot_box[box_y_heights[nx]][nx] = render_set["up_right"]
                    for y in range(box_y_heights[nx] + 1, box_y_heights[nx - 1]):
                        plot_box[y][nx] = render_set["vline"]
                else:
                    plot_box[box_y_heights[nx - 1]][nx] = render_set["right_down"]
                    plot_box[box_y_heights[nx]][nx] = render_set["down_right"]

                    for y in range(box_y_heights[nx - 1] + 1, box_y_heights[nx]):
                        plot_box[y][nx] = render_set["vline"]

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
