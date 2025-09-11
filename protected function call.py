class Function:
    def _input(self, n1, n2):
        
        print("number1 is:", n1)
        print("number2 is:", n2)

class DerivedFunction(Function):
    def access_protected(self):
        self._input(60, 40)

print("Call to protected function from derived class")
obj2 = DerivedFunction()
obj2.access_protected()
