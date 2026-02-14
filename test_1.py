# Power Loss Calculation

import matplotlib.pyplot as plt

linedata = [
    # R, P, Q, V
    (0.25, 0.0922, 0.0470, 220),
    (0.65, 0.4930, 0.2511, 221),
    (0.25, 0.3660, 0.1864, 224)
]

def power_loss(R, P, Q, V):
    return R * ((P**2 + Q**2) / V**2)

losses = []
for line in linedata:
    losses.append(power_loss(*line))

print("Line losses:", losses)
print("Total loss:", sum(losses))

plt.plot(losses, marker='o')
plt.xlabel("Line Number")
plt.ylabel("Power Loss")
plt.title("Power Loss per Line")
plt.show()
