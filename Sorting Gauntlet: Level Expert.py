# Sorting Gauntlet: Level Expert
##Task 1: The Scoreboard (Nested Sorting)
players = [
    {"user": "Prince", "stats": {"score": 450, "level": 5}},
    {"user": "Butiti", "stats": {"score": 900, "level": 10}},
    {"user": "Gae", "stats": {"score": 150, "level": 2}}
]

players_sorted = sorted(players,key=lambda x: x['stats']['score'], reverse=True)

print(players_sorted)

##Task 2: The Character Sorter

names = ["Alice", "Bob", "Charlie", "David"]
names_sorted = sorted(names,key=lambda x: x[-1])
print(names_sorted)

# The Multi-Step Filter & Sort
stock = [
    {"item": "Pen", "price": 10, "in_stock": True},
    {"item": "Paper", "price": 5, "in_stock": False},
    {"item": "Ink", "price": 100, "in_stock": True},
    {"item": "Eraser", "price": 2, "in_stock": True}
]

filtered_stock = list(filter(lambda x: x['in_stock'],stock))
sorted_stock = sorted(filtered_stock,key=lambda x: x['price'])
print(sorted_stock)