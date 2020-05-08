from test_demo.Game import Game


class Houyi(Game):
    def __init__(self):
        super().__init__(1000, 200)
        self.defense = 200

    def houyi_fight(self, enemy_hp,enemy_power):

        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的最终血量为{}".format(self.hp))
            print("敌人的最终血量为{}".format(enemy_hp))
            if self.hp <=0:
                print("我挂了！")
                break
            elif enemy_hp <= 0:
                print("敌人挂了")
                break

hp = 1000
power = 200
houyi = Houyi()
houyi.houyi_fight(hp,power)