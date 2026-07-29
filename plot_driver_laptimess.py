######################################################
# Installing the relevant packages to test fastf1 

import seaborn as sns
import matplotlib.pyplot as plt

import fastf1
import fastf1.plotting

######################################################
# Loading the desired race data

race = fastf1.get_session(2025, "Monza", "R")
race.load()

#######################################################
# Setting up the plotting environment with FastF1's dark color scheme and enabling support for timedelta values in Matplotlib

fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme="fastf1")

#######################################################
# Getting all the laps for a single driver and filtering out slow laps

driver_laps_HAM = race.laps.pick_drivers("HAM").pick_quicklaps().reset_index() 
driver_laps_VER = race.laps.pick_drivers("VER").pick_quicklaps().reset_index()

########################################################


#######################################################
# Making the scatterplot using lap number as x-axis and lap time as y-axis.

fig, ax = plt.subplots(figsize=(8, 8))

sns.scatterplot(data= driver_laps_HAM, 
                      x="LapNumber",
                        y="LapTime",
                        ax=ax,
                        hue="Compound", 
                        palette=fastf1.plotting.get_compound_mapping(session=race),
                        s=80,
                        linewidth=0,
                        legend="auto")

#########################################################
# Making the plot more aesthetic

ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")

#########################################################
# The y-axis increases from bottom to top by default
# Since we are plotting time, it makes sense to invert the axis

ax.invert_yaxis()
plt.suptitle("Hamilton Laptimes in the 2025 Monza Grand Prix")   

# Turn on major grid lines
plt.grid(color="w", which="major", axis="both")
sns.despine(left = True, bottom = True)

plt.show()