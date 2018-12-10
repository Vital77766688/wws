import csv
from os.path import splitext

class CarBase:

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            raise

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]

class Car(CarBase):

    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            raise



class Truc(CarBase):

    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self._body_whl = body_whl.split("x")
        try:
            self.body_width = float(self._body_whl[0])
            self.body_height = float(self._body_whl[1])
            self.body_length = float(self._body_whl[2])
        except ValueError:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):

    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(filename):
    res = []
    try:
        with open(filename) as f:
            reader = csv.reader(f, delimiter = ';')
            next(reader)
            for row in reader:
                if row:
                    if row[0] == "car":
                        car = Car(row[0], row[1], row[3], row[5], row[2])
                        #print(car.car_type, car.brand, car.passenger_seats_count, car.get_photo_file_ext(), car.carrying)
                        res.append(car)
                    elif row[0] == "truck":
                        car = Truc(row[0], row[1], row[3], row[5], row[4])
                        #print(car.car_type, car.brand, car.carrying, car.get_photo_file_ext(), car.body_width, car.body_height, car.body_length, car.get_body_volume())
                        res.append(car)
                    elif row[0] == "spec_machine":
                        car = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                        #print(car.car_type, car.brand, car.carrying, car.get_photo_file_ext(), car.extra)
                        res.append(car)
    except IOError:
        print("Wrong file or permission denied")

    return res

if __name__ == '__main__':

    print(get_car_list("week3_cars.csv"))