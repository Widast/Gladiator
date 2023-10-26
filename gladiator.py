import random

cool_descriptors = ['swings their blade down on','lunges forward at','angles a precise strike at','roars in fury at']
opponent_random_names = ['Gluteus Maximus','Jeffrey','Steve','Scarr','Mama Mildred','Maximus Decimus Meridius']

def attack():
    print('An attack just happened.')

class Gladiator:
    def __init__(self,name):
        self.name = name
        self.hp = 25
        self.maxhp = 25
        self.armor = 5
        self.defense = 1
        self.speed = 3
        self.is_alive = True
        self.inventory = []
        self.profession = ''
    def __repr__(self):
        return '{name} is a {profession}. They have {hp} health remaining out of {maxhp}'
    def attack(self,target):
        #this will have the Gladiator attempt to attack their target and trigger the target to take damage
        pass
    def has_died(self):
        self.is_alive = False
        if self.hp <= 0:
            print('{name} has died.'.format(name = self.name))
    def lose_health(self,amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.has_died()
        else:
            print('{name} took {amount} damage and now has {hp} health remaining.'.format(name = self.name, amount = amount, hp = self.hp))
    def attack(self,target):
        if self.is_alive == True:
            print('{name} {description} {target}'.format(name = self.name, description = random.choice(cool_descriptors), target = target.name))
            attack = random.randint(1,10)
        if attack >= target.ac:
            print('{name} hit {target}!'.format(name = self.name, target = target.name))
            target.lose_health(random.randint(1,10))
        else:
            print('{target} dodged {name}\'s attack!'.format(target = target.name, name = self.name))


class Item:
    def __init__(self,type,name):
        self.name = name
        self.type = type
    def use_potion(self,target):
        if self.type == 'potion':
            target.hp += 10
            print('{name} swigged a potion in the heat of battle. They gained 5 health and now have {hp} health remaining'.format(name = target.name, hp = target.hp))
    def equip_armor(self,armor,target):
        if self.type == 'armor':
            if armor == 'light':
                pass
                # armor types light, medium, and heavy give 1, 1.5, and 2 (?) to defense (damage reduction) and speed
                # target.defense += 
    def equip_weapon(self,weapon,target):
        # weapon types quick, balanced, and slow give 0.5, 1, and 1.5 to damage done and speed
        pass


class Profession:
    pass

