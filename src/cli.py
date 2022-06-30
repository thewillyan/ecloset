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

def clothing_menu():
    clth_menu_options = {
        'a': 'add clothing',
        'l': 'list all clothes',
        'b': 'back'
    }
    print_menu(clth_menu_options)
    selected_opt = sel_menu_opt(clth_menu_options)
    return selected_opt

def style_menu():
    style_menu_options = {
        'n': 'create a new style',
        'a': 'add clothes to style',
        'b': 'back'
    }
    print_menu(style_menu_options)
    selected_opt = sel_menu_opt(style_menu_options)
    return selected_opt

# create a new clothing based on user input
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

def read_clth_color():
    clth_color = input("Enter the clothing main color: ")
    if clth_color == "":
        print("Invalid color!")
        clth_color = read_clth_color()
    return clth_color

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

def print_clothes(clothes):
    for clth in clothes:
        print("-" * 30)
        print_clothing(clth)
        print("-" * 30)

def print_clothing(clth):
    for key,value in clth.items():
        if key == 'sex':
            if value == "M":
                sex = "Male"
            elif value == "F":
                sex = "Female"
            elif value == "U":
                sex = "Unisex"
            print(f"Sex: {sex}")
        elif key == 'purchase_date':
            formated_date = f"{value[0]:02d}/{value[1]:02d}/{value[2]:04d}"
            print(f"Purchase date: {formated_date}")
        elif key == 'status':
            print(f"Status: For {value}")
        elif key == 'price':
            if value > 0:
                print(f"Price: ${float(value/100):.2f}")
        else:
            clth_field = str(key).capitalize()
            clth_data = str(value).capitalize()
            print(f"{clth_field}: {clth_data}")

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

def read_style():
    style_name = input("Enter the style name: ")
    if style_name == "":
        print("Invalid name!")
        style_name = read_style()
    result = style.new_style(style_name)['content']
    return result

def select_style(styles, index=False):
    if len(styles) == 0:
        print("You have no style stored.")
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
            return { 'index': selected_index, 'style': selected }
        else:
            return selected

def update_clothes(clothes = []):
    while(True):
        print("")
        selected_opt = clothing_menu()
        if selected_opt == 'a':
            clothes = add_clothing(clothes)
            print("Added successfully!")
        elif selected_opt == 'l':
            print_clothes(clothes)
        elif selected_opt == 'b':
            break
    return clothes

def update_styles(styles = [], clothes = []):
    while(True):
        print("")
        selected_opt = style_menu()
        if selected_opt == 'n':
            style = read_style()
            styles.append(style)
            print(f"Style '{style['name']}' was created!")
        elif selected_opt == 'a':
            style = select_style(styles, index=True)
            # if is not a valid style, show the style menu again
            if style is None:
                continue
            print_clothes(clothes)
            clth_set = select_clth_set(clothes)
            # if is not a valid clothing set, show the style menu again
            if clth_set is None:
                continue
            index = style['index']
            styles[index]['clothes_sets'].append(clth_set)
            print("Added successfully!")
        elif selected_opt == 'b':
            break
    return styles

def add_clothing(clothes = []):
    free_id = clothing.request_id(clothes)
    new_clothing = read_clothing(free_id)
    clothes.append(new_clothing)
    return clothes
