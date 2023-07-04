class A:
    def a(self):
        return 'f is a'
    
class B:
     def a(self):
        return 'f is b'
     
class C:
    pass

class D(C,A,B):
    pass

d=D()
print(d.a())

