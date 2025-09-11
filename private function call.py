class Function:
    def __input(self, n1, n2):
       
        print("number1 is:", n1)
        print("number2 is:", n2)

class DerivedFunction(Function):
    def access_private(self):
        self._Function__input(70, 20)

print("Call to private function from derived class using name mangling")
obj2 = DerivedFunction()
obj2.access_private()
