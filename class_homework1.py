class Car:
    price = f'Цена машины: {1000000} рублей'
    horse_powers_ = f'Колличество ЛС у машин {100}'
    def horse_powers(self):
        return self.horse_powers_

class Nissan(Car):
    price = f'Цена 1 машины марки Nissan: {2000000} рублей'
    horse_powers_ = f'Колличество ЛС у машины {150}'
    def horse_powers(self):
        return self.horse_powers_

class Kia(Car):
    price = f'Цена 1 машины марки Kia: {1500000} рублей'
    horse_powers_ = f'Колличество ЛС у машины {200}'
    def horse_powers(self):
        return self.horse_powers_

car1 = Car()
print(car1.price)
print(car1.horse_powers())
car2 = Nissan()
print(car2.price)
print(car2.horse_powers())
car3 = Kia()
print(car3.price)
print(car3.horse_powers())