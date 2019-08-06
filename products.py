class Products:
    def __init__ (self, name, price, category, ID):
        self.name = name
        self.price = price
        self.category = category
        self.ID = ID
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
            print(f"Product: {self.name} has increased by {percent_change}. New price is now ${self.price}.")
        else:
            self.price = self.price - (self.price * percent_change)
            print(f"Product: {self.name} has decreased by {percent_change}. New price is now ${self.price}.")
        return self
    
    def print_info(self):
        return f"{self.name}"