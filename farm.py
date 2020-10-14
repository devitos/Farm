animal_weight = {}

class Goose:
    name = ''
    weight = 0
    egg = 0
    voice = 'Gagaga'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def collect_egg(self, egg):
        self.egg += egg

    def change_name(self, name):
        self.name = name

class Cow:
    name = ''
    milkey = 0 # liter
    weight = 150 # kg
    voice = 'Mooo'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def milk(self, milkey):
        self.milkey += milkey

    def change_name(self, name):
        self.name = name

class Sheep:
    name = ''
    wool = 0 # kg
    weight = 70
    voice = 'Beee'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def trim(self, wool):
        self.wool += wool

    def change_name(self, name):
        self.name = name

class Chicken:
    name = ''
    egg = 0
    weight = 4  # kg
    voice = 'Kokoko'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def collect_egg(self, egg):
        self.egg += egg

    def change_name(self, name):
        self.name = name

class Coat:
    name = ''
    milkey = 0  # liter
    weight = 80  # kg
    voice = 'Meee'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def milk(self, milkey):
        self.milkey += milkey

    def change_name(self, name):
        self.name = name

class Duck:
    name = ''
    egg = 0
    weight = 4  # kg
    voice = 'Krya-krya'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal_weight[self.name] = self.weight

    def feed(self, food):
        self.weight += food

    def collect_egg(self, egg):
        self.egg += egg

    def change_name(self, name):
        self.name = name

seriy = Goose('seriy', 6)

beliy = Goose('beliy', 5)

barashek = Sheep('barashek', 60)

kudryaviy = Sheep('kudryaviy', 63)

ko_ko = Chicken('ko_ko', 3)

kukareku = Chicken('kukareku', 4)

roga = Coat('roga', 55)

kopita = Coat('kopita', 47)

kryakva = Duck('kryakva', 7)

weight_sum = sum(animal_weight.values())
weight_max = max(animal_weight.values())

for animal in animal_weight:
    if animal_weight[animal] == weight_max:
        weight_max = animal

print(animal_weight)
print(weight_sum)
print(weight_max)