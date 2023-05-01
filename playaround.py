# Use *args (positional arguments)
def add(*numbers):
    total = 0
    for n in numbers:
        total += n

        print(total)

# add(1,2,3,4,5)

# Use **kwargs (key wards arguments)
def calculate(n, **test):
    # print(test)
    # print(test["add"])
    # for k, v in test.items():
    #     print(k)
    #     print(v)
    n += test["add"]
    n *= test["multiply"]
    print(n)

# calculate(5, add=3, multiply=5)

# practice class
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.make)
