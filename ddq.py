class Move():
    def __init__(self, name="", desc="", stat=None):
        self.name = name
        self.description = desc
        self.stats = stat
        self.results = {
            "10+": "None",
            "7-9": "None",
            "6-": "None"
        }

    def DetermineResults(self, roll, used_move):
        return


class CharClass():
    def __init__(self):
        self.class_name = ""

    def assign_class(self):
        print("Function not implemented")
        pass


class Cleric(CharClass):
    races_available = ["Dwarf", "Human"]
    look_choices = {
        "Eyes": ["Eyes1", "Eyes2", "Eyes3"],
        "Hair": ["Hair1", "Hair2", "Hair3"],
        "Body": ["Body1", "Body2", "Body3"],
        "Clothes": ["Clothes1", "Clothes2", "Clothes3"]
    }

    def __init__(self):
        self.class_name = "Cleric"
        self.HP = 0
        self.damage = 0
        self.races_avaiable = ["Dwarf", "Human"]


class Race():
    def __init__(self):
        self.name = ""

    def get_race_list(self, char_class):
        class_list = {
            "Cleric": ["Dwarf", "Human"],
            "Bard": ["Elf", "Human"],
            "Fighter": ["Elf", "Human", "Dwarf", "Halfling"],
            "Wizard": ["Elf", "Human"],
            "Rogue": ["Human", "Halfling"]
        }
        return class_list[char_class]


class Dwarf(Race):
    def __init__(self):
        self.name = "Dwarf"

    def add_racial_move(self, char_class):
        if char_class.name == "Cleric":
            return Move("Stone Speak", "can use to speak with stone", "WIS")


class Character():
    def __init__(self, p):
        self.owner = p
        self.charclass = CharClass()
        self.race = Race()
        self.name = ""
        self.look = {
            "Eyes": None,
            "Hair": None,
            "Body": None,
            "Clothes": None,
        }
        self.stats = {}  # includes modifiers, hp

    def choose_class(self, predetermined=""):
        class_list = [
            "Barbarian",
            "Bard",
            "Cleric",
            "Druid",
            "Fighter",
            "Immolator",
            "Paladin",
            "Ranger",
            "Thief",
            "Wizard",
        ]

        # Check to see if class was predetermined
        if predetermined == "Cleric":
            self.charclass = Cleric()
        else:
            print("Choose from the following list of classes: ")
            for i in range(len(class_list)):
                print(str(i) + ". " + class_list[i])
            choice = input("> ")

            self.charclass.class_name = class_list[int(choice)]

    def choose_race(self, char_class, predetermined=""):
        if predetermined == "Dwarf":
            self.race = Dwarf()
        else:
            races = self.race.get_race_list(char_class)
            for i in range(len(races)):
                print(str(i) + ". " + races[i])

    def choose_name(self, char_class, char_race):
        if char_class == "Cleric" and char_race == "Dwarf":
            self.name = "Whatever"
        else:
            print("Invalid")


class Player():
    def __init__(self, name=None, email=None):
        if name:
            self.name = name
        else:
            self.name = ""
        self.characters = {}
        self.current_character = None
        self.player_id = self.assign_id()
        self.email = self.assign_email(email)

    def assign_id(self):
        return 13

    def assign_email(self, email):
        if email:
            return email
        else:
            return "shpaackle@gmail.com"

    def create_character(self):
        new_char = Character(self)

        if not self.characters:
            self.characters[new_char.name] = new_char

        self.current_character = new_char


def print_info(player):
    print("Current player: {} (ID# {})\n".format(player.name, player.player_id))
    print("Current character:")
    print("Class: {}".format(player.current_character.charclass.class_name))
    print("Race: {}".format(player.current_character.race.name))
    print("Name: {}".format(player.current_character.name))


# TODO Add ability to LOG
# Create Player & enter player name
# print("Please enter your name: ")
# p_name = input(">")
p_name = "Daniel"
current_player = Player(p_name)

# Create new character
new_char = Character(current_player)

# Choose a Class for character
new_char.choose_class("Cleric")
print(new_char.charclass.class_name)
# Choose a Race
new_char.choose_race("Cleric", "Dwarf")
print(new_char.race.name)
# Choose a Name
new_char.choose_name("Cleric", "Dwarf")
print(new_char.name)

print("\n")
current_player.current_character = new_char
print_info(current_player)
# Choose Look
# Choose Stats
# Figure out Modifiers
# Set Maximum HP
# Choose Starting Moves
# Choose Alignment
# Choose Gear
# Introduce your Character
# Choose your Bonds

new_dict = {"Dwarf": {"Cleric": "Stone "}}

urban_dictionary = ["squirrel friend", "kai kai", "gender ninja", "fierceosity", "turn out a look", "kiki", "gay eyes",
                    "fierce", "ferosh", {"moffie": "South African slang word"},
                    {"the house down": "A drawn out version of the exclamation point"},
                    {"the T": "(T)alk of the (T)own"}, "Beef Steak Pantyhose", "cake-up",
                    {"Himither": "Somebody of a questionable gender"}, "Fish Queen", "Harlett O'Scara", "Stoic Beatbox",
                    "chante", "booger drag", "queen-out", "faux queen", "backrolls", "kalika", "sprepper",
                    "Mrs Doubtfire", "drag king", "Tranny get your gun", "drag queen bingo", "cha cha diva",
                    "snap & pose", "Executive Realness", "Femqueen", "drag hag", {"Kasrul": "Kusra"}, "bungee boi",
                    "Trannysaurus Mess", "She had hands like Andre the Giant", "coin-tosser", "Diana Paradise",
                    "Z-Snap", "Miss Lady", "cross dress for less", "bio-queen", "Tucking Nuts", "gag queen",
                    "Shenanagina", "saccident", "Drag Prince", "hangin' biscuit", "Dude Bluffy", "Huamonte",
                    "Ball Tucker", "trannedy", "wig chaser", "Brick", "training heels", "ratchet", "Dragazon",
                    "homospectacle", "swinging hammer", "hangin' shrimp", "Stag Queen", "White Dragon Breath"]
