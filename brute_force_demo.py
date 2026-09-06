from hashing import hash_password, verify_password
import itertools
import string
import time


# ------------------------------------------------
# Controlled character set
# ------------------------------------------------
# Deliberately small for a safe demonstration.
CHARACTER_SET = string.ascii_lowercase + string.digits

# Maximum password length used in this demonstration.
MAX_LENGTH = 4


def generate_candidates():

    """
    Generate candidates from a small, controlled
    character set.

    Example:
    a
    b
    ...
    aa
    ab
    ...
    """

    for length in range(1, MAX_LENGTH + 1):

        for combination in itertools.product(
            CHARACTER_SET,
            repeat=length
        ):
            yield "".join(combination)


def brute_force_demo(target_password):

    """
    Controlled brute-force demonstration.

    The password must be a test password and should
    be short enough to fit within the demonstration
    search space.
    """

    print("\n--- CONTROLLED BRUTE-FORCE DEMONSTRATION ---")

    stored_hash = hash_password(target_password)

    print("\nTarget password has been hashed.")
    print("Algorithm :", stored_hash["algorithm"])
    print("Iterations:", stored_hash["iterations"])

    print("\nSearch configuration:")
    print("Character set: lowercase letters + digits")
    print(f"Maximum length: {MAX_LENGTH}")

    attempts = 0
    start_time = time.perf_counter()

    for candidate in generate_candidates():

        attempts += 1

        if verify_password(candidate, stored_hash):

            end_time = time.perf_counter()
            elapsed_time = end_time - start_time

            print("\nPASSWORD FOUND")
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

    print("\nPassword was NOT found.")
    print(f"Attempts   : {attempts}")
    print(f"Time taken : {elapsed_time:.4f} seconds")

    return {
        "found": False,
        "attempts": attempts,
        "time": elapsed_time
    }


def show_configuration():

    print("\n--- BRUTE-FORCE CONFIGURATION ---")

    print("Character set:")
    print("abcdefghijklmnopqrstuvwxyz")
    print("0123456789")

    print(f"\nMaximum password length: {MAX_LENGTH}")

    print(
        "\nThis limited search space is intentionally used "
        "for an educational demonstration."
    )


# ------------------------------------------------
# Main program
# ------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("             BRUTE-FORCE ANALYSIS")
    print("=" * 60)

    print("\nControlled cybersecurity demonstration")
    print("Use TEST passwords only.")

    show_configuration()

    print("\nFor this demo, use a short lowercase/digit password.")
    print("Examples:")
    print("a")
    print("ab")
    print("abc")
    print("a12")

    target_password = input(
        "\nEnter a TEST password: "
    )

    if not target_password:

        print("Password cannot be empty.")

    elif len(target_password) > MAX_LENGTH:

        print(
            f"Password is longer than the demonstration "
            f"limit of {MAX_LENGTH} characters."
        )

    elif any(
        character not in CHARACTER_SET
        for character in target_password
    ):

        print(
            "Password contains characters outside the "
            "controlled demonstration character set."
        )

    else:

        result = brute_force_demo(target_password)

        print("\n--- SECURITY ANALYSIS ---")

        if result["found"]:

            print(
                "Finding: The short test password was "
                "discovered within the limited search space."
            )

            print(
                "Lesson: Increasing password length and "
                "complexity greatly increases the search space."
            )

        else:

            print(
                "Finding: The password was not discovered "
                "within the controlled search space."
            )

        print("\nRecommendation:")
        print(
            "Use long, unique passwords and avoid "
            "short predictable passwords."
        )

    print("=" * 60)