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
        print(self.login_attempts)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def set_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        full_name = self.first_name + self.last_name
        print("欢迎回到欲望都市," + full_name + "!")


login_user = User("王", "大力", "33", "能长能短")
#login_user.describe_user()
for i in range(10):
    login_user.increment_login_attempts()
login_user.read_login_attempts()
login_user.set_login_attempts()
login_user.read_login_attempts()