import matplotlib.pyplot as plt
#plt.rcParams["font.family"] = "Times New Roman"
import numpy as np

m = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,
              1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
              2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
              3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
              4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,
              5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,
              6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,
              7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,
              8.0,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,
              9.0,9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9,
              10])
r = 1.0
p = 1.5

# Group composition is defined as the number of contributors in an agent's group divided by the number of agents in the group.
gc_c = p / m # Group composition of contributor through p and m.
gc_nc = ( p - r ) / m # Group composition of non-contributor through p and m.

plt.ylim(0, 1)
plt.xlim(0, 10)
    
plt.plot(m, gc_c, label='Required group composition for contributor', color='orange')
plt.plot(m, gc_nc, label='Required group composition for non-contributor', color='blue')

plt.plot([.5, .5], [0, 1], 'r-', lw=1, linestyle='--')
plt.plot([1.5, 1.5], [0, 1], 'r-', lw=1, linestyle='--')
#plt.plot([3, 3], [0, 1], 'r-', lw=1, linestyle='--')

plt.fill_between(m, gc_c, np.max(gc_c), color='orange', alpha=0.2)
plt.fill_between(m, gc_nc, np.max(gc_nc), color='blue', alpha=0.1)

# plt.title('Required group composition at different benefit values')
plt.xlabel('Synergy')
plt.ylabel('Composition')
plt.grid(alpha=.5, linestyle='--')

plt.text(0.07, 0.45, r'1', fontsize=20)
plt.text(0.84, 0.45, r'2', fontsize=20)
plt.text(4.85, 0.45, r'3', fontsize=20)

extraticks = [0.5,1.5]
plt.xticks(list(plt.xticks()[0]) + extraticks)

plt.legend()
plt.savefig('Composition vs. Synergy.png', dpi=300)
plt.show()