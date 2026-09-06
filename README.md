# Password Security & Cracking Analysis

A Python-based cybersecurity project for analyzing password strength,
demonstrating secure password hashing, and studying controlled password
attack techniques in an ethical test environment.

## Project Overview

Weak and predictable passwords can be vulnerable to password-guessing
techniques such as dictionary attacks and brute-force attacks.

This project demonstrates these concepts using only test passwords and
a controlled local environment.

## Objectives

- Analyze password strength.
- Identify common and weak password patterns.
- Demonstrate secure password hashing.
- Demonstrate password verification.
- Perform a controlled dictionary attack.
- Perform a limited brute-force demonstration.
- Provide password security recommendations.

## Technologies Used

- Python 3
- Regular Expressions
- PBKDF2-HMAC-SHA256
- hashlib
- secrets
- itertools
- Base64
- CSV

## Project Structure

```text
password-security-and-cracking-analysis/
│
├── main.py
├── password_analyzer.py
├── hashing.py
├── dictionary_demo.py
├── brute_force_demo.py
├── report_generator.py
├── README.md
├── requirements.txt
│
├── data/
│   └── test_passwords.txt
│
└── reports/
    └── password_analysis.csv
