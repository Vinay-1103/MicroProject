words=["donkey","Cow","and"]

with open("donkey.txt","r") as f:
    content=f.read()

for word in words:
    new=content.replace(word , "#" * len(word))
with open("donkey.txt","w") as f:
    f.write(new)