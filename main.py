import random

class Hero:
    def __init__(self, role):
        self.__role = role

    def get_role(self):
        return self.__role
    
    def get_level(self):
        level = random.randint(1,11)
        return level
    
    def get_health(self, level):
        health = level * 10
        return health
    
class Dragon:
    def __init__(self, level, health, damage):
        self.__level = level
        self.__health = health
        self.__damage = damage
    
    def get_level(self):
        final_level = random.randint(1, self.__level)
        return final_level
    
    def get_health(self, level):
        final_health = int(((level * self.__health) / 2))
        return final_health
    
    def get_damage(self):
        final_damage = random.randint(self.__damage, int((self.__damage * 1.5)))
        return final_damage
    
    def get_element(self):
        element = elemental()
        return element
    
class Warrior(Hero):
    def __init__(self, role):
        super().__init__(role)

    def get_stat(self, level):
        strength = random.randint(1, level) * 2
        return strength
    
    def get_weapon(self, stat):
        chance = random.randint(1, stat)
        if chance < 3:
            weapon = list(weapons.keys()) [list(weapons.values()).index(2)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 6:
            weapon = list(weapons.keys()) [list(weapons.values()).index(5)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 9:
            weapon = list(weapons.keys()) [list(weapons.values()).index(8)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        else:
            weapon = list(weapons.keys()) [list(weapons.values()).index(12)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
    
    def damage(self, stat, weapon):
        damage = (stat * 3) + weapons.get(weapon[1])
        return damage
    
class Wizard(Hero):
    def __init__(self, role):
        super().__init__(role)

    def get_stat(self, level):
        intelligence = random.randint(1, level) * 2
        return intelligence
    
    def get_weapon(self, stat):
        chance = random.randint(1, stat)
        if chance < 9:
            weapon = list(weapons.keys()) [list(weapons.values()).index(9)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        else:
            weapon = list(weapons.keys()) [list(weapons.values()).index(13)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
    
    def damage(self, stat, weapon):
        damage = (stat * 3) + weapons.get(weapon[1])
        return damage

class Priest(Hero):
    def __init__(self, role):
        super().__init__(role)

    def get_stat(self, level):
        wisdom = random.randint(1, level) * 2
        return wisdom
    
    def get_weapon(self, stat):
        chance = random.randint(1, stat)
        if chance < 3:
            weapon = list(weapons.keys()) [list(weapons.values()).index(2)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 6:
            weapon = list(weapons.keys()) [list(weapons.values()).index(5)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 9:
            weapon = list(weapons.keys()) [list(weapons.values()).index(12)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        else:
            weapon = list(weapons.keys()) [list(weapons.values()).index(13)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
    
    def damage(self, stat, weapon):
        damage = (stat * 3) + weapons.get(weapon[1])
        return damage
    
class Rogue(Hero):
    def __init__(self, role):
        super().__init__(role)

    def get_stat(self, level):
        dexterity = random.randint(1, level) * 2
        return dexterity
    
    def get_weapon(self, stat):
        chance = random.randint(1, stat)
        if chance < 3:
            weapon = list(weapons.keys()) [list(weapons.values()).index(2)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 6:
            weapon = list(weapons.keys()) [list(weapons.values()).index(5)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        elif chance < 9:
            weapon = list(weapons.keys()) [list(weapons.values()).index(10)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
        else:
            weapon = list(weapons.keys()) [list(weapons.values()).index(15)]
            element = elemental()
            name = weapon_name()
            return name, weapon, element
    
    def damage(self, stat, weapon):
        damage = (stat * 3) + weapons.get(weapon[1])
        return damage

weapons = {'Dagger' : 2, 'Sword' : 5, 'Polearm' : 8, 'Warhammer' : 12, 'Wand' : 9, 'Staff' : 13, 'Short Bow' : 10, 'Long Bow' : 15}

def elemental():
    element = ['Fire', 'Water', 'Wind', 'Earth', 'Light', 'Darkness']
    return random.choice(element)

def weapon_name():
    name = ['Carnivorous', 'Bloodied', "Savior's", 'Breaker', 'Diabolical', 'Tormenting', 'Heavenly', 'Mysterious', 'Menacing']
    return random.choice(name)

def hero_attack(weapon, health, damage, dragon_health, dragon_element):
    if (weapon[2] == "Fire" and dragon_element == "Earth" or
        weapon[2] == "Wind" and dragon_element == "Water" or
        weapon[2] == "Earth" and dragon_element == "Wind" or
        weapon[2] == "Water" and dragon_element == "Fire" or
        weapon[2] == "Light" and dragon_element == "Darkness" or
        weapon[2] == "Darkness" and dragon_element == "Light"):
            total_damage = int(damage * 2)
            dragon_health -= total_damage
            health += int((total_damage) * .25)
            return health, dragon_health
    elif (weapon[2] == "Earth" and dragon_element == "Fire" or
            weapon[2] == "Water" and dragon_element == "Wind" or
            weapon[2] == "Wind" and dragon_element == "Earth" or
            weapon[2] == "Fire" and dragon_element == "Water"):
                total_damage = int(damage * 0.5)
                dragon_health -= total_damage
                return health, dragon_health
    else:
        dragon_health -= damage
        return health, dragon_health
    
def dragon_attack(weapon, health, dragon_element, dragon_damage, dragon_health):
    if (dragon_element == "Fire" and weapon[2] == "Earth" or
        dragon_element == "Wind" and weapon[2] == "Water" or
        dragon_element == "Earth" and weapon[2] == "Wind" or
        dragon_element == "Water" and weapon[2] == "Fire" or
        dragon_element == "Light" and weapon[2] == "Darkness" or
        dragon_element == "Darkness" and weapon[2] == "Light"):
            total_damage = int(dragon_damage * 2)
            health -= total_damage
            dragon_health += int((total_damage) * .25)
            return dragon_health, health
    elif (dragon_element == "Earth" and weapon[2] == "Fire" or
            dragon_element == "Water" and weapon[2] == "Wind" or
            dragon_element == "Wind" and weapon[2] == "Earth" or
            dragon_element == "Fire" and weapon[2] == "Water"):
                total_damage = int(dragon_damage * 0.5)
                health -= total_damage
                return dragon_health, health
    else:
        health -= int(dragon_damage)
        return dragon_health, health
    
def battle(weapon, health, damage, class_title, dragon_damage, dragon_health, dragon_element):
    while health > 0 or dragon_health > 0:
        result = hero_attack(weapon, health, damage, dragon_health, dragon_element)
        health, dragon_health = result
        if dragon_health <= 0:
            print(f'{class_title} Health: {"0" if result[0] <= 0 else result[0]} {dragon_element} Dragon Health: {"0" if result[1] <= 0 else result[1]}')
            return health, dragon_health
        print(f'{class_title} Health: {"0" if result[0] <= 0 else result[0]} {dragon_element} Dragon Health: {"0" if result[1] <= 0 else result[1]}')

        dragon_result = dragon_attack(weapon, health, dragon_element, dragon_damage, dragon_health)
        dragon_health, health = dragon_result
        if health <= 0:
            print(f'{dragon_element} Dragon Health: {"0" if dragon_result[0] <= 0 else dragon_result[0]} {class_title} Health: {"0" if dragon_result[1] <= 0 else dragon_result[1]}')
            return health, dragon_health
        print(f'{dragon_element} Dragon Health: {"0" if dragon_result[0] <= 0 else dragon_result[0]} {class_title} Health: {"0" if dragon_result[1] <= 0 else dragon_result[1]}')
    
def heal_increase_health(health, level, class_title):
    level += 2
    if health < ((level * 10) / 2):
        health = int(((level * 10) / 2))
        print(f'\n{class_title} Health: {health}\n')
        return health, level
    else:
        print(f'\n{class_title} Health: {health}\n')
        return health, level
    
def main():
    class_list = ['Priest', 'Warrior', 'Wizard', 'Rogue']
    while True:
        print('Choice of class: Priest, Warrior, Wizard, Rogue...')
        class_select = str(input('Enter your class: '))
        class_title = class_select.title()
        if class_title in class_list:
            print(f'{class_title} selected...')
            break;
        else:
            print('Enter valid class')
            continue
    
    if class_title == 'Warrior':
        warrior = Warrior(class_title)
        level = warrior.get_level()
        health = warrior.get_health(level)
        stat = warrior.get_stat(level)
        weapon = warrior.get_weapon(stat)
        damage = warrior.damage(stat, weapon)
        print(f'\nHero Class: {warrior.get_role()} \nHero Level: {level} \nHero Weapon: {weapon[0]} {weapon[1]} of {weapon[2]} \nHero Health: {health} \nHero Base Damage: {damage}')

    if class_title == 'Wizard':
        wizard = Wizard(class_title)
        level = wizard.get_level()
        health = wizard.get_health(level)
        stat = wizard.get_stat(level)
        weapon = wizard.get_weapon(stat)
        damage = wizard.damage(stat, weapon)
        print(f'\nHero Class: {wizard.get_role()} \nHero Level: {level} \nHero Weapon: {weapon[0]} {weapon[1]} of {weapon[2]} \nHero Health: {health} \nHero Base Damage: {damage}')

    if class_title == 'Priest':
        priest = Priest(class_title)
        level = priest.get_level()
        health = priest.get_health(level)
        stat = priest.get_stat(level)
        weapon = priest.get_weapon(stat)
        damage = priest.damage(stat, weapon)
        print(f'\nHero Class: {priest.get_role()} \nHero Level: {level} \nHero Weapon: {weapon[0]} {weapon[1]} of {weapon[2]} \nHero Health: {health} \nHero Base Damage: {damage}')

    if class_title == 'Rogue':
        rogue = Rogue(class_title)
        level = rogue.get_level()
        health = rogue.get_health(level)
        stat = rogue.get_stat(level)
        weapon = rogue.get_weapon(stat)
        damage = rogue.damage(stat, weapon)
        print(f'\nHero Class: {rogue.get_role()} \nHero Level: {level} \nHero Weapon: {weapon[0]} {weapon[1]} of {weapon[2]} \nHero Health: {health} \nHero Base Damage: {damage}')

    print('\nThree Dragons have been summoned...')
    # Dragon One
    dragon_one = Dragon(3, 50, 10)
    dragon_one_level = dragon_one.get_level()
    dragon_one_health = dragon_one.get_health(dragon_one_level)
    dragon_one_damage = dragon_one.get_damage()
    dragon_one_element = dragon_one.get_element()

    #Dragon Two
    dragon_two = Dragon(5, 60, 15)
    dragon_two_level = dragon_two.get_level()
    dragon_two_health = dragon_two.get_health(dragon_two_level)
    dragon_two_damage = dragon_two.get_damage()
    dragon_two_element = dragon_two.get_element()

    #Dragon Three
    dragon_three = Dragon(7, 70, 20)
    dragon_three_level = dragon_three.get_level()
    dragon_three_health = dragon_three.get_health(dragon_three_level)
    dragon_three_damage = dragon_three.get_damage()
    dragon_three_element = dragon_three.get_element()


    print(f'\n{dragon_one_element} Dragon Level: {dragon_one_level} {dragon_one_element} Dragon Health: {dragon_one_health} {dragon_one_element} Dragon Base Damage: {dragon_one_damage}')
    print(f'\n{dragon_two_element} Dragon Level: {dragon_two_level} {dragon_two_element} Dragon Health: {dragon_two_health} {dragon_two_element} Dragon Base Damage: {dragon_two_damage}')
    print(f'\n{dragon_three_element} Dragon Level: {dragon_three_level} {dragon_three_element} Dragon Health: {dragon_three_health} {dragon_three_element} Dragon Base Damage: {dragon_three_damage}\n')
    
    #Battle
    health, dragon_one_health = battle(weapon, health, damage, class_title, dragon_one_damage, dragon_one_health, dragon_one_element)
    if health > 0:
        health, level = heal_increase_health(health, level, class_title)
    if health > 0:
        health, dragon_two_health = battle(weapon, health, damage, class_title, dragon_two_damage, dragon_two_health, dragon_two_element)
    if health > 0:
        health, level = heal_increase_health(health, level, class_title)
    if health > 0:
        health, dragon_three_health = battle(weapon, health, damage, class_title, dragon_three_damage, dragon_three_health, dragon_three_element)
    if health > 0:
        print("\nThe Hero is Triumpant!")
    else:
        print("\nHero Defeated!")
           
if __name__ == "__main__":
    main()