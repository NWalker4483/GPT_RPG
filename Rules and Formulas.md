
## Stats
* Health: Represents the players HP, once it reaches 0 the player is eliminated. 
* Agility: Determines the movement speed, and interaction range 
* Damage: When an attack hits 1 + (rand(.1,1)* damage_stat) damage will be done 

## Objectives (Ways to Win)
* Last Man Standing: Be the last player with a health greater than 0. 
* Defeat the World Boss: Find and Defeat 
* Goblin 

## Turn Ordering
* Each players turns are taken sequentially.
* If a characters action is visible to another coming afterwards information about that action will be passed to subsequent character updates.

## Player <-> Character Interaction
Players and Characters interact through the Guide Prompt. Th
* Players are locked out of modifying the prompts when items or players are within interaction range
* After modifying the guide prompt the player must wait a minimum of 3 turns before doing so again 

## ~~Character <-> Character Interaction~~

## Traveling

### Landmarks
Landmarks allow the character to be moved to a specific position it has previously had within visual range

## Actions
### Interaction
* Go To: When an item, character, or location is visible but outside 
* Pick Up: When an item is within interaction range, it can be picked up added to inventory. Any status effects of the item are immediately applied.
* Exchange: A subset of the pickup action. When the inventory is full a model may choose to drop one of its currently held items to pickup the target item.

### Combat
* Attack: When a different player is within interaction range 
* Run: 


## Goblin Rules 
