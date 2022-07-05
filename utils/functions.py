

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
    Description: find price and returns price of product.
    '''
    dirty_price = data.find('span', class_='a-offscreen')
    clean_price = dirty_price.string
    price = clean_price.replace('$', '').strip()
    return price


def get_item_type(data):
    '''
    function: get_item_type(data) -> string
    description: find item type and return type
    '''
    item_type = data.find('span', class_='selection')
    clean_item_type = item_type.string
    return clean_item_type.strip()


def get_count_price(data):
    '''
    function: get_count_price(data) -> float
    description: find count and return price of individual
        item price per the whole price.
    '''
    span = data.find('span', class_='a-text-price')
    dirty_price = span.find('span', class_='a-offscreen')
    clean_price = dirty_price.string
    return clean_price.replace('$', '').strip()

#! issue Nonetype has no attribute 'strip'


def check_count(data):
    price_per_unit = data.find('span', class_='pricePerUnit')
    clean_ppu = price_per_unit.string
    return clean_ppu.strip()
