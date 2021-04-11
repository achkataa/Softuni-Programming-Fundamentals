class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        self.product = product
        if len(self.storage) < self.capacity:
            self.storage.append(product)


    def get_products(self):
        return self.storage

storage = Storage(4)

for num in range(storage.capacity):
    storage.add_product("apple")

print(storage.get_products())