'''# Campus Event Financial Planning

## 1. Filename
`CampusEventPlanning.py`

## 2. Algorithm

1. Start.
2. Initialize the costs of venue, equipment, catering, transport, and certificates.
3. Calculate the total event cost by adding all expenses.
4. Set the registration fee, expected number of participants, and sponsorship amount.
5. Calculate registration income by multiplying participants by the registration fee.
6. Calculate the sponsorship shortfall by subtracting sponsorship from the total event cost.
7. Calculate the total available funds by adding registration income and sponsorship.
8. Calculate the final balance by subtracting the total event cost from the total available funds.
9. Calculate the minimum registrations required to break even.
10. Display the total cost, registration income, sponsorship, shortfall, final balance, and minimum registrations.
11. Display whether the event makes a profit, incurs a loss, or breaks even.
12. Stop.

## 3. Text Flowchart

```text
             +------------------+
             |      START       |
             +------------------+
                      |
                      v
       +----------------------------+
       | Enter Event Expense Costs  |
       | Venue, Equipment, Catering,|
       | Transport, Certificates    |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Calculate Total Event Cost |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Set Registration Fee,      |
       | Participants, Sponsorship  |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Calculate Registration     |
       | Income                     |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Calculate Sponsorship      |
       | Shortfall                  |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Calculate Total Funds and  |
       | Final Balance              |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Calculate Minimum          |
       | Registrations Required     |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Display All Results        |
       +----------------------------+
                      |
                      v
       +----------------------------+
       | Check Profit, Loss, or      |
       | Break-Even Status          |
       +----------------------------+
                      |
                      v
             +------------------+
             |       STOP       |
             +------------------+
```

## 4. Python Code

Save the following program as **`CampusEventPlanning.py`**.

```python
# Campus Event Financial Planning

# Event expenses
venue = 5000
equipment = 4000
catering = 10000
transport = 3000
certificates = 2000

# Calculate total event cost
total_cost = venue + equipment + catering + transport + certificates

# Registration details
registration_fee = 200
participants = 100
sponsorship = 5000

# Calculate registration income
registration_income = participants * registration_fee

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - sponsorship)

# Calculate total available funds
total_funds = registration_income + sponsorship

# Calculate final balance
balance = total_funds - total_cost

# Calculate minimum registrations required
minimum_registrations = max(
    0,
    (shortfall + registration_fee - 1) // registration_fee
)

# Display results
print("CAMPUS EVENT FINANCIAL PLANNING")
print("--------------------------------")
print("Total Event Cost: Rs.", total_cost)
print("Registration Fee: Rs.", registration_fee)
print("Expected Participants:", participants)
print("Registration Income: Rs.", registration_income)
print("Sponsorship Received: Rs.", sponsorship)
print("Sponsorship Shortfall: Rs.", shortfall)
print("Total Available Funds: Rs.", total_funds)
print("Final Balance: Rs.", balance)
print("Minimum Registrations Required:", minimum_registrations)

# Check financial status
if balance > 0:
    print("Result: Event makes a profit.")
elif balance < 0:
    print("Result: Event makes a loss.")
else:
    print("Result: Event breaks even.")
```

## 5. Output

```text
CAMPUS EVENT FINANCIAL PLANNING
--------------------------------
Total Event Cost: Rs. 24000
Registration Fee: Rs. 200
Expected Participants: 100
Registration Income: Rs. 20000
Sponsorship Received: Rs. 5000
Sponsorship Shortfall: Rs. 19000
Total Available Funds: Rs. 25000
Final Balance: Rs. 1000
Minimum Registrations Required: 95
Result: Event makes a profit.
```

## Conclusion

The program calculates the total cost of organizing a campus event, registration income, sponsorship shortfall, and minimum registrations required to break even. In this example, the total event cost is ₹24,000, and the event makes a profit of ₹1,000 with 100 participants and ₹5,000 in sponsorship.
.'''