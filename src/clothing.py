# try to create a valid clothing and returns a dict with 
# is_valid and content (if is_valid is True) or
# is_valid and error (if is_valid is False)
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
        'price': clth_price,
        'styles': []
    }
    result = { 'is_valid': True, 'content': clothing }

    for key, value in clothing.items():
        check_result = check_field(value, key)
        if not check_result['is_valid']:
            result = check_result
            break
    return result

# verify if 'value' is valid for the 'field' and returns a dict with
# is_valid and arror (if any)
def check_field(value, field):
    result = { 'is_valid': False, 'err': f"'{field}' is not a Clothing key."}
    if field == 'id':
        result = check_id(value)
    elif field == 'type':
        result = check_type(value)
    elif field == 'sex':
        result = check_sex(value)
    elif field == 'size':
        result = check_size(value)
    elif field == 'color' or field == 'agent':
        result = check_not_empty(value, field)
    elif field == 'purchase_date' or field == 'resolved_date':
        result = check_date(value)
    elif field == 'status':
        result = check_status(value)
    elif field == 'price':
        result = check_price(value)
    elif field == 'styles':
        result = check_styles(value)
    return result

def check_id(value):
    is_valid_value = True
    err_msg = ""
    if not type(value) is int:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid id, it must be a integer."
    elif value <= 0:
        is_valid_value = False
        err_msg = 'The id must be greater than zero.'
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_type(value):
    is_valid_value = True
    err_msg = ""
    if value != 'upper' and value != 'lower' and value != 'footwear':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid type."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_sex(value):
    is_valid_value = True
    err_msg = ""
    if value != 'M' and value != 'F' and value != 'U':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid sex."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_size(value):
    is_valid_value = True
    err_msg = ""
    if value != 'P' and value != 'M' and value != 'G':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid size."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_not_empty(value, field):
    is_valid_value = True
    err_msg = ''
    if not type(value) is str:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid {field}, it must be a string."
    elif value == '':
        is_valid_value = False
        err_msg = f"Empty {field}."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_date(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is tuple:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid {field}, it must be a tuple."
    if (not type(value[0]) is int or not type(value[1]) is int or
        not type(value[2]) is int):
        is_valid_value = False
        err_msg = 'Date elements must be integers.'
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

def check_status(value):
    is_valid_value = True
    err_msg = ''
    if value != 'sale' and value != 'donation' and value != 'keep':
        is_valid_value = False
        err_msg = f"'{value}' is not a valid status."
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_price(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is int:
        is_valid_value = False
        err_msg = f"'{value}' is not a valid price, it must be a integer."
    elif value < 0:
        is_valid_value = False
        err_msg = 'The price must be a not negative number.'
    return { 'is_valid': is_valid_value, 'err': err_msg }

def check_styles(value):
    is_valid_value = True
    err_msg = ''
    if not type(value) is list:
        is_valid_value = Fase
        err_msg = 'styles must be a list.'
    return { 'is_valid': is_valid_value, 'err': err_msg }

# return a new valid clothing id
def request_id(clothes):
    free_id = 1
    while(True):
        same_id = filter('id', free_id, clothes)
        if len(same_id) == 0:
            break
        free_id += 1
    return free_id

# returns list of clothes where the 'field' matches the 'value'
def filter(field, value, clothes):
    result = []
    for clth in clothes:
        if clth[field] == value:
            result.append(clth)
    return result

# returns the compatibility score between 'clth1' and 'clth2'
def match_score(clth1, clth2):
    comparison_keys = ['type', 'sex', 'size', 'color']
    score = 0
    for key in comparison_keys:
        if clth1[key] == clth2[key]:
            score += 1
    return score

# returns a clothing with the most common attributes of 'clothes'
def ideal(clothes):
    result = {}
    for key in clothes[0].keys():
        if key != 'styles':
            result[key] = common_value(clothes, key)
    return result

# returns the most common value of 'key' in 'clothes'
def common_value(clothes, key):
    value_tree = {}
    for clth in clothes:
        value = clth[key]
        if value in value_tree:
            value_tree[value] += 1
        else:
            value_tree[value] = 1

    result = clothes[0][key]
    for key, value in value_tree.items():
        if value > value_tree[result]:
            result = key
    return result

# sort 'clothes' by che compatibility with 'comp_clth'
def sort_by_score(clothes, comp_clth):
    scores = []
    for i in range( len(clothes) ):
        score = match_score(clothes[i], comp_clth)
        scores.append([score, i])
    scores.sort(reverse=True)

    result = []
    for score in scores:
        clth = clothes[score[1]]
        result.append(clth)
    return result

# filter 'clothes' by the user interest
def filter_by_interest(clothes):
    ideal_clth = ideal(clothes)
    result = sort_by_score(clothes, ideal_clth)
    return result

# try to create a valid sold clothing and returns a dict with 
# is_valid and content (if is_valid is True) or
# is_valid and error (if is_valid is False)
def new_sold_clth(
    clth_id, clth_type, clth_sex, clth_size, clth_color,
    clth_sold_date, clth_price, clth_buyer
):
    clothing = {
        'id': clth_id,
        'type': clth_type,
        'sex': clth_sex,
        'size': clth_size,
        'color': clth_color,
        'resolved_date': clth_sold_date,
        'price': clth_price,
        'agent': clth_buyer
    }
    result = { 'is_valid': True, 'content': clothing }

    for key, value in clothing.items():
        check_result = check_field(value, key)
        if not check_result['is_valid']:
            result = check_result
            break
    return result

# transform 'clth' in a sold clothing, returns a sold clothing
def sell(clth, clth_id, sold_date, buyer):
    result = new_sold_clth( clth_id, clth['type'], clth['sex'], clth['size'],
                            clth['color'], sold_date, clth['price'], buyer )
    if clth['status'] != 'sale':
        raise Exception("Can't sell a clothing that is not for sale")
    elif not result['is_valid']:
        raise Exception(f"Error: {result['err']}")
    return result['content']


# try to create a valid donated clothing and returns a dict with 
# is_valid and content (if is_valid is True) or
# is_valid and error (if is_valid is False)
def new_donated_clth(
    clth_id, clth_type, clth_sex, clth_size, clth_color,
    clth_sold_date, clth_agent
):
    clothing = {
        'id': clth_id,
        'type': clth_type,
        'sex': clth_sex,
        'size': clth_size,
        'color': clth_color,
        'resolved_date': clth_sold_date,
        'agent': clth_agent
    }
    result = { 'is_valid': True, 'content': clothing }

    for key, value in clothing.items():
        check_result = check_field(value, key)
        if not check_result['is_valid']:
            result = check_result
            break
    return result

# transform 'clth' in a donated clothing, returns a donated clothing
def donate(clth, clth_id, donation_date, agent):
    result = new_donated_clth( clth_id, clth['type'], clth['sex'], clth['size'],
                            clth['color'], donation_date, agent )
    if clth['status'] != 'donation':
        raise Exception("Can't donate a clothing that is not for donation")
    elif not result['is_valid']:
        raise Exception(f"Error: {result['err']}")
    return result['content']

# remove a style from all the 'clothes', returns the modified clothes list
def remove_style(style, clothes):
    for i in range( len(clothes) ):
        styles = clothes[i]['styles'].copy()
        if style['name'] in styles:
            styles.remove(style['name'])
        clothes[i]['styles'] = styles
    return clothes
