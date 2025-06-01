# รับข้อมูลจากผู้ใช้,
name = input("What is your name? ")
age = int(input("How old are you? "))
taste = input("What kind of taste do you like? (spicy / sweet / bland): ").lower()
budget = int(input("What is your budget? "))

# แนะนำร้านตามรสชาติ,
if taste == "spicy":
    recommended = "ร้านส้มตำยายน้อย"
elif taste == "sweet":
    recommended = "ร้านขนมหวานในห้าง"
elif taste == "bland":
    recommended = "ร้านโจ๊กเพื่อชีวิต"
else:
    recommended = "ร้านที่คุณต้องลองเอง!"

# แสดงผล,
print(f"\nHi, {name}!")
if age <= 12:
    print("เด็กกินฟรี!")

print(f"Recommended: {recommended}")

# แนะนำตามงบ,
if budget < 50:
    print("เหมาะกับร้านริมทาง ราคาประหยัด")
elif 50 <= budget <= 200:
    print("เหมาะกับร้านทั่วไป ราคากลาง")
else:
    print("เหมาะกับร้านหรูระดับพรีเมียม")
