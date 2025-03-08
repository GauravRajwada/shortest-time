from Locations import Location
from DeliveryOptimizer import DeliveryOptimizer

if __name__ == "__main__":
    # Define Locations
    aman = Location("Aman", 12.9352, 77.6245) 
    r1 = Location("Restaurant 1", 12.9373, 77.6229)
    r2 = Location("Restaurant 2", 12.9325, 77.6265)
    c1 = Location("Consumer 1", 12.9407, 77.6198)
    c2 = Location("Consumer 2", 12.9281, 77.6289)

    # Meal Preparation Times (in hours)
    prep_time_r1 = 0.25  # 15 mins
    prep_time_r2 = 0.33  # 20 mins

    # Compute Best Route
    optimizer = DeliveryOptimizer(aman, r1, r2, c1, c2, prep_time_r1, prep_time_r2)
    best_route, best_time = optimizer.compute_best_route()

    # Print Result
    print("Best Route:")
    for loc in best_route:
        print(f"- {loc.name}")
    
    print(f"Total Estimated Time: {best_time:.2f} hours")
