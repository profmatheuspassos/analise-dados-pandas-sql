import matplotlib.pyplot as plt
import matplotlib

plt.style.use(['dark_background'])
plt.rcParams['axes.facecolor'] = (0,0,0,0)
plt.rcParams['figure.facecolor'] = (0,0,0,0)
plt.rcParams["legend.frameon"] = False
plt.rcParams['image.cmap'] = 'viridis'
plt.rcParams["legend.facecolor"] = (0,0,0,0)
plt.rcParams["font.family"] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Open Sans', 'Source Sans Pro', 'Noto Sans']
plt.rcParams['hist.bins'] = 50
plt.rcParams['lines.markersize'] = 2
plt.rcParams['axes3d.grid'] = False
from cycler import cycler

plt.rcParams['axes.prop_cycle'] = (cycler(color=['#e74c3c', '#b86dd6', '#fca821', '#3498db', '#f1c40f', '#ffa847', '#c4ef7a', '#e195e2', '#ced9ed', '#fff29b']) + cycler(linestyle=['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--']))
