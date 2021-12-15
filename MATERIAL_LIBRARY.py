'''MIT License

Copyright (c) 2022 Carlos M.C.G. Fernandes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. '''
class LIBRARY_MAT:
    def __init__(self, MAT_NAME):

        default = 'No defined material'
        getattr(self, MAT_NAME, lambda: default)()

    def Input(self):
        self.E = float(input('Young modulus / MPa: '))
        self.v = float(input('Poisson coeficient: '))
        self.cp = float(input('Heat capacity: '))
        self.k = float(input('Heat conductivity / W/mK: '))
        self.rho = float(input('Density / kg/m3: '))
        # self.SHlim = float(input('Contact fatigue limit / MPa: '))
        # self.SFlim = float(input('Bending fatigue limit / MPa: '))

    def STEEL(self):
        self.E = 206e3
        self.v = 0.3
        self.cp = 465
        self.k = 46 
        self.rho = 7830
        # self.SHlim = 1500
        # self.SFlim = 430
 
    def ADI(self):
        self.E = 210e3
        self.v = 0.26
        self.cp = 460.548
        self.kg = 55
        self.rho = 7850
        # self.SHlim = 1500
        # self.SFlim = 430
        
    def POM(self):
        self.E = 3.2e3
        self.v = 0.35
        self.cp = 1465  
        self.k = 0.3
        self.rho = 1415
        # self.SHlim = 36 - 0.0012*Tbulk**2 + (1000 - 0.025*Tbulk**2)*NL** - 0.21
        # self.SFlim = 26 - 0.0025*Tbulk**2 + 400*NL** - 0.2
    
    def PA66(self):
        self.E = 1.85e3
        self.v = 0.3
        self.cp = 1670
        self.k = 0.26 
        self.rho = 1140
        # self.SHlim = 36 - 0.0012*Tbulk**2 + (1000 - 0.025*Tbulk**2)*NL** - 0.21
        # self.SFlim = 30 - 0.22*Tbulk + (4600 - 900*Tbulk**0.3)*NL**( - 1/3)
        
    def PEEK(self):
        self.E = 3.65e3
        self.v = 0.38
        self.cp = 1472
        self.k = 0.25
        self.rho = 1320
        # self.SHlim = 36 - 0.0012*Tbulk**2 + (1000 - 0.025*Tbulk**2)*NL** - 0.21# Nylon (PA66)
        # self.SFlim = 30 - 0.22*Tbulk + (4600 - 900*Tbulk**0.3)*NL**( - 1/3) 
class MATERIAL:
    def __init__(self, PINION_MAT, WHEEL_MAT):
        
        Pmaterial = LIBRARY_MAT(PINION_MAT)
        self.E1 = Pmaterial.E
        self.v1 = Pmaterial.v
        self.cp1 = Pmaterial.cp
        self.k1 = Pmaterial.k
        self.rho1 = Pmaterial.rho
        
        Wmaterial = LIBRARY_MAT(PINION_MAT)
        self.E2 = Wmaterial.E
        self.v2 = Wmaterial.v
        self.cp2 = Wmaterial.cp
        self.k2 = Wmaterial.k
        self.rho2 = Wmaterial.rho
        