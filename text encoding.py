#open(), you usually pass it a few key pieces of information (arguments)
with open("random_word.txt", "w", encoding="utf-8") as f: #"c.txt": The name (or path) of the file you want to open.
    f.write("bonjour mes amis, Ça va?")

with open("random_word.txt", encoding="utf-8") as f: #encoding="utf-8": The text translator we talked about, ensuring special characters and accents are handled properly
    print(f.read()) #f creates a temporary nickname (a variable) for your opened file
