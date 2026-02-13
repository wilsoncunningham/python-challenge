#%%
url = "http://www.pythonchallenge.com/pc/def/equality.html"

#%%

mess = open("resources/level_3.txt").read()

def find_snippets(text):
    """
    Given a string, find all snippets that are exactly 3 uppercase letters
    followed by 1 lowercase and then exactly 3 uppercase
    """
    results = []

    for idx, char in enumerate(text):
        if char.isupper() and (idx == 0 or text[idx-1].islower()):
            
            # Check first block of Uppercase
            pointer1 = idx
            while pointer1 < len(text) and text[pointer1].isupper():
                pointer1 += 1
            len1 = pointer1 - idx
            
            # Check for exactly 3 Upper + 1 Lower
            if len1 == 3 and pointer1 < len(text) and text[pointer1].islower():
                bridge_idx = pointer1
                
                # Check second block of Uppercase
                pointer2 = bridge_idx + 1
                start2 = pointer2
                while pointer2 < len(text) and text[pointer2].isupper():
                    pointer2 += 1
                len2 = pointer2 - start2
                
                # Check for exactly 3 Upper + Boundary check
                if len2 == 3:
                    # Ensure the character after the second block isn't uppercase
                    if pointer2 == len(text) or text[pointer2].islower():
                        results.append(text[idx:pointer2])
                        
    return results


snippets = find_snippets(mess)
print(snippets)
#%%

# Isolate the lowercases

answer = ""

for snippet in snippets:
    answer += snippet[3]

print(answer)
# answer = 'linkedlist'
# upon putting this in the url, I was instructed to do linkedlist.php instead of '.html

new_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"