from cli import menu,read_clothing

def add_clothing(clothes_list = []):
    free_id = request_id(clothes_list)
    new_clothing = read_clothing(free_id)
    clothes_list.append(new_clothing)
    return clothes_list

def request_id(clothes_list):
    return len(clothes_list) + 1

clothes_list = []
main_menu_options = {
    'a': 'add a clothing',
    'q': 'quit'
}

while(True):
    selected_option = menu(main_menu_options)
    if selected_option == 'a':
        clothes_list = add_clothing(clothes_list)
        print("Added successfully!")
    elif selected_option == 'q':
        break

print(clothes_list)
