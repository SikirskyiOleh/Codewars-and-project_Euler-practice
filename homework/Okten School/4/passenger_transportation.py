# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) -
#   наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)

class Plane:
    def __init__(self, priceOfTicket: int, timeInRoad: float, timeOfRegistration: float, whichClass: str):
        self._priceOfTicket = priceOfTicket
        self._timeInRoad = timeInRoad
        self._timeOfRegistration = timeOfRegistration
        self._whichClass = whichClass

    def __str__(self):
        return f'Time in road by Plane: {self._timeInRoad} hours, time of start registration: {self._timeOfRegistration}, price if ticket: {self._priceOfTicket}, type of class: {self._whichClass}'

    def __repr__(self):
        return f'Time in road by Plane: {self._timeInRoad} hours, time of start registration: {self._timeOfRegistration}, price if ticket: {self._priceOfTicket}, type of class: {self._whichClass}'

    def allData(self):
        return self.__str__()

    def get_timeInRoad(self):
        return self._timeInRoad

    def timeInRoad(self):
        return f'Total time in road: {self._timeInRoad + 3} hours.'  # here we count total time of road, 3 is avarage count of total time before flight registration and after


class Car:
    def __init__(self, amountOfPassengers: int, timeInRoad: float, priceOfFuel: float, distance: float):
        self._amountOfPassengers = amountOfPassengers
        self._timeInRoad = timeInRoad
        self._priceOfFuel = priceOfFuel
        self._distance = distance

    def __str__(self):
        return f'Time in road by Car: {self._timeInRoad} hours, amount of passenger: {self._amountOfPassengers}, price of fuel: {self._priceOfFuel}, distance: {self._distance} km.'

    def __repr__(self):
        return f'Time in road by Car: {self._timeInRoad} hours, amount of passenger: {self._amountOfPassengers}, price of fuel: {self._priceOfFuel}, distance: {self._distance} km.'

    def allData(self):
        return self.__str__()

    def get_timeInRoad(self):
        return self._timeInRoad

    def priceOfRoad(self):
        amountOfFuel = self._distance / 10  # here we found how much fuel we will need if on 100 km we spend 10 l of fuel (distance / 100 * 10)
        return f'Total price of ride: {round(amountOfFuel * self._priceOfFuel, 1)}'  # here we count how much road will cost


class Train:
    def __init__(self, priceOfTicket: int, timeInRoad: float, seatOnTrain: str):
        self._priceOfTicket = priceOfTicket
        self._timeInRoad = timeInRoad
        self._seatOnTrain = seatOnTrain

    def get_timeInRoad(self):
        return self._timeInRoad

    def __str__(self):
        return f'Time in road by Train: {self._timeInRoad} hours, type of seat: {self._seatOnTrain}, price of ticket: {self._priceOfTicket}'

    def __repr__(self):
        return f'Time in road by Train: {self._timeInRoad} hours, type of seat: {self._seatOnTrain}, price of ticket: {self._priceOfTicket}'

    def allData(self):
        return self.__str__()


def whoIsFaster(firstTimeOfRoad, secondTimeOfRoad):
    if firstTimeOfRoad < secondTimeOfRoad:
        howFaster = round(secondTimeOfRoad - firstTimeOfRoad)  # here we count how much faster is this type of vehicle
        print(f'This is faster for: {howFaster} hours.')
        return
    else:
        howFaster = round(firstTimeOfRoad - secondTimeOfRoad)  # here we count how much faster is this type of vehicle
        print(f'This is faster for: {howFaster} hours.')
        return


firstPlane = Plane(300, 4.5, 12.30, 'First')
print(firstPlane.timeInRoad())

firstCar = Car(3, 9.3, 40.7, 5340)
print(firstCar.priceOfRoad())

firstTrain = Train(250, 6.2, 'Coach car seating')
print(firstTrain.allData())

whoFaster1 = whoIsFaster(firstPlane.get_timeInRoad(), firstTrain.get_timeInRoad())
whoFaster2 = whoIsFaster(firstCar.get_timeInRoad(), firstTrain.get_timeInRoad())
