class bird:
    def intro(self):
        print("Birds section start")

    def flight(self):
        print("Birds1 can fly")

class sparrow(bird):
    def flight(self):
        super().flight()
        print("Sparrows can fly")

class eagle(bird):
    def flight(self):
        print("Eagles can fly high")

a1=bird()
a1.intro()
a1.flight()
print("------------------")
a2=sparrow()
a2.flight()
print("!!!!!!!!!!!!!!")
a3=eagle()
a3.flight()
a3.intro()
