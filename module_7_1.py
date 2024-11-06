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
   __file_name = 'products.txt'

   def get_products(self):
       file = open(self.__file_name, 'r', encoding = 'utf-8')
       file_1 = file.read()
       file.close()
       return file_1

   def add(self, *products):
       for i in products:

           if i.__str__() in self.get_products():
               print(f'Продукт {(i.__str__()).replace('\n','')} уже есть в магазине')

           else:
               file = open(self.__file_name, 'a', encoding='utf-8')
               file.write(i.__str__())
               file.close()






s1 = Shop()
p1 = Product('Картофель',50.5, 'Овощи')
p2 = Product('Спагетти',3.4, 'Макаронные изделия')
p3 = Product('Картофель', 5.5, 'Овощи')

print(p2)
s1.add(p1,p2,p3)
print(s1.get_products())
