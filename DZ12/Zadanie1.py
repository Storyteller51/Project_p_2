class Car:
    def __init__(self, make: str, model: str, mileage: int = 0):
       
        self.__make = make
        self.__model = model
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")
        self.__mileage = mileage
    
    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    
    @property
    def mileage(self):
        return self.__mileage        
    
    @mileage.setter
    def mileage(self, value):
        try:
            is_negative = value < 0
            is_decrease = value < self.__mileage
        except TypeError:
            raise TypeError("Нужно ввести число")

        if is_negative:
            raise ValueError("Пробег не может быть отрицательным")
        if is_decrease:
            raise ValueError(
            f"Пробег не может уменьшаться: "
            f"сейчас {self.__mileage}, новый {value}"
        )
        self.__mileage = value

    def __str__(self):
        return f"{self.__make} {self.__model}, пробег: {self.__mileage} км"    

car = Car("Ford", "Focus", 15000)
print(car)    
car.mileage = 20000
print(car)