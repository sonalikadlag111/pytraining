class Computer:

    def __init__(self):
         self.__maxprice = 900       #private varible assign in __

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

obj = Computer()
obj.sell()

# change the price
obj.__maxprice = 1000
obj.sell()

# using setter function
obj.setMaxPrice(1000)
obj.sell()