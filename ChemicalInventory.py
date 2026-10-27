# Laboratory Chemical Inventory Validation – Python Program

## 1. Aim
To develop a Python program that validates hypothetical laboratory chemical inventory records based on storage categories, maximum permitted quantities, and chemical compatibility restrictions. The program identifies and flags invalid records.

## 2. Algorithm
1. Start the program.
2. Define chemical storage categories and their maximum quantities.
3. Define compatibility restrictions between storage categories.
4. Store hypothetical chemical inventory records.
5. Check whether each chemical belongs to a valid storage category.
6. Compare the recorded quantity with the maximum permitted quantity.
7. Check for incompatible chemicals stored in the same storage unit.
8. Flag invalid records and display the reasons.
9. Display the validation summary.
10. Stop the program.

## 3. Flowchart

```text
          START
            |
            v
  Define Storage Categories
            |
            v
 Define Maximum Quantities
            |
            v
 Define Compatibility Rules
            |
            v
 Read Inventory Records
            |
            v
 Check Storage Category
            |
            v
 Check Maximum Quantity
            |
            v
 Check Compatibility
            |
            v
 Are All Checks Valid?
       /           \
      No            Yes
      |              |
      v              v
 Flag Invalid     Mark as Valid
 Record               |
       \              /
        v            v
       Display Results
            |
            v
            STOP
```

## 4. Python Code

**Filename:** `ChemicalInventory.py`

The following program uses **hypothetical categories, quantities, and compatibility rules for educational purposes only**. Real laboratories must use chemical-specific safety data sheets and approved storage procedures.

# Laboratory Chemical Inventory Validation

# Maximum quantity allowed for each hypothetical storage category (litres)
max_quantities = {
    "Flammable": 50,
    "Corrosive": 30,
    "Oxidizer": 20,
    "General": 100
}

# Hypothetical incompatible storage categories
incompatible_categories = [
    ("Flammable", "Oxidizer"),
    ("Corrosive", "Oxidizer")
]

# Inventory records:
# Chemical, Category, Quantity (litres), Storage Unit
inventory = [
    ("Ethanol", "Flammable", 20, "Cabinet A"),
    ("Acid Solution", "Corrosive", 10, "Cabinet B"),
    ("Oxidizing Solution", "Oxidizer", 25, "Cabinet A"),
    ("Cleaning Liquid", "General", 15, "Cabinet C"),
    ("Solvent", "Flammable", 60, "Cabinet D")
]

print("LABORATORY CHEMICAL INVENTORY VALIDATION")
print("----------------------------------------")

valid_count = 0
invalid_count = 0

# Check each inventory record
for chemical, category, quantity, storage_unit in inventory:

    errors = []

    # Check whether the storage category exists
    if category not in max_quantities:
        errors.append("Invalid storage category")

    else:
        # Check maximum permitted quantity
        if quantity < 0:
            errors.append("Quantity cannot be negative")
        elif quantity > max_quantities[category]:
            errors.append("Maximum quantity exceeded")

    # Check compatibility with other chemicals
    for other_chemical, other_category, other_quantity, other_unit in inventory:

        if chemical == other_chemical:
            continue

        if storage_unit == other_unit:
            if (
                (category, other_category) in incompatible_categories
                or
                (other_category, category) in incompatible_categories
            ):
                errors.append(
                    "Incompatible with " + other_chemical
                )

    # Remove duplicate error messages
    errors = list(set(errors))

    # Display validation result
    print("\nChemical:", chemical)
    print("Category:", category)
    print("Quantity:", quantity, "litres")
    print("Storage Unit:", storage_unit)

    if errors:
        print("Status: INVALID")
        for error in errors:
            print(" -", error)
        invalid_count += 1
    else:
        print("Status: VALID")
        valid_count += 1

# Display summary
print("\n----------------------------------------")
print("INVENTORY VALIDATION SUMMARY")
print("Valid Records:", valid_count)
print("Invalid Records:", invalid_count)
print("Total Records:", len(inventory))
print("Validation completed.")

## 5. Sample Inventory Data

| Chemical | Category | Quantity | Storage Unit |
|---|---|---:|---|
| Ethanol | Flammable | 20 L | Cabinet A |
| Acid Solution | Corrosive | 10 L | Cabinet B |
| Oxidizing Solution | Oxidizer | 25 L | Cabinet A |
| Cleaning Liquid | General | 15 L | Cabinet C |
| Solvent | Flammable | 60 L | Cabinet D |

## 6. Expected Output

```text
LABORATORY CHEMICAL INVENTORY VALIDATION
----------------------------------------

Chemical: Ethanol
Category: Flammable
Quantity: 20 litres
Storage Unit: Cabinet A
Status: INVALID
 - Incompatible with Oxidizing Solution

Chemical: Acid Solution
Category: Corrosive
Quantity: 10 litres
Storage Unit: Cabinet B
Status: VALID

Chemical: Oxidizing Solution
Category: Oxidizer
Quantity: 25 litres
Storage Unit: Cabinet A
Status: INVALID
 - Maximum quantity exceeded
 - Incompatible with Ethanol

Chemical: Cleaning Liquid
Category: General
Quantity: 15 litres
Storage Unit: Cabinet C
Status: VALID

Chemical: Solvent
Category: Flammable
Quantity: 60 litres
Storage Unit: Cabinet D
Status: INVALID
 - Maximum quantity exceeded

----------------------------------------
INVENTORY VALIDATION SUMMARY
Valid Records: 2
Invalid Records: 3
Total Records: 5
Validation completed.
```

**Note:** The order of error messages may vary because the program removes duplicate messages using a Python set.

## 7. Logic Used

### A. Maximum quantity validation

If the quantity exceeds the maximum permitted quantity, the record is marked invalid.

Example:

- Category: Flammable
- Maximum quantity: 50 litres
- Recorded quantity: 60 litres
- Result: **Invalid — maximum quantity exceeded**

### B. Compatibility validation

The program checks whether two chemicals are assigned to the same storage unit and whether their categories appear in the hypothetical incompatibility rules.

Example:

- Ethanol: Flammable
- Oxidizing Solution: Oxidizer
- Storage unit: Cabinet A for both
- Result: **Invalid — incompatible storage combination**

### C. Validation summary

The program counts the valid and invalid inventory records and displays the total.

## 8. Conclusion

The Laboratory Chemical Inventory Validation program uses Python dictionaries, lists, loops, and conditional statements to validate hypothetical laboratory inventory records. It checks storage categories, maximum quantities, and compatibility restrictions, then identifies invalid records and explains the reasons.

