import re


def analyze_password(password):
    score = 0
    feedback = []

    # 1. Password length
    length = len(password)

    if length >= 16:
        score += 2
    elif length >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # 2. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # 3. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # 4. Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # 5. Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # 6. Common passwords
    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "welcome",
        "letmein"
    ]

    if password.lower() in common_passwords:
        score = max(0, score - 3)
        feedback.append("This is a commonly used password.")

    # 7. Repeated characters
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        feedback.append("Avoid repeated characters.")

    # 8. Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # 9. Recommendation
    if not feedback:
        feedback.append(
            "Good password structure. Keep it unique and do not reuse it."
        )

    return {
        "length": length,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


# Test the analyzer directly
if __name__ == "__main__":

    print("=" * 55)
    print("           PASSWORD SECURITY ANALYZER")
    print("=" * 55)

    password = input("Enter a TEST password: ")

    if password == "":
        print("Password cannot be empty.")
    else:
        result = analyze_password(password)

        print("\n--------- SECURITY REPORT ---------")
        print(f"Password Length : {result['length']}")
        print(f"Security Score  : {result['score']}/7")
        print(f"Strength        : {result['strength']}")

        print("\nRecommendations:")

        for message in result["feedback"]:
            print(f"- {message}")

        print("-----------------------------------")