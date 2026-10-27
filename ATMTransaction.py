# ATM Transaction Sequence Simulation

## 1. Filename
`ATMTransaction.py`

## 2. Algorithm

1. Start.
2. Initialize the ATM account balance and maximum withdrawal limit.
3. Enter the number of transactions to process.
4. For each transaction, enter the transaction type (deposit or withdrawal) and amount.
5. If the transaction is a deposit:
   - Check whether the amount is greater than zero.
   - If valid, add the amount to the balance and record the deposit.
   - Otherwise, reject the transaction.
6. If the transaction is a withdrawal:
   - Check whether the amount is greater than zero.
   - Check whether the amount is within the withdrawal limit.
   - Check whether sufficient balance is available.
   - If all conditions are satisfied, subtract the amount from the balance and record the withdrawal.
   - Otherwise, reject the transaction.
7. If the transaction type is invalid, reject the transaction.
8. Display the final balance, total deposits, total withdrawals, successful transactions, and rejected transactions.
9. Stop.

## 3. Text Flowchart

```text
              +------------------+
              |      START       |
              +------------------+
                       |
                       v
          +--------------------------+
          | Initialize Account      |
          | Balance and Withdrawal   |
          | Limit                    |
          +--------------------------+
                       |
                       v
          +--------------------------+
          | Enter Number of          |
          | Transactions             |
          +--------------------------+
                       |
                       v
          +--------------------------+
          | Enter Transaction Type   |
          | and Amount               |
          +--------------------------+
                       |
                       v
                +-------------+
                | Is Deposit? |
                +-------------+
                  /         \
                Yes          No
                 |            |
                 v            v
       +----------------+  +------------------+
       | Is Amount      |  | Is Withdrawal?   |
       | Greater Than 0? |  +------------------+
       +----------------+       /         \
          /       \            Yes         No
        Yes        No           |           |
         |          |           v           v
         v          v   +----------------+ +----------------+
   +-----------+ +---------+ | Check Amount,  | | Reject Invalid |
   | Add Amount| | Reject  | | Limit and      | | Transaction   |
   | to Balance| | Deposit | | Available      | +----------------+
   +-----------+ +---------+ | Balance        |         |
         |          |       +----------------+         |
         |          |          /       \               |
         |          |       Valid     Invalid           |
         |          |         |          |              |
         |          |         v          v              |
         |          |   +-----------+ +-----------+     |
         |          |   | Deduct    | | Reject    |     |
         |          |   | Withdrawal| | Withdrawal|     |
         |          |   +-----------+ +-----------+     |
         |          |         |          |              |
         +----------+---------+----------+--------------+
                                   |
                                   v
                       +-----------------------+
                       | More Transactions?    |
                       +-----------------------+
                           /             \
                         Yes              No
                          |                |
                          v                v
                  Enter Next       +------------------+
                  Transaction      | Display Summary  |
                                   +------------------+
                                            |
                                            v
                                   +------------------+
                                   |       STOP       |
                                   +------------------+
```

## 4. Python Code

Save the following program as **`ATMTransaction.py`**.

```python
# ATM Transaction Sequence Simulation

# Initial account details
balance = 5000
withdrawal_limit = 2000

# Transaction summary
total_deposits = 0
total_withdrawals = 0
successful_transactions = 0
rejected_transactions = 0

# Number of transactions
n = 5

print("ATM TRANSACTION SIMULATION")
print("--------------------------")
print("Initial Balance: Rs.", balance)
print("Withdrawal Limit: Rs.", withdrawal_limit)

# Process transactions
for i in range(1, n + 1):
    print("\nTransaction", i)

    transaction_type = input(
        "Enter transaction type (deposit/withdraw): "
    ).lower()

    amount = float(input("Enter amount: Rs. "))

    if amount <= 0:
        print("Rejected: Amount must be greater than zero.")
        rejected_transactions += 1

    elif transaction_type == "deposit":
        balance += amount
        total_deposits += amount
        successful_transactions += 1
        print("Deposit successful.")

    elif transaction_type == "withdraw":
        if amount > withdrawal_limit:
            print("Rejected: Withdrawal limit exceeded.")
            rejected_transactions += 1

        elif amount > balance:
            print("Rejected: Insufficient balance.")
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful_transactions += 1
            print("Withdrawal successful.")

    else:
        print("Rejected: Invalid transaction type.")
        rejected_transactions += 1

    print("Current Balance: Rs.", balance)

# Display transaction summary
print("\n========== TRANSACTION SUMMARY ==========")
print("Final Balance: Rs.", balance)
print("Total Deposits: Rs.", total_deposits)
print("Total Withdrawals: Rs.", total_withdrawals)
print("Successful Transactions:", successful_transactions)
print("Rejected Transactions:", rejected_transactions)
print("=========================================")
```

## 5. Sample Input

For this example, enter the following transactions when prompted.

| Transaction | Type | Amount |
|---|---|---:|
| 1 | Deposit | ₹1,000 |
| 2 | Withdraw | ₹2,000 |
| 3 | Withdraw | ₹3,000 |
| 4 | Withdraw | ₹5,000 |
| 5 | Deposit | ₹500 |

**Initial balance:** ₹5,000  
**Maximum withdrawal per transaction:** ₹2,000

## 6. Expected Output

```text
ATM TRANSACTION SIMULATION
--------------------------
Initial Balance: Rs. 5000
Withdrawal Limit: Rs. 2000

Transaction 1
Enter transaction type (deposit/withdraw): deposit
Enter amount: Rs. 1000
Deposit successful.
Current Balance: Rs. 6000

Transaction 2
Enter transaction type (deposit/withdraw): withdraw
Enter amount: Rs. 2000
Withdrawal successful.
Current Balance: Rs. 4000

Transaction 3
Enter transaction type (deposit/withdraw): withdraw
Enter amount: Rs. 3000
Rejected: Withdrawal limit exceeded.
Current Balance: Rs. 4000

Transaction 4
Enter transaction type (deposit/withdraw): withdraw
Enter amount: Rs. 5000
Rejected: Withdrawal limit exceeded.
Current Balance: Rs. 4000

Transaction 5
Enter transaction type (deposit/withdraw): deposit
Enter amount: Rs. 500
Deposit successful.
Current Balance: Rs. 4500

========== TRANSACTION SUMMARY ==========
Final Balance: Rs. 4500.0
Total Deposits: Rs. 1500.0
Total Withdrawals: Rs. 2000.0
Successful Transactions: 3
Rejected Transactions: 2
=========================================
```

## 7. Explanation

- **Initial balance:** The account starts with ₹5,000.
- **Total deposits:** ₹1,000 + ₹500 = ₹1,500.
- **Total withdrawals:** ₹2,000.
- **Withdrawal limit:** Withdrawals exceeding ₹2,000 per transaction are rejected.
- **Final balance:** ₹5,000 + ₹1,500 − ₹2,000 = ₹4,500.
- **Successful transactions:** 3.
- **Rejected transactions:** 2.

## Conclusion

This Python program simulates ATM transactions by processing deposits and withdrawals, maintaining the account balance, enforcing a withdrawal limit, rejecting invalid transactions, and displaying a transaction summary.

**Next step:** You can run this program in Python IDLE or VS Code and change the initial balance, withdrawal limit, or transaction count to test different cases.'''