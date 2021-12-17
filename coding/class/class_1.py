# class 類別(種類)

# Create a class
class Student:
    def __init__(self, name, score):   # init= initialize(初始化)-必要 會自動執行
        self.name = name   # 自設屬性
        self.score = score
        print('I was born!')

    def do_hw(self, hw):
        print("I'm doing homework!", hw)

    def study(self):
        print("I'm studying.")
        self.score += 5  # 可以自我查找屬性

    def sleep(self):
        print("I'm sleeping!")

s1 = Student('Nicky', 100)  # 投入參數
s2 = Student('Allen', 95)
students = [s1, s2]
for s in students:
    print(s.name)
    print(s.score)