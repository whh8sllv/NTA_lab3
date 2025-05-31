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
        self.k_list = []

    def check_k(self, num):
        if num in self.k_list:
            return 0
        else:
            return 1

    def generate_factor_base(self):
        size = ceil(self.c * exp(0.5 * (sqrt(log(self.n) * log(log(self.n))))))
        factor_base = [prime for prime in primerange(2, size+1)]
        return factor_base

    # def get_canonical_form(self):
    #     return [prime for prime in factorint(self.p)]
    
    def make_equation(self):
        k = randint(1, self.n)
        while self.check_k(k) == 0:
            k = randint(1, self.n)
        self.k_list.append(k)
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
        if sum(res) == 0:
            return
        return res, k
    
    def make_system(self):
        # print(self.generate_factor_base())
        system = []
        k = []
        while len(system) <= len(self.generate_factor_base()) + 2:
            eq = self.make_equation()
            if eq:
                system.append(eq[0])
                k.append(eq[1])
        new_system = self.check_system(system, k)
        result = []
        for i in range(len(new_system[1])):
            result.append((new_system[1][i], new_system[0][i]))
        return dict(result)
        
    def check_system(self, system, k):
        checker = [0] * len(system[0])
        for i in system:
            for j in range(len(i)):
                checker[j] = checker[j] + i[j]
        while 0 in checker:
            ind_zero = checker.index(0)
            new_eq = self.make_equation()
            if new_eq:
                while new_eq[0][ind_zero] == 0:
                    new_eq = None
                    while new_eq is None:
                        new_eq = self.make_equation()
                system.append(new_eq[0])
                k.append(new_eq[1])
                checker[ind_zero] = -1
        return system, k
        
        
                
                
    

    

        


# alpha = int(input('alpha = '))
# beta = int(input('beta = '))
# n = int(input('n = '))


dl = index_calculus(10, 17, 47)
print(dl.make_system())