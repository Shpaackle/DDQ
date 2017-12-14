import enemies
import random
import npc


class MapTile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def intro_text(self):
    raise NotImplementedError("Create a subclass instead!")
    
  def modify_player(self, player):
    raise NotImplementedError("Create a subclass instead!")
  
class StartTile(MapTile):
  def intro_text(self):
    return """
    You wake up in a cold, dark stone room. Next to you lies your belongings,
    conveniently placed within reach. Nothing seems to be missing as you quickly
    rummage through your backpack. 
    
    You see three exits from this room:
        (E)ast  - This exit turns sharply a few feet in.
        (W)est  - The tunnel looks like it leads upwards.
        (N)orth - Light shines from further down the hall.
    """
    
  def modify_player(self, player):
    # Room has no action on player
    pass

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from " \
                              "its web in front of you!"
            self.dead_text = "The corpse of a dead spider " \
                             "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre reminds you of your triumph."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a squeaking noise growing louder" \
                              "...suddenly you are lost in a swarm of bats!"
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You’ve disturbed a rock monster " \
                              "from his slumber!"
            self.dead_text = "Defeated, themonster has reverted" \
                             "into an ordinary rock"
            
        super().__init__(x, y)
    
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
    
    def modify_player(self, player):
        if self.enemy.is_alive():
          player.hp = player.hp - self.enemy.damage
          print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage,  player.hp))
      
class BoringTile(MapTile):
    def intro_text(self):
        return """
        A plain hallway, nothing new here.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class VictoryTile(MapTile):
     def intro_text(self):
         return """
         You see a bright light in the distance...
         ... it grows as you get closer! It’s sunlight!
         
         
         Victory is yours!
         """

world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FG|EN|  |TT|
|TT|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
            
    return True
    
world_map = []

start_tile_location = None
                                                
def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
        
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                print("found starting tile")
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
            
        world_map.append(row)

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)
        
    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """

    def modify_player(self, player):
        pass
        
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Coin".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError or IndexError:
                    print("Invalid choice!")
            for i, item in enumerate(seller.inventory, 1):
                print("{}. {} - {} Coin".format(i, item.name, item.value))
                
    def swap(self, seller, buyer, item):
        if item.value > buyer.coin:
            print("That’s too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.coin = seller.coin + item.value
        buyer.coin = buyer.coin - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here’s whatss available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S','s']:
                print("Here’s what’s available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")
            
class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.coin = random.randint(1, 50)
        self.coin_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.coin_claimed:
            self.coin_claimed = True
            player.coin = player.coin + self.coin
            print("+{} coin added.".format(self.coin))
            
    def intro_text(self):
        if self.coin_claimed:
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            Someone dropped some coin. You pick it up.
            """

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}

