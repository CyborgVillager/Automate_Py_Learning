
def number0():
    a = 10
    def addition(a=a):
        print(a + a)
    addition()

number0()


def number1(a):
        def addition1(a=a):
            print(a + a)
        addition1()
number1(5)