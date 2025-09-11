class Function:
    def input(self, n1, n2):
        
        print("number1 is:", n1)
        print("number2 is:", n2)

class OtherClass:
    def use_function(self):
        obj = Function()
        obj.input(50, 30)

print("Call to public function from another class")
obj2 = OtherClass()
obj2.use_function()

