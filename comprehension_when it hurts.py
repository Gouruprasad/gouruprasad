lines = ["the cat sat", "a big dog ran"]
words = []
for line in lines:
    for w in line.split():
        if len(w) > 2 and w != "the":
            words.append(w.upper())
print(words)
