from character import Character
import random
class Warrior(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Warrior", 10)
        self.max_stamina = 100
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.strength = 20
        self.max_hp = max_hp+50
        self.current_hp = max_hp+50
        self.attacks = {
            "Basic Attack": {"method": self.basic_attack, "stamina_cost": 10},
            "Charge": {"method": self.charge, "stamina_cost": 20},
            "Head Shot": {"method": self.head_shot, "stamina_cost": 30},
            "Shield Bash": {"method": self.shield_bash, "stamina_cost": 15},
            "Defensive Stance": {"method": self.defensive_stance, "stamina_cost": 5},
        }

    def choose_attack(self, target):
        print(f"Choose an attack (Current stamina: {self.current_stamina}):")
        attack_list = list(self.attacks.items())
        for i, (attack, info) in enumerate(attack_list):
            print(f"{i + 1}. {attack} (Stamina cost: {info['stamina_cost']})")
        chosen_attack = int(input("Enter the number of the attack: "))
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
            else:
                print("Not enough stamina for this attack.")
        else:
            print("Invalid attack.")

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)




    def attack(self, target):
        # Calculate damage based on warrior's level, strength, and any weapon modifiers
        # For simplicity, let's assume the warrior's damage is directly proportional to their level
        damage = self.strength*self.level
        target.take_damage(damage)  # Apply damage to the target
        return damage  # Return the amount of damage dealt

    def charge(self, target):
        print(f"{self.name} charges towards {target.name}!")
        target.take_damage(self.strength)  # Example: Charge deals damage equal to the warrior's strength

    def basic_attack(self, target):
        damage = self.strength  # Example: Basic attack damage equals warrior's strength
        print(f"{self.name} performs a basic attack on {target} for {damage} damage!")
        target.take_damage(damage)

    def head_shot(self, target):
        accuracy = random.randint(1,100)
        if accuracy >= 90:
            damage = self.strength * 5  # Example: 
            target.take_damage(damage)
            print(f"{self.name} quickscoped {target}, dealing {damage} damage with a head shot!")
        elif accuracy <90 and accuracy >= 75:
            damage = self.strength *3
            target.take_damage(damage)
            print(f"{self.name} pulled out a gun on {target}, dealing {damage} damage with a partially accurate head shot.")
        elif accuracy <75 and accuracy >= 50:
            damage = self.strength *1.5
            target.take_damage(damage)
            print(f"{self.name} fumbled while pulling out a gun on {target}, dealing {damage} damage due to a misfire.")
        elif accuracy <50:
            damage = self.strength *0.5
            target.take_damage(damage)
            self.take_damage(damage)
            print(f"{self.name} misfired while pulling out a gun, dealing {damage} damage to himself, and threw the gun at {target}, dealing {damage} damage.")

    def shield_bash(self, target):
        damage = (self.armor+self.armor_class) *1.5  # Example: Shield bash deals warrior's strength plus 5 additional damage
        print(f"{self.name} performs a shield bash on {target} for {damage} damage!")
        target.take_damage(damage)

    def defensive_stance(self):
        self.armor_class += 5  # Example: Defensive stance increases armor class by 5
        print(f"{self.name} enters a defensive stance, increasing armor class!")

