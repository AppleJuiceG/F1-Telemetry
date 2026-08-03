######################################################
# Installing the relevant packages to test fastf1 

import seaborn as sns
import matplotlib.pyplot as plt

import fastf1
import fastf1.plotting

#######################################################
# Setting up the plotting environment with FastF1's dark color scheme and enabling support for timedelta values in Matplotlib

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

#######################################################
# Calling the required session data
# In this case, qualifying data from Suzuka 2025 and 2026 

session25 = fastf1.get_session(2025, "Suzuka", "Q")  
session25.load(telemetry=True)
session26 = fastf1.get_session(2026, "Suzuka", "Q")
session26.load(telemetry=True)

########################################################
# Selecting the desired driver for comparison, ideally someone who performed well in both years.
# In this case we are picking Oscar Piastri (PIA), who placed 3rd in Qualifying in 2025 and in 2026 per the F1 website.

driver_lap25 = session25.laps.pick_drivers("PIA").pick_fastest()
driver_lap26 = session26.laps.pick_drivers("PIA").pick_fastest()

#########################################################
# Calling telemetry data for the selected driver in both years
driver_tel25 = driver_lap25.get_car_data().add_distance()
driver_tel26 = driver_lap26.get_car_data().add_distance()

#########################################################
# Assinging a colour to each year

qual25_colour = (0.1, 0.512, 0.512)
qual26_colour = (0.0, 0.259, 0.145)

#########################################################
# Drawing the plot to compare the two years

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(driver_tel25['Distance'], driver_tel25['Speed'], color=qual25_colour, label='2025',linestyle='dashed')
ax.plot(driver_tel26['Distance'], driver_tel26['Speed'], color=qual26_colour, label='2026', linestyle='dashed')

# Defining axis labels
ax.set_xlabel('Distance in meters')
ax.set_ylabel('Speed in km/h')

# cleaning up
ax.legend()
plt.suptitle("Best Lap Speed Trace Comparison \n 2025 vs 2026 Suzuka Qualifying")
#plt.savefig("PIA_2025vs2026_Suzuka_Qualifying.png")
plt.show()
