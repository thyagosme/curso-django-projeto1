import math

from django.core.paginator import Paginator


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


def make_pagination(request, queryset, per_page, qty_pages= 4):
       
    try:
        current_page = int(request.GET.get('page',1))
    except ValueError:
        current_page = 1
    paginator =  Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)
    try:
        page_range = list(paginator.page_range)
    except ValueError:
        page_range = list(range(1,qty_pages+1))
        
    pagination_range = make_pagination_range(
        page_range = page_range , 
        qty_pages = qty_pages, 
        current_page = current_page,)

    return page_obj, pagination_range

if __name__ == "__main__":
    print(make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=5,
            current_page=20,
        )['pagination'])
    
    
   