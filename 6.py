# �� �������� �������� �� ����� ������� ��� � ������ ������ ���� ��������� ������ ��������:

# ����� "�����" � "�����"
# ������ "������"
# ���� "�������" � "��������"
# ��� "��-��" � "��������"
# ��� "����" � "������"
# � ���� "������"
# �� ����� ��������� ��� ���������� ���-�� �����������������:

# �������
# ������ � ��� �����
# ���� ������
# �������� ���� � ���, ���� � �����
# ��������� �� �������(������ �����, ���� ������� � �.�.)
# ������ �1
# ����� ����������� ������ ��������, �� ������� ������������ ������������, ���������� ����� ������ �������������� � ��������� � ��������� �� � �������� �������, ���� �����������.
class Animal:
  def __init__(self, name, voice, weight):
    self.name = name
    self.voice = voice
    self.weight = weight
  def feed(self, n):
    if n == 1:
      return '����������'
    elif n == 0:
      return '��������'

class Gus(Animal):
  animal_type = '����'
  def eggs(self, e):
    if e == 1:
      return '���� �������'
gus_1 = Gus('�����', '��-��-��', 7)
gus_2 = Gus('�����', '��-��-��', 7.5)

class Cow(Animal):
  animal_type = '������'
  def milk(self, m):
    if m == 1:
      return '�������'
cow_1 = Cow('������', '����', 500)

class Sheep(Animal):
  animal_type = '����'
  def shave(self, s):
    if s == 1:
      return '����������'
sheep_1 = Sheep('�������', '����', 100)
sheep_2 = Sheep('��������', '����', 75)

class Goat(Animal):
  animal_type = '����'
  def milk(self, m):
    if m == 1:
      return '�������'
goat_1 = Goat('����', '����', 40)
goat_2 = Goat('������', '����', 67)

class Chicken(Animal):
  animal_type = '������'
  def eggs(self, e):
    if e == 1:
      return '���� �������'
chicken_1 = Chicken('��-��', '��-��', 3)
chicken_2 = Chicken('��������', '��-��', 0.8)

class Duck(Animal):
  animal_type = '����'
  def eggs(self, e):
    if e == 1:
      return '���� �������'
duck_1 = Duck('������', '�����', 1.6)

print('��������', gus_1.name, gus_1.animal_type, gus_1.feed(1), '�', gus_2.eggs(1))
print('��������', gus_2.name, gus_2.animal_type, gus_2.feed(1), '�', gus_2.eggs(1))
print('��������', cow_1.name, cow_1.animal_type, cow_1.feed(1), '�', cow_1.milk(1))
print('��������', sheep_1.name, sheep_1.animal_type, sheep_1.feed(1), '�', sheep_1.shave(1))
print('��������', sheep_2.name, sheep_2.animal_type, sheep_2.feed(1), '�', sheep_2.shave(1))
print('��������', chicken_1.name, chicken_1.animal_type, chicken_1.feed(1), '�', chicken_1.eggs(1))
print('��������', chicken_2.name, chicken_2.animal_type, chicken_2.feed(1), '�', chicken_2.eggs(1))
print('��������', goat_1.name, goat_1.animal_type, goat_1.feed(1), '�', goat_1.milk(1))
print('��������', goat_2.name, goat_2.animal_type, goat_2.feed(1), '�', goat_2.milk(1))
print('��������', duck_1.name, duck_1.animal_type, duck_1.feed(1), '�', duck_1.eggs(1))

print('��� ���� ��������:', gus_1.weight + gus_2.weight + cow_1.weight + sheep_1.weight + sheep_2.weight + chicken_1.weight +
chicken_2.weight + goat_1.weight + goat_2.weight + duck_1.weight, '��')


