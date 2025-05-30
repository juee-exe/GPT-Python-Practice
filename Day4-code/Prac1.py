# Testing double password or not?
"""
- Your password must have 8-12 charactors.
- Your password must not have space,!,@,#,$,%,&, and * so on (up to you bruh).
_ Your password must contain Uppercase and number.
"""


def if_valid_password(password):
    disallowed_chars = [" ", "!", "@", "#", "$", "%", "&", "*", "_", "-"]

    # Testing length password for user.
    if len(password) < 8 or len(password) > 12:
        return False, "Password must contain 8-12 charactors."
    
    # Testing if therr any disallowd chars.
    if any(char in password for char in disallowed_chars):
        return False, f"Password disallowed this: {disallowed_chars}"
    
    # Testing passsword must contain one or more numbers.
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."
    
    # Testing password must contain one or more Uppercase chars.
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one Uppercase."
    
    # Return this if all above code is True.
    return True, "Password is valid."

while True:

    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Password do not match!")
        continue
    print("✅ Password match!")

    is_valid, message = if_valid_password(password)
    if not is_valid:
        print("❌", message)
        continue

    print("✅ Password confirmed and accepted.")
    break
    