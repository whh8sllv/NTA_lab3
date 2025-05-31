from math import log, sqrt, exp, ceil
from sympy import primerange, factorint
from random import randint


class index_calculus():

    def __init__(self, a, b, n):
        self.alpha = a
        self.beta = b
        self.n = n
        self.p = n - 1
        self.c = 3.38

    def generate_factor_base(self):
        size = ceil(self.c * exp(0.5 * (sqrt(log(self.n) * log(log(self.n))))))
        factor_base = [prime for prime in primerange(2, size+1)]
        return factor_base

    # def get_canonical_form(self):
    #     return [prime for prime in factorint(self.p)]
    
    def make_equation(self):
        k = randint(1, self.n)
        alpha_k = (self.alpha**k) % self.n
        sp = []
        for i in factorint(alpha_k).keys():
            if i in self.generate_factor_base():
                sp.append(i)
            else:
                return
        res = [0] * len(self.generate_factor_base())
        for i in sp:
            ind = self.generate_factor_base().index(i)
            res[ind] = i
        return res
    
    def make_system(self):
        # print(self.generate_factor_base())
        system = []
        while len(system) <= len(self.generate_factor_base()) + 2:
            eq = self.make_equation()
            if eq:
                system.append(eq)
                print(eq)
            
        print('******************************************')
        
        new_eq = self.check_system(system)
        print(*new_eq)
        
    def check_system(self, system):
        checker = [0] * len(system[0])
        for i in system:
            for j in range(len(i)):
                checker[j] = checker[j] + i[j]
        print(checker)
        while 0 in checker:
            ind_zero = checker.index(0)
            new_eq = self.make_equation()
            if new_eq:
                while new_eq[ind_zero] == 0:
                    new_eq = None
                    while new_eq is None:
                        new_eq = self.make_equation()
                system.append(new_eq)
                checker[ind_zero] = -1
        return system
        
        
                
                
    

    

        


# alpha = int(input('alpha = '))
# beta = int(input('beta = '))
# n = int(input('n = '))


dl = index_calculus(10, 17, 47)
print(dl.make_system())