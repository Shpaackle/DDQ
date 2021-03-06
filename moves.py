"""
TODO: create function, in this class or from where called, to grab info from json files
import json
import os
"""


class Move:
    def __init__(self, name, description, trigger, results):
        self.name = name
        self.description = description
        self.trigger = trigger
        self.results = results
        
    def check_trigger(self):
        print("LOGGING: setup through subclass")
    
    def check_results(self):
        print("LOGGING: setup through subclass")
        
    def miss(self):
        print("LOGGING: setup through subclass")
        
    def success(self):
        print("LOGGING: setup through subclass")
        
    def partial(self):
        print("LOGGING: setup through subclass")
        
    def __str__(self):
        formatted = "{}: \n{}\n".format(self.name, self.description)
        for result in ["10+", "7-9", "6-"]:
            formatted += "{}: {}".format(result, self.results[result])
        return formatted


class BasicMove(Move):
    def __init__(self, name, description, trigger, results):
        super().__init__(name, description, trigger, results)
        
    def check_trigger(self, trigger_event):
        if trigger_event == self.trigger:
            return True
        else:
            return False
    
    def check_results(self, triggered, dice_total):
        if not triggered:
            return None
        
        if dice_total >= 10:
            return self.results["10+"]
        elif dice_total >= 7:
            return self.results["7-9"]
        else:
            return self.results["6-"]
    
        
class ClassMove(Move):
    def __init__(self, name, description, trigger, results, char_class, player):
        if player.char_class.name != char_class:
            raise NameError('Wrong class for move')
        # TODO: implement way to add other classes moves when available, i.e. Bard
        
        super().__init__(name, description, trigger, results)
