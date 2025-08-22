fruits = ["Kiwi", "Apple", "Orange", "Banana", "Grapes"]
print("Fruits list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
fruits[1] = "Mango"
print("After changing the second fruit:", fruits)
fruits.insert(2, "Watermelon")
print("After inserting Watermelon at index 2:", fruits)
name = input("Enter a fruit name: ").strip()
name = name.title()
if name in fruits:
    print(name, "is in the list")
else:
    print(name, "is not in the list ")
fruits.sort()
print("Fruits list after sorting:", fruits)
