## 🏧 ATM Simulation – Python Console App
A simple command-line ATM simulation built with Python that mimics real-world banking operations like 
deposits, withdrawals, balance checks, and transaction history.

## 🚀 Features

🔐 Secure PIN-based login
💰 Deposit & Withdraw money
📋 View transaction statement
👤 View user details
🔑 Change PIN/password
💾 Data saved automatically using JSON
⚠️ Input validation – handles invalid/non-numeric input gracefully


## 🛡️ Input Validation
This project handles invalid input using try/except:
python
try:
    x = int(input("choose a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    continue

If the user types letters or symbols instead of a number, the program shows a friendly error and re-prompts instead of crashing.


## 🧪 Sample Accounts (for Testing)
Account_No   Name     PIN       Balance
101          Sam      1433      ₹10,000
102          Ram      1566      ₹10,000
103          Sanju    1933      ₹10,000
