import math


def is_odd(num):
    return True if num%2!=0 else False

def make_pagination_range(
    page_range,
    qty_pages,
    current_page,
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset
    
    if is_odd(qty_pages):
        stop_range-=1
    
    if stop_range>=total_pages:
        start_range = start_range-abs(total_pages- stop_range)
        

    pagination =  page_range[start_range:stop_range]
    
    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }






if __name__ == "__main__":
    print(make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=5,
            current_page=20,
        )['pagination'])
    
    
   