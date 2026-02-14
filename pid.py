# PID Controler design

import control as ctrl
import matplotlib.pyplot as plt

# Plant
plant = ctrl.TransferFunction([1], [1, 3, 2])

# PID
Kp = 5
Ki = 1
Kd = 1

pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Closed loop
closed_loop = ctrl.feedback(pid * plant)

t, y = ctrl.step_response(closed_loop)

plt.plot(t, y)
plt.title("Closed Loop with PID")
plt.grid()
plt.show()