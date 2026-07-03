import datetime

FILENAME = "expense.txt"

try:
    with open(FILENAME, "r") as f:
        print("--- Existing expense ---")
        print(f.read())
except FileNotFoundError:
    print("No expense.txt yet — starting fresh.")

item = input("Item: ")
try:
    amount = float(input("Amount: "))
except ValueError:
    print("Invalid amount, must be a number.")
    amount = 0

today = datetime.date.today().isoformat()
with open(FILENAME, "a") as f:
    f.write(f"{today},{item},{amount}\n")

print(f"Saved: {item} - ₹{amount}")

total = 0
with open(FILENAME, "r") as f:
    for line in f:
        date, name, amt = line.strip().split(",")
        if date == today:
            total += float(amt)

print(f"Total spent today: ₹{total}")