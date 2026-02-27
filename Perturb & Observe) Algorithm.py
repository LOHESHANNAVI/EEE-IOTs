import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 0.5, 5000)

# PV parameters
Voc = 12
Isc = 5

# Initialize
D = 0.3          # Initial duty cycle
step = 0.002     # Perturbation step

prev_P = 0
prev_V = 0

V_pv_list = []
P_list = []
D_list = []
V_out_list = []

for i in range(len(t)):

    # Boost input voltage approx
    V_pv = Voc * (1 - D)

    # PV current
    I_pv = Isc * (1 - V_pv/Voc)

    P = V_pv * I_pv

    # P&O Algorithm
    dP = P - prev_P
    dV = V_pv - prev_V

    if dP > 0:
        if dV > 0:
            D -= step
        else:
            D += step
    else:
        if dV > 0:
            D += step
        else:
            D -= step

    # Limit duty cycle
    D = np.clip(D, 0.05, 0.9)

    # Boost output
    V_out = V_pv / (1 - D)

    # Store values
    V_pv_list.append(V_pv)
    P_list.append(P)
    D_list.append(D)
    V_out_list.append(V_out)

    prev_P = P
    prev_V = V_pv

# Plot results
plt.figure()
plt.plot(t, P_list)
plt.title("Power Tracking (P&O)")
plt.xlabel("Time")
plt.ylabel("Power (W)")
plt.show()

plt.figure()
plt.plot(t, V_out_list)
plt.title("Battery Charging Voltage")
plt.xlabel("Time")
plt.ylabel("Vout (V)")
plt.show()