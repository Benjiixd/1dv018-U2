


class Veichle:
    def __init__(self, name, brand, mileage, regnr):
        self.name = name
        self.mileage = mileage
        self.brand = brand
        self.regnr = regnr

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Mileage: {self.mileage}")

    def __repr__(self):
        return f"Veichle({self.regnr}, {self.brand} {self.name}, {self.mileage} km)"

    def hashCode(self, capacity):
        hv = 0
        for ch in self.regnr:
            hv = (hv * 31 + ord(ch)) % capacity
        return hv