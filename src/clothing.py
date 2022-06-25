# try to create a valid clothing and returns a dict with this information
def new_clothing(
    clth_id, clth_type, clth_sex, clth_size, clth_color,
    clth_purchase_date, clth_status, clth_price = 0
):
    clothing = {
        'id': clth_id,
        'type': clth_type,
        'sex': clth_sex,
        'size': clth_size,
        'color': clth_color,
        'purchase_date': clth_purchase_date,
        'status': clth_status,
        'price': clth_price
    }
    result = { 'is_valid': True, 'content': clothing }

    for key, value in clothing.items():
        check_result = check_clth_field(value, key)
        if not check_result['is_valid']:
            result = check_result
    return result

# verify if 'value' is valid for the 'field' and returns a dict with this
# information
def check_clth_field(value, field):
    result = { 'is_valid': False, 'err': f"'{field}' is not a Clothing key."}
    if field == 'id':
        result = check_clth_id(value)
    elif field == 'type':
        result = check_clth_type(value)
    elif field == 'sex':
        result = check_clth_sex(value)
    elif field == 'size':
        result = check_clth_size(value)
    elif field == 'color':
        result = check_clth_color(value)
    elif field == 'purchase_date':
        result = check_clth_purchase_date(value)
    elif field == 'status':
        result = check_clth_status(value)
    elif field == 'price':
        result = check_clth_price(value)
    return result

def check_clth_id(value):
    is_valid_value = True
    err_msg = ""
    if not type(value) is int:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid id, it must be a integer."
    elif value <= 0:
        is_valid_value = False
        err_msg = 'The id must be greater than zero.'
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_type(value):
    is_valid_value = True
    err_msg = ""
    if value != 'upper' and value != 'lower' and value != 'footwear':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid type."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_sex(value):
    is_valid_value = True
    err_msg = ""
    if value != 'M' and value != 'F' and value != 'U':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid sex."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_size(value):
    is_valid_value = True
    err_msg = ""
    if value != 'P' and value != 'M' and value != 'G':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid size."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_color(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is str:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid color, it must be a string."
    elif value == '':
        is_valid_value = False
        err_msg = 'Empty color.'
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_purchase_date(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is tuple:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid {field}, it must be a tuple."
    if (not type(value[0]) is int or not type(value[1]) is int or
        not type(value[2]) is int):
        is_valid_value = False
        err_msg = 'The purchase_date elements must be integers.'
    elif value[0] < 1 or value[0] > 31:
        is_valid_value = False
        err_msg = f"'{value[0]}' is not a valid day."
    elif value[1] < 1 or value[1] > 12:
        is_valid_value = False
        err_msg = f"'{value[1]}' is not a valid month."
    elif value[2] < 1:
        is_valid_value = False
        err_msg = f"'{value[2]}' is not a valid year."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_status(value):
    is_valid_value = True
    err_msg = ''
    if value != 'sale' and value != 'donation' and value != 'keep':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid status."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_clth_price(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is int:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid price, it must be a integer."
    elif value < 0:
        is_valid_value = False
        err_msg = 'The price must be a not negative number.'
    return { 'is_valid': is_valid_value, 'err': err_msg }
