import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(0,2*np.pi,0.001)
y1_axis = np.sin(x_axis)
y2_axis = np.cos(x_axis)
plt.title("Sin cosine")
#plt.legend(['Sine','Cosine'])
plt.plot(x_axis,y1_axis)
plt.xlabel("x_axis")
plt.ylabel("Y_axis")
plt.plot(x_axis,y2_axis)
plt.show()