import sys
import os.path


def formatting_menu_items(menu_items):
    """Formatting the list that is received from reading the json file
    into tuples that has the dish and the price. Also, checks at the beginning
    if the list length is greater than two to check if the file isn't empty."""
    if len(menu_items) <= 2:
        print("The file is empty.")
        return
    menu_items.pop(0)
    menu_items.pop(-1)
    updated_menu_items = []
    for item in menu_items:
        (dish, value) = item.replace('"', '').lower().strip().split(":")
        price = float(value.strip()[1:-1])
        updated_menu_items.append((dish, price))
    return updated_menu_items


def finding_combo_dishes(dishes):
    (target_price, amount) = dishes[0]
    print(repr(target_price), repr(amount))


filename = sys.argv[1]
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        content = f.read().splitlines()
    menutItems = formatting_menu_items(content)
    finding_combo_dishes(menutItems)
