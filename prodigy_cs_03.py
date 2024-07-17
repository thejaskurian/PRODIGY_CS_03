import re

def assess_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1

    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1

    # Determine password strength level
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Medium"
    else:
        return "Weak"

def main():
    password = input("Enter a password: ")
    strength = assess_password_strength(password)

    print(f"Password strength: {strength}")

    if strength == "Weak":
        print("Your password is weak. Consider using a longer password with a mix of uppercase and lowercase letters, numbers, and special characters.")
    elif strength == "Medium":
        print("Your password is medium strength. Consider adding more characters or using a more complex password.")
    else:
        print("Your password is strong. Good job!")

if __name__ == "__main__":
    main()
