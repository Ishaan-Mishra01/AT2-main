from character import Character
import random

class Rogue(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Rogue", 7)
        self.max_stamina = 110
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 15
        self.strength = 18
        self.max_hp = max_hp-20
        self.current_hp = max_hp-20
        self.attacks = {
            "Basic Attack": {"method": self.basic_attack, "stamina_cost": 10},
            "Crippling Strike": {"method": self.crippling_strike, "stamina_cost": 25},
            "Dagger Throw": {"method": self.dagger_throw, "stamina_cost": dagger_throw_stamina},
            "Random Vials": {"method": self.random_vials, "stamina_cost": 15},
            "Shadow Cloak": {"method": self.shadow_cloak, "stamina_cost": 5},
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
        damage = self.strength*self.level
        target.take_damage(damage)  # Apply damage to the target
        return damage  # Return the amount of damage dealt
    
    def basic_attack(self, target):
        damage = self.strength  
        print(f"{self.name} performs a basic attack on {target} for {damage} damage!")
        target.take_damage(damage)

    def crippling_strike(self, target):
        damage = self.strength*2.5
        target.take_damage(damage)
        print(f"{self.name} performs a crippling strike on {target} for {damage} damage!")
    
    def dagger_throw(self, target):
        num_of_daggers = random.randint(1,7)
        if num_of_daggers == 1:
            damage = self.strength - 3
            dagger_throw_stamina = 5
        elif num_of_daggers == 2:
            damage = (self.strength - 3)*2
            dagger_throw_stamina=11
        elif num_of_daggers == 3:
            damage = (self.strength - 3)*3
            dagger_throw_stamina = 15
        elif num_of_daggers == 4:
            damage = (self.strength - 3)*4
            dagger_throw_stamina = 22
        elif num_of_daggers ==5:
            damage = (self.strength - 3)*5
            dagger_throw_stamina = 30
        elif num_of_daggers == 6:
            damage = (self.strength - 3)*6
            dagger_throw_stamina = 37
        else:
            damage = (self.strength - 3)*7
            dagger_throw_stamina = 45

