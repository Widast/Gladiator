import random

cool_descriptors = ['swings their blade down on','lunges forward at','angles a precise strike at','roars in fury at']
line_break = '______________________________________________________________________________________________________\n'
swirly_line = '`````````````````````````````````````````````````````````````````````````````````````````````````````'
gladiator_title ="""
     _,---.              ,---.                    .=-.-.  ,---.   ,--.--------.   _,.---._                 
  _.='.'-,  \   _.-.    .--.'  \      _,..---._  /==/_ /.--.'  \ /==/,  -   , -\,-.' , -  `.   .-.,.---.   
 /==.'-     / .-,.'|    \==\-/\ \   /==/,   -  \|==|, | \==\-/\ \\==\.-.  - ,-./==/_,  ,  - \ /==/  `   \  
/==/ -   .-' |==|, |    /==/-|_\ |  |==|   _   _\==|  | /==/-|_\ |`--`\==\- \ |==|   .=.     |==|-, .=., | 
|==|_   /_,-.|==|- |    \==\,   - \ |==|  .=.   |==|- | \==\,   - \    \==\_ \|==|_ :   ;=:- |==|   '='  / 
|==|  , \_.' )==|, |    /==/ -   ,| |==|,|   | -|==| ,| /==/ -   ,|    |==|- ||==| , '='     |==|- ,   .'  
\==\-  ,    (|==|- `-._/==/-  /\ - \|==|  '='   /==|- |/==/-  /\ - \   |==|, | \==\ -    ,_ /|==|_  . ,'.  
 /==/ _  ,  //==/ - , ,|==\ _.\=\.-'|==|-,   _`//==/. /\==\ _.\=\.-'   /==/ -/  '.='. -   .' /==/  /\ ,  ) 
 `--`------' `--`-----' `--`        `-.`.____.' `--`-`  `--`           `--`--`    `--`--''   `--`-`--`--'  
"""


class Gladiator:
    def __init__(self,name):
        self.name = name
        self.hp = 25
        self.maxhp = 25
        self.armor = 5 #target "roll" for a hit to meet
        self.defense = 1 #incoming damage reduction
        self.atk = 1 #outgoing damage multiplier
        self.hit_chance = 0 #only specified so that guarding works by increasing hit chance when hit
        self.speed = 3 #when gladiator will act in the rounds iteration
        self.is_alive = True
        self.inventory = []
        self.profession = ''
        self.soldier_bonus = 0 #0 by default unless gladiator has the 'soldier' profession
        self.is_lucky = False
        self.is_not_guarding = True
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
            print('\n{name} has died.'.format(name = self.name))
    def lose_health(self,amount):
        rounded_amount = round(amount/self.defense)
        if rounded_amount == 0:
            rounded_amount += 1
        self.hp -= rounded_amount
        if self.hp <= 0:
            self.hp = 0
            print('{name} took {amount} damage and now has {hp} health remaining.'.format(name = self.name, amount = rounded_amount, hp = self.hp))
            self.has_died()
        else:
            print('{name} took {amount} damage and now has {hp} health remaining.'.format(name = self.name, amount = rounded_amount, hp = self.hp))
    def guard(self):
        print('{name} assumes a defense stance, waiting for a chance to strike.'.format(name = self.name))
        self.is_not_guarding = False
        self.armor += 2
        self.hit_chance += 2
    def lose_guard(self):
        self.is_not_guarding = True
        self.armor = 5
        self.hit_chance = 0
    def attack(self,target):
        if self.is_alive == True:
            print('{name} {description} {target}...'.format(name = self.name, description = random.choice(cool_descriptors), target = target.name))
            attack = random.randint(1,10)
            damage = random.randint(1,10)
            if (attack == 9 or attack == 10) and self.is_lucky:
                print('{name} critically injured {target}!'.format(name = self.name, target = target.name))
                damage += random.randint(1,10)
            elif attack == 10:
                print('{name} critically injured {target}!'.format(name = self.name, target = target.name))
                damage += random.randint(1,10)
            if (attack + self.hit_chance) >= target.armor:
                missed = False
                if not target.is_not_guarding and not missed:
                    print('{target}\'s guard is broken!'.format(target = target.name))
                # print('{name} hit {target}!'.format(name = self.name, target = target.name))
                target.lose_health((damage * self.atk) + self.soldier_bonus)
            else:
                print('{target} dodged {name}\'s attack!'.format(target = target.name, name = self.name))
                missed = True
            self.lose_guard()
        #attacking will 'use up' your guard, so when self attacks target they will make them lose their guard benefits after it resolves
        #if target wasn't guarding, these values would be set to these defaults anyway
            if not target.is_not_guarding and missed:
                print('\n{target} parries {self}\'s weapon and launches a counterattack!'.format(target = target.name, self = self.name))
                target.attack(self)
                target.lose_guard()
            target.lose_guard()

