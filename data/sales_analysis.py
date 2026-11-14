# Exercise 1:
# Name: Haylee Jones
# Date: 20261114
# Lab 12 - CSV File Processing

import csv
from datetime import datetime

# Exercise 2: Read and print raw rows
with open("data/sales.csv", "r", newline="") as file: 
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Skip the header
print("\nExercise 3")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("\nExercise 4")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")


# Exercise 5: Filter and write

print("\nExercise 5")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Product", "Price", "Qty", "Total"])

            for row in reader: 
                original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, f"{total:.2f}"])
                cleaned_count += 1

print(f"Rows written: {cleaned_count} out of {original_count}")

# Exercise 6: DictReader

# csv.reader uses index numbers to access each value.
# DictReader uses column names, which is easier to understand.

print("\nExercise 6")

dict_total = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: ${total:.2f}")

print(f"Total Revenue: ${dict_total:.2f}")

# Exercise 7: Sales summary

print("\nExercise 7")

summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in summary:
            summary[product] += total
        else:
            summary[product] = total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append mode log 

print("\nExercise 8")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Run log updated!")



















# Reflection 1:
# Python and Excel can both organize and calculate data.
# Python is better for automating repetitive tasks and handling
# large files, while Excel makes it easier to see and edit data.

# Reflection 2:
# A business could use append mode to keep track of daily sales
# Append mode is useful because it adds new info without deleting the 
# previous records.