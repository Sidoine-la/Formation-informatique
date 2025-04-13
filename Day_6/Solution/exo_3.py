def main():
    fruits = input().split(",")
    fruits = [fruit.strip() for fruit in fruits]
    fruits.sort()
    print(fruits)

if __name__ == "__main__":
    main()
