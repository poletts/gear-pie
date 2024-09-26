import sys

import numpy as np
import matplotlib.pyplot as plt

# import gmsh

# Add path to the sys path
sys.path.append('./')

from CLASSES import (GEAR_LIBRARY, MATERIAL_LIBRARY, LUBRICANT_LIBRARY,
                     LOAD_STAGES, CALC_GEOMETRY, LOAD_SHARING, 
                     FORCES_SPEEDS, CONTACT, INVOLUTE_GEOMETRY, DIN3990, 
                     VDI2736, MESH_GENERATOR, OUTPUT_PRINT, PLOTTING)

# Load gear
gear_type='C14'
gear = GEAR_LIBRARY.GEAR(gear_type)

# Gear geometry calculation
geo_specs = CALC_GEOMETRY.MAAG(gear)

# Involute geometry
discretization = 1000
Pprofile = INVOLUTE_GEOMETRY.LITVIN('P', geo_specs, discretization)
Wprofile = INVOLUTE_GEOMETRY.LITVIN('W', geo_specs, discretization)

# plot involute geometry
# involute profile from XinvT, YinvT
fig, ax = plt.subplots()
ax.plot(Pprofile.xGEO, Pprofile.yGEO, label='Pinion')
# ax.plot(Wprofile.xGEO, Wprofile.yGEO, label='Wheel')
plt.show()

# Save profile to csv
data = [-Pprofile.xGEO, Pprofile.xGEO]
data = np.array(data).T
# np.savetxt('C14_pinion_tooth_profile.csv', data, delimiter=',')
np.savetxt('./data/C14_pinion_tooth_profile.csv', data, delimiter=',')
