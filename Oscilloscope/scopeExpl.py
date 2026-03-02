import numpy as np
import matplotlib.pyplot as plt

a = 3.3 # volts
f = 100000   # Hz
w = 2*np.pi*f
p = 1/f

tmin = .23478
tmax = tmin + 12*p

nwaves = 3

t = np.linspace(tmax, tmin, 1200)
y = a * np.sin(w*t)

print('dpi: ', plt.rcParams['figure.dpi'])
plt.rcParams['figure.dpi']=300
fig,ax = plt.subplots(1,1)
fig.set_size_inches(12,2)

ax.plot(t,y)
ax.grid()

plt.show()

