def float_range(x_value_from, x_value_to, number_of_points):
    """
    Floating point range
    :param x_value_from:
    :param x_value_to:
    :param number_of_points:
    :return: Range in list form
    """
    return [x_value_from + i * (x_value_to - x_value_from) / (number_of_points - 1) for i in range(number_of_points)]
