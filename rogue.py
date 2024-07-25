from character import Character
import random

class Rogue(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Rogue", 6)
        self.max_stamina = 110
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 15
        self.strength = 18
        self.max_hp = max_hp - 20
        self.current_hp = max_hp - 20
        self.attacks = {
            "Basic Attack": {"method": self.basic_attack, "stamina_cost": 10},
            "Shadow Strike": {"method": self.shadow_strike, "stamina_cost": 25},
            "Random Vials": {"method": self.random_vials, "stamina_cost": 15},
            "Shadow Cloak": {"method": self.shadow_cloak, "stamina_cost": 10},
            "Dagger Throw": {"method": self.dagger_throw},
        }
        self.shadow_cloak_active = False
        
    def choose_attack(self, target):
        self.display_message(f"Choose an attack (Current stamina: {self.current_stamina}):")
        attack_list = list(self.attacks.items())
        for i, (attack, info) in enumerate(attack_list):
            stamina_cost = info.get("stamina_cost", "Variable")
            self.display_message(f"{i + 1}. {attack} (Stamina cost: {stamina_cost})")
        chosen_attack = int(input("Enter the number of the attack: "))
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if attack == "Dagger Throw":
                attack_info["method"](target)
            else:
                stamina_cost = attack_info["stamina_cost"]
                if self.current_stamina >= stamina_cost:
                    self.current_stamina -= stamina_cost
                    attack_method = attack_info["method"]
                    attack_method(target)
                else:
                    self.display_message("Not enough stamina for this attack.")
        else:
            self.display_message("Invalid attack.")

    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)

    def attack(self, target):
        damage = self.strength * self.level
        target.take_damage(damage)  # Apply damage to the target
        return damage  # Return the amount of damage dealt
    
    def basic_attack(self, target):
        damage = self.strength  
        self.display_message(f"{self.name} performs a basic attack on {target} for {damage} damage!")
        target.take_damage(damage)

    def shadow_strike(self, target):
        damage = self.strength * 2.5
        self_damage = self.strength - 8
        target.take_damage(damage)
        self.display_message(f"{self.name} performs 'Shadow Strike' on {target} for {damage} damage!")
        self.display_message(f"{self.name} took {self_damage} recoil damage")

    def random_vials(self, target):
        vial = random.randint(1, 4)
        if vial == 1:
            damage = self.strength + 2
            target.take_damage(damage)
            self.display_message(f"{self.name} throws a weak damage vial on {target} for {damage} damage!")
        elif vial == 2:
            damage = self.strength * (25 / 9)
            target.take_damage(damage)
            self.display_message(f"{self.name} throws a strong damage vial on {target} for {damage} damage!")
        elif vial == 3:
            damage = self.strength - 8
            self.take_damage(damage)
            self.display_message(f"{self.name} drinks a poison vial, dealing {damage} damage!")
        else:
            self.current_hp = min(self.max_hp, self.current_hp + 15)
            self.display_message(f"{self.name} drinks a health vial, healing up to 15 HP!")

    def shadow_cloak(self, target):
        self.display_message(f"{self.name} uses Shadow Cloak, preventing any damage this turn!")
        self.shadow_cloak_active = True

    def deactivate_shadow_cloak(self):
        self.shadow_cloak_active = False

    def is_shadow_cloak_active(self):
        return self.shadow_cloak_active

    def dagger_throw(self, target):
        num_of_daggers = random.randint(1, 7)
        if num_of_daggers == 1:
            stamina_cost = 5
        elif num_of_daggers == 2:
            stamina_cost = 11
        elif num_of_daggers == 3:
            stamina_cost = 15
        elif num_of_daggers == 4:
            stamina_cost = 22
        elif num_of_daggers == 5:
            stamina_cost = 30
        elif num_of_daggers == 6:
            stamina_cost = 37
        else:
            stamina_cost = 45

        if self.current_stamina >= stamina_cost:
            self.current_stamina -= stamina_cost
            damage = (self.strength - 3) * num_of_daggers
            self.display_message(f"{self.name} throws {num_of_daggers} daggers at {target} for {damage} damage!")
            target.take_damage(damage)
        else:
            self.display_message(f"Not enough stamina to throw {num_of_daggers} daggers!")