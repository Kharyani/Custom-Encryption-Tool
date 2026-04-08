# 🔐 Custom Data Encryption & Decryption Tool

## 📌 Overview
This is a Python CLI-based application that securely encrypts and decrypts text using a custom multi-layer encryption algorithm. It simulates real-world data protection systems.

---

## ⚙️ Features
- Encrypt text using a **custom multi-layer algorithm**  
- Decrypt encrypted text back to its original form  
- Save encrypted data to a JSON file  
- Load and decrypt stored data  
- Key-based encryption system  
- Timestamp included for saved data  

---

## 🔐 Encryption Algorithm
The encryption process includes multiple layers:

1. **Dynamic Character Shifting**  
   Each character is shifted using the formula:  
   `new_char = ord(char) + (key + index)`

2. **String Reversal**  
   The shifted string is reversed to make the output harder to read  

3. **Base64 Encoding**  
   Converts the reversed string into a non-readable format  

### 🔓 Decryption Process
To decrypt the text, the steps are reversed: