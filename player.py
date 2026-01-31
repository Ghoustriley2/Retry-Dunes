import random

class Player:
    def __init__(self):
        self.effects = {}
        self.location = None
        self.is_alive = True
        self.inventory = {}
        self.name = "empty"
        self.max_hp = 100
        self.hp = 100
        self.dp = 50
        self.exp = 0
        self.gold = 100
        self.player_class = "empty"
        self.turns = 0
    def init_player(self):
        PC = [
            "штурмовик", "танк", "снайпер", "тактик",
            "навигатор", "оператор дронов", "кочевник",
            "медик", "химик", "киберфрагмент", "перегруженный",
            "архивист", "проклятый песком", "никто", "повторённый",
        ]
        if self.player_class == PC[0]:
            self.hp = 120
            self.max_hp = self.hp
            self.dp = 70
        elif self.player_class == PC[1]:
            self.hp = 250
            self.max_hp = self.hp
            self.dp = 30
        elif self.player_class == PC[2]:
            self.hp = 50
            self.max_hp = self.hp
            self.dp = 170
        elif self.player_class == PC[3]:
            self.hp = 70
            self.max_hp = self.hp
            self.dp = 50
        elif self.player_class == PC[4]:
            self.hp = 50
            self.max_hp = self.hp
            self.dp = 50
        elif self.player_class == PC[5]:
            self.hp = 70
            self.max_hp = self.hp
            self.dp = 120
        elif self.player_class == PC[6]:
            self.hp = 120
            self.max_hp = self.hp
            self.dp = 80
        elif self.player_class == PC[7]:
            self.hp = 150
            self.max_hp = self.hp
            self.dp = 20
        elif self.player_class == PC[8]:
            self.hp = 150
            self.max_hp = self.hp
            self.dp = 120
        elif self.player_class == PC[9]:
            self.hp = 200
            self.max_hp = self.hp
            self.dp = 150
        elif self.player_class == PC[10]:
            self.hp = 300
            self.max_hp = self.hp
            self.dp = 250
        elif self.player_class == PC[11]:
            pass
        elif self.player_class == PC[12]:
            self.hp = 150
            self.max_hp = self.hp
            self.dp = 100
        elif self.player_class == PC[13]:
            self.hp = random.randint(100, 1000)
            self.max_hp = self.hp
            self.dp = random.randint(50, 300)
        elif self.player_class == PC[14]:
            self.hp = 100 * 2
            self.max_hp = self.hp
            self.dp = 50 * 2
        else:
            raise Exception("\n\nневозможно определить тип или он не был задан...")
    def stata(self):
        info = f"""\n
---------------------------------
          статистика
имя: \"{self.name}\"
здоровье: {self.hp} из {self.max_hp}
урон: {self.dp}
опыт: {self.exp}
золото: {self.gold}
класс: {self.player_class}
---------------------------------\n"""
        print(info)
        def effect_stata():
            effects_value = 0
            print("---------------------------------")
            print("           эффекты")
            if len(self.effects.items()) == 0:
                print("\nсдесь пока что пусто:(\n")
            for i, j in self.effects.items():
                effects_value += 1
                print(f"{effects_value}. эффект \"{i}\" на {j} ходов.")
            print("---------------------------------")
        effect_stata()
    def open_inventory(self):
        print("----------ИНВЕНТАРЬ----------")
        cycle_value = 0
        if len(self.inventory.items()) == 0:
            print("\nсдесь пока пусто:(\n")
        for i, j in self.inventory.items():
            cycle_value += 1
            print(f"|{cycle_value}. название: {i} | количество: {j} |")
        print("-----------------------------")
    def reset_location(self, location_name):
        self.location = location_name
    def take_damage(self, damage):
        self.hp -= damage
    def alive_check(self):
        if self.is_alive == True:
            print("\nигрок жив")
        if self.is_alive == False:
            text = """
    ------------------------------
              GAME OVER
            вы проиграли
    ------------------------------"""
    # BETA FUNCTIONS
    def settings(self):
        while True:
            user = input("Player > настройки: ")
    # --------------
    def add_item(self, item_name, value):
        self.inventory[item_name] = value
    def remove_item(self, item_name):
        del self.inventory[item_name]
    def items_list(self):
        print("ваши предметы: ")
        print("---------------------------")
        for i in list(self.inventory.keys()):
            print(i)
        print("---------------------------")
    def drop_item(self, item_name, value):
        if int(value) > self.inventory.get(item_name, 0):
            raise Exception("нельзя выкинуть больше чем есть!")
        elif self.inventory[item_name] <= 0:
            del self.inventory[item_name]
        self.inventory[item_name] = value
    def has_item(self, item_name):
        if item_name in self.inventory:
            pass
        else:
            raise Exception("\n\nу вас нет такого предмета в инвентаре")
    def apply_effect(self, effect_name, time):
        self.effects[effect_name] = time
    def remove_effect(self, effect_name):
        del self.effects[effect_name]
    def tick(self, action, arg1):
        if action == "-hp":
            self.hp -= arg1
        elif action == "+TH":
            self.hp += arg1
        elif action == "+exp":
            self.exp += arg1
        elif action == "-gold":
            self.gold -= arg1
        elif action == "+arrmor":
            self.hp += arg1
        elif action == "+damage":
            self.dp += arg1
        else:
            raise Exception("впиши правильные аргументы или посмотри в классовые настройки")
    def rest(self):
        heal = min(10, self.max_hp - self.hp)
        self.hp += heal
        print(f"Вы отдохнули и восстановили {heal} HP.")