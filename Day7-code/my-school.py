print("Welcome to the School Activity Registration System!")

# ชื่อ
while True:
    name = input("Enter your name: ").strip().capitalize()
    if len(name) < 3:
        print("Please enter a valid name (at least 3 characters).")
    else:
        break

# อายุ
age = int(input("Enter your age: "))
if age < 7:
    print("Sorry, you're too young to register.")
    exit()

# กิจกรรม
print(
    "\nAvailable activities:", 
      "\n1.sport",
      "\n2.music", 
      "\n3.drawing"
      )

# กิจกรรมที่เลือก
activity = input("Choose your activity: ").strip().lower()

# ตรวจสอบกิจกรรมผิด
valid_activity = ["sport", "music", "drawing"]
if activity not in valid_activity:
    print("Invalid activity, Please try again later.")
    exit()

# แสดงผลข้อมูลการสมัคร
print(
    "\nRegistration Summary",
        f"\nName: {name}",
        f"\nAge: {age}",
        f"\nSelected Activity: {activity}",
        "\nStatus: Registered successfully ✅"
    )


