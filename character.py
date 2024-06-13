class Character:
    __MAX_LEVEL = 50  # Maximum level a character can reach
    __ATTRIBUTE_POINTS_PER_LEVEL = 3  # Number of attribute points gained per level
    __name = None
    __character_class = None  
    __armor = None  # Character's armor value
    __level = None  # Character's current level
    __experience_points = None  # Character's current experience points
    __hit_points = None  # Example starting value for character's hit points
    __armor_class = None  # Example starting value for character's armor class
    __skills = {}  # Example empty dictionary for character's skills
    __inventory = []
    __gold = None 

    def __init__(self, __name, __character_class, __armor):
        self.name = __name  # Character's name
        self.character_class = __character_class  # Character's class
        self.armor = __armor  # Character's armor value
        self.level = 1  # Character's current level
        self.experience_points = 0  # Character's current experience points
        self.hit_points = 10  # Example starting value for character's hit points
        self.armor_class = 10  # Example starting value for character's armor class
        self.skills = {}  # Example empty dictionary for character's skills
        self.inventory = []  # Example empty list for character's inventory
        self.gold = 0  # Example starting value for character's gold
        self.attribute_points = 0  # Attribute points available to allocate

    #accessors
    def getMAXLEVEL(self):
        return self.__MAX_LEVEL

    def getATTRIBUTEPOINTSPERLEVEL(self):
        return self.__ATTRIBUTE_POINTS_PER_LEVEL

    def getName(self):
        return self.__name

    def getCharacterclass(self):
        return self.__character_class

    def getArmor(self):
        return self.__armor

    def getLevel(self):
        return self.__level

    def getExperiencepoints(self):
        return self.__experience_points

    def getHitpoints(self):
        return self.__hit_points

    def getArmorclass(self):
        return self.__armor_class

    def getSkills(self):
        return self.__skills

    def getInventory(self):
        return self.__inventory

    def getGold(self):
        return self.__gold
    
    #mutators
    def setMAXLEVEL(self, newMAXLEVEL):
        self.__MAX_LEVEL = newMAXLEVEL

    def setATTRIBUTEPOINTSPERLEVEL(self, newATTRIBUTEPOINTSPERLEVEL):
        self.__ATTRIBUTE_POINTS_PER_LEVEL = newATTRIBUTEPOINTSPERLEVEL

    def setName(self, newName):
        self.__name = newName

    def setCharacterclass(self, newCharacterclass):
        self.__character_class = newCharacterclass

    def setArmor(self, newArmor):
        self.__armor = newArmor

    def setLevel(self, newLevel):
        self.__level = newLevel

    def setExperiencepoints(self, newExperiencepoints):
        self.__experience_points = newExperiencepoints

    def setHitpoints(self, newHitpoints):
        self.__hit_points = newHitpoints

    def setArmorclass(self, newArmorclass):
        self.__armor_class = newArmorclass

    def setSkills(self, newSkills):
        self.__skills = newSkills

    def setInventory(self, newInventory):
        self.__inventory = newInventory

    def setGold(self, newGold):
        self.__gold = newGold

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
        while self.experience_points >= required_experience and self.level < self.__MAX_LEVEL:
            self.level += 1  # Level up the character
            self.experience_points -= required_experience  # Decrease character's experience points
            self.hit_points += 10  # Example: Increase hit points by 10 each level up
            self.attribute_points += self.__ATTRIBUTE_POINTS_PER_LEVEL  # Allocate attribute points
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
