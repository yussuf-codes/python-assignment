class Product:
    def __init__(self, Id, name, unit, quantity, price):
        self.__Id = Id
        self.__name = name
        self.__unit = unit
        self.__quantity = quantity
        self.__price = price
        

    def __str__(self) -> str:
        str = '-----------------------------------------------------------\n'
        str += f'ID: {self.__Id}, Name: {self.__name}, Unit: {self.__unit}, Quantity: {self.__quantity}, Price: {self.__price}.'
        str += '\n-----------------------------------------------------------'
        return str

    def totalPrice(self):
        return self.__quantity * self.__price
    

    # getters
    def getID(self):
        return self.__Id
    def getName(self):
        return self.__name
    def getQuantity(self):
        return f'{self.__quantity} {self.__unit}'
    def getPrice(self):
        return f'{self.__price}/{self.__unit}'
    
    
    # setters
    def setName(self, name):
        self.__name = name
    def setQuantity(self, quantity):
        self.__quantity = quantity
    def setPrice(self, price):
        self.__price = price