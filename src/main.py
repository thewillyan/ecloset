import cli

clothes = []
styles = []

# default clothes for test purposes
clothes = [{'id': 1, 'type': 'upper', 'sex': 'M', 'size': 'P', 'color': 'blue',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0},
          {'id': 2, 'type': 'lower', 'sex': 'M', 'size': 'P', 'color': 'red',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0},
          {'id': 3, 'type': 'footwear', 'sex': 'M', 'size': 'P', 'color': 'black',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0},
          {'id': 4, 'type': 'footwear', 'sex': 'M', 'size': 'P', 'color': 'black',
           'purchase_date': (20, 2, 2022), 'status': 'sale', 'price': 10000},
          {'id': 5, 'type': 'lower', 'sex': 'M', 'size': 'P', 'color': 'red',
           'purchase_date': (20, 2, 2022), 'status': 'sale', 'price': 5000},
          {'id': 6, 'type': 'lower', 'sex': 'F', 'size': 'M', 'color': 'orange',
           'purchase_date': (20, 2, 2022), 'status': 'keep', 'price': 0}]

def main_menu():
    main_menu_options = {
        'c': 'clothing options',
        's': 'style options',
        'q': 'quit'
    }
    cli.print_menu(main_menu_options)
    selected_opt = cli.sel_menu_opt(main_menu_options)
    return selected_opt

while(True):
    print("")
    selected_opt = main_menu()
    if selected_opt == 'c':
        clothes = cli.update_clothes(clothes)
    elif selected_opt == 's':
        style_list = cli.update_styles(styles, clothes)
    elif selected_opt == 'q':
        break

print('')
print('stored clothes:', clothes)
print('')
print('stored styles:', styles)
