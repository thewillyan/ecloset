# try to create a valid style and returns a dict with 
# is_valid and content (if is_valid is True) or
# is_valid and error (if is_valid is False)
def new_style(style_name, clothes_sets):
    style = {
        'name': style_name,
        'count': 0,
        'clothes_sets': clothes_sets
    }
    result = {
        'is_valid': True,
        'content': style
    }

    if len(clothes_sets) > 0:
        for clothes_set in clothes_sets:
            check_result = check_clothes_set(clothes_set)
            if not check_result['is_valid']:
                result = check_result
    return result

# try to create a valid clothing set and returns a dict with 
# is_valid and content (if is_valid is True) or
# is_valid and error (if is_valid is False)
def new_clth_set(clth1, clth2, clth3):
    clth_set = [ clth1, clth2, clth3 ]
    if can_make_set(clth_set):
        # put clothes in order
        for clth in clth_set.copy():
            if clth['type'] == 'upper':
                clth_set[0] = clth
            elif clth['type'] == 'lower':
                clth_set[1] = clth
            elif clth['type'] == 'footwear':
                clth_set[2] = clth

    result = {
        'is_valid': True,
        'content': clth_set
    }

    check_result = check_clothes_set(clth_set)
    if not check_result['is_valid']:
        result = check_result
    return result

# verify if 'clothes' is a valid clothing set and returns a dict with
# is_valid and arror (if any)
def check_clothes_set(clothes):
    is_valid = True
    err_msg = ""
    try:
        if not type(clothes) is list:
            raise Exception("A clothes set must be a list")
        elif len(clothes) != 3:
            raise Exception("A clothes set must have 3 elements")

        if clothes[0]['type'] != 'upper':
            raise Exception("The first element of a clothes set must be a" \
                            " 'upper' clothing")
        elif clothes[1]['type'] != 'lower':
            raise Exception("The second element of a clothes set must be a" \
                            " 'lower' clothing")
        elif clothes[2]['type'] != 'footwear':
            raise Exception("The third element of a clothes set must be a" \
                            " 'footwear' clothing")
    except Exception as err:
        is_valid = False
        err_msg = str(err)

    return { 'is_valid': is_valid, 'err': err_msg }

# check if it is possible to make at least 1 'clothes set' with the available
# 'clothes'.
def can_make_set(clothes):
    result = False
    count_upper = count_lower = count_footwear = 0
    for clth in clothes:
        if clth['type'] == 'upper':
            count_upper += 1
        elif clth['type'] == 'lower':
            count_lower += 1
        elif clth['type'] == 'footwear':
            count_footwear += 1

        if count_upper >= 1 and count_lower >= 1 and count_footwear >= 1:
            result = True
            break
    return result

# returns a list with all styles where 'clth' appears
def get_styles(clth, styles):
    result = []
    for style in styles:
        for clth_set in style['clothes_sets']:
            if clth in clth_set:
                result.append(style['name'])
                break
    return result

# retuns a style where all clothing sets where 'clth' appears are removed
def remove_clth(clth, styles):
    for i in range( len(styles) ):
        style = styles[i]
        new_clth_sets = style['clothes_sets'].copy()
        for clth_set in style['clothes_sets']:
            if clth in clth_set:
                new_clth_sets.remove(clth_set)
        styles[i]['clothes_sets'] = new_clth_sets
    return styles
