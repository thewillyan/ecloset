import clothing 
import style

# shows a menu where a dict key is the option and its value is the description
def print_menu(menu_options):
    for key, value in menu_options.items():
        print(f"[{key}] {value.capitalize()}")

# returns the menu option selected by the user
def sel_menu_opt(menu_options, msg="Select an option: "):
    valid_options = list(menu_options.keys())
    selected_opt = input(msg)
    if not selected_opt in valid_options:
        print("Invalid option!")
        selected_opt = sel_menu_opt(menu_options)
    return selected_opt

# shows the clothing menu and returns the option selected by the user
def clothing_menu():
    clth_menu_options = {
        'a': 'add clothing',
        'e': 'edit clothing',
        'r': 'remove clothing',
        'b': 'back'
    }
    print_menu(clth_menu_options)
    selected_opt = sel_menu_opt(clth_menu_options)
    return selected_opt

# asks the user to select a changeable field from 'clth'
def clothing_fields_menu(clth):
    clothing_fields_options = {
        't': 'type',
        'x': 'sex',
        's': 'size',
        'c': 'color',
        'd': 'purchase date',
        'a': 'status'
    }
    if clth['price'] > 0:
        clothing_fields_options['p'] = 'price'
    print_menu(clothing_fields_options)
    selected_opt = sel_menu_opt(clothing_fields_options)
    return selected_opt

# shows the style menu and returns the option selected by the user
def style_menu():
    style_menu_options = {
        'n': 'create a new style',
        'r': 'rename style',
        'm': 'remove style',
        'a': 'add clothes to style',
        'b': 'back'
    }
    print_menu(style_menu_options)
    selected_opt = sel_menu_opt(style_menu_options)
    return selected_opt

# asks the user to select a changeable field from 'clth_style'
def styles_field_menu(clth_style):
    style_field_options = { 'r': 'rename style' }
    if len( clth_style['clothes_sets'] ) > 0:
        style_field_options['c'] = 'change clothing set'
    print_menu(style_field_options)
    selected_opt = sel_menu_opt(style_field_options)
    return selected_opt

# shows the menu and returns the option selected by the user
def select_clth_menu():
    select_menu_options = {
        'c': 'select clothing',
        's': 'select by style',
        'b': 'back'
    }
    print_menu(select_menu_options)
    selected_opt = sel_menu_opt(select_menu_options)
    return selected_opt

# shows the conifirm menu and returns the option selected by the user
def confirm_menu():
    confirm_menu_options = {
        'y': 'yes',
        'n': 'no'
    }
    print("Are you sure of your choice?")
    print_menu(confirm_menu_options)
    selected_opt = sel_menu_opt(confirm_menu_options)
    return selected_opt

# create a new clothing based on user input, return a new clothing
def read_clothing(clth_id):
    clth_type = read_clth_type()
    clth_sex = read_clth_sex()
    clth_size = read_clth_size()
    clth_purchase_date = read_date("Date of purchase.")
    clth_color = read_not_empty('Enter the clothing main color', 'color')
    clth_status = read_clth_status()

    if clth_status == 'sale':
        clth_price = read_clth_price()
    else:
        clth_price = 0

    result = clothing.new_clothing(
        clth_id            = clth_id,           clth_type   = clth_type,
        clth_size          = clth_size,         clth_status = clth_status,
        clth_purchase_date = clth_purchase_date,
        clth_color         = clth_color,        clth_price  = clth_price,
        clth_sex           = clth_sex)

    if not result['is_valid']:
        print('here')
        print("Error: ", result['err'])
        result = read_clothing(clth_id)
    else:
        result = result['content']
    return result

# asks the user to select a type and return the selected one
def read_clth_type():
    clth_type_menu = { 
        'u': "upper",
        'l': "lower",
        'f': "footwear"
    }
    print_menu(clth_type_menu)
    selected_opt = sel_menu_opt(clth_type_menu)
    clth_type = clth_type_menu[selected_opt]
    return clth_type

# asks the user to select a sex and return the selected one
def read_clth_sex():
    clth_sex_menu = {
        'm': "male",
        'f': "female",
        'u': "unisex"
    }
    print_menu(clth_sex_menu)
    selected_opt = sel_menu_opt(clth_sex_menu)
    clth_sex = selected_opt.upper()
    return clth_sex

# asks the user to select a size and return the selected one
def read_clth_size():
    clth_size_menu = {
        'p': "p size",
        'm': "m size",
        'g': "g size"
    }
    print_menu(clth_size_menu)
    selected_opt = sel_menu_opt(clth_size_menu)
    clth_size = selected_opt.upper()
    return clth_size

