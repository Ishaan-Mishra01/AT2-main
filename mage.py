from character import Character
import random

class Mage(Character):
    def __init__(self, name, max_hp):
        super().__init__(name, "Mage", 5)
        self.max_stamina = 200
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 10
        self.strength = 15
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attacks = {
            "Basic Attack": {"method": self.basic_attack, "stamina_cost": 10},
            "Lightning Strike": {"method": self.lightning_strike, "stamina_cost": 30},
            "ORB OF HELLFIRE": {"method": self.orb_of_hellfire, "stamina_cost": 50},
            "Healing Aura": {"method": self.healing_aura, "stamina_cost": 20},
            "Staff Stab": {"method": self.staff_stab, "stamina_cost": 20},
        }

    def choose_attack(self, target):
        print(f"Choose an attack (Current mana: {self.current_stamina}):")
        attack_list = list(self.attacks.items())
        for i, (attack, info) in enumerate(attack_list):
            print(f"{i + 1}. {attack} (stamina cost: {info['stamina_cost']})")
        chosen_attack = int(input("Enter the number of the attack: "))
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
            else:
                self.display_message("Not enough mana for this attack.")
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
        self.display_message(f"{self.name} casts a basic attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

    def lightning_strike(self, target):
        strikes = random.randint(1, 3)
        damage = self.strength * strikes
        self.display_message(f"{self.name} struck {target.name} {strikes} time(s) with lightning for {damage} damage!")
        target.take_damage(damage)

    def orb_of_hellfire(self, target):
        roll = random.randint(1, 20)
        if roll == 20:
            self.display_message(f"{self.name} rolled a nat 20 and will land a critical hit!")
            damage = self.strength * 5 + self.strength
            target.take_damage(damage)
            self.display_message(f"{self.name} casts 'ORB OF HELLFIRE' on {target.name}, dealing {damage} damage!")
        elif 15 <= roll < 20:
            damage = self.strength * 5
            target.take_damage(damage)
            self.display_message(f"{self.name} casts 'ORB OF HELLFIRE' on {target.name}, dealing {damage} damage!")
        else:
            damage = self.strength * 5
            self_damage = self.strength / 3
            target.take_damage(damage)
            self.take_damage(self_damage)
            self.display_message(f"{self.name} casts 'ORB OF HELLFIRE' on {target.name}, dealing {damage} damage!")
            self.display_message(f"{self.name} took {self_damage} fire damage from the spell.")

    def healing_aura(self, target):
        healing = self.strength * 3
        self.display_message(f"{self.name} uses 'Healing Aura' and heals for {healing} HP!")
        self.current_hp = min(self.current_hp+healing,self.max_hp)

    def staff_stab(self, target):
        roll = random.randint(1,20)
        if roll == 20:
            self.display_message(f"{self.name} rolled a nat 20 and will land a critical hit!")
            damage = self.strength * 4
            self.display_message(f"{self.name} performs a critical 'Staff Stab' on {target.name}, dealing {damage} damage!")
            target.take_damage(damage)
        elif 15<=roll<20:
            damage = self.strength*3
            self.display_message(f"{self.name} performs a strong 'Staff Stab' on {target.name}, dealing {damage} damage!")
            target.take_damage(damage)
        elif 10<roll<15:
            damage = self.strength*2
            self.display_message(f"{self.name} performs 'Staff Stab' on {target.name}, dealing {damage} damage!")
            target.take_damage(damage)
        else:
            damage = self.strength
            self.display_message(f"{self.name} performs a weak 'Staff Stab' on {target.name}, dealing {damage} damage!")
            self.display_message(f"{self.name} hits themselves with the staff dealing {damage} self damage!")
            target.take_damage(damage)
            self.take_damage(damage)

        # Accessor methods (getters)
    def get_max_stamina(self):
        return self.max_stamina

    def get_current_stamina(self):
        return self.current_stamina

    def get_stamina_regeneration(self):
        return self.stamina_regeneration

    def get_max_hp(self):
        return self.max_hp

    def get_strength(self):
        return self.strength

    def get_current_hp(self):
        return self.current_hp

    def get_attacks(self):
        return self.attacks

    # Mutator methods (setters)
    def set_max_stamina(self, max_stamina):
        self.max_stamina = max_stamina

    def set_current_stamina(self, current_stamina):
        self.current_stamina = current_stamina

    def set_stamina_regeneration(self, stamina_regeneration):
        self.stamina_regeneration = stamina_regeneration

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp

    def set_strength(self, strength):
        self.strength = strength

    def set_current_hp(self, current_hp):
        self.current_hp = current_hp

    def set_attacks(self, attacks):
        self.attacks = attacks
