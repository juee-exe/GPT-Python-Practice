print("Welcome to Jaymart!")
name = input("Enter your name: ").capitalize()

# ราคาสินค้า
prices = {
    "water": 10,
    "snack": 20,
    "milk": 15
}

# แสดงสินค้า
print("\nสินค้าที่มีจำหน่าย:")
for item, price in prices.items():
    print(f"- {item}: {price} baht")

# รับรายการสั่งซื้อ
total = 0

for i in range(2):
    item = input("\nWhat do you want to buy? ").strip().lower()
    quantity = int(input("How many? "))
    
    if item in prices:
        cost = prices[item] * quantity
        total += cost
        print(f"Added {quantity} x {item} = {cost} baht")
    else:
        print("Sorry, we don't have that item.")

# คำนวณส่วนลด
discount = total * 0.10 if total > 100 else 0
final_total = total - discount

# แสดงบิล
print("\n🧾 Final Bill")
print(f"Total before discount: {total} baht")
print(f"Discount: {discount} baht")
print(f"Amount to pay: {final_total} baht")
print(f"Thank you {name}, have a nice day!")
