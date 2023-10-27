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
        self.armor = 5 #target "roll" for a hit to meet
        self.defense = 1 #incoming damage reduction
        self.atk = 1 #outgoing damage multiplier
        self.speed = 3 #when gladiator will act in the rounds iteration
        self.is_alive = True
        self.inventory = []
        self.profession = ''
        self.soldier_bonus = 0 #0 by default unless gladiator has the 'soldier' profession
        self.is_lucky = False
    def __repr__(self):
        return '''
    {name} is a gladiator who used to be a {profession}. 
    They have {hp} health remaining out of {maxhp}.  Their inventory includes {inventory}.
    Their stats are {armor} armor, {defense} damage reduction, {atk} damage multiplier, and {speed} speed. With a damage bonus of {damage_bonus}.
    Are they alive? {is_alive}. Are they lucky? {is_lucky}.
    '''.format(name = self.name, profession = self.profession, hp = self.hp, maxhp = self.maxhp, inventory = self.inventory, armor = self.armor, defense = self.defense, atk = self.atk, speed = self.speed, damage_bonus = self.soldier_bonus, is_alive = self.is_alive, is_lucky = self.is_lucky)
    def gain_item(self,item):
        #item should be an instance of the Item class
        self.inventory.append(item.name)
    def drink_potion(self):
        if 'potion' in self.inventory:
            self.inventory.remove('potion')
            potion.use_potion(self)
    def has_died(self):
        self.is_alive = False
        if self.hp <= 0:
            print('{name} has died.'.format(name = self.name))
    def lose_health(self,amount):
        rounded_amount = round(amount/self.defense)
        if rounded_amount == 0:
            rounded_amount += 1
        self.hp -= rounded_amount
        if self.hp <= 0:
            self.hp = 0
            self.has_died()
        else:
            print('{name} took {amount} damage and now has {hp} health remaining.'.format(name = self.name, amount = rounded_amount, hp = self.hp))
    def attack(self,target):
        if self.is_alive == True:
            print('{name} {description} {target}'.format(name = self.name, description = random.choice(cool_descriptors), target = target.name))
            attack = random.randint(1,10)
            damage = random.randint(1,10)
            if attack == 9 or 10 and self.is_lucky:
                print('{name} critically injured {target}!'.format(name = self.name, target = target.name))
                damage += random.randint(1,10)
            elif attack == 10:
                print('{name} critically injured {target}!'.format(name = self.name, target = target.name))
                damage += random.randint(1,10)
            if attack >= target.armor:
                # print('{name} hit {target}!'.format(name = self.name, target = target.name))
                target.lose_health((damage * self.atk) + self.soldier_bonus)
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
            print('{name} swigged a potion in the heat of battle. They gained 10 health and now have {hp} health remaining'.format(name = target.name, hp = target.hp))
    def equip_armor(self,armor,target):
        #armor variable should equal 'light', 'medium', or 'heavy'; changes target.defense to a specified integer to divide damage by
        if self.type == 'armor':
            if armor == 'light':
                target.inventory.append('light armor')
                target.defense = 1
            elif armor == 'medium':
                target.inventory.append('medium armor')
                target.defense = 1.25
                target.speed += 1
            elif armor == 'heavy':
                target.inventory.append('heavy armor')
                target.defense = 1.5
                target.speed += 2
                # armor types light, medium, and heavy give 1, 1.5, and 2 (?) to defense (damage reduction) and speed
    def equip_weapon(self,weapon,target):
        # weapon types quick, balanced, and slow give 0.5, 1, and 1.5 to damage done and speed
        if self.type == 'weapon':
            if weapon == 'quick':
                target.inventory.append('quick {name}'.format(name = self.name))
                target.atk = 0.5
                target.speed = 2
            if weapon == 'balanced':
                target.inventory.append('balanced {name}'.format(name = self.name))
                target.atk = 1
                target.speed = 3
            if weapon == 'slow':
                target.inventory.append('slow {name}'.format(name = self.name))
                target.atk = 1.5
                target.speed = 4


class Profession:
    #'farmer', 'soldier', or 'merchant' are profession options that will be given to the player and randomly set for opponents.
    #'farmer's are hardy, gives the Gladiator increased hp and maxhp values
    #'soldier's know how to fight, give Gladiator increased damage by adding a target.damage_bonus variable equaling 2 that is added to damage rolls.
    #'merchant's are lucky, allows the Gladiator to 'crit' on a 9 and 10 instead of just a 10.
    def __init__(self,name):
        self.name = name
    def past_profession(self,target):
        if self.name == 'farmer':
            target.profession = 'farmer'
            target.hp += 10
            target.maxhp += 10
        elif self.name == 'soldier':
            target.profession = 'soldier'
            target.soldier_bonus += 2
        elif self.name == 'merchant':
            target.profession = 'merchant'
            target.is_lucky = True

def combat_turns(player,opponent):
    #begins combat with a while loop, iterates through 12 asking for player input whenever their attack comes.
    quick_attacks = 0
    balanced_attacks = 0
    while player.hp > 0 and opponent.hp > 0:
        for turn in range(1,13):
            if turn % player.speed == 0 and opponent.hp > 0:
                choice = input('The battle rages. Would you like to attack, parry, or use a potion? Please type attack, parry, or potion. ').lower()
                if choice == 'attack':
                    player.attack(opponent)
                    quick_attacks += 1
                elif choice == 'parry':
                    pass
                elif choice == 'potion':
                    player.drink_potion()
            if turn % opponent.speed == 0 and player.hp > 0:
                opponent.attack(player)
                balanced_attacks += 1
    print('There were ' + str(quick_attacks) + ' quick attacks.')
    print('There were ' + str(balanced_attacks) + ' balanced attacks.')
    

farmer = Profession('farmer')
soldier = Profession('soldier')
merchant = Profession('merchant')
armor = Item('armor','armor')
spear = Item('weapon','spear')
shortsword = Item('weapon','shortsword')
potion = Item('potion','potion')


opponent = Gladiator('Bot')
farmer.past_profession(opponent)
spear.equip_weapon('balanced',opponent)
armor.equip_armor('medium',opponent)
opponent.gain_item(potion)

player = Gladiator('Dalton')
soldier.past_profession(player)
shortsword.equip_weapon('quick',player)
armor.equip_armor('light',player)
player.gain_item(potion)

print(opponent)
print(player)

combat_turns(player,opponent)

print(opponent)
print(player)