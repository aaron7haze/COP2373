import re

# Validate US phone numbers in common formats
def validate_phone(phone):
    # Regex allows: (123) 456-7890, 123-456-7890, or 1234567890
    pattern = r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$'
    return bool(re.fullmatch(pattern, phone))


# Validate SSN in the format 123-45-6789
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.fullmatch(pattern, ssn))


# Validate ZIP codes: 12345 or 12345-6789
def validate_zip(zipcode):
    pattern = r'^(\d{5}|\d{5}-\d{4})$'
    return bool(re.fullmatch(pattern, zipcode))


# Main program: get input and show validation results
def main():
    print("=== Input Validation Program ===")

    phone = input("Enter a phone number: ")
    ssn = input("Enter a social security number: ")
    zipcode = input("Enter a ZIP code: ")

    print("\n--- Validation Results ---")
    print(f"Phone Number Valid: {validate_phone(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"ZIP Code Valid: {validate_zip(zipcode)}")


# Run the program
if __name__ == "__main__":
    main()
