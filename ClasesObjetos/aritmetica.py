class Aritmetica:
    # Para ponerlos como Opcionales se pueden inicializar con None
    def __init__(self,operando1=None,operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2
    @property
    def operando1(self):
        return self._operando1
    @property
    def operando2(self):
        return self._operando2

    @operando1.setter
    def operando1(self,operando1):
        self._operando1 = operando1
    @operando2.setter
    def operando2(self,operando2):
        self._operando2= operando2


    def sumar(self):
        print(f'Suma: {self._operando1+self._operando2}')
    def restar(self):
        print(f'Resta: {self._operando1 - self._operando2}')
    def mult(self):
        print(f'Multiplicación: {self._operando1 * self._operando2}')
    def div(self):
        print(f'División: {self._operando1 / self._operando2}')

if __name__ == '__main__':
    print('--clase 1--')
    clasenum1 = Aritmetica(5,7)
    clasenum1.sumar()
    clasenum1.restar()
    clasenum1.mult()
    clasenum1.div()
    print('--clase 2--')
    clasenum2 = Aritmetica()
    clasenum2.operando1= 10
    clasenum2.operando2= 10
    clasenum2.sumar()
    clasenum2.restar()
    clasenum2.mult()
    clasenum2.div()
    print(f'exp: {clasenum2.operando1**clasenum2.operando2}')
    # Tercer objeto
    print('--clase 3--')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()

    # Cuarto objeto
    print('--clase 4--')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()

    print('--clase 5--')
    aritmetica5 = Aritmetica(operando2=3,operando1=3)
    aritmetica5.sumar()