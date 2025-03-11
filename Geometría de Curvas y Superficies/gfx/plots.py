from matplotlib import pyplot as plt
import numpy as np

def default_axis(given_ax):
	given_ax.axhline(color="black")
	given_ax.axvline(color="black")

x = np.linspace(-2, 2, 100)
y = (lambda x: x**2)(x)

plt.figure()
ax = plt.axes([0,0,1,1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
default_axis(ax)
ax.plot(x, y, color="#DC2616")
#plt.show()
plt.savefig("ej1_1_1.pdf")


plt.figure()
def ej1_2(t):
	if t <= 0:
		return -(t**4)
	else:
		return t**4
x_ = (np.vectorize(ej1_2))(x)
y = (lambda x: x**4)(x)
ax = plt.axes([0,0,1,1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
default_axis(ax)
ax.plot(x_, y, color="#DC2616")
#plt.show()
plt.savefig("ej1_2.pdf")

