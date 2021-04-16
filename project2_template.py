
import georinex as gr  # "pip install georinex" from command prompt launched from Anaconda to add to environment
import numpy as np
import ephemeris
import calc_sv_pos_tate as csp   # update to use your filename instead of "calc_sv_pos"
# import calc_sv_pos_STUDENT-LAST-NAME as csp
import helper


# assignment defined values
filename = 'ohdt3490.20n'  # RINEX nav filename
prn = 'G03'
tow = 80000
rcvr_ecef = np.array([-1485881.487, -5152018.353, 3444641.847])

# GeoRinex file loading and PRN extraction
nav = gr.load(filename)
nav_values = nav.sel(sv=prn).dropna(dim='time', how='all')  # select PRN and drop unused times ("nan" values)

# find closest T_oe index
idx = helper.computeClosest(tow, nav_values.Toe.data)

# Construct ephemeris object with the params from the closest T_oe
ephem = ephemeris.Ephemeris(nav_values, idx)

sv_ecef, sv_clock_error = csp.calc_sv_pos(ephem, tow, rcvr_ecef)  # update to use your filename instead of "calc_sv_pos"

# print satellite position and clock correction
print(f"satellite position: {sv_ecef}")
print(f"clock error: {sv_clock_error}")
