# Create a Python class for a microwave
#  includes methods to turn it on, turn it off, run it for a certain amount of time


class Microwave:
    def __init__(self, brand: str, power_rating: str):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on: 
            print(f"Microwave {self.brand} is already turned on. ")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is now turned on. ")

    def turn_off(self) -> None:        
        if self.turned_on: 
            self.turned_on = False
            print(f"Microwave {self.brand} is now turned off. ")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is already turned off. ")

    def run(self, seconds: int) -> None:

        if self.turned_on:
            print(f"Running {self.brand} for {seconds} seconds ")
        else:
            print(f"A mystical force whispers: 'Turn on your microwave first...' ")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"


smeg: Microwave = Microwave('smeg', 'B')
bosch: Microwave = Microwave('Bosch', 'C')