class Item:
    def __init__(self,type,name):
        self.name = name
        self.type = type
        #self.type should equal 'item', 'armor', or 'weapon'
    def use_potion(self,target):
        if self.type == 'potion' and target.is_alive:
            heal_amount = target.hp + 10
            if heal_amount > target.maxhp:
                target.hp = target.maxhp
            else:
                target.hp = heal_amount
            print('{name} swigged a potion in the heat of battle. They gained 10 health and now have {hp} health remaining'.format(name = target.name, hp = target.hp))
    def equip_armor(self,target):
        #armor variable should equal 'light', 'medium', or 'heavy'; changes target.defense to a specified integer to divide damage by
        if self.type == 'armor':
            if self.name == 'light':
                target.inventory.append('light armor')
                target.defense = 1
            elif self.name == 'medium':
                target.inventory.append('medium armor')
                target.defense = 1.25
                target.speed += 1
            elif self.name == 'heavy':
                target.inventory.append('heavy armor')
                target.defense = 1.5
                target.speed += 2
                # armor types light, medium, and heavy give 1, 1.5, and 2 (?) to defense (damage reduction) and speed
    def equip_weapon(self,target):
        # weapon types quick, balanced, and slow give 0.5, 1, and 1.5 to damage done and speed
        if self.type == 'weapon':
            if self.name == 'shortsword':
                target.inventory.append('quick shortsword')
                target.atk = 0.5
                target.speed = 2
            if self.name == 'spear':
                target.inventory.append('balanced spear')
                target.atk = 1
                target.speed = 3
            if self.name == 'greataxe':
                target.inventory.append('slow greataxe')
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
    #begins combat with a while loop, iterates through 12 asking for player input whenever turn variable == a multiple of their speed attribute.
    if 'potion' not in player.inventory:
        player.gain_item(potion)

    if 'potion' not in opponent.inventory:
        opponent.gain_item(potion)

    opponent_turns = ['attack','guard','potion']
    while player.hp > 0 and opponent.hp > 0:
        both_alive = opponent.is_alive and player.is_alive
        for turn in range(1,13):
            if not both_alive:
                break
            if (turn % player.speed == 0 and player.is_not_guarding) and player.is_alive:
                choice = input('The battle rages. Would you like to attack, guard, or use a potion? Please type attack, guard, or potion. \n').lower()
                while choice not in ['attack','guard','potion']:
                    choice = input('It looks like you chose something else. Please enter attack, guard, or potion and press enter: ').lower()
                if choice == 'potion':
                    if 'potion' not in player.inventory:
                        choice = input('You have no potions in your inventory. Please enter attack or guard: ').lower()
                    else:
                        player.drink_potion()
                if choice == 'attack':
                    player.attack(opponent)
                if choice == 'guard':
                    player.guard()
                print(line_break)
            #elif turn % player.speed == 0 and not player.is_not_guarding:
                #print('{name} has their guard up and is waiting to attack.'.format(name = player.name))
                #print(line_break)
            if not both_alive:
                break
            if (turn % opponent.speed == 0 and opponent.is_not_guarding) and opponent.is_alive:
                opponent_choice = random.choice(opponent_turns)
                if opponent_choice == 'potion':
                    if 'potion' not in opponent.inventory:
                        opponent_choice = random.choice(['attack','guard'])
                    elif (opponent.hp > (opponent.maxhp - 10)):
                        opponent_choice = random.choice(['attack','guard'])
                    else:
                        opponent.drink_potion()
                # check to see if player is guarding, opponent cannot guard if player is guarding or we hit an infinite loop of waiting
                if not player.is_not_guarding:
                    opponent_choice = 'attack'
                if opponent_choice == 'attack':
                    opponent.attack(player)
                if opponent_choice == 'guard':
                    opponent.guard()
                print(line_break)

            elif turn % opponent.speed and not opponent.is_not_guarding:
                if not player.is_not_guarding:
                    opponent.attack(player)
                    print(line_break)
               # else:
               #    print('{name} has their guard up and is waiting to attack.'.format(name = opponent.name))
               # print(line_break)
    if player.is_alive:
        print('\nYou are victorious! The crowd is lost in excitement and you live to fight another day.')
    else:
        print('\nIt was a valiant effort, but your time in the arena has come to an end. GAME OVER')

