with open("a.txt", "r") as f1:
    words_a = f1.read().split()

with open("b.txt", "r") as f2:
    words_b = f2.read().split()

set_a = set(words_a)
set_b = set(words_b)

print(f"a.txt total words: {len(words_a)}, unique words: {len(set_a)}")
print("Common words (sorted):", sorted(set_a.intersection(set_b)))
print("Words only in a.txt (sorted):", sorted(set_a - set_b))