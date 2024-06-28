
import math


def make_pagination_range(
    pagination_range,
    qty_page,
    current_page,

):
    middle_range = math.ceil(qty_page/2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(pagination_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = pagination_range[start_range:stop_range]
    return {
        'pagination': pagination,
        'page_range': pagination_range,
        'qty_pages': qty_page,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }
