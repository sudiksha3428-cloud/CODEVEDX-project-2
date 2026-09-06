from password_analyzer import analyze_password


def display_banner():
    print("\n" + "=" * 60)
    print("        PASSWORD SECURITY & CRACKING ANALYSIS")
    print("=" * 60)


def analyze_single_password():

    print("\n--- PASSWORD STRENGTH ANALYSIS ---")

    password = input("Enter a TEST password: ")

    if not password:
        print("Password cannot be empty.")
        return

    result = analyze_password(password)

    print("\n--------- SECURITY REPORT ---------")
    print(f"Password Length : {result['length']}")
    print(f"Security Score  : {result['score']}/7")
    print(f"Strength        : {result['strength']}")

    print("\nRecommendations:")

    for message in result["feedback"]:
        print(f"- {message}")

    print("-----------------------------------")


def compare_passwords():

    print("\n--- PASSWORD COMPARISON ---")
    print("Use TEST passwords only.")

    passwords = []

    for i in range(3):

        password = input(
            f"Enter test password {i + 1}: "
        )

        if password:
            passwords.append(password)

    if not passwords:
        print("No passwords entered.")
        return

    print("\n--------- COMPARISON RESULT ---------")

    for number, password in enumerate(passwords, start=1):

        result = analyze_password(password)

        print(
            f"Password {number}: "
            f"Length = {result['length']}, "
            f"Score = {result['score']}/7, "
            f"Strength = {result['strength']}"
        )


def show_security_tips():

    print("\n--- PASSWORD SECURITY BEST PRACTICES ---")

    tips = [
        "Use at least 12 characters.",
        "Use uppercase and lowercase letters.",
        "Include numbers.",
        "Include special characters.",
        "Avoid common passwords.",
        "Avoid names and birthdays.",
        "Never reuse passwords.",
        "Use a password manager.",
        "Never store passwords as plain text.",
        "Use secure password-hashing algorithms.",
        "Enable multi-factor authentication."
    ]

    for number, tip in enumerate(tips, start=1):
        print(f"{number}. {tip}")


def main():

    while True:

        display_banner()

        print("\nMAIN MENU")
        print("1. Analyze Password Strength")
        print("2. Compare Test Passwords")
        print("3. Password Security Best Practices")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":

            analyze_single_password()

        elif choice == "2":

            compare_passwords()

        elif choice == "3":

            show_security_tips()

        elif choice == "4":

            print("\nThank you for using the project.")
            print("Exiting...")
            break

        else:

            print("\nInvalid option.")
            print("Please select a number from 1 to 4.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()