class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=4)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=20, damage=10)
    
class BatColony(Enemy):
    def __init__(self):
        super().__init__(name="Colony of bats", hp=100, damage=4)
        
class RockMonster(Enemy):
    def __init__(self):
        super().__init__(name="Rock Monster", hp=80, damage=15)
