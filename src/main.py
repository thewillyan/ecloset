import cli
import storage
import clothing
from style import sort_by_counter
from os.path import dirname, join

# get the current script path
PATH = dirname(__file__)
CLOTHES_DIR = join(PATH, 'clothes_data.txt')
STYLES_DIR = join(PATH, 'styles_data.txt')
SOLD_DIR = join(PATH, 'sold_data.txt')
DONATED_DIR = join(PATH, 'donated_data.txt')

# if dont exists, create data files
data_files = [ CLOTHES_DIR, STYLES_DIR, SOLD_DIR, DONATED_DIR ]
for file_dir in data_files:
    open(file_dir, "a+")

clothes = storage.read_clothes( CLOTHES_DIR )
styles = storage.read_styles( STYLES_DIR, clothes )
sold_clothes = storage.read_sell( SOLD_DIR )
donated_clothes = storage.read_donations( DONATED_DIR )

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
        'a': 'clothes',
        'y': 'clothes for you',
        's': 'sold clothes',
        'd': 'donated clothes',
        't': 'styles',
        'f': 'favorite styles',
        'c': 'list clothes of a style',
        'e': 'search donated clothes by agent'
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
        # list clothes by user interest (5 of then)
        elif opt == 'y':
            interest_clothes = clothing.filter_by_interest(clothes)[:5]
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
        # list styles with higher counter (5 of then)
        elif opt == 'f':
            favorites = sort_by_counter(styles)[:5]
            cli.print_styles(favorites)
        # list clothes of a certain style
        elif opt == 'c':
            clth_style, index = cli.select_style(styles, index=True)
            if not clth_style is None:
                cli.print_clth_sets(clth_style['clothes_sets'], clothes)
        # list donated clothes based on the agent
        elif opt == 'e':
            agent = cli.read_not_empty("Enter the agent name", "agent")
            filtered_clths = clothing.filter('agent', agent, donated_clothes)
            cli.print_clothes(filtered_clths)
    # quit
    elif selected_opt == 'q':
        # save changes to file
        storage.upadate_clothes( CLOTHES_DIR, clothes )
        storage.update_style( styles, STYLES_DIR, clothes )
        storage.upadate_donation( DONATED_DIR, donated_clothes )
        storage.upadate_sell( SOLD_DIR, sold_clothes )
        break

# DEBUG INFO
# print('')
# print('stored clothes:', clothes)
# print('')
# print('sold clothes:', sold_clothes)
# print('')
# print('donated clothes:', donated_clothes)
# print('')
# print('stored styles:', styles)
