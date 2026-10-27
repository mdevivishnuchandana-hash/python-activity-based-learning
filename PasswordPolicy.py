# Password Policy Validation Engine – Python Program

## 1. Aim
To develop a Python program that validates passwords based on minimum length, character categories, repeated characters, and prohibited substrings. The program identifies invalid passwords and explains each failed condition.

## 2. Algorithm
1. Start the program.
2. Define the password policy rules.
3. Store a list of sample passwords.
4. Check whether each password meets the minimum length.
5. Check whether it contains uppercase letters, lowercase letters, digits, and special characters.
6. Check for excessive consecutive repeated characters.
7. Check whether the password contains prohibited substrings.
8. Display each failed condition.
9. Display whether each password is valid or invalid.
10. Stop the program.

## 3. Flowchart

```text
          START
            |
            v
    Define Password Rules
            |
            v
     Read Sample Password
            |
            v
   Check Minimum Length
            |
            v
 Check Character Categories
            |
            v
  Check Repeated Characters
            |
            v
 Check Prohibited Substrings
            |
            v
   Are All Rules Satisfied?
        /          \
       No           Yes
       |              |
       v              v
 Display Failed    Password
 Conditions         Valid
        \             /
         v           v
       Display Result
            |
            v
       More Passwords?
         /       \
       Yes        No
        |          |
        v          v
      Repeat      STOP
```

## 4. Python Code

**Filename:** `PasswordPolicy.py`

# Password Policy Validation Engine

import string

# Password policy settings
MIN_LENGTH = 8
MAX_REPEATED_CHARACTERS = 2

# Prohibited substrings
prohibited_substrings = ["password", "123456", "admin"]

# Sample passwords for testing
passwords = [
    "Abc@1234",
    "abc123",
    "AAA@1234",
    "Admin@567",
    "Strong#Pass9"
]

print("PASSWORD POLICY VALIDATION ENGINE")
print("---------------------------------")

for password in passwords:

    errors = []

    # Rule 1: Minimum length
    if len(password) < MIN_LENGTH:
        errors.append(
            "Password must contain at least 8 characters."
        )

    # Rule 2: Uppercase letter
    if not any(char.isupper() for char in password):
        errors.append(
            "Password must contain an uppercase letter."
        )

    # Rule 3: Lowercase letter
    if not any(char.islower() for char in password):
        errors.append(
            "Password must contain a lowercase letter."
        )

    # Rule 4: Digit
    if not any(char.isdigit() for char in password):
        errors.append(
            "Password must contain a digit."
        )

    # Rule 5: Special character
    if not any(char in string.punctuation for char in password):
        errors.append(
            "Password must contain a special character."
        )

    # Rule 6: Repeated consecutive characters
    repeated_count = 1
    repetition_found = False

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            repeated_count += 1

            if repeated_count > MAX_REPEATED_CHARACTERS:
                repetition_found = True
                break
        else:
            repeated_count = 1

    if repetition_found:
        errors.append(
            "Password must not contain more than 2 "
            "consecutive identical characters."
        )

    # Rule 7: Prohibited substrings (case-insensitive)
    password_lower = password.lower()

    for word in prohibited_substrings:
        if word in password_lower:
            errors.append(
                "Password contains prohibited substring: "
                + word
            )

    # Display results
    print("\nPassword:", password)

    if errors:
        print("Status: INVALID")

        for error in errors:
            print("-", error)
    else:
        print("Status: VALID")

print("\nValidation completed.")

## 5. Sample Input Data

The program tests these sample passwords:

| Password | Purpose |
|---|---|
| `Abc@1234` | Meets the defined rules |
| `abc123` | Tests minimum length and missing character categories |
| `AAA@1234` | Tests consecutive repeated characters and missing lowercase letters |
| `Admin@567` | Tests prohibited substring detection |
| `Strong#Pass9` | Tests a password that meets the defined rules |

*These are illustrative test strings, not recommendations for passwords to use on real accounts.*

## 6. Expected Output

```text
PASSWORD POLICY VALIDATION ENGINE
---------------------------------

Password: Abc@1234
Status: VALID

Password: abc123
Status: INVALID
- Password must contain at least 8 characters.
- Password must contain an uppercase letter.
- Password must contain a special character.

Password: AAA@1234
Status: INVALID
- Password must contain a lowercase letter.
- Password must not contain more than 2 consecutive identical characters.

Password: Admin@567
Status: INVALID
- Password contains prohibited substring: admin

Password: Strong#Pass9
Status: VALID

Validation completed.
```

**Note:** The failed-condition messages may appear in a different order, but the validation results will remain the same.

## 7. Explanation of the Rules

| Rule | Description | Example of Failure |
|---|---|---|
| Minimum length | Password must have at least 8 characters. | `abc123` |
| Uppercase letter | Must contain at least one uppercase letter. | `hello@123` |
| Lowercase letter | Must contain at least one lowercase letter. | `ABC@1234` |
| Digit | Must contain at least one number. | `Hello@World` |
| Special character | Must contain punctuation such as `@`, `#`, or `!`. | `Hello123` |
| Repetition | Must not contain more than 2 identical consecutive characters. | `AAA@1234` |
| Prohibited substring | Must not contain `password`, `123456`, or `admin`, regardless of case. | `Admin@567` |

## 8. Conclusion

The Password Policy Validation Engine checks passwords against multiple rules using Python strings, loops, conditional statements, and built-in functions. It identifies invalid passwords and explains each failed condition, helping users understand how to satisfy the defined password policy.

