input_string = input("")
fruit_to_remove = input("")
fruits = input_string.split(",")
if fruit_to_remove in fruits :
    fruits.remove(fruit_to_remove)
print(fruits)