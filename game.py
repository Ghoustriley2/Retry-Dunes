from player import Player
from enemy import Enemy
from events import EVENTS, ENEMIES, SCENARIOS
from items import Item, Water, Lemon, Medkit, Scrap, Electro_Scrap, Keycard
import time
import os
import random

class Game:
    def __init__(self, running):
        self.achievements = {}
        self.player = Player()
        self.event = None
        self.game_turns = 0
        self.running = running
        self.step = 0
        self.location = None
        self.world_data = None
    def combat(self, enemy):
        os.system("clear")
        print(f"На вас напал {enemy.name}!\n")
        while enemy.is_alive() and self.player.hp > 0:
            print(f"Ваше HP: {self.player.hp}")
            print(f"name: {enemy.name}\nHP: {enemy.hp}\n")
            print("1. Атаковать")
            print("2. Использовать предмет")
            print("3. Убежать")
            choice = input("> ")
            if choice == "1":
                dmg = random.randint(5, 10)
                enemy.hp -= dmg
                print(f"Вы нанесли {dmg} урона.")
            elif choice == "2":
                self.player.open_inventory()
            elif choice == "3":
                if random.random() < 0.5:
                    print("Вы успешно сбежали.")
                    return
                else:
                    print("Побег не удался!")
            else:
                print("Неверный выбор.")
                continue
            if enemy.is_alive():
                self.player.hp -= enemy.damage
                print(f"{enemy.name} ударил вас на {enemy.damage} урона.")
            input("\nEnter для продолжения...")
            os.system("clear")
        if self.player.hp <= 0:
            print("Вы погибли.")
            self.running = False
        else:
            print(f"Вы победили {enemy.name}!")
    def spawn_enemy(self):
        data = random.choice(ENEMIES)
        enemy = Enemy(
            name=data["name"],
            hp=data["hp"],
            damage=data["damage"],
            description=data["description"]
        )
        return enemy
    def show_title(self):
            print("""
██████╗ ███████╗████████╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗     ██║   ██████╔╝ ╚████╔╝ 
██╔══██╗██╔══╝     ██║   ██╔══██╗  ╚██╔╝  
██║  ██║███████╗   ██║   ██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   

██████╗ ██╗   ██╗███╗   ██╗███████╗███████╗
██╔══██╗██║   ██║████╗  ██║██╔════╝██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  ███████╗
██║  ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║
██████╔╝╚██████╔╝██║ ╚████║███████╗███████║
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
""")
    def handle_loot(self):
        LOOT_POOL = [
        (Water, 1, 3),
        (Lemon, 1, 5),
        (Medkit, 1, 1),
        (Scrap, 5, 20),
        (Electro_Scrap, 1, 5),
        (Keycard, 1, 1)
        ]
        item, min_amt, max_amt = random.choice(LOOT_POOL)
        amount = random.randint(min_amt, max_amt)
        item_instance = item()
        for _ in range(amount):
            self.player.add_item(item_instance, amount)
        print(f"вы нашли: {item.__name__} x{amount}")
    def look_around(self):
        os.system("clear")
        print("Вы осматриваетесь вокруг...\n")
        roll = random.random()
        if roll < 0.5:
            print("Ничего полезного. Только песок и руины.")
        elif roll < 0.8:
            print("Вы нашли что-то незначительное.")
            self.player.add_item(Water(), 1)
            print("Получено: вода x1")
        else:
            print("Вы заметили следы. Здесь кто-то был недавно.")
        input("\nНажмите Enter, чтобы продолжить...")
        os.system("clear")
    def get_random_event(self):
        get_event = random.choice(EVENTS)
        print(f"{get_event['название']}:")
        print(f"{get_event['описание']}")
        if get_event["тип"] == "находка":
            while True:
                actions = """\n
    1. обыскать
    2. уйти"""
                print(actions)
                user = input("\nваш выбор: ")
                if user == "1":
                    self.handle_loot()
                    break
                elif user == "2":
                    os.system("clear")
                    break
        if get_event["тип"] == "враг":
            enemy = self.spawn_enemy()
            print(f"\n{enemy.description}")
            self.combat(enemy)
    def get_turn(self):
        if self.player.hp < self.player.max_hp:
            self.player.tick("+TH", 1)
        self.update()
        self.player.turns += 1
        self.game_turns += 1
        return self.get_random_event()
    def run(self):
        def clear():
            os.system("clear")
        while True:
            self.show_title()
            actions = """
    1. начать игру
    2. выход из игры"""
            print(actions)
            user = input("\nваш выбор: ")
            if user == "1":
                def clear():
                    os.system("clear")
                clear()
                while True:
                    print("введите своё имя...\n")
                    user = input("ваше имя: ")
                    if user == " " or user == "" or user.isdigit():
                        print("введи нормальное имя! имя не должно содержать пробелов или цыфр")
                        time.sleep(3)
                        clear()
                    else:
                        self.player.name = user
                        clear()
                        break
                while True:
                    text = """
--------------------------------------------------------------
1. штурмовик       | 7. кочевник       | 13. проклятый песком
2. танк            | 8. медик          | 14. никто
3. снайпер         | 9. химик          | 15. повторённый
4. тактик          | 10. киберфрагмент |----------------------
5. навигатор       | 11. перегруженный | nn. nn
6. оператор дронов | 12. архивист      | nn. nn
--------------------------------------------------------------"""
                    print(f"\nвыбирите класс персонажа...\n")
                    print(f"\n{text}")
                    user = input("ваш выбор: ")
                    match user:
                        case "1":
                            self.player.player_class = "штурмовик"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "2":
                            self.player.player_class = "танк"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "3":
                            self.player.player_class = "снайпер"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "4":
                            self.player.player_class = "тактик"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "5":
                            self.player.player_class = "навигатор"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "6":
                            self.player.player_class = "оператор дронов"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "7":
                            self.player.player_class = "кочевник"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "8":
                            self.player.player_class = "медик"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "9":
                            self.player.player_class = "химик"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "10":
                            self.player.player_class = "киберфрагмент"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "11":
                            self.player.player_class = "перегруженный"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "12":
                            self.player.player_class = "архивист"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "13":
                            self.player.player_class = "проклятый песком"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "14":
                            self.player.player_class = "никто"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case "15":
                            self.player.player_class = "повторённый"
                            self.player.init_player()
                            os.system("clear")
                            break
                        case _:
                            print("выбери класс из списка!")
                            time.sleep(2)
                            clear()
                self.show_title()
                running = True
                while running == True:
                    actions = """\n
    1. продолжить путь
    2. осмотреться
    3. инвентарь
    4. статус персонажа
    5. отдых
    6. выйти в меню"""
                    print(actions)
                    user = input("\nваш выбор: ")
                    if user == "1":
                        os.system("clear")
                        self.get_turn()
                    elif user == "2":
                        self.look_around()
                    elif user == "3":
                        def clear():
                            os.system("clear")
                        while True:
                            clear()
                            self.player.open_inventory()
                            text = """
1. закрыть инвентарь | 2. выкинуть предмет"""
                            print(f"{text}")
                            user = input("\nваш выбор: ")
                            if user == "1":
                                clear()
                                break
                            elif user == "2":
                                os.system("clear")
                                self.player.add_item("lemon", 10)
                                self.player.items_list()
                                name = input("что бы вы хотели выкинуть: ")
                                value = input("сколько бы вы хотели выкинуть: ")
                                self.player.drop_item(name, value)
                    elif user == "4":
                        while True:
                            os.system("clear")
                            self.player.stata()
                            text = """
1. закрыть статистику"""
                            print(text)
                            user = input("\nваш выбор: ")
                            if user == "1":
                                os.system("clear")
                                break
                            else:
                                print("выбери то что есть в списке!")
                                time.sleep(3)
                                os.system("clear")
                    elif user == "5":
                        self.player.rest()
                    elif user == "6":
                        os.system("clear")
                        break
                    else:
                        print("выбери вариант который есть в меню!")
                        time.sleep(3)
                        clear()
                    if self.game_turns == 1001:
                        os.system("clear")
                        self.achievements["прошёл игру"] = "пройти 1000 ходов в Retry Dunes."
                        text = """
            -------------------------------
                   новое достижение!
            -------------------------------
            
            пройти 1000 ходов в Retry Dunes
            
            -------------------------------
            
            поздравляю ты прошёл мою игру:)
            
            -------------------------------"""
                        while True:
                            print(text)
                            actions = """\n\n
            1. забрать награду"""
                            print(actions)
                            user = input("\nваш выбор: ")
                            if user == "1":
                                os.system("clear")
                                break
                            else:
                                print("заберите достижение что бы продолжить!")
                                time.sleep(2)
                                os.system("clear")
                    if self.game_turns >= 1001:
                        os.system("clear")
                        print("\nВы дошли до конца пути.")
                        print("игра окончена")
                        while True:
                            actions = """
1. выйти"""
                            print(actions)
                            user = input("\nваш выбор: ")
                            if user == "1":
                                os.system("clear")
                                running = False
                                break
                            else:
                                os.system("clear")
                                print("ваша игра завершена вв можете только выйти.")
                                time.sleep(2)
            elif user == "2":
                clear()
                self.running = False
                break
            else:
                print("выбери нужный вариант в меню из тех что есть")
                time.sleep(2)
                clear()
    def update(self):
        self.step += 1
        effects = self.player.effects
        for i in list(self.player.effects.keys()):
            effects[i] -= 1
            if effects[i] <= 0:
                del effects[i]
    def change_location(self, location_name):
        self.location = location_name
        
if __name__ == "__main__":
    main = Game(True)
    main.run()