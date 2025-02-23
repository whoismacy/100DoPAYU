def add(*args):
    temp = 0
    for n in args:
        temp += n
    return temp
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(n, **kwargs):
    r = n + kwargs["add"]
    m =  n * kwargs["multiply"]

    return r,m

print(calculate(10, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
       self.make = kw.get("make", "NaN")
       self.model = kw.get("model", "NaN")
       self.color = kw.get("color", "NaN")
       self.seats = kw.get("seats", "NaN")

my_car = Car(make="Nissan", model="GT-R", color="Black", seats="4")
print(my_car.model)
