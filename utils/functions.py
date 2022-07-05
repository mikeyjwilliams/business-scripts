

def get_title(data):
    '''
    Function: get_title(data) -> string
    Description: find product title from data
        use string method to clean product title from
        data. find index of |, use substring method to
        find end of product title from data. Then strip
        any white spaces from new_title and return string.
    '''
    title = data.find('span', id='productTitle')
    clean_title = title.string
    end_title_at = clean_title.index('│')
    new_title = title[:end_title_at]
    return new_title.strip()


def get_price(data):
    '''
    function: get_price(data) -> float
    Description: find price and returns
        the product price as a float value without the
        dollar sign and stripped of any white spaces.
    '''
    whole_num = data.find('span', class_='a-offscreen')
    clean_number = whole_num.string
    whole_number = clean_number.replace('$', '').strip()
    return whole_number


def get_item_type(data):
    item_type = data.find('span', class_='selection')
    clean_item_type = item_type.string
    return clean_item_type.strip()


def get_count_price(data):
    span = data.find('span', class_='a-text-price')
    dirty_price = span.find('span', class_='a-offscreen')
    clean_price = dirty_price.string
    return clean_price.replace('$', '').strip()
