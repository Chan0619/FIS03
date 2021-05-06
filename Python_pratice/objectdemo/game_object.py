"""
* 一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
* 定义一个fight方法：
* my_hp = hp - enemy_power
* enemy_final_hp = enemy_hp - my_power
* 两个hp进行对比，血量剩余多的人获胜
"""


class Game:
    # my_hp = 1000
    my_power = 200
    # enemy_hp = 1200
    enemy_power = 199

    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # 三目表达式
            # print('我赢了') if my_final_hp > enemy_final_hp else print('我输了')
            print(self.my_hp, self.enemy_hp)
            if self.my_hp <= 0:
                print('我输了')
                break
            if self.enemy_hp <= 0:
                print('我赢了')
                break

    def back_home(self):
        print('回城')


class HouYi(Game):
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # 三目表达式
            # print('我赢了') if my_final_hp > enemy_final_hp else print('我输了')
            print(f'my_hp: {self.my_hp}, enemy_hp: {self.enemy_hp}')
            if self.my_hp <= 0:
                print('我输了')
                break
            if self.enemy_hp <= 0:
                print('我赢了')
                break


# game = Game(1000, 1300)
# game.fight()

houyi = HouYi(200, 1000, 1500)
houyi.fight()
houyi.back_home()
