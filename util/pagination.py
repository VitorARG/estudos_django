
import math


def make_pagination_range(
    pagination_range,
    qty_page,
    current_page,

):
    middle_range = math.ceil(qty_page/2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    return pagination_range[start_range:stop_range]
