
## Stats
* Health: Represents the players HP, once it reaches 0 the player is eliminated. 
* Agility: Determines the movement speed, and interaction range 
* Damage: When an attack hits 1 + (rand(.1,1)* damage_stat) damage will be done 

## Objectives (Ways to Win)
* Last Man Standing: Be the last player with a health greater than 0. 
* Defeat the World Boss: Find and Defeat 
* Goblin King: We'll get there

## Turn Ordering
* Each players turns are taken sequentially.
* If a Avatars action is visible to another coming afterwards information about that action will be passed to subsequent Avatar updates.

## Player <-> Avatar Interaction
Players and Avatars interact through the Guide Prompt. Its contents along with each update prompt with be given to the model on each of its turns 
* Players are locked out of modifying the prompts when items or players are within interaction range
* After modifying the guide prompt the player must wait a minimum of 3 turns before doing so again 

## Avatar <-> Avatar Interaction
### Combat
* Attack: When avatars are within interaction range, either avatar may start combat by selecting the attack action
* Run: When 
## Items
### Inventory

### Actions
* Pick Up: When an item is within interaction range, it can be picked up added to inventory. Any status effects of the item are immediately applied.
* Exchange: When an avatar attempts a pickup and the inventory is full they'll be prompted to select a current inventory item to drop for the target item.

## Traveling
### Movements
Actors are restricted from taking direct movement action i.e up, left, etc. Instead Actors can select a target location to travel to. However the number of grid locations traveled per turn is 
### Landmarks
 Once an Item or Avatar becomes visible its last location is stored and an Actor may select to start travel back to that location at any time. For example (Go To: Wooden Sword). If the location that a landmark references becomes visible and no longer contains that item it is removed from the 'Known Landmarks' set.

### Actions
* Go To:  A landmark from the "Known Landmarks" set is selected. BFS path planning determines how movements are applied until the target landmark is within interaction range. The Avatar Update prompted will be modified with "Currently Traveling to: {landmark}" and "Turns Till arrival : {int}" information

* Explore (North, South, East, West):  


## Goblin Rules 
