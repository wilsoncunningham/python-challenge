#%%
URL = "http://www.pythonchallenge.com/pc/def/ocr.html"

#%%
# 1. Press Ctrl u to see that page's html.

mess = open("resources/level_2.txt").read()

counts = {}
for char in mess:
    counts[char] = counts.get(char, 0) + 1

print(counts)

# %%

rares = []
for char, count in counts.items():
    if counts[char] == 1:
        rares.append(char)

cleaned_mess = "".join(char for char in mess if char in rares)
print(cleaned_mess)

#%%
# cleaned_mess is 'equality'

new_url = "http://www.pythonchallenge.com/pc/def/equality.html"
