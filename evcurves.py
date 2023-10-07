import sys
import os
import matplotlib.pyplot as plt

file = open(sys.argv[1])
lines = file.readlines()

# speed = []
# dist = []

x = []
y = []

current = os.getcwd()

if len(sys.argv) > 2:
    if not os.path.exists(os.path.join(current, sys.argv[2])):
        os.makedirs(os.path.join(current, sys.argv[2]))
        current = os.path.join(current, sys.argv[2])

for line in lines:
    line = line.replace("\n", "")
    splited = line.split(";")
    x.append(float(splited[0]) / 10)
    y.append(float(splited[1]))

# time = range(0, len(y))

plt.plot(x, y, color="orange", label="Position")
plt.title("Evolution de la position")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper left")
plt.grid()
plt.savefig(os.path.join(current, "position.jpeg"), dpi=300)
plt.clf()

"""
plt.plot(time, dist, color="red", label="Distance")
plt.plot(time, speed, color="orange", label="Vitesse")
plt.title("Distance et vitesse en fonction du temps")
plt.xlabel("T")
plt.ylabel("Vitesse & Distance")
plt.legend(loc="upper left")
plt.grid()
plt.savefig(os.path.join(current, "vitesse_distance.jpeg"), dpi=300)
plt.clf()


plt.plot(time, dist, color="red", label="Distance")
plt.title("Distance en fonction du temps")
plt.xlabel("T")
plt.ylabel("Distance")
plt.legend(loc="upper left")
plt.grid()
plt.savefig(os.path.join(current, "distance.jpeg"), dpi=300)
"""
