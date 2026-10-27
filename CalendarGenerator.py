# Nested Loop Calendar Generator – Python Program

## 1. Aim
To develop a Python program that generates a formatted monthly calendar using the starting weekday and number of days in a month. The program uses nested loops to align dates correctly into weeks and validates the supplied month length.

## 2. Algorithm
1. Start the program.
2. Enter the month name, starting weekday, and number of days.
3. Validate the starting weekday and the number of days.
4. Display the weekday headings.
5. Print blank spaces before the first date based on the starting weekday.
6. Use a loop to generate the dates.
7. Use a nested loop to print dates in properly aligned rows.
8. Move to a new line after each week.
9. Display the completed calendar.
10. Stop the program.

## 3. Flowchart

```text
           START
             |
             v
 Enter Month, Starting Weekday,
       and Number of Days
             |
             v
     Validate Input Values
             |
             v
       Are Values Valid?
         /         \
       No           Yes
       |              |
       v              v
 Display Error    Print Weekday
       |           Headings
       |              |
       |              v
       |       Print Initial Spaces
       |              |
       |              v
       |       Generate Dates
       |       Using Nested Loops
       |              |
       |              v
       |       Align Dates into Weeks
       |              |
       |              v
       |       Display Calendar
       |              |
       └───────┬──────┘
               v
              STOP
```

## 4. Python Code

**Filename:** `CalendarGenerator.py`

# Nested Loop Calendar Generator

# Get calendar details
month = input("Enter month name: ")
start_day = int(input("Enter starting weekday (0=Mon, 6=Sun): "))
days = int(input("Enter number of days in the month: "))

# Validate the input
if start_day < 0 or start_day > 6:
    print("Invalid starting weekday. Enter a value from 0 to 6.")

elif days < 28 or days > 31:
    print("Invalid month length. Enter a value from 28 to 31.")

else:
    print("\n       ", month)
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Print spaces before the first date
    for i in range(start_day):
        print("    ", end="")

    # Print dates using nested loops
    date = 1

    while date <= days:

        # Print one week at a time
        for weekday in range(7):

            if date <= days:
                print(f"{date:3}", end=" ")

                date += 1

            else:
                break

        print()

    print("\nCalendar generated successfully.")

## 5. Sample Input

```text
Enter month name: October
Enter starting weekday (0=Mon, 6=Sun): 3
Enter number of days in the month: 31
```

Here, `3` means Thursday because Monday is represented by `0`.

## 6. Expected Output

```text
        October
Mon Tue Wed Thu Fri Sat Sun
                  1   2   3   4
  5   6   7   8   9  10  11
 12  13  14  15  16  17  18
 19  20  21  22  23  24  25
 26  27  28  29  30  31

Calendar generated successfully.
```






