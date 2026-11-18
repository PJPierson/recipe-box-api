from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(plaintext_password: str) -> str:
    return generate_password_hash(plaintext_password)

def verify_password(stored_hash: str, candidate_password: str) -> bool:
    return check_password_hash(stored_hash, candidate_password)

if __name__ == "__main__":
    password = "P@ssw0rd123!"
    stored_hash = hash_password(password)
    print("Stored hash:", stored_hash)
    print("Correct password matches:", verify_password(stored_hash, "P@ssw0rd123!"))
    print("Wrong password matches:", verify_password(stored_hash, "wrongpassword"))