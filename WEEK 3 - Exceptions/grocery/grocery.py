def get_item_name(item_count):
    return item_count[0].upper()

def main():
    grocery_list = {

    }

    while True:
        try:
            grocery = input("")
            if not grocery:
                break

            grocery = grocery.lower()

            grocery_list[grocery] = grocery_list.get(grocery, 0) + 1
        except EOFError:
            break

    sorted_list = sorted(grocery_list.items(), key=get_item_name)

    for item, count in sorted_list:
        print(f"{count} {item.upper()}")

main()
