class Item():
  def __init__(self, name, description, value, weight):
    self.name = name
    self.description = description
    self.value = value
    self.weight = weight
    
  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class Coin(Item):
  def __init__(self, amount):
    self.amount = amount
    super().__init__(name="Coin",
                     description = "It's shiny and valuable.",
                     value = self.amount)
                     
class Weapon(Item):
  def __init__(self, name, description, value, weight, damage, tags=None):
    self.damage = damage
    self.tags = tags
    super().__init__(name, description, value, weight)
    
  def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
        
class Dagger(Weapon):
  def __init__(self):
    super().__init__(name="Dagger", description="Small, pointy and sharp", value=20, weight=1, damage=10, tags="hand")
    
class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "It’s a sword and it’s rusty"
        self.damage = 20
        self.value = 100
    
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")
        
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)
        
class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
