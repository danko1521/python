import random

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

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

    def play_dota(self):
        cprint('{} играл в доту целый день'.format(self.name), color='cyan')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} денег нет еды нет!'.format(self.name), color='magenta')

    def go_into_house(self,house):
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
            self.play_dota()

class House:

    def __init__(self):
        self.food = 10
        self.money = 50


beavis = Man(name='Бивис')
butthead = Man(name='Батхед')
for day in range(1, 366):
    print('=============== день {} ==============='.format(day))
    beavis.act()
    butthead.act()
    print(butthead)
    print(beavis)
