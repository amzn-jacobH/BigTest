class Earth:
    """
    A class representing planet Earth with basic properties and methods.
    """
    
    def __init__(self):
        """
        Initialize Earth instance with default properties.
        """
        # Physical properties (in metric units)
        self.radius = 6371  # km
        self.mass = 5.972e24  # kg
        self.surface_area = 510.1e6  # km²
        self.average_temperature = 15  # °C
        
        # Orbital properties
        self.orbital_period = 365.256  # days
        self.rotation_period = 24  # hours
        
        # Atmospheric composition (percentage)
        self.atmosphere = {
            'nitrogen': 78.08,
            'oxygen': 20.95,
            'argon': 0.93,
            'carbon_dioxide': 0.04
        }
        
    def get_surface_gravity(self):
        """
        Calculate and return Earth's surface gravity in m/s².
        """
        G = 6.67430e-11  # gravitational constant
        return (G * self.mass) / (self.radius * 1000) ** 2
    
    def get_escape_velocity(self):
        """
        Calculate and return Earth's escape velocity in km/s.
        """
        G = 6.67430e-11  # gravitational constant
        return ((2 * G * self.mass) / (self.radius * 1000)) ** 0.5 / 1000
    
    def get_atmospheric_composition(self):
        """
        Return the atmospheric composition of Earth.
        """
        return self.atmosphere