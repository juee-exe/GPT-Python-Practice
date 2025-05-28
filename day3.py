# Practice No.1 Adult?
user_age = int(input("How old are you? "))
if user_age >= 18:
    print("You are underage.")
elif user_age <= 18:
    print("You are an adult")

# Practice No.2
grade = int(input("Enter your grade: "))
if grade >= 80:
    print("Grade A")
elif grade >= 70:
    print("Grade B")
elif grade >= 60:
    print("Grade C")
elif grade >= 50:
    print("Grade D")
else: 
    print("Grade F")

#Practice No.3
number = int(input("Enter your number: "))
if number % 2 == 0:
    print("This is even number.")
else:
    print("This is odd number.")

# Practice No.4
password = input("Enter your password: ")
if password == "python123":
    print("Access granted!")
else:
    print("Incorrect password.")

# Practice No.5
english = int(input("English score: "))
math = int(input("Math score: "))

if english >= 50 and math >= 50:
    print("You passed both subjects.")
elif english >=50 or math >= 50:
    print("You did not pass both subjects.")
else:
    print("You did not pass both subjects.")
