import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 0.1, 5000)

# Input AC (230V RMS, 50Hz)
Vrms = 230
f = 50
Vpeak = Vrms * np.sqrt(2)

Vin = Vpeak * np.sin(2*np.pi*f*t)

# Transformer (230V → 15V)
turn_ratio = 15/230
V_secondary = Vin * turn_ratio

# Bridge Rectifier
V_rectified = np.abs(V_secondary)

# Filter Capacitor Approximation
# Simple RC smoothing
C = 2200e-6
R_load = 10  # battery equivalent resistance approx

V_filtered = np.zeros_like(V_rectified)

for i in range(1, len(t)):
    if V_rectified[i] > V_filtered[i-1]:
        V_filtered[i] = V_rectified[i]
    else:
        dt = t[1] - t[0]
        V_filtered[i] = V_filtered[i-1] * np.exp(-dt/(R_load*C))

# Regulated Output (limit to 14.4V)
V_battery = np.minimum(V_filtered, 14.4)

# Plot AC input
plt.figure()
plt.plot(t, Vin)
plt.title("230V AC Input (50Hz)")
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.show()

# Plot Rectified + Filtered
plt.figure()
plt.plot(t, V_rectified, label="Rectified")
plt.plot(t, V_filtered, label="Filtered")
plt.legend()
plt.title("Rectifier and Filter Output")
plt.show()

# Final battery voltage
plt.figure()
plt.plot(t, V_battery)
plt.title("12V Battery Charging Voltage (~14.4V)")
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.show()