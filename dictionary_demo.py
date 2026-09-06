from hashing import hash_password, verify_password
import time


# ------------------------------------------------
# Sample dictionary for controlled demonstration
# ------------------------------------------------

TEST_WORDLIST = [
    "123456",
    "password",
    "password123",
    "admin",
    "welcome",
    "qwerty",
    "letmein",
    "student123",
    "cybersecurity",
    "test123",
    "MyTest@123",
    "MyTest@123456"
]


def dictionary_attack(target_password):
    """
    Demonstrates a controlled dictionary attack.

    The target password is generated and hashed inside
    this program. Only the supplied test wordlist is used.
    """

    print("\n--- DICTIONARY ATTACK DEMONSTRATION ---")

    # Generate a hash for our test password
    stored_hash = hash_password(target_password)

    print("\nTarget password has been securely hashed.")
    print("Algorithm :", stored_hash["algorithm"])
    print("Iterations:", stored_hash["iterations"])

    print("\nTesting dictionary entries...")

    attempts = 0
    start_time = time.perf_counter()

    for candidate in TEST_WORDLIST:

        attempts += 1

        # Compare candidate with the generated hash
        if verify_password(candidate, stored_hash):

            end_time = time.perf_counter()
            elapsed_time = end_time - start_time

            print("\n⚠ PASSWORD FOUND")
            print(f"Test password : {candidate}")
            print(f"Attempts      : {attempts}")
            print(f"Time taken    : {elapsed_time:.4f} seconds")

            return {
                "found": True,
                "attempts": attempts,
                "time": elapsed_time
            }

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("\nPassword was NOT found in the test dictionary.")
    print(f"Attempts   : {attempts}")
    print(f"Time taken : {elapsed_time:.4f} seconds")

    return {
        "found": False,
        "attempts": attempts,
        "time": elapsed_time
    }


def display_wordlist():

    print("\n--- CONTROLLED TEST WORDLIST ---")

    for number, word in enumerate(TEST_WORDLIST, start=1):
        print(f"{number}. {word}")


# ------------------------------------------------
# Main program
# ------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("          DICTIONARY ATTACK ANALYSIS")
    print("=" * 60)

    print("\nThis is a controlled cybersecurity demonstration.")
    print("Use TEST passwords only.")

    print("\nAvailable test passwords include:")
    print("password123")
    print("admin")
    print("student123")
    print("MyTest@123456")

    target_password = input(
        "\nEnter one of the TEST passwords: "
    )

    if not target_password:
        print("Password cannot be empty.")

    else:

        display_wordlist()

        result = dictionary_attack(target_password)

        print("\n--- ANALYSIS ---")

        if result["found"]:
            print("Security finding: The password exists in the")
            print("test dictionary and is therefore vulnerable")
            print("to this type of dictionary attack.")

        else:
            print("Security finding: The password was not found")
            print("in the supplied test dictionary.")

        print("\nRecommendation:")
        print("Use long, unique passwords that are not based")
        print("on common words or predictable patterns.")

        print("=" * 60)