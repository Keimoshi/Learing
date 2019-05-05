# 9-6 冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让他继承你为完成练习9-1或练习9-4而编写的Restaurant类。 这两个版本的Reataurant类都可以，挑选你更喜欢的即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并条用这个方法。
class Restaurant():
    def __init__(self, restaurant_name, cusisine_type):
        self.restaurant_name = restaurant_name
        self.cusisine_type = cusisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name + '.'
              )
        print("This restaurant cuisine_type is " + self.cusisine_type + '.')

    def open_restaurant(self):
        """显示这家餐馆正在营业的字样"""
        print(self.restaurant_name + " is opening !")

    def read_number_served(self):
        """读取这家餐馆的就餐人数"""
        print(self.number_served)

    def set_number_served(self, num):
        """设置这家餐馆的默认就餐人数"""
        self.number_served = num

    def increment_number_served(self, increment_num):
        """设置这家餐馆的增长人数"""
        self.number_served += increment_num


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cusisine_type):
        super().__init__(restaurant_name,cusisine_type)
        self.flavors = ['草莓','芒果','蓝莓','樱花']

    def show_ice_flavors(self):
        print(self.flavors)

IceCreamStand = IceCreamStand("冰雪皇后","ICE CREAM")
IceCreamStand.show_ice_flavors()