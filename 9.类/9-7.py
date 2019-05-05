#9-7 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个字符串（如“can add post”、 “can delete post”、“can add user”）组成的列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。
class User():
    def __init__(self, first_name, last_name, age, skill):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skill = skill
        self.login_attempts = 0

    def describe_user(self):
        print(
            "--------" + self.first_name + self.last_name + "--------" +
            "\n姓：" + self.first_name +
            "\n名：" + self.last_name +
            "\n年龄 " + self.age +
            "\n天赋： " + self.skill
        )

    def read_login_attempts(self):
        """读取登陆失败次数"""
        print(self.login_attempts)

    def increment_login_attempts(self):
        """增加登陆失败次数"""
        self.login_attempts += 1

    def set_login_attempts(self):
        """重置登陆失败次数"""
        self.login_attempts = 0

    def greet_user(self):
        full_name = self.first_name + self.last_name
        print("欢迎回到欲望都市," + full_name + "!")

class Admin(User):
    def __init__(self,first_name,last_name, age, skill):
        super().__init__(first_name,last_name, age, skill)
        self.privileges = ["add user","delete user","change password"]

    def show_privileges(self):
        print(self.privileges)

admin_privileges = Admin("张","大力",23,"大力出奇迹")
admin_privileges.show_privileges()