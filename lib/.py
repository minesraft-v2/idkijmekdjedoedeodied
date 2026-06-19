import secrets
import string

def generate_secure_string(length=16, use_special_chars=True):
    # Base character sets
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += "!@#$%^&*"
        
    # Generate a cryptographically secure random string
    secure_string = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_string

# Example Usage:
print("Your secure token/password is:")
print(generate_secure_string(24))
