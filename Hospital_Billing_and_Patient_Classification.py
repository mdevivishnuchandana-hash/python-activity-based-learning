
"""
HOSPITAL BILLING AND PATIENT CLASSIFICATION SYSTEM

# ALGORITHM
   1. Start.
   2. Input patient name, age, and insurance status.
   3. Validate the inputs.
   4. Initialize consultation, diagnostic, and treatment charges.
   5. Calculate the total bill.
   6. Apply a 10% consultation concession if age >= 60.
   7. Apply a 20% insurance concession to the remaining bill
      if the patient has insurance.
   8. Classify the patient.
   9. Display the bill and final payable amount.
   10. Stop.

# FLOWCHART
   (START)
      |
      v
   / Input patient details /
      |
      v
   { Valid input? }
      | No                 | Yes
      v                    v
   / Display error /    [Calculate total bill]
      |                    |
      v                    v
    (STOP)            { Age >= 60? }
                         | Yes       | No
                         v            |
                  [Senior discount]   |
                         |            |
                         +-----+------+
                               |
                               v
                         { Insured? }
                          | Yes    | No
                          v         |
                   [Insurance      |
                    discount]      |
                          |         |
                          +----+----+
                               |
                               v
                      [Classify patient]
                               |
                               v
                       / Display bill /
                               |
                               v
                            (STOP)



#TEST CASES
   TC01: Age 35, no insurance -> General, Rs. 4700
   TC02: Age 65, no insurance -> Senior Citizen, Rs. 4650
   TC03: Age 40, insurance -> Insured, Rs. 3760
   TC04: Age 65, insurance -> Senior Citizen, Rs. 3720
   TC05: Negative age -> Error
   TC06: Invalid insurance status -> Error
   TC07: Age 60, no insurance -> Senior Citizen, Rs. 4650
   TC08: Age 0, no insurance -> General, Rs. 4700

#SAMPLE OUTPUT
   Patient: Ravi
   Age: 65
   Insurance: yes

   Total Charges: Rs. 4700.00
   Senior Citizen Discount: Rs. 50.00
   Insurance Discount: Rs. 930.00
   Net Payable: Rs. 3720.00
   Patient Category: Senior Citizen



CONSULTATION_FEE = 500.00
DIAGNOSTIC_FEE = 1200.00
TREATMENT_FEE = 3000.00

SENIOR_AGE = 60
SENIOR_DISCOUNT_RATE = 0.10
INSURANCE_DISCOUNT_RATE = 0.20


def calculate_bill(name, age, insured):
    """Calculate charges, concessions, and patient category."""

    if not name.strip():
        raise ValueError("Patient name cannot be empty.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if not isinstance(insured, bool):
        raise ValueError("Insurance status must be True or False.")

    charges = [
        CONSULTATION_FEE,
        DIAGNOSTIC_FEE,
        TREATMENT_FEE
    ]

    if any(charge < 0 for charge in charges):
        raise ValueError("Charges cannot be negative.")

    total_bill = sum(charges)

    senior_discount = 0.0
    if age >= SENIOR_AGE:
        senior_discount = (
            CONSULTATION_FEE * SENIOR_DISCOUNT_RATE
        )

    balance = total_bill - senior_discount

    insurance_discount = 0.0
    if insured:
        insurance_discount = (
            balance * INSURANCE_DISCOUNT_RATE
        )

    net_bill = balance - insurance_discount

    if age >= SENIOR_AGE:
        category = "Senior Citizen"
    elif insured:
        category = "Insured"
    else:
        category = "General"

    return {
        "name": name,
        "consultation": CONSULTATION_FEE,
        "diagnostics": DIAGNOSTIC_FEE,
        "treatment": TREATMENT_FEE,
        "total": total_bill,
        "senior_discount": senior_discount,
        "insurance_discount": insurance_discount,
        "net_bill": net_bill,
        "category": category
    }


def main():
    try:
        name = input("Enter patient name: ").strip()
        age = int(input("Enter patient age: "))

        insurance_input = input(
            "Has insurance? (yes/no): "
        ).strip().lower()

        if insurance_input not in ("yes", "no"):
            raise ValueError(
                "Insurance status must be yes or no."
            )

        bill = calculate_bill(
            name,
            age,
            insurance_input == "yes"
        )

        print("\n===== HOSPITAL BILL =====")
        print("Patient Name:", bill["name"])
        print("Patient Category:", bill["category"])
        print(f"Consultation Fee: Rs. {bill['consultation']:.2f}")
        print(f"Diagnostic Fee: Rs. {bill['diagnostics']:.2f}")
        print(f"Treatment Fee: Rs. {bill['treatment']:.2f}")
        print(f"Total Charges: Rs. {bill['total']:.2f}")
        print(
            f"Senior Citizen Discount: "
            f"Rs. {bill['senior_discount']:.2f}"
        )
        print(
            f"Insurance Discount: "
            f"Rs. {bill['insurance_discount']:.2f}"
        )
        print(f"Net Payable: Rs. {bill['net_bill']:.2f}")
        print("=========================")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
