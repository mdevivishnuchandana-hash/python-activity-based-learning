# Fuel Consumption and Route Comparison

**Objective:** To develop a Python program that calculates fuel requirements and journey costs for multiple vehicles based on distance, mileage, and fuel prices. The program also includes reserve fuel requirements and identifies the lowest-cost feasible vehicle for the journey.

## 1. Filename

`FuelRouteComparison.py`

## 2. Algorithm

1. Start.
2. Input the journey distance in kilometres.
3. Input the minimum reserve fuel required in litres.
4. Enter the number of vehicles to compare.
5. For each vehicle, input its name, mileage (km/litre), and fuel price (₹/litre).
6. Validate the input values to ensure that distance, mileage, and fuel price are positive and reserve fuel is non-negative.
7. Calculate the fuel required for the journey using distance divided by mileage.
8. Add the reserve fuel to determine the total fuel required.
9. Calculate the journey cost using the journey fuel requirement multiplied by the fuel price.
10. Check whether each vehicle can meet the total fuel requirement using its available fuel capacity.
11. Identify the feasible vehicles and compare their journey costs.
12. Display the fuel requirements and costs for all vehicles.
13. Identify and display the lowest-cost feasible vehicle.
14. If no vehicle is feasible, display an appropriate message.
15. Stop.

## 3. Text Flowchart

```text
              +----------------------+
              |        START         |
              +----------------------+
                         |
                         v
              +----------------------+
              | Input Journey        |
              | Distance and Reserve |
              +----------------------+
                         |
                         v
              +----------------------+
              | Enter Vehicle Details|
              | Mileage, Fuel Price, |
              | Available Fuel       |
              +----------------------+
                         |
                         v
              +----------------------+
              | Calculate Journey    |
              | Fuel Requirement     |
              +----------------------+
                         |
                         v
              +----------------------+
              | Calculate Total Fuel |
              | Including Reserve    |
              +----------------------+
                         |
                         v
                  +-------------+
                  | Is Vehicle  |
                  | Feasible?   |
                  +-------------+
                    /         \
                  Yes          No
                   |            |
                   v            v
          +----------------+ +----------------+
          | Calculate      | | Mark Vehicle   |
          | Journey Cost   | | Infeasible     |
          +----------------+ +----------------+
                   |            |
                   +-----+------+
                         |
                         v
              +----------------------+
              | Compare Feasible     |
              | Vehicle Costs        |
              +----------------------+
                         |
                         v
              +----------------------+
              | Lowest-Cost Vehicle? |
              +----------------------+
                         |
                         v
              +----------------------+
              | Display Fuel, Costs  |
              | and Best Vehicle     |
              +----------------------+
                         |
                         v
              +----------------------+
              |         STOP         |
              +----------------------+
```

## 4. Python Code

Save this program as **`FuelRouteComparison.py`**.

In this example, the journey distance is 300 km, and at least 5 litres of fuel must remain as a reserve.

```python
# Fuel Consumption and Route Comparison

# Journey details
distance = 300
reserve_fuel = 5

# Vehicle details:
# Name, Mileage, Fuel Price, Available Fuel

vehicles = [
    ("Car", 15, 105, 30),
    ("Bike", 40, 105, 10),
    ("SUV", 12, 100, 35)
]

# Store feasible vehicle details
feasible_vehicles = []

print("FUEL CONSUMPTION AND ROUTE COMPARISON")
print("-------------------------------------")
print("Journey Distance:", distance, "km")
print("Required Reserve Fuel:", reserve_fuel, "litres")

# Process each vehicle
for name, mileage, price, available_fuel in vehicles:

    # Validate vehicle details
    if mileage <= 0 or price <= 0 or available_fuel < 0:
        print("\nInvalid details for", name)
        continue

    # Calculate journey fuel
    journey_fuel = distance / mileage

    # Calculate total fuel including reserve
    total_required = journey_fuel + reserve_fuel

    # Calculate journey cost
    cost = journey_fuel * price

    print("\nVehicle:", name)
    print("Mileage:", mileage, "km/litre")
    print("Fuel Price: Rs.", price, "per litre")
    print("Journey Fuel:", round(journey_fuel, 2), "litres")
    print("Total Fuel Required:", round(total_required, 2), "litres")
    print("Available Fuel:", available_fuel, "litres")
    print("Journey Cost: Rs.", round(cost, 2))

    # Check feasibility
    if available_fuel >= total_required:
        print("Status: Feasible")
        feasible_vehicles.append((name, cost, total_required))
    else:
        print("Status: Not Feasible")

# Find lowest-cost feasible vehicle
print("\n========== FINAL COMPARISON ==========")

if feasible_vehicles:
    best_vehicle = min(feasible_vehicles, key=lambda x: x[1])

    print("Lowest-Cost Feasible Vehicle:", best_vehicle[0])
    print("Journey Cost: Rs.", round(best_vehicle[1], 2))
    print("Total Fuel Required:", round(best_vehicle[2], 2), "litres")
else:
    print("No vehicle satisfies the fuel reserve requirement.")

print("======================================")
```

