Password Security & Cracking Analysis
1. Introduction

Password Security & Cracking Analysis is a Python-based cybersecurity project designed to analyze password strength and demonstrate the security risks associated with weak passwords. The project uses only test passwords in a controlled environment.

2. Objective
Analyze password strength.
Identify weak and common passwords.
Demonstrate secure password hashing.
Demonstrate controlled dictionary and brute-force attacks.
Provide recommendations for creating stronger passwords.
3. Technologies Used
Python
hashlib
secrets
Regular Expressions
itertools
PBKDF2-HMAC-SHA256
4. Modules
main.py
password_analyzer.py
hashing.py
dictionary_demo.py
brute_force_demo.py
Password Analyzer: Checks length, uppercase, lowercase, numbers, symbols, and common patterns.
Hashing: Converts test passwords into salted secure hashes.
Dictionary Demo: Demonstrates how common test passwords can be found using a limited wordlist.
Brute-Force Demo: Demonstrates password guessing using a deliberately small search space.
Main: Provides the user interface and connects the modules.
5. Result

The project successfully demonstrates that short, common, and predictable passwords are easier to discover in controlled testing. It also shows how password hashing and salting can improve the security of stored passwords.

6. Conclusion

This project provided practical knowledge of password security, hashing, password analysis, and ethical password-cracking concepts. It highlights the importance of using long, unique passwords, secure password hashing, and multi-factor authentication.

Ethical Note: All testing is performed locally using test passwords and limited attack demonstrations. No real accounts or external systems are targeted.