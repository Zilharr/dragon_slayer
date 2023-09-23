# dragon_slayer
A short demonstration of using classes/inheritance/polymorphism in python.

With a few inputs the user will generate a random weapon type with a random name and element. All inputs will have error handling.

1) The user selects a class i.e. Wizard, Warrior, Rogue, or Priest
2) The user inputs a class-specific stat like strength or intelligence
3) The class-specific class is created and based on the random chance derived from the class-specific stat a weapon is created and a random name and element are assigned
4) The result is printed to the terminal

9/23/2023

Randomized class-based game that involves dragons...of course.

Update random_weapon_generator to include randomized damage to the weapon, lock level to random between 1-10, and lock stats to range determined by level.

Weapon damage is independent of other variables besides weapon type and element.
Stats will fall between 1 and (level * multiplier). a. The Health multiplier will be 10. b. The Stat multiplier will be 2.
Dragons will be generated randomly by a Dragon class and damage will be dictated by elemental opposition to the random_weapon_generator.

For example, a fire dragon would deal half the damage to a Hero with a water element but double the damage to a Hero with an earth element. One caveat is, that light and darkness deal double the damage to each other. This also holds true for damage dealt by the Hero towards the Dragon. a. Fire -> Earth 2x b. Earth -> Wind 2x c. Wind -> Water 2x d. Water -> Fire 2x e. Light -> Darkness 2x f. Darkness -> Light 2x
If the attacker is not using an opposing element then damage will be the base damage.
The attacker will receive 25% of damage dealt as health if the element is stronger than the opponent.
There will be 3 Dragons that must be defeated to win the game. Each dragon fight will be considered a round. At the end of each round, the player will heal 50% of their total health and their level will increase by 2. Dragon health will be determined randomly between 70-100 health points and base damage of 10-15.
