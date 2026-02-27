import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# TIME SETTINGS
# ----------------------------
dt = 1e-4
t = np.arange(0, 2, dt)

# ----------------------------
# AC INPUT (India 230V 50Hz)
# ----------------------------
Vrms = 230
Vin_peak = Vrms * np.sqrt(2)
f = 50

Vin_ac = Vin_peak * np.sin(2*np.pi*f*t)
Vin_rect = np.abs(Vin_ac)

# DC bus after rectifier (approx peak hold)
Vdc = np.maximum.accumulate(Vin_rect)

# ----------------------------
# FLYBACK PARAMETERS
# ----------------------------
Np = 100
Ns = 10
turn_ratio = Ns/Np

D = 0.2  # initial duty cycle

# ----------------------------
# BATTERY MODEL (12V Lead Acid)
# ----------------------------
Vbat = 11.5   # initial battery voltage
R_internal = 0.2
Capacity_Ah = 7
Capacity = Capacity_Ah * 3600  # Coulombs
charge = 0

# Control targets
V_cv = 14.4
I_cc = 5

Vout_list = []
Iout_list = []
Vbat_list = []
mode_list = []

for i in range(len(t)):

    # Flyback Output Equation
    Vout = turn_ratio * (D/(1-D)) * 325

    # Battery current
    Iout = (Vout - Vbat) / R_internal

    # CC-CV CONTROL
    if Vbat < V_cv:
        # Constant Current mode
        mode = 0
        error_I = I_cc - Iout
        D += 0.0005 * error_I
    else:
        # Constant Voltage mode
        mode = 1
        error_V = V_cv - Vbat
        D += 0.0005 * error_V

    D = np.clip(D, 0.05, 0.7)

    # Update battery charge
    charge += Iout * dt
    Vbat = 11.5 + (charge / Capacity) * 3  # simplified rise

    Vout_list.append(Vout)
    Iout_list.append(Iout)
    Vbat_list.append(Vbat)
    mode_list.append(mode)

# ----------------------------
# PLOTS
# ----------------------------

plt.figure()
plt.plot(t, Vbat_list)
plt.title("Battery Voltage (CC-CV Charging)")
plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.show()

plt.figure()
plt.plot(t, Iout_list)
plt.title("Charging Current")
plt.xlabel("Time")
plt.ylabel("Current (A)")
plt.show()

plt.figure()
plt.plot(t, mode_list)
plt.title("Mode (0=CC, 1=CV)")
plt.xlabel("Time")
plt.ylabel("Mode")
plt.show()