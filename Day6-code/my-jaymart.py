print("Welcome to Jaymart!")
name = str(input("Enter your name: ")).capitalize()

# กำหนดค่าสินค้า
water = 10
snack = 20
milk = 15

# รายการสินค้า
print(
    "สินค้าที่มีจำหน่าย:\n", 
      f"- water: {water} baht\n", 
      f"- snack: {snack} baht\n", 
      f"- milk: {milk} baht\n"
)

# รับข้อมูลรายการที่ 1
order1 = input("What do you want to buy? ").strip().lower()
item1 = int(input("How many? "))

# รับข้อมูลรายการที่ 2
order2 = input("What do you want to buy? ").strip().lower()
item2 = int(input("How many? "))

# คำนวนราคาและส่วนลด
total = 0
if order1 == "water":
    total += item1 * water
elif order1 == "snack":
    total += item1 * snack
elif order1 == "milk":
    total += item1 * milk

if order2 == "water":
    total += item2 * water
elif order2 == "snack":
    total += item2 * snack
elif order2 == "milk":
    total += item2 * milk

# ส่วนลด 10%
if total > 100:
    discount = total * 0.10
else:
    discount = 0

# บิลของลูกค้า
print(
    f"You need to pay: {total} baht\n", 
    f"Thank you {name} Have a nice day\n"
)
