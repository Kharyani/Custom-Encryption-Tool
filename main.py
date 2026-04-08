import json
import time
import base64

# ==============================
# 🔐 ADVANCED ENCRYPTION
# ==============================
def encrypt(text, key):
    shifted = ""
    for i, char in enumerate(text):
        shift = key + i
        shifted += chr((ord(char) + shift) % 256)
    reversed_text = shifted[::-1]
    encoded = base64.b64encode(reversed_text.encode()).decode()
    return encoded

# ==============================
# 🔓 ADVANCED DECRYPTION
# ==============================
def decrypt(text, key):
    try:
        decoded = base64.b64decode(text.encode()).decode()
        reversed_text = decoded[::-1]
        original = ""
        for i, char in enumerate(reversed_text):
            shift = key + i
            original += chr((ord(char) - shift) % 256)
        return original
    except Exception:
        return "❌ Invalid data or key!"

# ==============================
# 💾 SAVE FILE
# ==============================
def save_to_file(data):
    content = {
        "timestamp": time.ctime(),
        "encrypted_data": data
    }
    try:
        with open("secure_data.json", "w") as file:
            json.dump(content, file, indent=4)
        print("✅ Data saved successfully!")
    except Exception as e:
        print("❌ Error saving file:", e)

# ==============================
# 📂 LOAD FILE
# ==============================
def load_from_file():
    try:
        with open("secure_data.json", "r") as file:
            content = json.load(file)
            print("📅 Saved on:", content["timestamp"])
            return content["encrypted_data"]
    except FileNotFoundError:
        print("❌ File not found!")
        return ""
    except Exception as e:
        print("❌ Error loading file:", e)
        return ""

# ==============================
# 🧠 MAIN MENU
# ==============================
def main():
    encrypted_data = ""
    while True:
        print("\n==== 🔐 Advanced Encryption Tool ====")
        print("1. Encrypt Data")
        print("2. Decrypt Data")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter text: ")
            try:
                key = int(input("Enter key (number): "))
                encrypted_data = encrypt(text, key)
                print("🔒 Encrypted:", encrypted_data)
            except ValueError:
                print("❌ Key must be a number!")

        elif choice == "2":
            if not encrypted_data:
                print("❌ No encrypted data available!")
            else:
                try:
                    key = int(input("Enter key (number): "))
                    result = decrypt(encrypted_data, key)
                    print("🔓 Decrypted:", result)
                except ValueError:
                    print("❌ Key must be a number!")

        elif choice == "3":
            if encrypted_data:
                save_to_file(encrypted_data)
            else:
                print("❌ Nothing to save!")

        elif choice == "4":
            encrypted_data = load_from_file()

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()