## 5. Sample Input

The program uses the following sample values directly in the code.

| Parameter | Car | Bike | SUV |
|---|---:|---:|---:|
| Journey distance | 300 km | 300 km | 300 km |
| Mileage | 15 km/litre | 40 km/litre | 12 km/litre |
| Fuel price | ₹105/litre | ₹105/litre | ₹100/litre |
| Available fuel | 30 litres | 10 litres | 35 litres |
| Required reserve | 5 litres | 5 litres | 5 litres |

## 6. Expected Output

```text
FUEL CONSUMPTION AND ROUTE COMPARISON
-------------------------------------
Journey Distance: 300 km
Required Reserve Fuel: 5 litres

Vehicle: Car
Mileage: 15 km/litre
Fuel Price: Rs. 105 per litre
Journey Fuel: 20.0 litres
Total Fuel Required: 25.0 litres
Available Fuel: 30 litres
Journey Cost: Rs. 2100.0
Status: Feasible

Vehicle: Bike
Mileage: 40 km/litre
Fuel Price: Rs. 105 per litre
Journey Fuel: 7.5 litres
Total Fuel Required: 12.5 litres
Available Fuel: 10 litres
Journey Cost: Rs. 787.5
Status: Not Feasible

Vehicle: SUV
Mileage: 12 km/litre
Fuel Price: Rs. 100 per litre
Journey Fuel: 25.0 litres
Total Fuel Required: 30.0 litres
Available Fuel: 35 litres
Journey Cost: Rs. 2500.0
Status: Feasible

========== FINAL COMPARISON ==========
Lowest-Cost Feasible Vehicle: Car
Journey Cost: Rs. 2100.0
Total Fuel Required: 25.0 litres
======================================
```

## 7. Calculations

**Formula 1: Journey fuel requirement**

Journey fuel = Distance ÷ Mileage

For the car:

300 ÷ 15 = **20 litres**

**Formula 2: Total fuel requirement**

Total fuel = Journey fuel + Reserve fuel

20 + 5 = **25 litres**

**Formula 3: Journey cost**

Journey cost = Journey fuel × Fuel price

20 × ₹105 = **₹2,100**

### Vehicle Comparison

| Vehicle | Journey Fuel | Total Fuel Required | Journey Cost | Feasibility |
|---|---:|---:|---:|---|
| Car | 20 litres | 25 litres | ₹2,100 | Feasible |
| Bike | 7.5 litres | 12.5 litres | ₹787.50 | Not feasible |
| SUV | 25 litres | 30 litres | ₹2,500 | Feasible |

The bike has the lowest calculated journey cost, but it does not have enough fuel to complete the journey and maintain the required reserve.

Therefore, **the car is the lowest-cost feasible option**, with a journey cost of ₹2,100.

## 8. Conclusion

The Fuel Consumption and Route Comparison program calculates the fuel required and journey cost for multiple vehicles. It considers mileage, fuel prices, available fuel, and reserve requirements to identify the lowest-cost vehicle that can complete the journey safely.

