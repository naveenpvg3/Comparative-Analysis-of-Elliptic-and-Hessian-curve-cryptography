import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
ecc_time = (0.001567,0.003833,0.006130,0.007508)
hes_time = (0.001109,0.001981,0.005481,0.005547)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8





rects1 = plt.bar(index, ecc_time, bar_width,
                 alpha=opacity,
                 color='white',
                 label='ECC',edgecolor='black', hatch="*")
 
rects2 = plt.bar(index + bar_width, hes_time, bar_width,
                 alpha=opacity,
                 color='white',
                 label='Hessian',edgecolor='black', hatch="//")
 
plt.ylabel('time taken in secs')
plt.xlabel('file size in bits')
plt.title('ECC vs Hessian Curve')
plt.xticks(index + bar_width, (1,8,10,12))
plt.legend()
 

plt.show()
