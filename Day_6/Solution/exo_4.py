def main():
    fruits = input().split(",")
    fruits = [fruit.strip() for fruit in fruits]
    item_to_remove = input().strip()
    if item_to_remove in fruits:
        fruits.remove(item_to_remove)
        print(fruits)
    else:
        print("Item not found in list.")

if __name__ == "__main__":
    main()
