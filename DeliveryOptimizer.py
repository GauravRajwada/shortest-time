from HarversineCalculator import HaversineCalculator

class DeliveryOptimizer:
    """ Computes the best route to minimize total delivery time """

    def __init__(self, aman, restaurant1, restaurant2, consumer1, consumer2, prep_time1, prep_time2):
        """
            Initialize the optimizer with locations and meal preparation times
            Args:
                aman (Location): Aman's location
                restaurant1 (Location): First restaurant's location
                restaurant2 (Location): Second restaurant's location
                consumer1 (Location): First consumer's location
                consumer2 (Location): Second consumer's location
                prep_time1 (float): Meal preparation time at first restaurant in hours
                prep_time2 (float): Meal preparation time at second restaurant in hours
        """
        self.aman = aman
        self.r1 = restaurant1
        self.r2 = restaurant2
        self.c1 = consumer1
        self.c2 = consumer2
        self.pt1 = prep_time1
        self.pt2 = prep_time2

    def compute_best_route(self):
        """ 
            Determines the optimal delivery sequence minimizing total time 
            Returns:
                list: Best route sequence
                float: Total time taken to deliver all meals    
        """
        possible_routes = [
            [self.r1, self.c1, self.r2, self.c2],
            [self.r1, self.r2, self.c1, self.c2],
            [self.r2, self.c2, self.r1, self.c1],
            [self.r2, self.r1, self.c2, self.c1],
        ]

        best_time = float('inf')
        best_route = None

        for route in possible_routes:
            total_time = self.compute_route_time(route)
            if total_time < best_time:
                best_time = total_time
                best_route = route

        return best_route, best_time

    def compute_route_time(self, route):
        """ 
            Calculate total time for a given delivery sequence 
            Args:
                route (list): List of locations in the delivery sequence
            Returns:
                float: Total time taken to deliver all meals in hours
        """
        time_elapsed = 0

        # Aman travels to first restaurant
        time_elapsed += HaversineCalculator.travel_time_km(self.aman.distance_to(route[0]))

        # Wait for meal preparation
        if route[0] == self.r1:
            time_elapsed = max(time_elapsed, self.pt1)
        else:
            time_elapsed = max(time_elapsed, self.pt2)

        # Travel through the rest of the route
        for i in range(len(route) - 1):
            time_elapsed += HaversineCalculator.travel_time_km(route[i].distance_to(route[i + 1]))

        return time_elapsed
