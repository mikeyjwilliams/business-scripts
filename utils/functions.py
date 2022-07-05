

def get_title(title_data):
    end_title_at = title_data.index('│')
    new_title = title_data[:end_title_at]
    return new_title.strip()
