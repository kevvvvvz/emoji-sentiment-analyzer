import demoji

text = "Hello. ☀️"

test = demoji.findall(text)
new = demoji.replace_with_desc(text)
h1 = demoji.replace(text, "")

print(new)
print(test)
print(h1)