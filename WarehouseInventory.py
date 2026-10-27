# Warehouse Inventory Reconciliation

**Objective:** To develop a Python program that compares opening stock, incoming quantities, dispatched quantities, and actual closing stock for multiple products. The program detects stock discrepancies and calculates replenishment requirements.

## 1. Filename

`WarehouseInventory.py`

## 2. Algorithm

1. Start.
2. Define the product details, including opening stock, incoming stock, dispatched stock, actual closing stock, and minimum stock level.
3. Calculate the expected closing stock using opening stock, incoming stock, and dispatched stock.
4. Compare the expected closing stock with the actual closing stock.
5. If both values are equal, display "No Discrepancy."
6. Otherwise, calculate the stock discrepancy.
7. Compare the actual closing stock with the minimum stock level.
8. If the actual stock is below the minimum level, calculate the replenishment quantity.
9. Repeat the process for all products.
10. Display the inventory reconciliation report, discrepancies, and replenishment requirements.
11. Stop.

## 3. Text Flowchart

```text
             +----------------------+
             |        START         |
             +----------------------+
                        |
                        v
             +----------------------+
             | Enter Product Details|
             | Opening, Incoming,   |
             | Dispatched, Actual   |
             | Closing Stock        |
             +----------------------+
                        |
                        v
             +----------------------+
             | Calculate Expected   |
             | Closing Stock        |
             +----------------------+
                        |
                        v
             +----------------------+
             | Compare Expected and |
             | Actual Closing Stock |
             +----------------------+
                        |
                        v
                +---------------+
                | Stock Matches?|
                +---------------+
                  /           \
                Yes            No
                 |              |
                 v              v
       +----------------+ +------------------+
       | No Discrepancy | | Calculate Stock  |
       |                | | Discrepancy      |
       +----------------+ +------------------+
                 |              |
                 +------+-------+
                        |
                        v
             +----------------------+
             | Check Minimum Stock  |
             | Level                |
             +----------------------+
                        |
                        v
                +---------------+
                | Stock Below   |
                | Minimum Level?|
                +---------------+
                  /           \
                Yes            No
                 |              |
                 v              v
       +----------------+ +------------------+
       | Calculate      | | No Replenishment |
       | Replenishment  | | Required         |
       +----------------+ +------------------+
                 |              |
                 +------+-------+
                        |
                        v
             +----------------------+
             | Display Inventory    |
             | Reconciliation Report|
             +----------------------+
                        |
                        v
             +----------------------+
             |         STOP         |
             +----------------------+
```

## 4. Python Code

Save the program as **`WarehouseInventory.py`**.

```python
# Warehouse Inventory Reconciliation

# Product details:
# Name, Opening Stock, Incoming Stock,
# Dispatched Stock, Actual Closing Stock, Minimum Stock

products = [
    ("Laptop", 100, 20, 50, 70, 30),
    ("Keyboard", 80, 30, 40, 65, 25),
    ("Mouse", 60, 10, 30, 35, 20),
    ("Monitor", 50, 15, 20, 40, 25)
]

print("WAREHOUSE INVENTORY RECONCILIATION")
print("----------------------------------")

for name, opening, incoming, dispatched, actual, minimum in products:

    # Calculate expected closing stock
    expected = opening + incoming - dispatched

    # Calculate stock discrepancy
    discrepancy = actual - expected

    # Calculate replenishment requirement
    replenishment = max(0, minimum - actual)

    # Display product details
    print("\nProduct:", name)
    print("Opening Stock:", opening)
    print("Incoming Stock:", incoming)
    print("Dispatched Stock:", dispatched)
    print("Expected Closing Stock:", expected)
    print("Actual Closing Stock:", actual)

    # Detect discrepancy
    if discrepancy == 0:
        print("Discrepancy: 0 (No Discrepancy)")
    else:
        print("Discrepancy:", discrepancy)

        if discrepancy > 0:
            print("Status: Excess stock found.")
        else:
            print("Status: Stock shortage detected.")

    # Display replenishment requirement
    print("Minimum Stock Level:", minimum)
    print("Replenishment Required:", replenishment)

    if replenishment > 0:
        print("Action: Reorder stock.")
    else:
        print("Action: No replenishment required.")

print("\nInventory reconciliation completed.")
```

## 5. Sample Input

The program uses the following sample inventory data.

| Product | Opening | Incoming | Dispatched | Actual Closing | Minimum Stock |
|---|---:|---:|---:|---:|---:|
| Laptop | 100 | 20 | 50 | 70 | 30 |
| Keyboard | 80 | 30 | 40 | 65 | 25 |
| Mouse | 60 | 10 | 30 | 35 | 20 |
| Monitor | 50 | 15 | 20 | 40 | 25 |

All quantities are measured in units.

## 6. Expected Output

```text
WAREHOUSE INVENTORY RECONCILIATION
----------------------------------

Product: Laptop
Opening Stock: 100
Incoming Stock: 20
Dispatched Stock: 50
Expected Closing Stock: 70
Actual Closing Stock: 70
Discrepancy: 0 (No Discrepancy)
Minimum Stock Level: 30
Replenishment Required: 0
Action: No replenishment required.

Product: Keyboard
Opening Stock: 80
Incoming Stock: 30
Dispatched Stock: 40
Expected Closing Stock: 70
Actual Closing Stock: 65
Discrepancy: -5
Status: Stock shortage detected.
Minimum Stock Level: 25
Replenishment Required: 0
Action: No replenishment required.

Product: Mouse
Opening Stock: 60
Incoming Stock: 10
Dispatched Stock: 30
Expected Closing Stock: 40
Actual Closing Stock: 35
Discrepancy: -5
Status: Stock shortage detected.
Minimum Stock Level: 20
Replenishment Required: 0
Action: No replenishment required.

Product: Monitor
Opening Stock: 50
Incoming Stock: 15
Dispatched Stock: 20
Expected Closing Stock: 45
Actual Closing Stock: 40
Discrepancy: -5
Status: Stock shortage detected.
Minimum Stock Level: 25
Replenishment Required: 0
Action: No replenishment required.

Inventory reconciliation completed.
```

## 7. Formulas Used

**Expected Closing Stock**

Expected Closing Stock = Opening Stock + Incoming Stock − Dispatched Stock

**Stock Discrepancy**

Stock Discrepancy = Actual Closing Stock − Expected Closing Stock

- Zero discrepancy: stock matches the records.
- Positive discrepancy: excess stock exists.
- Negative discrepancy: a stock shortage exists.

**Replenishment Requirement**

Replenishment = Maximum of (0, Minimum Stock Level − Actual Closing Stock)

For example, if the minimum stock level is 50 units and actual stock is 35 units:

Replenishment = 50 − 35 = **15 units**

### Important distinction

A stock discrepancy and a replenishment requirement are different. A product may have a discrepancy but still have enough stock, so replenishment is not necessarily required.

## 8. Conclusion

The Warehouse Inventory Reconciliation program calculates expected closing stock, identifies differences between recorded and actual quantities, and determines whether products need replenishment. It helps warehouse managers identify stock shortages, excess inventory, and products that require reordering.
.