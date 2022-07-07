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
        'l': 'list all clothes',
        'y': 'clothes for you',
        's': 'clothes for sale',
        'd': 'clothes for donation',
        'b': 'back'
    }
    print_menu(clth_menu_options)
    selected_opt = sel_menu_opt(clth_menu_options)
    return selected_opt

# shows the style menu and returns the option selected by the user
def style_menu():
    style_menu_options = {
        'n': 'create a new style',
        'l': 'list all styles',
        'c': 'list clothes of a style',
        'a': 'add clothes to style',
        'b': 'back'
    }
    print_menu(style_menu_options)
    selected_opt = sel_menu_opt(style_menu_options)
    return selected_opt

# create a new clothing based on user input, return a new clothing
def read_clothing(clth_id):
    clth_type = read_clth_type()
    clth_sex = read_clth_sex()
    clth_size = read_clth_size()
    clth_purchase_date = read_clth_purchase_date()
    clth_color = read_clth_color()
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

# asks the user to select a color and return the selected one
def read_clth_color():
    clth_color = input("Enter the clothing main color: ")
    if clth_color == "":
        print("Invalid color!")
        clth_color = read_clth_color()
    return clth_color

# asks the user to select a purcharse date and return the selected one
def read_clth_purchase_date(): #Explicar para o Enzo 
    try:
        clth_purchase_day = int(input("Enter the purchase day: "))
        clth_purchase_month = int(input("Enter the purchase month: "))
        clth_purchase_year = int(input("Enter the purchase year: "))
        date = (clth_purchase_day, clth_purchase_month, clth_purchase_year)
    except:
        print("Invalid date!")
        date = read_clth_purchase_date()
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
            selected = int(input("Select a clothing Id: "))
            found_id = False
            for clth in clothes:
                if clth['id'] == selected:
                    found_id = True
                    result = clth
                    break
            if not found_id:
                raise Exception("Invalid Id")
        except Exception as err:
            print(f"Error: {err}")
        except:
            print("Invalid input!")
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
def print_clth_sets(clth_sets):
    for i, clothes in enumerate(clth_sets):
        print('-=' * 15)
        print(f"-> Outfit {i+1}")
        print_clothes(clothes)
        print('-=' * 15)

# asks the user to select a valid clothing set, return the selected one
# if is impossible to make a clothing set it returns None
def select_clth_set(clothes):
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
            result = select_clth_set(clothes)
    else:
        print("You can't make any clothing set yet.")
    return result

# creates a new style based on user input
def read_style():
    style_name = input("Enter the style name: ")
    if style_name == "":
        print("Invalid name!")
        style_name = read_style()
    result = style.new_style(style_name)['content']
    return result

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

# read the user input to modify a given clothing list, return the modified list
def update_clothes(clothes = []):
    while(True):
        print("")
        selected_opt = clothing_menu()
        if selected_opt == 'a':
            clothes = add_clothing(clothes)
            print("Added successfully!")
        elif selected_opt == 'l':
            print_clothes(clothes)
        elif selected_opt == 'y':
            interest_clothes = clothing.filter_by_interest(clothes)
            print_clothes(interest_clothes)
        elif selected_opt == 's':
            for_sale = clothing.filter('status', 'sale', clothes)
            print_clothes(for_sale)
        elif selected_opt == 'd':
            for_donation = clothing.filter('status', 'donation', clothes)
            print_clothes(for_donation)
        elif selected_opt == 'b':
            break
    return clothes

# read the user input to modify a given style list, return the modified list
def update_styles(styles = [], clothes = []):
    while(True):
        print("")
        selected_opt = style_menu()
        if selected_opt == 'n':
            style = read_style()
            styles.append(style)
            print(f"Style '{style['name']}' was created!")
        elif selected_opt == 'l':
            print_styles(styles)
        elif selected_opt == 'c':
            style, index = select_style(styles, index=True)
            if not style is None:
                styles[index]['count'] += 1
                print_clth_sets(style['clothes_sets'])
        elif selected_opt == 'a':
            style, index = select_style(styles, index=True)
            # if is not a valid style, show the style menu again
            if style is None:
                continue
            print_clothes(clothes)
            clth_set = select_clth_set(clothes)
            # if is not a valid clothing set, show the style menu again
            if clth_set is None:
                continue
            styles[index]['clothes_sets'].append(clth_set)
            print("Added successfully!")
        elif selected_opt == 'b':
            break
    return styles

# read new clothing from the user and add it to a clothing list
def add_clothing(clothes = []):
    free_id = clothing.request_id(clothes)
    new_clothing = read_clothing(free_id)
    clothes.append(new_clothing)
    return clothes
