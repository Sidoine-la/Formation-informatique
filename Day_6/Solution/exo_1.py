def main():
    fruits = input().split(",")
    if len(fruits) > 1:
        print(fruits[1].strip())
    else:
        print("Not enough fruits.")

if __name__ == "__main__":
    main()
