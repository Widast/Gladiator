# Gladiator
This is a quick little turn-based game made for the Codecademy Python Terminal Game project.  
The user will create a gladiator by giving them a name, picking their past profession, equiping them with a weapona and armor, and then pitting them against 3 opponents.
Different choices give different bonuses or penalties (except their name, of course).

The SPEED stat dictates when you take turns in the fight. A lower number is quicker, a higher number is slower. For example, a gladiator with 2 speed will go twice in the
time it takes a gladiator with 4 speed to go once.

There are 3 options on each turn. You may attack, guard, or consume your potion:
- Attack - attempt to damage the other gladiator
- Guard - reduce your chances of being hit, but forgo any other action until your opponent attacks
  - if your opponent hits you, they break your guard and deal damage as normal
  - if your opponent misses you, you will automatically attempt to counterattack with an increased chance to hit
- Potion - each gladiator starts combat with 1 potion that restores 10 hp

Professions:
- Farmer - +10 bonus to hp
- Soldier - +2 bonus to damage
- Merchant - a 10% higher chance of critical hits

Weapons:
- Shortsword - 2 speed and a 0.5 damage multiplier
- Spear - 3 speed and a 1 damage multiplier
- Greataxe - 4 speed and a 1.5 damage multiplier

Armor:
- Light - no speed penalty, but no damage reduction
- Medium - +1 speed penatly and 1.25 damage reduction
- Heavy - +2 speed penalty and 1.5 damage reduction
