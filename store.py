class Store:
    def __init__(self, name):
        self.name = name
        self.list_products = []

    def add_product(self, new_product):
        self.list_products.append(new_product)

    def sell_product(self, id):
        for i in range(len(self.list_products)-1,-1,-1):
            if id == self.list_products[i].unique_id:
                self.list_products.pop(i).print_info()

    def inflation(self, percent_increase):
        for j in range(len(self.list_products)):
            self.list_products[j].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for k in range(len(self.list_products)):
            if category == self.list_products[k].category:
                self.list_products[k].update_price(percent_discount, False)