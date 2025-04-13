def main():
    fruits = input().split(",")
    fruits = [fruit.strip() for fruit in fruits]
    fruits.append("Mango")
    print(fruits)

if __name__ == "__main__":
    main()
