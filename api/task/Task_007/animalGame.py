from random import randint
import time
class Tiger:
    animalName = '老虎'
    def __init__(self,weight):
        self.weight = weight
    def call(self):
        print('WOW !!，体重减少5')
        self.weight -= 5
    def eat(self,food):
        if food == 'meat':
            self.weight += 10
            print('喂食正确，体重增加10')
        else:
            self.weight -= 10
            print('喂食错误，体重减少10')
class Sheep:
    animalName = '羊'
    def __init__(self,weight):
        self.weight = weight
    def call(self):
        print('mie~~~，体重减少5')
        self.weight -= 5
    def eat(self,food):
        if food == 'grass':
            self.weight += 10
            print('喂食正确，体重增加10')
        else:
            self.weight -= 10
            print('喂食错误，体重减少10')
class Room:
    def __init__(self,num,inanimal):
        self.num = num
        self.animal = inanimal
rooms = []
for i in range(2,12):#循环创建10个房间实例,根据随机数添加每个房间的动物实例
    if randint(0,1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(i,ani)
    rooms.append(room)
startTimes = time.time()
while True:#当前减去开始时间大于120秒结束循环
    nowTimes = time.time()
    roomNum = randint(1, 10)
    if (nowTimes - startTimes ) > 120:
        print('游戏结束')
        for idx, room in enumerate(rooms):
            print(f'{idx+1:},{room.animal.animalName:},{room.animal.weight:}')
        break
    hit = input(f'当前房间号是：{roomNum:},请问是否敲门：1 or 2 : ')
    if hit == '1':
        room.animal.call()
    eatFood = str(input("请选择喂食食物:'meat' or 'grass' : "))
    room.animal.eat(eatFood)
