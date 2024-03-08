class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_list = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.parking_list[0]:
                self.parking_list[0] -= 1
                return True
        if carType == 2:
            if self.parking_list[1]:
                self.parking_list[1] -= 1
                return True

        if carType == 3:
            if self.parking_list[2]:
                self.parking_list[2] -= 1
                return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)