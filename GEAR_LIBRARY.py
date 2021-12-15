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
class GEAR:
    def __init__(self, NAME):

        default = 'No Gear Selected Input'
        getattr(self, NAME, lambda: default)()

    def Input(self):
        self.alpha = float(input('Pressure angle / º: '))
        self.beta = float(input('Helix angle / º: '))
        self.m = float(input('Gear module / mm: '))
        self.z = [float(input('z1: ')), float(input('z2: '))]
        self.x = [float(input('x1: ')), float(input('x2: '))]
        self.b = [float(input('b1: ')), float(input('b2: '))]
        self.dshaft = [float(input('ds1: ')), float(input('ds2: '))]
        self.al = None
        self.haP = float(input('Addednum coefficient: '))
        self.hfP = float(input('Deddednum coefficient: '))
        self.rfP = float(input('Root radius coefficient: '))
        self.Ra = [float(input('Ra1 / m: ')), float(input('Ra2 / m: '))]
        self.Rq = [float(input('Rq1 / m: ')), float(input('Rq2 / m: '))]
        self.Rz = [float(input('Rz1 / m: ')), float(input('Rz2 / m: '))]

    def C14(self):
        self.alpha = 20.0
        self.beta = 0.0
        self.m = 4.5
        self.z = [16, 24]
        self.x = [0.1817, 0.1715]
        self.b = [14., 14.]
        self.dshaft = [30., 30.]
        self.al = None
        self.haP = 1.
        self.hfP = 1.25
        self.rfP = 0.38
        self.Ra = [0.6, 0.6]
        self.Rq = [0.7, 0.7]
        self.Rz = [4.8, 4.8]
        
    def H501(self):
        self.alpha = 20.
        self.beta = 15.
        self.m = 4.5
        self.z = [20, 30]
        self.x = [0.1809, 0.0891]
        self.b = [23., 23.]
        self.dshaft = [30., 30.]
        self.al = None
        self.haP = 1.
        self.hfP = 1.25
        self.rfP = 0.38
        self.Ra = [0.6, 0.6]
        self.Rq = [0.7, 0.7]
        self.Rz = [4.8, 4.8]

    def H701(self):
        self.alpha = 20.
        self.beta = 15.
        self.m = 2.5
        self.z = [28, 42]
        self.x = [0.2290, 0.1489]
        self.b = [17., 17.]
        self.dshaft = [30., 30.]
        self.al = None
        self.haP = 1.
        self.hfP = 1.25
        self.rfP = 0.38
        self.Ra = [0.6, 0.6]
        self.Rq = [0.7, 0.7]
        self.Rz = [4.8, 4.8]
        
    def H951(self):
        self.alpha = 20.
        self.beta = 15.
        self.m = 1.75
        self.z = [38, 57]
        self.x = [1.6915, 2.0003]
        self.b = [21.2418, 21.2418]
        self.dshaft = [30., 30.]
        self.al = None
        self.haP = 1.
        self.hfP = 1.25
        self.rfP = 0.38
        self.Ra = [0.6, 0.6]
        self.Rq = [0.7, 0.7]
        self.Rz = [4.8, 4.8]
 