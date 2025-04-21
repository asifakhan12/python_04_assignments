from hashlib import sha256

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that password.
    """
    return sha256(password.encode()).hexdigest()


def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    if email not in stored_logins:
        return False  # Email not found, return False safely

    return stored_logins[email] == hash_password(password_to_check)


def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }

    # Testing login attempts
    print(login("example@gmail.com", stored_logins, "word"))              # False
    print(login("example@gmail.com", stored_logins, "password"))          # True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))        # True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))        # False

    print(login("student@stanford.edu", stored_logins, "password"))       # False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))    # True

    print(login("notfound@email.com", stored_logins, "anything"))         # False


if __name__ == '__main__':
    main()
