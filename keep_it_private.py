class myClass:
    __privateVar = 27;
    def __privMeth(self):
      print("I am inside class, myClass")
    def hello(self):
      print("Private Variable Value : ",myClass.privateVar)
foo = myClass()
foo.hello()
foo.__privMeth