# asks the user to enter a string and returns a non-empty string
def read_not_empty(msg, field='input'):
    result = input(f"{msg}: ")
    if result == "":
        print(f"Invalid {field}!")
        result = read_not_empty(msg, field)
    return result

# asks the user to select a purcharse date and return the selected one
def read_date(msg=""):
    if msg != "":
        print(msg)
    try:
        day = int(input("Enter the day: "))
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        date = (day, month, year)
        check_result = clothing.check_date(date)
        if not check_result['is_valid']:
            raise Exception(check_result['err'])
    except:
        print("Invalid date!")
        date = read_date()
    return date

# asks the user to select a status and return the selected one
def read_clth_status():
    clth_status_menu = {
        'd': "donation",
        's': "sale",
        'k': "keep"
    }
    print_menu(clth_status_menu)
    selected_opt = sel_menu_opt(clth_status_menu)
    clth_status = clth_status_menu[selected_opt]
    return clth_status

# asks the user to select a price and return the selected one
def read_clth_price():
    try:
        clth_price = float(input("Enter selling price: "))
        # convert to cents
        clth_price = int(round(clth_price, 2) * 100)
        if clth_price == 0:
            raise Exception("The price of a clothing for sale cannot be 0")
        return clth_price
    except:
        print("Invalid price!")
        clth_price = read_clth_price()
    return clth_price

# asks the user to choose one of the 'clothes' and returns the selected one.
def select_clth(clothes):
    result = None
    if len(clothes) == 0:
        print("Error: No clothes to choose from")
    else:
        try:
            found_id = False
            selected = int(input("Select a clothing Id: "))
            for clth in clothes:
                if clth['id'] == selected:
                    found_id = True
                    result = clth
                    break
            if not found_id:
                raise Exception("Not found")
        except:
            print("Invalid Id!")
            result = select_clth(clothes)
    return result

# prints all clothes from 'clothes'
def print_clothes(clothes):
    for clth in clothes:
        print("-" * 30)
        print_clothing(clth)
        print("-" * 30)

# prints a clothing
def print_clothing(clth):
    for key,value in clth.items():
        clth_field = str(key).capitalize()
        clth_data = str(value).capitalize()
        if key == 'sex':
            if value == "M":
                clth_data = "Male"
            elif value == "F":
                clth_data = "Female"
            elif value == "U":
                clth_data = "Unisex"
        elif key == 'purchase_date':
            clth_field = "Purchase date"
            clth_data = f"{value[0]:02d}/{value[1]:02d}/{value[2]:04d}"
        elif key == 'resolved_date':
            if 'price' in clth.keys():
                clth_field = "Sale date"
            else:
                clth_field = "Donation date"
            clth_data = f"{value[0]:02d}/{value[1]:02d}/{value[2]:04d}"
        elif key == 'status':
            clth_data = f"For {value}"
        elif key == 'price':
            if value > 0:
                clth_data = f"${float(value/100):.2f}"
            else:
                continue
        print(f"{clth_field}: {clth_data}")

# prints a style
def print_style(style):
    for key,value in style.items():
        style_field = str(key).capitalize()
        style_data = str(value).capitalize()
        if key == 'clothes_sets':
            style_field = "Clothes sets"
            style_data = len(value)
        print(f"{style_field}: {style_data}")

# prints all styles from 'styles'
def print_styles(styles):
    for style in styles:
        print('-' * 30)
        print_style(style)
        print('-' * 30)

# prints all clothes_sets from 'clth_sets'
def print_clth_sets(clth_sets, clothes):
    clothes_matrix = []
    for clth_set in clth_sets:
        line = style.to_clothes(clth_set, clothes)
        clothes_matrix.append(line)

    for i, clothes in enumerate(clothes_matrix):
        print('-=' * 15)
        print(f"-> Outfit {i+1}")
        print_clothes(clothes)
        print('-=' * 15)

# asks the user to select a valid clothing set, return the selected one
# if is impossible to make a clothing set it returns None
def read_clth_set(clothes):
    result = None
    if style.can_make_set(clothes):
        selected_clothes = []
        for i in range(3):
            print(f"Enter the {i+1}° clothing.")
            selected = select_clth(clothes)
            selected_clothes.append(selected)
        clth_set = style.new_clth_set(*selected_clothes)
        if clth_set['is_valid']:
            result = clth_set['content']
        else:
            print("")
            print(f"Error: {clth_set['err']}")
            result = read_clth_set(clothes)
    else:
        print("You can't make any clothing set yet.")
    return result

