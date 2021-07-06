import sys
import os.path


def formatting_menu_items(menu_items):
    """Formatting the list that is received from reading the json file.
     Also, checks at the beginning if the list length is greater than
    two to check if the file isn't empty and returns a tuple of dicitonaries:
    one dictionary has dish as the key an the price as the value in the second
    dictionray the dish is the value and the key is the price."""
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
    """Takes in a tuple which is broken into a dishes map and prices map. Then
    using two for loops to iterate through the keys in the dishes map. This
    solution contain three different loops for different number of dishes."""
    dishes, prices = menu
    if "target price" not in dishes:
        print("The file doesn't have a target price.")
        return
    elif len(dishes.keys()) <= 2:
        print("Missing dishes only have a target price.")
        return
    amount = dishes.pop("target price")
    current_amount = float(0)
    different_amount = amount - current_amount
    combo_dishes = []
    # This for loop iterates in line.
    for dish in dishes.keys():
        current_amount += dishes[dish]
        different_amount -= current_amount
        combo_dishes.append(dish)
        if round(different_amount, 2) in prices:
            combo_dishes.append(prices[round(different_amount, 2)])

        if round(current_amount, 2) == amount:
            print(combo_dishes)
            return
    current_amount = float(0)
    different_amount = amount - current_amount
    dishes_list = list(dishes.keys())
    dishes_list.reverse()
    combo_dishes = []
    # This for loop iterates in reverse.
    for dish in dishes_list:
        current_amount += dishes[dish]
        different_amount -= current_amount
        combo_dishes.append(dish)
        if round(different_amount, 2) in prices:
            combo_dishes.append(prices[round(different_amount, 2)])

        if round(current_amount, 2) == amount:
            print(combo_dishes)
            return
    # This a double for loop to find upto three dishes in the list.
    for i in range(len(dishes_list)):
        dish = dishes_list[i]
        current_amount = float(0)
        different_amount = amount - current_amount
        combo_dishes = [dish]
        for j in range(1, len(dishes_list)):
            dish2 = dishes_list[j]
            if dish == dish2:
                continue
            current_amount = float(0)
            current_amount = dishes[dish2] + dishes[dish]
            combo_dishes.append(dish2)
            different_amount -= current_amount
            if round(different_amount, 2) in prices:
                combo_dishes.append(prices[round(different_amount, 2)])

            if round(current_amount, 2) == amount:
                print(combo_dishes)
                return
            combo_dishes = [dish]
    else:
        print("No combination of dishes are equal to the target price.")


filename = sys.argv[1]
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        content = f.read().splitlines()
    try:
        menutItems = formatting_menu_items(content)
        finding_combo_dishes(menutItems)

    except Exception as error:
        print(f"An error occur: {error}")
