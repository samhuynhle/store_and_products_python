class Store:
    def __init__ (self, name):
        self.name = name
        self.products = []
    
    def add_products(self,new_product):
        self.products.append(new_product)
        print(f"{self.name} has added: {new_product.name}, which costs {new_product.price}")
        return self

    def sell_products(self,id):
        for x in self.products:
            if x.ID == id:
                print(f"At {self.name}, the {x.print_info()}, Item ID: {id}, has been sold.")
                self.products.pop()
        return self

    def inflation(self, percent_increase):
        print(f"{self.name} has adjusted prices for inflation!")
        for x in self.products:
            x.update_price(percent_increase,is_increased=True)

    def set_clearance(self, category, percent_discount):
        print(f"{self.name} has set {category} on clearance")
        for x in self.products:
            if x.category == category:
                x.update_price(percent_discount,is_increased=False)