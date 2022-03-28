class Calculator:
    def __init__(self,input1,input2):
        self.input1=int(input1)
        self.input2=int(input2)
        self.result=0

    # return sum of two values
    def adder(self):
        self.result= self.input1+self.input2
        return self.result
    # sub input2 from input1
    def subtractor(self):
        self.result= self.input1-self.input2
        return self.result

    # mul input1 with input2
    def multiplier(self):
        self.result= self.input1*self.input2
        return self.result
    # return result =0
    def clear(self):
        self.result=0
        return self.result

input1=input("Input 1st value: ")
input2=input("Input 2nd value: ")

# create an object for calculator class with user inputs
c=Calculator(input1,input2)
print("Adder: ",c.adder())
print("subtractor: ",c.subtractor())
print("multiplier: ",c.multiplier())
print("clear: ",c.clear())
