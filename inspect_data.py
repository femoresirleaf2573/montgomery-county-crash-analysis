import csv

with open("data/crashes.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    columns = next(reader)

    print("Number of columns:", len(columns))
    print("\nColumn names:")

    for column in columns:
        print(column)

    count = 0

    for row in reader:
        count += 1

    print("\nTotal crash records:", count)
