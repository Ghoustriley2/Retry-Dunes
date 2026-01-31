class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def use(self):
        print("этот предмет нельзя использовать")
    def __str__(self):
        return self.name

class Water(Item):
    def __init__(self):
        super().__init__("вода", "жажда в таких местах самый неуместный враг по этому береги её.")
    def use(self, player_hp):
        player_hp += 10

class Lemon(Item):
    def __init__(self):
        super().__init__("лимон", "простой лимон всё же лучше чем просто ничего.")
    def use(self, player_hp):
        player_hp += 5
    
class Medkit(Item):
    def __init__(self):
        super().__init__("аптечка", "аптечка высокого качества, значительно увеличивает здоровье.")
    def use(self, player_hp):
        player_hp += 100
    
class Scrap(Item):
    def __init__(self):
        super().__init__("хлам", "безполезный хлам может оказаться нужной вещью в этой местности это может быть валюта.")
        
class Electro_Scrap(Item):
    def __init__(self):
        super().__init__("електрические микросхемы", "нужны для создания чего то тяжёлого в знаниях техники.")
        
class Keycard(Item):
    def __init__(self):
        super().__init__("ключ карта", "ключ карта для входа в закрытые местности запертые дверью.")
    def open_door(self, player_door):
        player_door = True

class Radio(Item):
    def __init__(self):
        super().__init__("радио", "поломаное радио уже не годится для использования но есть надежда починить его.")