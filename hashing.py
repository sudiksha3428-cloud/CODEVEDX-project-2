import hashlib
import secrets
import base64


def hash_password(password):
    """
    Securely hash a password using PBKDF2-HMAC-SHA256.

    A random salt is generated for every password.
    """

    # Generate a random 16-byte salt
    salt = secrets.token_bytes(16)

    # PBKDF2 parameters
    iterations = 600_000

    # Generate password hash
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations
    )

    # Convert binary values to text for storage
    salt_encoded = base64.b64encode(salt).decode("utf-8")
    hash_encoded = base64.b64encode(password_hash).decode("utf-8")

    return {
        "algorithm": "PBKDF2-HMAC-SHA256",
        "iterations": iterations,
        "salt": salt_encoded,
        "hash": hash_encoded
    }


def verify_password(password, stored_hash):
    """
    Verify a password against a previously generated hash.
    """

    try:
        salt = base64.b64decode(stored_hash["salt"])
        expected_hash = base64.b64decode(stored_hash["hash"])
        iterations = stored_hash["iterations"]

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations
        )

        return secrets.compare_digest(new_hash, expected_hash)

    except Exception:
        return False


# ------------------------------------------------
# Test the hashing module directly
# ------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("             SECURE PASSWORD HASHING")
    print("=" * 60)

    password = input("Enter a TEST password: ")

    if not password:
        print("Password cannot be empty.")

    else:

        stored_hash = hash_password(password)

        print("\n--- HASH INFORMATION ---")
        print(f"Algorithm : {stored_hash['algorithm']}")
        print(f"Iterations: {stored_hash['iterations']}")
        print(f"Salt      : {stored_hash['salt']}")
        print(f"Hash      : {stored_hash['hash']}")

        print("\n--- PASSWORD VERIFICATION ---")

        test_password = input(
            "Enter password again to verify: "
        )

        if verify_password(test_password, stored_hash):
            print("Result: Password verified successfully.")
        else:
            print("Result: Password verification failed.")

        print("=" * 60)