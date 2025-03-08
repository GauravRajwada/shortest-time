import math

class HaversineCalculator:
    """ Provides utility to calculate distance between two geo-locations using the Haversine formula """
    EARTH_RADIUS_KM = 6371  # Earth radius in km
    AVERAGE_SPEED_KMH = 20  # Assumed constant speed in km/h

    @staticmethod
    def calculate(lat1, lon1, lat2, lon2):
        """ 
            Compute great-circle distance between two points on Earth 
            Args:
                lat1 (float): Latitude of point 1 in degrees
                lon1 (float): Longitude of point 1 in degrees
                lat2 (float): Latitude of point 2 in degrees
                lon2 (float): Longitude of point 2 in degrees
            Returns:
                float: Distance between the two points in kilometers    
        """
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return HaversineCalculator.EARTH_RADIUS_KM * c  # Distance in km

    @staticmethod
    def travel_time_km(distance_km):
        """ 
            Convert distance to time in hours based on average speed 
            Args:
                distance_km (float): Distance to travel in kilometers
            Returns:
                float: Time in hours to travel the given distance    
        """
        return distance_km / HaversineCalculator.AVERAGE_SPEED_KMH

