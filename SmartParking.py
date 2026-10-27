# Smart Parking Fee Management System

**Objective:** To develop a Python program that calculates parking fees based on vehicle category, entry and exit times, overnight parking, daily fee limits, and penalty conditions while validating time inputs.

## 1. Filename
`SmartParking.py`

## 2. Algorithm

1. Start.
2. Define parking rates for different vehicle categories.
3. Define the daily parking limit and penalty charges.
4. Input the vehicle category, entry time, and exit time.
5. Validate the vehicle category and time inputs.
6. Calculate the parking duration using the entry and exit times.
7. If the exit time is earlier than the entry time, consider the possibility of overnight parking.
8. Calculate the parking fee based on the vehicle category and duration.
9. Apply the daily parking limit wherever applicable.
10. Add penalty charges if the parking duration or other conditions violate the parking rules.
11. Display the parking duration, base fee, penalty, and total fee.
12. Stop.

## 3.Flowchart

```text
             +----------------------+
             |        START         |
             +----------------------+
                        |
                        v
             +----------------------+
             | Define Vehicle Rates |
             | Daily Limits &        |
             | Penalties             |
             +----------------------+
                        |
                        v
             +----------------------+
             | Enter Vehicle Type,   |
             | Entry Time & Exit Time|
             +----------------------+
                        |
                        v
             +----------------------+
             | Validate Inputs       |
             +----------------------+
                        |
                        v
                 +-------------+
                 | Inputs Valid?|
                 +-------------+
                   /         \
                 No           Yes
                 |             |
                 v             v
        +----------------+  +------------------+
        | Display Error  |  | Calculate Parking|
        | Message        |  | Duration         |
        +----------------+  +------------------+
                 |                  |
                 |                  v
                 |         +------------------+
                 |         | Overnight       |
                 |         | Parking?        |
                 |         +------------------+
                 |                  |
                 |                  v
                 |         +------------------+
                 |         | Calculate Base   |
                 |         | Parking Fee      |
                 |         +------------------+
                 |                  |
                 |                  v
                 |         +------------------+
                 |         | Apply Daily Fee  |
                 |         | Limit            |
                 |         +------------------+
                 |                  |
                 |                  v
                 |         +------------------+
                 |         | Add Penalties    |
                 |         | If Applicable    |
                 |         +------------------+
                 |                  |
                 |                  v
                 |         +------------------+
                 |         | Display Duration,|
                 |         | Charges & Total  |
                 |         +------------------+
                 |                  |
                 +------------------+
                        |
                        v
             +----------------------+
             |         STOP         |
             +----------------------+
```

## 4. Python Code

**Assumptions used in this program:**

- Parking charges are calculated for every started hour.
- Car: ₹30 per hour, with a daily fee limit of ₹300.
- Bike: ₹15 per hour, with a daily fee limit of ₹150.
- Van: ₹50 per hour, with a daily fee limit of ₹500.
- Overnight parking attracts an additional ₹50 penalty.
- Parking for more than 12 hours attracts an additional ₹100 long-stay penalty.
- If the exit time is earlier than the entry time, the vehicle is assumed to have exited the following day.
- The daily limit applies to the base parking fee; penalties are added afterward.

Save this code as **`SmartParking.py`**.

```python
# Smart Parking Fee Management System

from datetime import datetime
import math

# Vehicle rates and daily limits
rates = {
    "car": 30,
    "bike": 15,
    "van": 50
}

daily_limits = {
    "car": 300,
    "bike": 150,
    "van": 500
}

# Penalty charges
overnight_penalty = 50
long_stay_penalty = 100

print("SMART PARKING FEE MANAGEMENT")
print("--------------------------------")

# Input vehicle category
vehicle = input("Enter vehicle type (car/bike/van): ").lower()

if vehicle not in rates:
    print("Error: Invalid vehicle category.")

else:
    entry_time = input("Enter entry time (HH:MM): ")
    exit_time = input("Enter exit time (HH:MM): ")

    try:
        # Validate time format
        entry = datetime.strptime(entry_time, "%H:%M")
        exit = datetime.strptime(exit_time, "%H:%M")

        # Reject identical times because they are ambiguous
        if entry_time == exit_time:
            print("Error: Entry and exit times cannot be identical.")

        else:
            # Calculate parking duration
            duration = (exit - entry).total_seconds() / 60

            overnight = False

            # Handle overnight parking
            if duration < 0:
                duration += 24 * 60
                overnight = True

            # Calculate billed hours
            hours = math.ceil(duration / 60)

            # Calculate base fee
            base_fee = hours * rates[vehicle]

            # Apply daily fee limit
            base_fee = min(base_fee, daily_limits[vehicle])

            # Calculate penalties
            penalty = 0

            if overnight:
                penalty += overnight_penalty

            if duration > 12 * 60:
                penalty += long_stay_penalty

            # Calculate total fee
            total_fee = base_fee + penalty

            # Display parking summary
            print("\n--------- PARKING SUMMARY ---------")
            print("Vehicle Type:", vehicle.capitalize())
            print("Entry Time:", entry_time)
            print("Exit Time:", exit_time)
            print("Parking Duration:", round(duration / 60, 2), "hours")
            print("Billed Hours:", hours)
            print("Base Parking Fee: Rs.", base_fee)
            print("Penalty Charges: Rs.", penalty)
            print("Total Parking Fee: Rs.", total_fee)
            print("-----------------------------------")

    except ValueError:
        print("Error: Invalid time format.")
        print("Please enter time in HH:MM format, e.g., 09:30.")
```

## 5. Sample Input

Consider the following example:

| Input | Value |
|---|---|
| Vehicle type | car |
| Entry time | 22:30 |
| Exit time | 01:15 |

The vehicle enters at 10:30 PM and exits at 1:15 AM the following day.

## 6. Expected Output

```text
SMART PARKING FEE MANAGEMENT
--------------------------------
Enter vehicle type (car/bike/van): car
Enter entry time (HH:MM): 22:30
Enter exit time (HH:MM): 01:15

--------- PARKING SUMMARY ---------
Vehicle Type: Car
Entry Time: 22:30
Exit Time: 01:15
Parking Duration: 2.75 hours
Billed Hours: 3
Base Parking Fee: Rs. 90
Penalty Charges: Rs. 50
Total Parking Fee: Rs. 140
-----------------------------------
```

### Calculation

**Step 1: Calculate parking duration**

From 10:30 PM to 1:15 AM = 2 hours 45 minutes = 2.75 hours.

**Step 2: Calculate billed hours**

Since every started hour is charged, 2.75 hours is rounded up to 3 hours.

**Step 3: Calculate the base fee**

3 × ₹30 = ₹90.

**Step 4: Apply penalties**

The vehicle parked overnight, so an additional ₹50 is charged.

**Step 5: Calculate the total fee**

Total fee = ₹90 + ₹50 = **₹140**.

## 7. Conclusion

The Smart Parking Fee Management System calculates parking charges according to vehicle category and parking duration. It handles overnight parking, applies daily fee limits, adds penalties for overnight and long-stay parking, and validates the time inputs.

