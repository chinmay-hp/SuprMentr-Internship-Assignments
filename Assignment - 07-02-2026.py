import re
import hashlib
import getpass

# Function to check password strength

def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, "Strong password."

# Function to hash password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User Registration

def register():
    print("\n===== USER REGISTRATION =====")
    username = input("Enter username: ")

    while True:
        password = getpass.getpass("Create password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password != confirm_password:
            print("❌ Passwords do not match. Try again.\n")
            continue

        valid, message = is_strong_password(password)
        if not valid:
            print(f"❌ {message}\n")
            continue

        hashed = hash_password(password)
        print("✅ Registration successful!")
        return username, hashed

# User Login

def login(stored_username, stored_password_hash):
    print("\n===== USER LOGIN =====")
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if username == stored_username and hash_password(password) == stored_password_hash:
            print("✅ Login successful! Access granted.")
            return True
        else:
            attempts -= 1
            print(f"❌ Invalid credentials. Attempts left: {attempts}")

    print("🚫 Too many failed attempts. Access denied.")
    return False

# Main Program

def main():
    print("===== PASSWORD AUTHENTICATION SYSTEM =====")
    stored_username, stored_password_hash = register()
    login(stored_username, stored_password_hash)

if __name__ == "__main__":
    main()