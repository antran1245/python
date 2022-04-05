class Product:
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
        
    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
        
    def print_info(self):
        print(f"{self.name} - {self.category} - ${self.price}")
        return self
