import sys
import os.path


def formatting_menu_items(menu_items):
    """Formatting the list that is received from reading the json file
    into a dictionary with a dish key and the value is the price. Also, checks
    at the beginning if the list length is greater than two to check if the
    file isn't empty."""
    if len(menu_items) <= 2:
        print("The file is empty.")
        return
    menu_items.pop(0)
    menu_items.pop(-1)
    updated_menu_items = dict()
    updated_menu = dict()
    for item in menu_items:
        dish, value = item.replace('"', '').lower().strip().split(":")
        price = float(value.strip()[1:-1])
        updated_menu_items[dish] = price
        updated_menu[price] = dish
    return updated_menu_items, updated_menu


def finding_combo_dishes(menu):
    dishes, prices = menu
    if "target price" not in dishes:
        print("The file doesn't have a target price.")
        return
    elif len(dishes.keys()) <= 2:
        print("Missing dishes only have a target price.")
        return
    # amount = dishes.pop("target price")
    dishes.pop("target price")
    amount = float(6.35)
    current_amount = float(0)
    different_amount = amount - current_amount
    combo_dishes = []
    for dish in dishes.keys():
        current_amount += dishes[dish]
        different_amount -= current_amount
        print(current_amount, round(different_amount, 2))
        combo_dishes.append(dish)
        if round(different_amount, 2) in prices:
            combo_dishes.append(prices[round(different_amount, 2)])
            print(combo_dishes)
            return

        if current_amount == amount:
            print(combo_dishes)
            return
    else:
        print(current_amount - amount)
        print(dishes)
        print(current_amount)
        print("No combination of dishes are equal to the target price.")


filename = sys.argv[1]
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        content = f.read().splitlines()
    menutItems = formatting_menu_items(content)
    finding_combo_dishes(menutItems)
