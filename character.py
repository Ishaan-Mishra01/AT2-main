class Character():
    MAX_LEVEL = 50  # Maximum level a character can reach
    ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level
    name = None
    character_class = None
    armor = None  # Character's armor value
    level = None  # Character's current level
    experience_points = None  # Character's current experience points
    hit_points = None  # Example starting value for character's hit points
    armor_class = None  # Example starting value for character's armor class
    skills = {}  # Example empty dictionary for character's skills
    inventory = []
    gold = None 
    max_hp = 100
    max_stamina = 100
    stamina = 100


    def __init__(self, name, character_class, armor):
        self.name = name  # Character's name
        self.character_class = character_class  # Character's class
        self.armor = armor  # Character's armor value
        self.level = 1  # Character's current level
        self.experience_points = 0  # Character's current experience points
        self.hit_points = 50  # Example starting value for character's hit points
        self.armor_class = 10  # Example starting value for character's armor class
        self.skills = {}  # Example empty dictionary for character's skills
        self.inventory = []  # Example empty list for character's inventory
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate
        self.max_hp = 50  # Maximum hit points for the character
        self.max_stamina = 50
        self.stamina = 50


    #accessors
    def getMAXLEVEL(self):
        return self.MAX_LEVEL

    def getATTRIBUTEPOINTSPERLEVEL(self):
        return self.ATTRIBUTE_POINTS_PER_LEVEL

    def getName(self):
        return self.name

    def getCharacterclass(self):
        return self.character_class

    def getArmor(self):
        return self.armor

    def getLevel(self):
        return self.level

    def getExperiencepoints(self):
        return self.experience_points

    def getHitpoints(self):
        return self.hit_points

    def getArmorclass(self):
        return self.armor_class

    def getSkills(self):
        return self.skills

    def getInventory(self):
        return self.inventory

    def getGold(self):
        return self.gold
    
    #mutators
    def setMAXLEVEL(self, newMAXLEVEL):
        self.MAX_LEVEL = newMAXLEVEL

    def setATTRIBUTEPOINTSPERLEVEL(self, newATTRIBUTEPOINTSPERLEVEL):
        self.ATTRIBUTE_POINTS_PER_LEVEL = newATTRIBUTEPOINTSPERLEVEL

    def setName(self, newName):
        self.name = newName

    def setCharacterclass(self, newCharacterclass):
        self.character_class = newCharacterclass

    def setArmor(self, newArmor):
        self.armor = newArmor

    def setLevel(self, newLevel):
        self.level = newLevel

    def setExperiencepoints(self, newExperiencepoints):
        self.experience_points = newExperiencepoints

    def setHitpoints(self, newHitpoints):
        self.hit_points = newHitpoints

    def setArmorclass(self, newArmorclass):
        self.armor_class = newArmorclass

    def setSkills(self, newSkills):
        self.skills = newSkills

    def setInventory(self, newInventory):
        self.inventory = newInventory

    def setGold(self, newGold):
        self.gold = newGold

    def assign_attribute_points(self, attribute, points):
        # Ensure the attribute exists before assigning points
        if attribute in self.__dict__:
            setattr(self, attribute, getattr(self, attribute) + points)  # Add points to the attribute
            self.attribute_points -= points  # Decrease available attribute points
        else:
            print(f"Error: Attribute '{attribute}' does not exist.")

    def gain_experience(self, experience):
        self.experience_points += experience  # Increase character's experience points
        # Calculate experience required for next level
        required_experience = self.calculate_required_experience(self.level + 1)
        # Check if character has enough experience to level up and is below the level cap
        while self.experience_points >= required_experience and self.level < self.MAX_LEVEL:
            self.level += 1  # Level up the character
            self.experience_points -= required_experience  # Decrease character's experience points
            self.max_hp += 10  # Example: Increase max hit points by 10 each level up
            self.hit_points = min(self.max_hp, self.hit_points + 10)  # Restore some health on level up
            self.attribute_points += self.ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points
            print(f"Level up! {self.name} is now level {self.level}.")
            # Calculate experience required for next level
            required_experience = self.calculate_required_experience(self.level + 1)

    def calculate_required_experience(self, level):
        # Example exponential scaling: Each level requires 100 more experience points than the previous level
        return int(100 * (1.5 ** (level - 1)))

    def is_alive(self):
        return self.hit_points > 0

    def take_damage(self, amount):
        # Calculate the actual damage taken, taking into account the character's armor
        actual_damage = max(0, amount - self.armor)
        self.hit_points -= actual_damage
        if self.hit_points <= 0:
            print(f"{self.name} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.name} takes {actual_damage} damage. Remaining hit points: {self.hit_points}")
