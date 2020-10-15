animal_weight = {}
animal_list = list()
birds = list()
woolly = list()
milking = list()


class Animal:
    name = ''
    weight = 0  # kg
    age = 0  # year

    def __init__(self, name, weight, age=0):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight
        self.age = age
        animal_list.append(self)

    def grow(self, age):
        self.age += age
        self.weight += age / 2
        animal_weight[self.name] = self.weight
        print(f'{self.name}, вырос на {age}, и набрал {age / 2} кг!')

    def feed(self, food):
        self.weight += food
        print(f'{self.name} покормили, он набрал {food} кг!')

    def change_name(self, name):
        self.name = name


class Milking(Animal):
    milkey = 0  # ltr
    voice = 'kekeke'

    def __init__(self, name, weight, age=0):
        super().__init__(name, weight, age=0)
        milking.append(self)

    def milk(self, hour):
        self.milkey += hour * 2
        print(f'{self.name} подоили получаем {hour * 2} молока.')


class Woolly(Animal):
    wool = 0  # kg

    def __init__(self, name, weight, age=0):
        super().__init__(name, weight, age=0)
        woolly.append(self)

    def trim(self, hours):
        self.wool += hours / 2
        print(f'{self.name} постригли получаем {hours / 2} шерсти.')


class Bird(Animal):
    egg = 0  # count

    def __init__(self, name, weight, age=0):
        super().__init__(name, weight, age)
        birds.append(self)

    def collect_egg(self, egg):
        self.egg += egg
        print(f'{self.name} приносит нам {egg} яиц.')


class Goose(Bird):
    voice = 'Gagaga'


class Cow(Milking):
    voice = 'Mooo'


class Sheep(Woolly):
    voice = 'Beee'


class Chicken(Bird):
    voice = 'Kokoko'


class Coat(Milking):
    voice = 'Meee'


class Duck(Bird):
    voice = 'Krya-krya'


seriy = Goose('seriy', 6)

beliy = Goose('beliy', 5)

barashek = Sheep('barashek', 60)

kudryaviy = Sheep('kudryaviy', 63)

ko_ko = Chicken('ko_ko', 3)

kukareku = Chicken('kukareku', 4)

roga = Coat('roga', 55)

kopita = Coat('kopita', 47)

kryakva = Duck('kryakva', 7)

kopita.grow(21)

for animal1 in animal_list:
    animal1.grow(2)
    animal1.feed(1)
    print(f'{animal1.name} говорит {animal1.voice}')

for each_bird in birds:
    each_bird.collect_egg(5)

for each_woolly in woolly:
    each_woolly.trim(4)

for each_milking in milking:
    each_milking.milk(2)

weight_sum = sum(animal_weight.values())
weight_max = max(animal_weight.values())

for animal in animal_weight:
    if animal_weight[animal] == weight_max:
        weight_max = animal

print()
print(animal_weight)
print(weight_sum)
print(weight_max)