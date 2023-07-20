import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

# Creating an Enum class
class prompts:
    ACTOR_GUIDE = """."""
    ACTOR_SYSTEM = """."""
    GENERATE_ITEMS = lambda count: f"""
Generate {count} varying RPG style items that each effects 2 of the 3 potential stats (health, agility, damage). 

Items generated must follow these rules 
* Each item should have, a name, brief lore no longer than two sentences, 
* An items cost is related to its total stat boost but must be no higher than 9 coins. 
* Items should have a range of trade-offs between effects.
* If an item increase two stats it must either decrease the third stat of have a cost >= 9 coins.
* Most of the Items should have a cost between 3 and 7 coins. 
* Without mentioning the labs name directly, items should relate to the Johns Hopkins Applied Physics lab and its work, keep the names lighthearted. 
* Assign one of these categories to each item ['dagger', 'sword', 'shield', 'amulet', 'boots', 'potion', 'facewear']

The output should be in json format using the following key and datatype pairs 
{'name':str, 'lore':str, 'stats': {'health':int, 'agility':int, 'damage':int}, 'category': str, 'cost':int}."""
    
def build_update_prompt(Actor, World):
    pass


if __name__ == "__main__":
    from item import Dagger, Shield, Sword, Potion
    
    pass