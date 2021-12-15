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

import sys
sys.dont_write_bytecode = True
import GEAR_LIBRARY, MATERIAL_LIBRARY, CALC_GEOMETRY, RIGID_LOAD_SHARING,\
    FORCES_SPEEDS, CONTACT, INVOLUTE_GEOMETRY, MESH_GENERATOR, PLOTTING

## GEAR GEOMETRY, MATERIAL AND FINISHING ######################################
# name of gear on library (includes geometry and surface finishing)
GEAR_NAME = 'H501'

# pinion and wheel material
MAT_PINION = 'STEEL'
MAT_WHEEL = 'STEEL'
Gmat = MATERIAL_LIBRARY.MATERIAL(MAT_PINION, MAT_WHEEL)

## LUBRICANT ##################################################################
# lubricant
class lub:
    def __init__(self):
        self.miu = 30
        self.xl = 0.85
    
Lubricant = lub()

# select element when is applied speed and torque (P - pinion, W - wheel)
element = 'P'

# torque Nm
torque = 200

# speed rpm
speed = 1000

# discretization of path of contact
size = 1000

# discretization of involute geometry
DISCRETIZATION = 100

# element order
ORDER = 1

NODEM = 21

## GEAR SELECTION #############################################################
Gtype = GEAR_LIBRARY.GEAR(GEAR_NAME)

## FZG LOAD STAGE CONDITIONS ##################################################
if torque is str:
    torque = torque

## GEAR GEOMETRY ACCORDING TO MAAG BOOK #######################################
Ggeo = CALC_GEOMETRY.MAAG(Gtype)

## LINES OF CONTACT ASSUMING A RIGID LOAD SHARING (SPUR AND HELICAL) ##########
Glines = RIGID_LOAD_SHARING.LINES(size, Ggeo)

## FORCES AND SPEEDS ##########################################################
Goper = FORCES_SPEEDS.OPERATION(element, torque, speed, Ggeo, Glines)

## GEAR CONTACT QUANTITIES (PRESSURE, FILM THICKNESS, POWER LOSS) #############
Gcontact = CONTACT.HERTZ(Gmat, Lubricant, Ggeo, Glines, Goper)

x = Glines.xd
y = Glines.bpos
import numpy as np
X, Y = np.meshgrid(x, y)
Sr = Glines.lsum.T
import matplotlib.pyplot as plt
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Sr,cmap='jet', edgecolor='k')
# ax.view_init(10, 15)
plt.show()

## INVOLUTE PROFILE GEOMETRY ##################################################
Pprofile = INVOLUTE_GEOMETRY.LITVIN('P', Ggeo, DISCRETIZATION)

Wprofile = INVOLUTE_GEOMETRY.LITVIN('W', Ggeo, DISCRETIZATION)

# thF = np.arccos(rb/ra)
# thP = np.arccos(rb/r)
# Sinvol = rb*(np.tan(thF)**2-np.tan(thP)**2)/2
# ce = 0.25 # 3
# eS = (-0.2*ce + 1.2)*min(a[-1])*1e3
# nM = int(Sinvol/eS)

## INVOLUTE PROFILE GEOMETRY ##################################################
# Pmesh = MESH_GENERATOR.MESHING('P', GEAR_NAME, Ggeo, Pprofile, 3, ORDER, NODEM)

# Wmesh = MESH_GENERATOR.MESHING('W', GEAR_NAME, Ggeo, Wprofile, 4, ORDER, NODEM)

## GRAPHICS ###################################################################
# Ploted = PLOTTING.GRAPHICS(Glines, Goper)