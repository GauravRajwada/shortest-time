from HarversineCalculator import HaversineCalculator
from DeliveryOptimizer import DeliveryOptimizer

class Location:
    """ Represents a geographical location with latitude and longitude """
    def __init__(self, name, latitude, longitude):
        """
            Define a new location with a name and coordinates
            Args:
                name (str): Name of the location
                latitude (float): Latitude in degrees
                longitude (float): Longitude in degrees
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other):
        """ 
            Compute distance to another location using the Haversine formula 
            Args:
                other (Location): The other location to calculate distance to 
            Returns:
                float: Distance in kilometers
        """
        return HaversineCalculator.calculate(self.latitude, self.longitude, other.latitude, other.longitude)
