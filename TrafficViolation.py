# Traffic Violation Penalty Calculator – Python Program

**Filename:** `TrafficViolation.py`

## 1. Aim
To develop a Python program that processes multiple traffic violations based on vehicle category, offence type, and repeat-offence status. The program calculates the final penalty and identifies possible disqualification conditions.

## 2. Algorithm
1. Start the program.
2. Define fine amounts for different offences and vehicle categories.
3. Store the details of multiple traffic violations.
4. Read the vehicle category, offence type, and repeat-offence status.
5. Calculate the fine for each violation.
6. Apply an additional fine for repeat offences, where specified.
7. Calculate the total penalty.
8. Check whether the violation triggers a possible disqualification condition.
9. Display the violation details, individual fines, total penalty, and status.
10. Stop the program.

## 3. Flowchart

```text
       START
         |
         v
 Define Fine Rules
         |
         v
 Enter Violation Details
         |
         v
 Identify Vehicle Category
         |
         v
 Identify Offence Type
         |
         v
 Is it a Repeat Offence?
      /         \
    Yes          No
     |            |
     v            |
 Apply Repeat     |
 Fine             |
      \           /
       v         v
   Calculate Final Fine
         |
         v
 Check Disqualification
 Condition
         |
         v
 Display Penalty Details
         |
         v
 More Violations?
      /       \
    Yes        No
     |          |
     v          v
 Process      Display Total
 Next         Penalty
 Violation       |
      |          v
      └──────>  STOP
```

## 4. Python Code

The following program uses **illustrative fine amounts for a college assignment**, not official legal rates. Disqualification flags are also simplified examples; actual consequences depend on applicable traffic laws and the circumstances of the offence.

# Traffic Violation Penalty Calculator

# Illustrative fine rules (amounts in rupees)
fine_rules = {
    "Car": {
        "Over Speeding": 1000,
        "No Helmet/Seat Belt": 500,
        "Signal Jumping": 1000,
        "No License": 2000
    },
    "Bike": {
        "Over Speeding": 1000,
        "No Helmet/Seat Belt": 500,
        "Signal Jumping": 1000,
        "No License": 2000
    },
    "Truck": {
        "Over Speeding": 1500,
        "No Helmet/Seat Belt": 500,
        "Signal Jumping": 1000,
        "No License": 2000
    }
}

# Illustrative repeat-offence additional fine
repeat_extra = 500

# Example disqualification flags for demonstration
disqualification_offences = [
    "No License"
]

total_penalty = 0
disqualification_flag = False

violations = [
    ("Car", "Over Speeding", False),
    ("Bike", "No Helmet/Seat Belt", True),
    ("Truck", "No License", False),
    ("Car", "Signal Jumping", True)
]

print("TRAFFIC VIOLATION PENALTY CALCULATOR")
print("------------------------------------")

for vehicle, offence, repeat in violations:

    # Validate vehicle category
    if vehicle not in fine_rules:
        print("Invalid vehicle category:", vehicle)
        continue

    # Validate offence type
    if offence not in fine_rules[vehicle]:
        print("Invalid offence type:", offence)
        continue

    # Calculate base fine
    fine = fine_rules[vehicle][offence]

    # Add extra fine for repeat offences
    if repeat:
        fine = fine + repeat_extra

    total_penalty = total_penalty + fine

    # Check disqualification condition
    if offence in disqualification_offences:
        disqualification_flag = True

    # Display violation details
    print("\nVehicle Category:", vehicle)
    print("Offence Type:", offence)
    print("Repeat Offence:", "Yes" if repeat else "No")
    print("Final Fine: Rs.", fine)

    if offence in disqualification_offences:
        print("Disqualification Check: Review required")
    else:
        print("Disqualification Check: Not flagged by this example")

print("\n------------------------------------")
print("Total Penalty: Rs.", total_penalty)

if disqualification_flag:
    print("Disqualification Status: Review required")
else:
    print("Disqualification Status: No disqualification flag")

print("Penalty calculation completed.")

## 5. Sample Input Data

The program processes these four violations:

| No. | Vehicle Category | Offence Type | Repeat Offence |
|---:|---|---|---|
| 1 | Car | Over Speeding | No |
| 2 | Bike | No Helmet/Seat Belt | Yes |
| 3 | Truck | No License | No |
| 4 | Car | Signal Jumping | Yes |

## 6. Expected Output

```text
TRAFFIC VIOLATION PENALTY CALCULATOR
------------------------------------

Vehicle Category: Car
Offence Type: Over Speeding
Repeat Offence: No
Final Fine: Rs. 1000
Disqualification Check: Not flagged by this example

Vehicle Category: Bike
Offence Type: No Helmet/Seat Belt
Repeat Offence: Yes
Final Fine: Rs. 1000
Disqualification Check: Not flagged by this example

Vehicle Category: Truck
Offence Type: No License
Repeat Offence: No
Final Fine: Rs. 2000
Disqualification Check: Review required

Vehicle Category: Car
Offence Type: Signal Jumping
Repeat Offence: Yes
Final Fine: Rs. 1500
Disqualification Check: Not flagged by this example

------------------------------------
Total Penalty: Rs. 5500
Disqualification Status: Review required
Penalty calculation completed.
```

## 7. Formula

**Final Fine = Base Fine + Repeat-Offence Additional Fine**

For example, for a repeat signal-jumping offence:

Final Fine = ₹1,000 + ₹500 = **₹1,500**

**Total Penalty** = Sum of all individual fines.

Total Penalty = ₹1,000 + ₹1,000 + ₹2,000 + ₹1,500 = **₹5,500**

## 8. Conclusion

The Traffic Violation Penalty Calculator processes multiple traffic offences and calculates the total penalty. It considers vehicle category, offence type, and repeat-offence status. It also flags cases that require a disqualification review. The program demonstrates how Python dictionaries, loops, conditions, and arithmetic operations can be used to automate penalty calculations.