def title_screen():
    print(line_break)
    print(gladiator_title)
    print(line_break)
    print('WELCOME TO THE ARENA')
    print('DO YOU HAVE WHAT IT TAKES TO BE THE CHAMPION?')
    print(line_break)
    quiery = input('Have you braved The Arena before? (Do you already know the rules?): y/n: ').lower()
    while quiery not in ['y','n']:
        quiery = input('Please enter y if you don\'t need to know how the rules. Enter n if you do: ').lower()
    if quiery == 'n':
        print(swirly_line)
        print("""
In Gladiator you will create a fighter who aims to become champion of The Arena. Your fighter must defeat 3 opponents to claim the 
coveted title. If your fighter is defeated, their time in The Arena comes to an end. Don\'t worry though! There are always others 
willing to test their mettle.

In each fight, combatants will act depending on their SPEED stat. This number dictates the order in which they attack, a lower number
means you act sooner while a higher number means you act later. A fighter with a SPEED of 2 may attack twice in the time it takes a 
fighter with a SPEED of 4 to attack once.
- SPEED is set by weapon choice and further influenced by your armor choice.

On you turn, you will have the option to attack, guard, or use your potion:
- Attack: Attempt to damage your opponent. Your fighter strikes out at their enemy with a chance to hit or miss. Damage varies by weapon.
              
- Guard: While guarding, you are harder to hit but cannot take other actions until attacked. If the opponent's attack hits, your guard is lost.
         If the opponent's attack misses, your fighter will counter-attack automatically with an increased chance to hit.
              
- Potion: Both combatants receive 1 potion per fight, use it wisely. Your potion will heal you for 10 hit points.
              
At its core, Gladiator is a simple game of luck. So GOOD luck and have fun.
""")
        print(swirly_line)

def character_creation():
    # sets name of player's gladiator
    player_name = input('What is your fighter\'s name?: ').capitalize()
    player_gladiator.name = player_name
    print(line_break)
    # set past_profession of player's gladiator
    player_profession_choice = input("""
What was {name} before they joined The Arena?
    Farmer - Your time spent laboring under the sun has made you quite hardy, you have a bonus to your hitpoints. 
    Soldier - You have honed your fighting instincts in the field of battle, you deal increased damage.
    Merchant - You've always been lucky, you have an increased chance to critically injure your opponent.
    Please enter farmer, soldier, or merchant:
    """.format(name = player_gladiator.name)).lower()
    while player_profession_choice not in ['farmer','soldier','merchant']:
        player_profession_choice = input('It looks like you enetered something else. Please enter farmer, soldier, or merchant: ').lower()
    player_profession = Profession(player_profession_choice)
    player_profession.past_profession(player_gladiator)
    print(line_break)
    # sets weapon of player's gladiator
    player_weapon_choice = input('''
Choose {name}\'s weapon: 
    Shortsword - A quick weapon that allows you to strike often but with decreased damage.  (2 speed, 0.5 damage multiplier)
    Spear - A balanced weapon that strikes with a reasonable speed and deals normal damage. (3 speed,  1  damage multiplier)
    Greataxe - A slow weapon that is cumbersome to wield but hits harder.                   (4 speed, 1.5 damage multiplier)
    Please enter shortsword, spear, or greataxe:
    '''.format(name = player_gladiator.name)).lower()
    while player_weapon_choice not in ['shortsword','spear','greataxe']:
        player_weapon_choice = input('It looks like you entered something else. Please enter shortsword, spear, or greataxe: ').lower()
    player_weapon = Item('weapon',player_weapon_choice)
    player_weapon.equip_weapon(player_gladiator)
    print(line_break)
    # sets armor of player's gladiator
    player_armor_choice = input('''
Choose {name}\'s armor:
    Light Armor - This armor offers no additional protection, but doesn\'t hinder your speed.  (+0 speed, 0 damage reduction)
    Medium Armor - This armor restricts your movement slightly, but gives increased protetion. (+1 speed, 1.25 damage reduction)
    Heavy Armor - This armor greatly hinders your speed, but offers the most protection.       (+2 speed, 1.5 damage reduction)
    Please enter light, medium, or heavy:
    '''.format(name = player_gladiator.name)).lower()
    while player_armor_choice not in ['light','medium','heavy']:
        player_armor_choice = input('It looks like you entered something else. Please enter light, medium, or heavy: ').lower()
    player_armor = Item('armor',player_armor_choice)
    player_armor.equip_armor(player_gladiator)
    print(line_break)
    return player_gladiator

