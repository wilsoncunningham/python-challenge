#%%

url = "http://www.pythonchallenge.com/pc/def/peak.html"

from urllib.request import urlopen
raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
straw = str(raw)
#%%
# I needed hints for this one.

import pickle

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:
    print("".join([k * v for k, v in line]))


new_url = "http://www.pythonchallenge.com/pc/def/channel.html"