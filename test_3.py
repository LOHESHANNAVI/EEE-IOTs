# Battery Discharge Simulation


import matplotlib.pyplot as plt

battery_ah = 200
load_current = 20

time = list(range(0, 11))
remaining_ah = [battery_ah - load_current*t for t in time]

plt.plot(time, remaining_ah)
plt.xlabel("Time (hours)")
plt.ylabel("Remaining Ah")
plt.title("Battery Discharge Curve")
plt.show()


