import random

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='yellow')
        self.house.money += 50
        self.fullness -= 20

    def watch_TV(self):
        cprint('{} смотрел MTV весь день'.format(self.name), color='cyan')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} денег нет еды нет!'.format(self.name), color='magenta')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -=10
        cprint('{} вьехал в дом!!!'.format(self.name), color='red')
    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='magenta')
            return
        dice = random.randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
           self.shopping()
        elif self.house.money < 50:
           self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_TV()

class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)

citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни')
]

beavis = Man(name='Бивис')
butthead = Man(name='Батхед')

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)


for day in range(1, 366):
    print('=============== день {} ==============='.format(day))

    for citizen in citizens:
        citizen.act()
    print('--------------------- в конце дня ---------------------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
