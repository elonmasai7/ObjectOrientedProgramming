class MyClass():

     a = 5
     def  __init__(self, x):
          self.x = x
 
     def method1(self):
          print(self.x)

     @classmethod      
     def method2(cls):
          print(cls.a)

     @staticmethod
     def method3(m,n):
          retrun m+n     
 
