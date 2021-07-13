from models.vehicle import Car, Bike
from parkslot.park import Parkinglot
if __name__ == '__main__':
    car1 = Car(1234)
    car2 = Car(2332)
    car3 = Car(1223)
    bike1 = Bike(4352)
    bike2 = Bike(3224)
    bike3 = Bike(3452)


    # print(car1.veh_num)

    park1 = Parkinglot(5)
    print(park1.park(car1.veh_num))
    print(park1.park(bike1.veh_num))
    print(park1.park(car2.veh_num))
    print(park1.park(bike2.veh_num))
    print(park1.park(car3.veh_num))
    print(park1.park(bike3.veh_num))
    print(park1.list_parked_vehicles())
    print(park1.unpark(1223))
    print(park1.park(3345))
    print(park1.list_parked_vehicles())







