class Animal:
  def __init__(self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight
  def feed(self, n):
    if n == 1:
      return 'накормлено'
    elif n == 0:
      return 'голодный'

class Gus(Animal):
  animal_type = 'гусь'
  def eggs(self, e):
    if e == 1:
      return 'яйца собраны'
gus_1 = Gus('Серый', 'га-га-га', 7)
gus_2 = Gus('Белый', 'га-га-га', 7.5)

class Cow(Animal):
  animal_type = 'корова'
  def milk(self, m):
    if m == 1:
      return 'подоено'
cow_1 = Cow('Манька', 'мууу', 500)

class Sheep(Animal):
  animal_type = 'овца'
  def shave(self, s):
    if s == 1:
      return 'пострижено'
sheep_1 = Sheep('Барашек', 'беее', 100)
sheep_2 = Sheep('Кудрявый', 'беее', 75)

class Goat(Animal):
  animal_type = 'коза'
  def milk(self, m):
    if m == 1:
      return 'подоено'
goat_1 = Goat('Рога', 'меее', 40)
goat_2 = Goat('Копыта', 'меее', 67)

class Chicken(Animal):
  animal_type = 'курица'
  def eggs(self, e):
    if e == 1:
      return 'яйца собраны'
chicken_1 = Chicken('Ко-Ко', 'Ко-Ко', 3)
chicken_2 = Chicken('Кукареку', 'Ко-Ко', 0.8)

class Duck(Animal):
  animal_type = 'утка'
  def eggs(self, e):
    if e == 1:
      return 'яйца собраны'
duck_1 = Duck('Кряква', 'кряяя', 1.6)

print('Животное', gus_1.name, gus_1.animal_type, gus_1.feed(1), 'и', gus_2.eggs(1))
print('Животное', gus_2.name, gus_2.animal_type, gus_2.feed(1), 'и', gus_2.eggs(1))
print('Животное', cow_1.name, cow_1.animal_type, cow_1.feed(1), 'и', cow_1.milk(1))
print('Животное', sheep_1.name, sheep_1.animal_type, sheep_1.feed(1), 'и', sheep_1.shave(1))
print('Животное', sheep_2.name, sheep_2.animal_type, sheep_2.feed(1), 'и', sheep_2.shave(1))
print('Животное', chicken_1.name, chicken_1.animal_type, chicken_1.feed(1), 'и', chicken_1.eggs(1))
print('Животное', chicken_2.name, chicken_2.animal_type, chicken_2.feed(1), 'и', chicken_2.eggs(1))
print('Животное', goat_1.name, goat_1.animal_type, goat_1.feed(1), 'и', goat_1.milk(1))
print('Животное', goat_2.name, goat_2.animal_type, goat_2.feed(1), 'и', goat_2.milk(1))
print('Животное', duck_1.name, duck_1.animal_type, duck_1.feed(1), 'и', duck_1.eggs(1))

print('Вес всех животных:', gus_1.weight + gus_2.weight + cow_1.weight + sheep_1.weight + sheep_2.weight + chicken_1.weight +
chicken_2.weight + goat_1.weight + goat_2.weight + duck_1.weight, 'кг')
