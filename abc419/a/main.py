s = input()

memory = {"red": "SSS", "green": "MMM", "blue": "FFF"}

if s in memory:
    print(memory[s])
else:
    print("Unknown")
