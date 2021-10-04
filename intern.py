#multi level inheritance
class p:
    def m1(self):
        print('parnt method')

class c(p):
    def m2(self):
        print('chlid method')
class cc(c):
    def m3(self):
        print('subchild method')
child=cc()
child.m1()
child.m2()
child.m3()


#single inheritance
class p:
    def m1(self):
        print('parent method')
class c(p):
    def m2(self):
        print('child method')
M=c()
M.m1()
M.m2()

#multiple inheritence
class p:
    def m1(self):
        print('parent1 method')
class q:
    def m2(self):
        print('parent2 method')
class c(p,q):
    def m3(self):
        print('child method')
Z=c()
Z.m1()
Z.m2()
Z.m3()


#hierarchical inhertance
class p:
    def m1(self):
        print('parent method')
class c1(p):
    def m2(self):
        print('child1 method')
class c2(p):
    def m3(self):
        print('child2 method')
A=c1()
A.m1()
A.m2()
X=c2()
X.m3()
X.m1()








        




              
        









        






              
