class SpaceAge:
    earth_year_in_seconds: int = 31557600
    mercury_year_in_seconds: int = 0.2408467 * earth_year_in_seconds
    venus_year_in_seconds: int = 0.61519726 * earth_year_in_seconds
    mars_year_in_seconds: int = 1.8808158 * earth_year_in_seconds
    jupiter_year_in_seconds: int = 11.862615 * earth_year_in_seconds
    saturn_year_in_seconds: int = 29.447498 * earth_year_in_seconds
    uranus_year_in_seconds: int = 84.016846 * earth_year_in_seconds
    neptune_year_in_seconds: int = 164.79132 * earth_year_in_seconds

    def __init__(self, seconds):
        self.age_in_seconds: int = seconds

    def on_mercury(self):
        return round((self.age_in_seconds / self.mercury_year_in_seconds), 2)

    def on_venus(self):
        return round((self.age_in_seconds / self.venus_year_in_seconds), 2)

    def on_earth(self):
        return round((self.age_in_seconds / self.earth_year_in_seconds), 2)

    def on_mars(self):
        return round((self.age_in_seconds / self.mars_year_in_seconds), 2)

    def on_jupiter(self):
        return round((self.age_in_seconds / self.jupiter_year_in_seconds), 2)

    def on_saturn(self):
        return round((self.age_in_seconds / self.saturn_year_in_seconds), 2)

    def on_uranus(self):
        return round((self.age_in_seconds / self.uranus_year_in_seconds), 2)

    def on_neptune(self):
        return round((self.age_in_seconds / self.neptune_year_in_seconds), 2)
