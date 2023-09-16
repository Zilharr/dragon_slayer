import random

class Hero:
    def __init__(self, role, level):
        self.__role = role
        self.__level = level

    def get_role(self):
        return self.__role
    
    def get_level(self):
        return self.__level
    
class Warrior(Hero):
    def __init__(self, role, level, strength):
        super().__init__(role, level)
        self.__strength = strength

    def get_stat(self):
        return self.__strength
    
    def get_weapon(self):
        war_weapons = ['Dagger', 'Sword', 'Polearm', 'Warhammer']
        chance = random.randint(0, self.__strength)
        if chance < 3:
            return f'{weapon_name()} {war_weapons[0]} of {elemental()}'
        elif chance < 5:
            return f'{weapon_name()} {war_weapons[random.randint(0,1)]} of {elemental()}'
        elif chance < 8:
            return f'{weapon_name()} {war_weapons[random.randint(0,2)]} of {elemental()}'
        return f'{weapon_name()} {war_weapons[random.randint(0,3)]} of {elemental()}'
    
class Wizard(Hero):
    def __init__(self, role, level, intelligence):
        super().__init__(role, level)
        self.__intelligence = intelligence

    def get_stat(self):
        return self.__intelligence
    
    def get_weapon(self):
        war_weapons = ['Wand', 'Staff']
        chance = random.randint(0, self.__intelligence)
        if chance < 5:
            return f'{weapon_name()} {war_weapons[0]} of {elemental()}'
        return f'{weapon_name()} {war_weapons[random.randint(0,1)]} of {elemental()}'

class Priest(Hero):
    def __init__(self, role, level, wisdom):
        super().__init__(role, level)
        self.__wisdom = wisdom

    def get_stat(self):
        return self.__wisdom
    
    def get_weapon(self):
        war_weapons = ['Staff', 'Sword', 'Club', 'Warhammer']
        chance = random.randint(0, self.__wisdom)
        if chance < 3:
            return f'{weapon_name()} {war_weapons[0]} of {elemental()}'
        elif chance < 5:
            return f'{weapon_name()} {war_weapons[random.randint(0,1)]} of {elemental()}'
        elif chance < 8:
            return f'{weapon_name()} {war_weapons[random.randint(0,2)]} of {elemental()}'
        return f'{weapon_name()} {war_weapons[random.randint(0,3)]} of {elemental()}'
    
class Rogue(Hero):
    def __init__(self, role, level, dexterity):
        super().__init__(role, level)
        self.__dexterity = dexterity

    def get_stat(self):
        return self.__dexterity
    
    def get_weapon(self):
        war_weapons = ['Dagger', 'Sword', 'Short Bow', 'Long Bow']
        chance = random.randint(0, self.__dexterity)
        if chance < 3:
            return f'{weapon_name()} {war_weapons[0]} of {elemental()}'
        elif chance < 5:
            return f'{weapon_name()} {war_weapons[random.randint(0,1)]} of {elemental()}'
        elif chance < 8:
            return f'{weapon_name()} {war_weapons[random.randint(0,2)]} of {elemental()}'
        return f'{weapon_name()} {war_weapons[random.randint(0,3)]} of {elemental()}'

def elemental():
    element = ['Fire', 'Water', 'Wind', 'Earth', 'Light', 'Darkness']
    return random.choice(element)

def weapon_name():
    name = ['Carnivorous', 'Bloodied', "Savior's", 'Breaker', 'Diabolical', 'Tormenting', 'Heavenly', 'Mysterious', 'Menacing']
    return random.choice(name)

def warrior(class_title, level_select):
    while True:
            try:
                strength = int(input('Current strength; 0 - 10: '))
                if strength >=0 and strength < 11:
                    warrior = Warrior(class_title, level_select, strength)
                    print(f'\nClass: {warrior.get_role()}\nLevel: {warrior.get_level()}\nStrength: {warrior.get_stat()}\nWeapon: {warrior.get_weapon()}\n')
                    break;
                else:
                    print('Enter valid integer...')
                    continue
            except ValueError:
                print('Enter valid integer...')

def wizard(class_title, level_select):
    while True:
            try:
                intelligence = int(input('Current intelligence; 0 - 10: '))
                if intelligence >=0 and intelligence < 11:
                    wizard = Wizard(class_title, level_select, intelligence)
                    print(f'\nClass: {wizard.get_role()}\nLevel: {wizard.get_level()}\nIntelligence: {wizard.get_stat()}\nWeapon: {wizard.get_weapon()}\n')
                    break;
                else:
                    print('Enter valid integer...')
                    continue
            except ValueError:
                print('Enter valid integer...')

def priest(class_title, level_select):
    while True:
            try:
                wisdom = int(input('Current wisdom; 0 - 10: '))
                if wisdom >=0 and wisdom < 11:
                    priest = Priest(class_title, level_select, wisdom)
                    print(f'\nClass: {priest.get_role()}\nLevel: {priest.get_level()}\nWisdom: {priest.get_stat()}\nWeapon: {priest.get_weapon()}\n')
                    break;
                else:
                    print('Enter valid integer...')
                    continue
            except ValueError:
                print('Enter valid integer...')

def rogue(class_title, level_select):
    while True:
            try:
                dexterity = int(input('Current dexterity; 0 - 10: '))
                if dexterity >=0 and dexterity < 11:
                    rogue = Rogue(class_title, level_select, dexterity)
                    print(f'\nClass: {rogue.get_role()}\nLevel: {rogue.get_level()}\nDexterity: {rogue.get_stat()}\nWeapon: {rogue.get_weapon()}\n')
                    break;
                else:
                    print('Enter valid integer...')
                    continue
            except ValueError:
                print('Enter valid integer...')
    
def main():
    class_list = ['Priest', 'Warrior', 'Wizard', 'Rogue']
    while True:
        print('Choice of class: Priest, Warrior, Wizard, Rogue...')
        class_select = str(input('Enter your class: '))
        class_title = class_select.title()
        if class_title in class_list:
            print('Class entered successfully...')
            break;
        else:
            print('Enter valid class')
            continue
    
    while True:
        try:
            level_select = int(input('Enter your current level: '))
            if type(level_select) is int:
                print('Level entered successfully...')
                break;
            else:
                print('Enter valid level...')
                continue
        except ValueError:
            print('Enter valid integer...')
    
    if class_title == 'Warrior':
        warrior(class_title, level_select)

    if class_title == 'Wizard':
        wizard(class_title, level_select)

    if class_title == 'Priest':
        priest(class_title, level_select)

    if class_title == 'Rogue':
        rogue(class_title, level_select)
           
if __name__ == "__main__":
    main()