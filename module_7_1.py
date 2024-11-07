import io
from pprint import pprint

class Product:
    def __init__(self, name, weight, categori):
        self.name = name
        self.weight = weight
        self.categori = categori

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.categori}\n'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r', encoding = 'utf-8')
        file_1 = file.read()
        file.close()
        return file_1

    def add(self, *products):
        file = open(self.__file_name, 'r+', encoding='utf-8')
        for i in products:
            k = False
            for line in file:
                if i.__str__() == line:
                    print(f'Продукт {(i.__str__()).replace('\n','')} уже есть в магазине')
                    k = True
                    break
            if k == False:
                file.write(i.__str__())
            file.seek(0)
        file.close()






s1 = Shop()
p1 = Product('Картофель',50.5, 'Овощи')
p2 = Product('Спагетти',3.4, 'Макаронные изделия')
p3 = Product('Картофель', 5.5, 'Овощи')
p4 = Product('артофель', 5.2, 'Овощи')

print(p2)
s1.add(p1,p2,p3)
print(s1.get_products())
s1.add(p4)
print(s1.get_products())
