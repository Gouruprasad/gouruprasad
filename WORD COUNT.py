words = ["a", "b", "a", "c", "a" , "t" , "p" , "p"]

counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts)
