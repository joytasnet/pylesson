class Hero:
    def __init__(self,name,hp=100):
        self.name=name
        self.hp=hp
    def sleep(self,hours):
        print('{}は{}時間寝た!'.format(self.name,hours))
        self.hp +=hours

# ゲーム開始
print('スッキリファンタジー')
h=Hero('松田',200)
h1=Hero('スズキ')
h.sleep(3)
h1.sleep(10)
print('{}のHPは現在{}です'.format(h.name,h.hp))
print('{}のHPは現在{}です'.format(h1.name,h1.hp))

