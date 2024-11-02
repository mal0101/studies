#overloading : la capacite d'une fonction ou d'une méthode à avoir plusieurs définitions avec le même nom, mais avec des signatures différentes.
#Cela signifie qu'une même fonction peut accepter différents types ou nombres de paramètres,
# meme declaration mais avec parametres differents
#overloading is an exemple of compile tim (static polymorphism or early biding)
# le compilateur utiliser les informations fournies lors de l'appel pour déterminer laquelle des versions va s'exécuter

# int add (int a , int b):
        #return a+b
# int  add (int a , int b, int c):
        #return a+b+c 
# float add (float a  , float b ):
        #return a+b
# float add (int a , float  b):
        #return a+b
#add(1,0)
#add(1.0,2.0)
#add (1,12.6)
#add(1,5,9)


# int add (int a , int b):
        #return a+b
# int  add2 (int a , int b, int c):
        #return a+b+c

# ce n'est pas overloading , on doit avoir meme nom mais signature différentes
#python ne supporte pas overloading , tout de meme on peut l'appliquer de cette maniere

class calcul:
    def __init__(self):
        self.result=0
    def add(self,a,b,c=0):
        self.result=a+b
        return self.result

c=calcul()
print(c.add(1,1.0))
print(c.add(1,1,8))
print(c.add(1.2,1.0,1.6))

class calcul1:
    def __init__(self):
        self.result=0
    def add1(self,*args):
        self.result=sum(args)
        return self.result

x=calcul1()
print(x.add1(1,1.0))
print(x.add1(11,1,8))
print(x.add1(1.2,1.0,1.6))
print(x.add1(1.2,1.0,1.6,2.5,2.7,2.9))

class calcul2:
    def __init__(self):
        self.result=0
    def add2(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            self.result=a+b
            return self.result
        elif isinstance(a, float) and isinstance(b, float):
            return a + b
        else:
            raise TypeError("Unsupported type for addition")
        
x=calcul2()
print(x.add2(1,1))
print(x.add2(1.2,1.0))

