class Desk:
    def __init__(self, color):
        self.color = color
        print("I was been created!")
    
    def re_color(self, new_color):
        self.color = new_color

d = Desk("Blue")  #instantiation 實體化
d.re_color("Red")

print(d.color)
