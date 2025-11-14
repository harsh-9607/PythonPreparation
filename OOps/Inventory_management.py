class item:
    number_of_products= 0        
    def __init__(self, id, name, category, price):
        self.id = id
        self.name=name
        self.cate=category
        self.price= price

class hardware(item):
    def __init__(self, id, name, category, price, manufacturer,warranty_years):
        super().__init__(id, name, category, price)
        self.manu = manufacturer
        self.warr_years = warranty_years

class software(item):
    def __init__(self, id, name, category, price, licence_key ,expiry_date):
        super().__init__(id, name, category, price)
        self.licence_key = licence_key
        self.exp_date= expiry_date

class inventory_management:
   
    def __init__(self):
        self.items={}
    def add_item(self,item):
        self.items[item.id]= (item)
        print(f"Added an Item : {item.name}")
    def remove_item(self,id):
        if id in self.items:
            print(f"removed {self.items[id].__dict__}")
            self.items.pop(id)
        else:
            print("Id not found")
    def show(self):
        for item in self.items.values():
            print(item.__dict__)

 