# creates a new style based on user input
def read_style():
    style_name = read_not_empty("Enter the style name", 'name')
    result = style.new_style(style_name,[])
    return result['content']

# ask for the user to select one of the given styles, return the selected one
# if index=True it returns a dict with the selected one and its index
def select_style(styles, index=False):
    if len(styles) == 0:
        print("You have no style stored.")
        if index:
            return None, None
        else:
            return None
    else:
        # make a style menu where a number is the option and the value
        # is the style name
        styles_menu = {}
        for i in range( len(styles) ): 
            key = str(i+1)
            value = styles[i]['name']
            styles_menu[key] = value

        print_menu(styles_menu)
        selected_opt = sel_menu_opt(styles_menu, "Select a style: ")
        selected_index = int(selected_opt) - 1
        selected = styles[selected_index]
        if index:
            return selected, selected_index
        else:
            return selected

# asks the user to select a clothing set in 'clth_sets' and returns the 
# selcted one
def select_clth_set(clth_sets):
    result = None
    if len(clth_sets) == 0:
        print("No clothing set to choose!")
    else:
        try:
            index = int(input("Select a outfit number: ")) - 1
            result = clth_sets[index]
            return result
        except:
            print("Invalid outfit number!")
            result = select_clth_set(clth_sets)
    return result

# asks the user to select a field and change that field in 'clth', returns the
# changed clothing
def update_clothing(clth, clothes):
    field = clothing_fields_menu(clth)
    if field == 't':
        clth['type'] = read_clth_type()
    elif field == 'x':
        clth['sex'] = read_clth_sex()
    elif field == 's':
        clth['size'] = read_clth_size()
    elif field == 'c':
        clth['color'] = read_not_empty('Enter the clothing main color','color')
    elif field == 'd':
        clth['purchase_date'] = read_date("Date of purchase.")
    elif field == 'a':
        clth['status'] = read_clth_status()
        if clth['status'] == 'sale':
            clth['price'] = read_clth_price()
    elif field == 'p':
        clth['price'] = read_clth_price()
    return clth

# read the user input to modify a given clothing list, return the modified list
def update_clothes(clothes, styles):
    while(True):
        print("")
        selected_opt = clothing_menu()
        # add clothing
        if selected_opt == 'a':
            clothes = add_clothing(clothes)
            print("Added successfully!")
        # edit clothing
        elif selected_opt == 'e':
            print_clothes(clothes)
            clth = select_clth(clothes)
            if clth is None:
                continue
            index = clothes.index(clth)
            clothes[index] = update_clothing(clth, clothes)
        # remove clothing
        elif selected_opt == 'r':
            print_clothes(clothes)
            clth = select_clth(clothes)
            if clth is None:
                continue
            styles, clothes = style.remove_clth(clth, styles, clothes)
            clothes.remove(clth)
            print(f"Clothing {clth['id']} was removed!")
        # back
        elif selected_opt == 'b':
            break
    return clothes, styles

# read the user input to modify a given style list, return the modified list
def update_styles(styles = [], clothes = []):
    while(True):
        print("")
        selected_opt = style_menu()
        # new style
        if selected_opt == 'n':
            clth_style = read_style()
            styles.append(clth_style)
            print(f"Style '{clth_style['name']}' was created!")
        # rename style
        elif selected_opt == 'r':
            clth_style, index = select_style(styles, index=True)
            style_name = read_not_empty("Enter the style name", 'name')
            styles[index], clothes = style.rename(clth_style, style_name,
                                                  clothes)
            print(f"Renamed to '{style_name}'.")
        # remove style
        elif selected_opt == 'm':
            clth_style, index = select_style(styles, index=True)
            styles.remove(clth_style)
            clothes = clothing.remove_style(clth_style, clothes)
            print(f"Style '{clth_style['name']}' was removed!")
        # add clothing set to style
        elif selected_opt == 'a':
            clth_style, index = select_style(styles, index=True)
            # if is not a valid style, show the style menu again
            if clth_style is None:
                continue
            style_name = clth_style['name']
            print_clothes(clothes)
            clth_set = read_clth_set(clothes)
            # if is not a valid clothing set, show the style menu again
            if clth_set is None:
                continue
            elif clth_set in styles[index]['clothes_sets']:
                print(f"This outfit is already in {style_name}.")
                continue
            styles[index]['clothes_sets'].append(clth_set)
            styles[index]['count'] += 1
            for clth in style.to_clothes(clth_set, clothes):
                if style_name in clth['styles']:
                    continue
                i = clothes.index(clth)
                clothes[i]['styles'].append(style_name)
            print("Added successfully!")
        # back
        elif selected_opt == 'b':
            break
    return styles, clothes

