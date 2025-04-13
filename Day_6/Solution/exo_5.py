def main():
    fruits = input().split(",")
    fruits = [fruit.strip() for fruit in fruits]
    if fruits:
        print(fruits[-1])
    else:
        print("List is empty.")

if __name__ == "__main__":
    main()
