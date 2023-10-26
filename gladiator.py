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
        self.atk = 1
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
        rounded_amount = round(amount)
        if rounded_amount == 0:
            amount += 1
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
        #self.type should equal 'item', 'armor', or 'weapon'
    def use_potion(self,target):
        if self.type == 'potion':
            target.hp += 10
            print('{name} swigged a potion in the heat of battle. They gained 5 health and now have {hp} health remaining'.format(name = target.name, hp = target.hp))
    def equip_armor(self,armor,target):
        #armor variable should equal 'light', 'medium', or 'heavy'; changes target.defense to a specified integer to divide damage by
        if self.type == 'armor':
            if armor == 'light':
                target.defense = 1
            elif armor == 'medium':
                target.defense = 1.25
                target.speed += 1
            elif armor == 'heavy':
                target.defense = 1.5
                target.speed += 2
                # armor types light, medium, and heavy give 1, 1.5, and 2 (?) to defense (damage reduction) and speed
    def equip_weapon(self,weapon,target):
        # weapon types quick, balanced, and slow give 0.5, 1, and 1.5 to damage done and speed
        if self.type == 'weapon':
            if weapon == 'quick':
                target.atk = 0.5
                target.speed = 2
            if weapon == 'balanced':
                target.atk = 1
                target.speed = 3
            if weapon == 'slow':
                target.atk = 1.5
                target.speed = 4


class Profession:
    pass

def combat_turns(player,opponent):
    while player.hp > 0 and opponent.hp > 0:
        for num in range(1,13):
            turn = num
            if turn % 2 == 0 and turn % 3 == 0 and turn % 4 == 0:
                #would be replaced with gladiator.attack() based on weapon type
                
                print(str(turn) + ' - Quick Attack')
                print(str(turn) + ' - Balanced Attack')
                print(str(turn) + ' - Heavy Attack')
            elif turn % 2 ==0 and turn % 4 == 0:
                print(str(turn) + ' - Quick Attack')
                print(str(turn) + ' - Heavy Attack')
            elif turn % 2 ==0 and turn % 3 ==0:
                print(str(turn) + ' - Quick Attack')
                print(str(turn) + ' - Balanced Attack')
            elif turn % 2 ==0:
                print(str(turn) + ' - Quick Attack')
            elif turn % 3 ==0:
                print(str(turn) + ' - Balanced Attack')
            elif turn % 4 ==0:
                print(str(turn) + ' - Heavy Attack')
