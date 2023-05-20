class Stock:
    __stock = []

    def AllProducts(self):
        for product in self.__stock:
            print(product)

    def getProduct(self, Id):
        for product in self.__stock:
            if product.getID() == Id:
                return product

    def insert(self, product):
        self.__stock.append(product)

    def remove(self, Id):
        for product in self.__stock:
            if product.getID() == Id:
                self.__stock.remove(product)