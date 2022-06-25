from clothing import new_clothing

# shows a menu where a dict key is the option and its value is the description
def menu(menu_options):
    valid_options = list(menu_options.keys())
    for key, value in menu_options.items():
        print(f"[{key}] {value.capitalize()}")
    while(True):
        selected_option = input("Select an option: ")
        if selected_option in valid_options:
            break
        else:
            print("Invalid option!")
    return selected_option

# create a new clothing based on user input
def read_clothing(clth_id):
    while(True):
        clth_type = read_clth_type()
        clth_sex = read_clth_sex()
        clth_size = read_clth_size()
        clth_status = read_clth_status()
        clth_purchase_date = read_clth_purchase_date()
        clth_color = read_clth_color()

        if clth_status == 'sale':
            clth_price = read_clth_price()
        else:
            clth_price = 0

        result = new_clothing(clth_id = clth_id, clth_type = clth_type,
                              clth_size = clth_size, clth_status = clth_status,
                              clth_purchase_date = clth_purchase_date,
                              clth_color = clth_color, clth_price = clth_price,
                              clth_sex = clth_sex)

        if result['is_valid']:
            return result['content']
        else:
            print("Error: ", result['err'])

def read_clth_type():
    clth_type_menu = { 
        'u': "upper",
        'l': "lower",
        'f': "footwear"
    }
    clth_type = clth_type_menu[menu(clth_type_menu)]
    return clth_type

def read_clth_sex():
    clth_sex_menu = {
        'm': "male",
        'f': "female",
        'u': "unisex"
    }
    clth_sex = menu(clth_sex_menu).upper()
    return clth_sex

def read_clth_size():
    clth_size_menu = {
        'p': "p size",
        'm': "m size",
        'g': "g size"
    }
    clth_size = menu(clth_size_menu).upper()
    return clth_size

def read_clth_color():
    clth_color = input("Enter the clothing main color: ")
    return clth_color

def read_clth_purchase_date():
    while(True):
        try:
            clth_purchase_day = int(input("Enter the purchase day: "))
            clth_purchase_month = int(input("Enter the purchase month: "))
            clth_purchase_year = int(input("Enter the purchase year: "))
            date = (clth_purchase_day, clth_purchase_month, clth_purchase_year)
            return date
        except:
            print("Invalid date!")

def read_clth_status():
    clth_status_menu = {
        'd': "donation",
        's': "sale",
        'k': "keep"
    }
    clth_status = clth_status_menu[menu(clth_status_menu)]
    return clth_status

def read_clth_price():
    while(True):
        try:
            clth_price = float(input("Enter selling price: "))
            # convert to cents
            clth_price = int(round(clth_price, 2) * 100)
            if clth_price == 0:
                raise Exception("The price of a clothing for sale cannot be 0")
            return clth_price
        except:
            print("Invalid price!")
