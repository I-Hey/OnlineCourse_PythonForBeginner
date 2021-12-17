class Player:
    def __init__(self, name, ap):
        self.name = name  # 玩家姓名
        self.hp = 100
        self.ap = ap
    
    def attack(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.ap  # 目標生命值


p1 = Player("Player1", 5)   # 實體化，做成一個物件
p2 = Player("Player2", 10)
p1.attack(p2)  # p1攻擊p2
print(p2.hp)