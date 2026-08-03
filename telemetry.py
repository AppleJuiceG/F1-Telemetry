# importing the required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import fastf1
import fastf1.plotting

######################################################
# Comparing speed traces of two drivers in a race ####
######################################################

# Calling session data
session = fastf1.get_session(2025, 'Japan', 'R')
session.load()

# As per documentaion:
# 'Enabling support for timedelta values in Matplotlib and setting up the plotting environment with FastF1's dark color scheme'
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

# Selecting drivers for comparison
ant_lap = session.laps.pick_drivers("ANT").pick_fastest()
rus_lap = session.laps.pick_drivers("RUS").pick_fastest()

# Calling telemetry data for selected drivers
ant_tel = ant_lap.get_car_data().add_distance()
rus_tel = rus_lap.get_car_data().add_distance()

# assigning colours to each driver to distinguish them in drawn plot
ant_colour = (0.1, 0.512, 0.512)
rus_colour = (0.0, 0.259, 0.145)

# drawing plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(ant_tel['Distance'], ant_tel['Speed'], color=ant_colour, label='ANT',linestyle='dashed')
ax.plot(rus_tel['Distance'], rus_tel['Speed'], color=rus_colour, label='RUS', linestyle='dashed')

# Defining axis labels
ax.set_xlabel('Distance in meters')
ax.set_ylabel('Speed in km/h')

# cleaning up
session25.load(telemetry=True)
session26.load(telemetry=True)

############################################
# Plotting throttle and braking traces  ####
############################################

# Calling session data
session = fastf1.get_session(2025, 'Japan', 'R')
session.load()

# Enabling matplotlb support for timedelta values
# Setting fastf1's color scheme
fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

ham_lap = session.laps.pick_drivers("HAM").pick_fastest()
ham_tel = ham_lap.get_car_data().add_distance()
ham_brake = (0.8, 0.0, 0.0)
ham_accel = (0.0, 0.8, 0.0)

fig, ax = plt.subplots(figsize=(8, 8))
# Plotting throttle traces
ax.plot(ham_tel['Distance'], ham_tel['Throttle'], color=ham_accel, label='Throttle')

# defining axis labels
ax.set_xlabel('Distance in meters')
ax.set_ylabel('Throttle')

ax.legend()
plt.suptitle("Hamilton's Throttle \n"
             f"{session.event['EventName']} {session.event.year}")  
plt.savefig("HAM_Throttle.png")
plt.show()