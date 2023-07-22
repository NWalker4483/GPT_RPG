import os
from typing import Any, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

class OPAL_MODELS:
    LLAMA2 = ""
    
class CustomLLM(LLM):
    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[: self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}
    
# Creating an Enum class
class prompts:
    DEFAULT_ACTOR_GUIDE = """."""
    ACTOR_SYSTEM = """."""
    GENERATE_ITEMS = lambda count: f"""Generate {count} varying RPG style items that each effects 2 of the 3 potential stats (health, agility, damage). 

Items generated must follow these rules 
* Each item should have, a name, brief lore no longer than two sentences, 
* An items cost is related to its total stat boost but must be no higher than 9 coins. 
* Items should have a range of trade-offs between effects.
* If an item increase two stats it must either decrease the third stat of have a cost >= 9 coins.
* Most of the Items should have a cost between 3 and 7 coins. 
* Without mentioning the labs name directly, items should relate to the Johns Hopkins Applied Physics lab and its work, keep the names lighthearted. 
* Assign one of these categories to each item ['dagger', 'sword', 'shield', 'amulet', 'boots', 'potion', 'facewear']

The output should be in json format using the following key and datatype pairs 
{{'name':str, 'lore':str, 'stats': {{'health':int, 'agility':int, 'damage':int}}, 'category': str, 'cost':int}}."""
    
def build_update_prompt(Actor, World):
    pass

import requests

def make_api_request(api_url, request_body):
    try:
        # Send POST request to the API with the given request body
        response = requests.post(api_url, json=request_body)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response if the API returns JSON data
            data = response.json()
            return data
        else:
            # If the request was not successful, raise an exception
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_URL' with the actual API endpoint URL
    api_url = 'https://opal.livelab.jhuapl.edu:8080/completions'
    
    # Replace 'YOUR_REQUEST_BODY' with the actual request body you provided
    request_body = {
        "model": "lmsys/vicuna-33b",
        "prompt": prompts.GENERATE_ITEMS(2),
        "max_tokens": 300,
        "temperature": 0.9,
        "top_p": 1,
        "n": 1,
        "bad_word_list": [
            [""]
        ],
        "stop_word_list": [
            [""]
        ],
        "repetition_penalty": 1.2,
        "random_seed": -1,
        "top_k": 50,
        "client_type": "http"
    }
    
    api_response = make_api_request(api_url, request_body)

    if api_response:
        print("API Response:")
        print(api_response)

# if __name__ == "__main__":
#     from item import Dagger, Shield, Sword, Potion
    
#     pass