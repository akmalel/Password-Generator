
import random
import string

# Keep track of generated passwords to ensure uniqueness
generated_passwords = set()

def generate_password():
    # Define the characters to choose from
    alphanumerical_characters = string.ascii_letters + string.digits
    symbols = string.punctuation
    
    # Generate 8 random alphanumerical characters
    password = ''.join(random.choices(alphanumerical_characters, k=8))
    
    # Add 1 random symbol
    password += random.choice(symbols)
    
    # Shuffle the resulting password to mix the symbol
    password = ''.join(random.sample(password, len(password)))
    
    # Ensure the password is unique
    if password in generated_passwords:
        return generate_password()  # Recursively generate a new password if not unique
    else:
        generated_passwords.add(password)
        return password

# Generate a password and print it
print(generate_password())
