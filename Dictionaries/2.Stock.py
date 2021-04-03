products = input().split()

wanted_products = input().split()

my_dict = {products[i]: products[i + 1] for i in range(0, len(products), 2)}

for el in wanted_products:
    if el in my_dict:
        print(f"We have {my_dict.get(el)} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")

