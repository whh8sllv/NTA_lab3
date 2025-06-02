from math import log, sqrt, exp, ceil
from sympy import primerange, factorint
from random import randint
import time

class index_calculus():

    def __init__(self, a, b, n):
        self.alpha = a
        self.beta = b
        self.n = n
        self.p = n - 1
        self.c = 3.38
        self.factor_base = self.generate_factor_base()

    def generate_factor_base(self):
        size = ceil(self.c * exp(0.5 * (sqrt(log(self.n) * log(log(self.n))))))
        factor_base = [prime for prime in primerange(2, size+1)]
        return factor_base
    
    def make_equation(self):
        k = randint(1, self.n)
        alpha_k = (self.alpha**k) % self.n
        key = []
        value = []
        canonical_form = factorint(alpha_k)
        can_key = [i for i in canonical_form.keys()]
        can_val = [i for i in canonical_form.values()]
        for i in range(len(can_key)):
            if can_key[i] in self.factor_base:
                key.append(can_key[i])
                value.append(can_val[i])
            else:
                return
        res = [0] * len(self.factor_base)
        for i in range(len(key)):
            ind = self.factor_base.index(key[i])
            res[ind] = value[i]
        if sum(res) == 0:
            return
        return res, k
    
    def make_equations_system(self):
        system = []
        k = []
        while len(system) <= len(self.factor_base) + 2:
            eq = self.make_equation()
            if eq:
                system.append(eq[0])
                k.append(eq[1])
        result = []
        for i in range(len(system)):
            result.append((k[i], system[i]))
        # print(result)
        return dict(result)
        
    def check_equations_system(self, system, k):
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
    
    def extended_EA(self, a, b):
        u0, u1 = 1, 0
        v0, v1 = 0, 1
        r = a % b
        q = a // b
        while r != 0:
            u0, u1 = u1, (u0 - q * u1)
            v0, v1 = v1, (v0 - q * v1)
            a = b
            b = r
            r = a % b
            q = a // b
        return (b, u1, v1)

    def get_inverse(self, a, mod):
        if self.extended_EA(a, mod)[0] % mod != 1:
            return 'No inverse'
        inverse_element = self.extended_EA(a, mod)[1] % mod
        return inverse_element

    
    def get_main_dl(self, small_dl, factor_base):
        l = randint(0, self.n)
        b_alpha = (self.beta * self.alpha**l) % self.n
        b_alpha_canonical = factorint(b_alpha)
        for i in b_alpha_canonical.keys():
            if i not in factor_base:
                return
        b_alpha_keys = [i for i in b_alpha_canonical.keys()]
        b_alpha_values = [i for i in b_alpha_canonical.values()]
        res = 0
        for i in range(len(b_alpha_keys)):
            ind = factor_base.index(b_alpha_keys[i])
            sm_dl = small_dl[ind]
            res += sm_dl*b_alpha_values[i]
        return ((res - l) % self.p)
    
    def main(self):
        x_i = self.solve_equations_system(self.make_equations_system())
        while type(x_i) is not list:
            x_i = self.solve_equations_system(self.make_equations_system())
        fb = self.factor_base
        res = self.get_main_dl(x_i, fb)
        while type(res) is not int:
            res = self.get_main_dl(x_i, fb)
        return res

start = time.time()
dl = index_calculus(135, 340, 673).main()
print(dl)
end = time.time()
print(end-start)