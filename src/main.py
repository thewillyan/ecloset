import cli
import clothing

clothes = []
sold_clothes = []
donated_clothes = []
styles = []

# default clothes for test purposes
clothes = [{'id': 1, 'type': 'upper', 'sex': 'M', 'size': 'P', 'color': 'blue',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0,
            'styles': []},
          {'id': 2, 'type': 'lower', 'sex': 'M', 'size': 'P', 'color': 'red',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0,
            'styles': []},
          {'id': 3, 'type': 'footwear', 'sex': 'M', 'size': 'P', 'color': 'black',
           'purchase_date': (20, 2, 2022), 'status': 'donation', 'price': 0,
            'styles': []},
          {'id': 4, 'type': 'footwear', 'sex': 'M', 'size': 'P', 'color': 'black',
           'purchase_date': (20, 2, 2022), 'status': 'sale', 'price': 10000,
            'styles': []},
          {'id': 5, 'type': 'lower', 'sex': 'M', 'size': 'P', 'color': 'red',
           'purchase_date': (20, 2, 2022), 'status': 'sale', 'price': 5000,
            'styles': []},
          {'id': 6, 'type': 'lower', 'sex': 'F', 'size': 'M', 'color': 'orange',
           'purchase_date': (20, 2, 2022), 'status': 'keep', 'price': 0,
            'styles': []}]

def main_menu():
    main_menu_options = {
        'c': 'clothing options',
        's': 'style options',
        'e': 'sell a clothing',
        'd': 'donate a clothing',
        'l': 'list',
        'q': 'quit'
    }
    cli.print_menu(main_menu_options)
    selected_opt = cli.sel_menu_opt(main_menu_options)
    return selected_opt

def list_menu():
    list_menu_options = {
        'a': 'all clothes',
        'y': 'clothes for you',
        's': 'sold clothes',
        'd': 'donated clothes',
        't': 'styles',
        'c': 'list clothes of a style'
    }
    cli.print_menu(list_menu_options)
    selected_opt = cli.sel_menu_opt(list_menu_options)
    return selected_opt

while(True):
    print("")
    selected_opt = main_menu()
    # modify clothes (and styles as a side effect)
    if selected_opt == 'c':
        clothes, styles = cli.update_clothes(clothes, styles)
    # modify styles (and clothes as a side effect)
    elif selected_opt == 's':
        styles, clothes = cli.update_styles(styles, clothes)
    # modify sold clothes (and clothes and styles as a s.e)
    elif selected_opt == 'e':
        clothes, sold_clothes, styles = cli.update_sold(clothes, sold_clothes,
                                                        styles)
    # modify donated clothes (and clothes and styles as a s.e)
    elif selected_opt == 'd':
        clothes, donated_clothes, styles = cli.update_donated(clothes, donated_clothes,
                                                              styles)
    # listing options
    elif selected_opt == 'l':
        opt = list_menu()
        # list all clothes
        if opt == 'a':
            cli.print_clothes(clothes)
        # list clothes by user interest
        elif opt == 'y':
            interest_clothes = clothing.filter_by_interest(clothes)
            cli.print_clothes(interest_clothes)
        # list sold clothes
        elif opt == 's':
            cli.print_clothes(sold_clothes)
        # list donated clothes
        elif opt == 'd':
            cli.print_clothes(donated_clothes)
        # list styles
        elif opt == 't':
            cli.print_styles(styles)
        # list clothes of a certain style
        elif opt == 'c':
            clth_style, index = cli.select_style(styles, index=True)
            if not clth_style is None:
                cli.print_clth_sets(clth_style['clothes_sets'], clothes)
    # quit
    elif selected_opt == 'q':
        break

print('')
print('stored clothes:', clothes)
print('')
print('sold clothes:', sold_clothes)
print('')
print('donated clothes:', donated_clothes)
print('')
print('stored styles:', styles)