def opponent_creation(opponent):
    # set opponent's name
    opponent_random_names = ['Gluteus Maximus','Jeffrey','Steve','Scarr','Mama Mildred','Maximus Decimus Meridius','The Dread Gladiator Roberticus','Xena','Stacy']
    opponent.name = random.choice(opponent_random_names)
    opponent_random_names.remove(opponent.name)
    # set opponent's profession
    opponent_profession_choice = random.choice(['farmer','soldier','merchant'])
    opponent_profession = Profession(opponent_profession_choice)
    opponent_profession.past_profession(opponent)
    # set opponent's weapon
    opponent_weapon_choice = random.choice(['shortsword','spear','greataxe'])
    opponent_weapon = Item('weapon',opponent_weapon_choice)
    opponent_weapon.equip_weapon(opponent)
    # set opponent's armor
    opponent_armor_choice = random.choice(['light','medium','heavy'])
    opponent_armor = Item('armor',opponent_armor_choice)
    opponent_armor.equip_armor(opponent)
    return opponent

def opponent_intro(player,opponent):
    print(swirly_line)
    print('The iron gates open before you. The cheers of the crowd thrum in your ears and anticipation of battle sets your heart to racing.')
    print('''
The announcer motions towards you and bellows, "OUR CHALLENGER FOR THE TITLE OF CHAMPION, {NAME}!!"
          
On the opposite end of the walled in arena, the portcullis opens to reveal your opponent.
          
The announcer\'s hand moves to the opposite end and they shout, "OUR DEFENDING FIGHTER, {OPPONENT}!!!"
          
After the crowd\'s cheers die down slightly with the rising tension, the announcer brings their fist down and yells,
          
                                                FIGHT!
          
'''.format(NAME = player.name.upper(), OPPONENT = opponent.name.upper()))
    print(swirly_line)    

def post_fight(player,fight_counter):
    if player.is_alive:
        player.hp = player.maxhp
        if fight_counter == 1:
            print('\nYou have defeated your first opponent and are one step closer to become Champion of The Arena.')
            print('Your next challenge begins now...\n')
        elif fight_counter == 2:
            print('\nYou\'ve done it! Only one more challenger stands in your way.  Prepare yourself for your final fight.\n')
        elif fight_counter == 3:
            input('''
You are a warrior unlike any The Arena has ever seen, you are its Champion!! {name} has cemented themselves in the annals of history.
              
Thank you so much for playing my barebones and over-complicated-yet-painfully-simple game! 
Please input absolutely whatever you want: 
'''.format(name = player.name))
            exit()
    else:
        input('Thank you so much for playing! If you\'re feeling luck, try playing again.')
        exit()

# instantiating default objects like professions and items.
farmer = Profession('farmer')
soldier = Profession('soldier')
merchant = Profession('merchant')
medium_armor = Item('armor','medium')
spear = Item('weapon','spear')
shortsword = Item('weapon','shortsword')
greataxe = Item('weapon','greataxe')
potion = Item('potion','potion')


#create 3 opponents
opponent1 = Gladiator('')
opponent_creation(opponent1)
opponent2 = Gladiator('')
opponent_creation(opponent2)
opponent3 = Gladiator('')
opponent_creation(opponent3)

#begin game
title_screen()

#create player
player_gladiator = Gladiator('')
character_creation()

fight_counter = 0
#introduce and fight opponent 1
opponent_intro(player_gladiator,opponent1)

combat_turns(player_gladiator,opponent1)

#check to see if game should exit()
fight_counter += 1
post_fight(player_gladiator,fight_counter)

#introduce and fight opponent 2
opponent_intro(player_gladiator,opponent2)

combat_turns(player_gladiator,opponent2)

#check to see if game should exit()
fight_counter += 1
post_fight(player_gladiator,fight_counter)

#introduce and fight opponent 3
opponent_intro(player_gladiator,opponent3)

combat_turns(player_gladiator,opponent3)

#check to see if game should exit()
fight_counter += 1
post_fight(player_gladiator,fight_counter)
