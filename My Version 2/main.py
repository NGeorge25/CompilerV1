import parser as p
class Main:
    def __init__(self, x):
        par = p.Parser(x)
        print(par.rawArr)
        par.process1 = par.scanFunc()
        print(par.process1)

