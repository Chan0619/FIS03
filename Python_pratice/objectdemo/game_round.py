"""
* 一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
* 定义一个fight方法：
* my_hp = hp - enemy_power
* enemy_final_hp = enemy_hp - my_power
* 两个hp进行对比，血量剩余多的人获胜
"""


def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1200
    enemy_power = 199
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 三目表达式
        # print('我赢了') if my_final_hp > enemy_final_hp else print('我输了')
        print(my_hp, enemy_hp)
        if my_hp <= 0:
            print('我输了')
            break
        if enemy_hp <= 0:
            print('我赢了')
            break


game()
