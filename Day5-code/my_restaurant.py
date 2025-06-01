name = input("What is your name? ")
age = int(input("How old are you? "))
taste = str(input("What kind of taste do you like? (spicy / sweet / blend): "))
budget = int(input("What is your budget? "))

if age <= 12:
    print("เด็กกินฟรี")

spicy = "ร้านส้มตำยายน้อย"
sweet = "ร้านขนมหวานในห้าง"
blend = "ร้านโจ๊กเพื่อชีวิต"

if taste == spicy:
    print(f"Recommended: {spicy} เหมาะกับคุณเลย!")
elif taste == blend:
    print(f"Recommended: {blend} เหมาะกับคุณเลย!")
else:
    print(f"Recommended: {sweet} เหมาะกับคุณเลย!")


if budget <= 50:
    print("งบร้านอาหารของคุณต่ำเกินไป")