# sell 'clth' based on user input, returns the clothes and sold list
def sell_clth(clth, clothes, sold_clothes):
    clth_id = clothing.request_id(sold_clothes)
    sold_date = read_date("Date of sale.")
    buyer = read_not_empty("Enter the buyer name", 'name')
    sold_clth = clothing.sell(clth, clth_id, sold_date, buyer)
    sold_clothes.append(sold_clth)
    clothes.remove(clth)
    print(f"Clothing {clth['id']} was successfully selled!")
    return clothes, sold_clothes

# read the user input to modify the sold_clothes, changing clothes and styles
# list as a side effect, returns clothes, sold clothes and styles lists
def update_sold(clothes, sold_clothes, styles):
    while(True):
        print("")
        selected_opt = select_clth_menu()
        if selected_opt == 'c':
            for_sale = clothing.filter('status', 'sale', clothes)
            print_clothes(for_sale)
            clth = select_clth(for_sale)
            styles, clothes = style.remove_clth(clth, styles, clothes)
            clothes, sold_clothes = sell_clth(clth , clothes, sold_clothes)
        elif selected_opt == 's':
            clth_style, index = select_style(styles, index=True)
            if clth_style is None:
                continue
            clth_sets = clth_style['clothes_sets']
            print_clth_sets(clth_sets, clothes)
            confirm = confirm_menu()
            if confirm == 'n':
                continue
            clth_set = select_clth_set(clth_sets)
            if clth_set is None:
                continue
            clths = style.to_clothes(clth_set, clothes)
            for_sale = clothing.filter('status', 'sale', clths)
            print_clothes(for_sale)
            clth = select_clth(for_sale)
            if clth is None:
                continue
            styles, clothes = style.remove_clth(clth, styles, clothes)
            clothes, sold_clothes = sell_clth(clth, clothes, sold_clothes)
            styles[index]['count'] += 1
        elif selected_opt == 'b':
            break
    return clothes, sold_clothes, styles

# sell 'clth' based on user input, returns the clothes and sold list
def donate_clth(clth, clothes, donated_clothes):
    clth_id = clothing.request_id(donated_clothes)
    donation_date = read_date("Date of donation.")
    agent = read_not_empty("Enter the donation target", 'target')
    donated_clth = clothing.donate(clth, clth_id, donation_date, agent)
    donated_clothes.append(donated_clth)
    clothes.remove(clth)
    print(f"Clothing {clth['id']} was successfully donated!")
    return clothes, donated_clothes

# read the user input to modify the donated_clothes, changing clothes and styles
# list as a side effect, returns clothes, donated clothes and styles lists
def update_donated(clothes, donated_clths, styles):
    while(True):
        print("")
        selected_opt = select_clth_menu()
        if selected_opt == 'c':
            for_donation = clothing.filter('status', 'donation', clothes)
            print_clothes(for_donation)
            clth = select_clth(for_donation)
            styles, clothes = style.remove_clth(clth, styles, clothes)
            clothes, donated_clths = donate_clth(clth, clothes, donated_clths)
        elif selected_opt == 's':
            clth_style, index = select_style(styles, index=True)
            if clth_style is None:
                continue
            clth_sets = clth_style['clothes_sets']
            print_clth_sets(clth_sets, clothes)
            confirm = confirm_menu()
            if confirm == 'n':
                continue
            clth_set = select_clth_set(clth_sets)
            if clth_set is None:
                continue
            clths = style.to_clothes(clth_set, clothes)
            for_donation = clothing.filter('status', 'donation', clths)
            print_clothes(for_donation)
            clth = select_clth(for_donation)
            if clth is None:
                continue
            styles, clothes = style.remove_clth(clth, styles, clothes)
            clothes, donated_clths = donate_clth(clth, clothes, donated_clths)
            styles[index]['count'] += 1
        elif selected_opt == 'b':
            break
    return clothes, donated_clths, styles

# read new clothing from the user and add it to a clothing list
def add_clothing(clothes = []):
    free_id = clothing.request_id(clothes)
    new_clothing = read_clothing(free_id)
    clothes.append(new_clothing)
    return clothes
