#%%
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

nothing_url0 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

import requests
from bs4 import BeautifulSoup

response = requests.get(nothing_url0)
text = response.text
nothing_number = text.split(" ")[-1]


def find_nothing_number(n):
    """
    Finds the n-th 'nothing' number for this challenge.
    """
    if n == 1:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        response = requests.get(url)
        text = response.text
        nothing_number = text.split(" ")[-1]
    else:
        response = requests.get(url)
        text = response.text
        nothing_number = text.split(" ")[-1]
        next_url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing_number}"
        return find_nothing_number(next_url)

    return nothing_number

#%%

def find_final_nothing(start_nothing):
    """
    Finds the final 'nothing' number for this challenge.
    """
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    current_nothing = start_nothing
    
    while True:
        url = f"{base_url}{current_nothing}"
        response = requests.get(url)
        text = response.text
        
        print(f"Current message: {text}")
        parts = text.split()
        next_numbers = [s for s in parts if s.isdigit()]
        
        if not next_numbers:
            # If no number is found
            print(f"Final Answer Found: {text}")
            break
            
        current_nothing = next_numbers[-1]

find_final_nothing("12345")

# final message is: Yes. Divide by two and keep going.

#%%
find_final_nothing("8022")

# New final answer: 'peak.html'

new_url = "http://www.pythonchallenge.com/pc/def/peak.html"
