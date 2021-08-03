products = input().split("|")

command = input()

def important(products, product):
    if product in products:
        products.remove(product)
        products.insert(0, product)
    else:
        products.insert(0, product)

def add(products, product):
    if product not in products:
        products.append(product)
    else:
        print("The product is already in the list.")

def swap(products, first_product, second_product):
    if first_product in products and second_product in products:
        first_product_index = products.index(first_product)
        second_product_index = products.index(second_product)
        first_ele = products.pop(first_product_index)
        second_ele = products.pop(second_product_index - 1)

        products.insert(first_product_index, second_ele)
        products.insert(second_product_index, first_ele)

    else:
        if not first_product in products:
            print(f"Product {first_product} missing!")
        else:
            print(f"Product {second_product} missing!")


def remove(products, product):
    if product in products:
        products.remove(product)
    else:
        print(f"Product {product} isn't in the list.")

while command != "Shop!":
    data = command.split("%")
    action = data[0]

    if action == "Important":
        product = data[1]
        important(products, product)
    elif action == "Add":
        product = data[1]
        add(products, product)
    elif action == "Swap":
        first_product = data[1]
        second_product = data[2]
        swap(products, first_product, second_product)
    elif action == "Remove":
        product = data[1]
        remove(products, product)
    elif action == "Reversed":
        products = list(reversed(products))

    command = input()


for i in range(len(products)):
    print(f"{i + 1}. {products[i]}")