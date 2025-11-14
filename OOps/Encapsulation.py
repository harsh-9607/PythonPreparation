class Payment:
    def __init__(self,price):
        
        self.__price = price #Super Private
        self._final_price= self.__price + 10 #Private 
    def change_price(self,value):
        self.__price= value
        return self.__price
book =Payment(2)
print (book._final_price)

print(book.change_price(4))

print (book.__price) ##Throws an error