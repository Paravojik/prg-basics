class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(f'This driver has rate {self.rate_per_km}/km, distznce you passed is {self.distance}km, you have to pay {self.fare}')


def main():
    # your program
    driver1=TaxiRide(10)
    driver1.calculate_fare(1.8)
    driver1.print_receipt()

    driver2=TaxiRide(15)
    driver2.calculate_fare(6.7)
    driver2.print_receipt()

if __name__ == "__main__":
    main()
