# Delivery Optimizer

## Overview
This project implements a **Delivery Optimizer** to determine the best route for a delivery executive (Aman) to deliver food orders from two restaurants to two consumers in the shortest possible time. It calculates travel time using the **Haversine formula** and optimizes the sequence of deliveries while considering meal preparation times.

## Features
- Computes the best delivery route to minimize total time.
- Uses the **Haversine formula** to compute real-world geographical distances.
- Considers **meal preparation times** for accurate delivery estimates.
- Implements **modular and well-structured Python code** following best practices.

## File Structure
```
.
├── DeliveryOptimizer.py   # Optimizes the delivery route
├── HaversineCalculator.py # Computes distances using the Haversine formula
├── Locations.py           # Defines location objects with latitude and longitude
├── main.py                # Entry point to run the optimization
```

## Code Explanation
### 1. **HaversineCalculator.py**
This file implements the **Haversine formula** to calculate distances between two geo-locations.
#### Key Functions:
- `calculate(lat1, lon1, lat2, lon2)`: Computes the great-circle distance between two points.
- `travel_time_km(distance_km)`: Converts distance into travel time assuming an average speed of **20 km/h**.

### 2. **Locations.py**
This file defines a `Location` class to represent a geographical location.
#### Key Functions:
- `distance_to(other)`: Uses **HaversineCalculator** to compute distance between locations.

### 3. **DeliveryOptimizer.py**
This file contains the `DeliveryOptimizer` class, which determines the best sequence for deliveries.
#### Key Functions:
- `compute_best_route()`: Evaluates multiple delivery sequences and selects the fastest one.
- `compute_route_time(route)`: Computes the total time taken for a specific delivery sequence.

### 4. **main.py**
This is the entry point of the program.
#### Steps:
1. Defines locations for Aman, two restaurants, and two consumers.
2. Specifies meal preparation times for each restaurant.
3. Instantiates `DeliveryOptimizer` to compute the best route.
4. Prints the optimal delivery sequence and estimated total time.

## How to Run the Code
### Prerequisites
Ensure you have **Python 3.x** installed.

### Steps:
1. Clone or download the project files.
2. Open a terminal and navigate to the project folder.
3. Run the script using:
   ```sh
   python main.py
   ```

### Expected Output (Example)
```
Best Route:
- Restaurant 1
- Consumer 1
- Restaurant 2
- Consumer 2
Total Estimated Time: X.XX hours
```
*Note: The actual route and time will depend on the locations provided.*

## Assumptions
- Aman, restaurants, and consumers get notified at the same time.
- Restaurants confirm order preparation immediately.
- Travel speed is fixed at **20 km/h**.
- No real-world road constraints or traffic considerations.

## Author
- **Name:** Gaurav Singh  
- **Email:** [sintg1999@gmail.com](mailto:sintg1999@gmail.com)  
- **Location:** New Delhi, India  