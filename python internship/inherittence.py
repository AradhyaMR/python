# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "machuu"
# d1=Dog("Jack")
# print(d1.name)
# print(d1.make_sound()) 


class Brands:
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "Purple"
class products:
    prod_1 = "online ecommerce store"
    prod_2 = "online store"
    prod_3 = "online Buy sell store"
class popularity(Brands,products):
    prod_1_popularity = 100
    prod_2_popularity = 80
obj_1 = popularity()
print(obj_1.brand_name_1+" is an"+obj_1.prod_1)
  


        