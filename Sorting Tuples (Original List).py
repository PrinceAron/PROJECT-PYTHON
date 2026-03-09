items = [("Shirt", 20), ("Pants", 50), ("Shoes", 40)]
items.sort(key=lambda x : x[1])

print(items)

## Sorting Dictionaries (New List)

people = [{"name": "A", "age": 30}, {"name": "B", "age": 20}, {"name": "C", "age": 25}]
sorted_people = sorted(people, key=lambda x: x["age"])

print(sorted_people)

# Task 3: Reverse Sorting

fruits = ["apple", "kiwi", "banana", "strawberry"]
sorted_fruits = sorted(fruits, key=lambda x: len(x), reverse=True)

print(sorted_fruits)