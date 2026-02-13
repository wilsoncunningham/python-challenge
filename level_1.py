#%%

URL = "http://www.pythonchallenge.com/pc/def/map.html"

# %%
import string 

my_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
my_string_list = list(my_string)
alphabet = list(string.ascii_lowercase)
alphabet_offset = [alphabet[i - 24] for i, _ in enumerate(alphabet)]
alpha_map = dict(zip(alphabet, alphabet_offset))

#%%
def translate(my_string):
    my_string_list = list(my_string)
    for idx, char in enumerate(my_string_list):
        if char in alpha_map.keys():
            my_string_list[idx] = alpha_map[char]
            
    my_string = "".join(my_string_list)

    return my_string

message = translate(my_string)
print(message)

#%%

url = "http://www.pythonchallenge.com/pc/def/map.html"

new_snip = translate("map")
new_url = f"http://www.pythonchallenge.com/pc/def/{new_snip}.html"

print(new_url)
# %%

new_url = "http://www.pythonchallenge.com/pc/def/ocr.html"
