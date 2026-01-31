class Enemy:
    def __init__(self, name, hp, damage, description=""):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.description = description

    def is_alive(self):
        return self.hp > 0