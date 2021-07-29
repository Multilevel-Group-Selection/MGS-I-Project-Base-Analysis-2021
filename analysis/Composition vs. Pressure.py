import matplotlib.pyplot as plt
#plt.rcParams["font.family"] = "Times New Roman"
import numpy as np

p = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0])
r = 1
m = 2

# Group composition is defined as the number of contributors in an agent's group divided by the number of agents in the group.
gc_c = p / m # Group composition of contributor through p and m.
gc_nc = ( p - r ) / m # Group composition of non-contributor through p and m.

plt.ylim(0, 1)
plt.xlim(0, 3.2)
    
plt.plot(p, gc_c, label='Required group composition for contributor', color='orange')
plt.plot(p, gc_nc, label='Required group composition for non-contributor', color='blue')

plt.plot([1, 1], [0, 1], 'r-', lw=1, linestyle='--')
plt.plot([2, 2], [0, 1], 'r-', lw=1, linestyle='--')
plt.plot([3, 3], [0, 1], 'r-', lw=1, linestyle='--')

plt.fill_between(p, gc_c, np.max(gc_c), color='orange', alpha=0.2)
plt.fill_between(p, gc_nc, np.max(gc_nc), color='blue', alpha=0.1)

plt.text(0.45, 0.45, r'1', fontsize=20)
plt.text(1.45, 0.45, r'2', fontsize=20)
plt.text(2.45, 0.45, r'3', fontsize=20)
plt.text(3.04, 0.45, r'4', fontsize=20)

plt.xlabel('Pressure')
plt.ylabel('Composition')
plt.grid(alpha=.5, linestyle='--')
plt.legend()
plt.savefig('Composition vs. Pressure.png', dpi=300)
plt.show()