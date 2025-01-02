**Python Banking System**

**Project Description**

This project implements a Banking System using Python. It simulates basic banking operations such as account creation, balance inquiry, deposits, withdrawals, transfers, and transaction history. The system is designed with object-oriented programming principles and includes features for data validation and secure access.

**Features**

Account Management

Create customer accounts with details such as name, phone, age, Aadhaar, address, balance, and PIN.
Validate customer data (phone number, age, Aadhaar, PIN) during account creation.
Transactions

Check Balance: View current account balance.
Deposit: Add funds to an account.
Withdraw: Withdraw funds with balance validation.
Transfer Money: Transfer funds between accounts within the same bank.
Account Modifications

Update customer details (name, address, phone number).
Change account PIN securely.
Transaction History

View a mini statement of recent transactions.
Security

Validate user credentials (account number and PIN) before any operation.
Technologies Used
Programming Language: Python
Modules:
datetime: For tracking transaction dates and times.
How to Use
Create Accounts

Use the Sbi class constructor to create accounts.
python

c1 = Sbi("John Doe", 9876543210, 30, 123456789012, "123 Main St", 1000, 1234)
Perform Transactions

Use class methods like check_balance(), deposite(), withdraw(), transfer_money(), and mini_statement().
Modify Account Details

Use the modify_customer_details() method to update customer details.
View Mini Statement

Use the mini_statement() method to view transaction history.
Example Usage
python
Copy code
# Create customers
c1 = Sbi("Alice", 9876543210, 25, 123456789012, "123 Elm St", 5000, 1234)
c2 = Sbi("Bob", 8765432109, 30, 234567890123, "456 Oak St", 3000, 5678)

# Deposit money
Sbi.deposite()

# Withdraw money
Sbi.withdraw()

# Transfer funds
Sbi.transfer_money()

# Check balance
Sbi.check_balance()

# View mini statement
Sbi.mini_statement()
Validation Rules
Phone Number: Must be 10 digits.
Aadhaar Number: Must be 12 digits.
Age: Must be 18 or above.
PIN: Must be a 4-digit number.
Future Enhancements
Add persistent data storage using a database (e.g., SQLite).
Implement a graphical user interface (GUI).
Introduce multi-bank support with cross-bank transfers.
Add SMS or email notifications for transactions.
Author
Konapa Saiprakash Reddy, Python Full Stack Developer from Hyderabad.

