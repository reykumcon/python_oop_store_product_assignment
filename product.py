class Product:
    def __init__(self, name, price, category, unique_id):
        self.name = name
        self.price = price
        self.category = category
        self.unique_id = unique_id
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Price: {self.price}, Unique Id: {self.unique_id}")
        return self