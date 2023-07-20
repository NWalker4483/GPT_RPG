import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

# Creating an Enum class
class prompts:
    ACTOR_GUIDE = """."""
    ACTOR_SYSTEM = """."""
    GENERATE_ITEMS = """."""
    
def build_update_prompt():
    pass