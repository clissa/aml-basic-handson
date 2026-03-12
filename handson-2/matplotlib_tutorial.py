"""Matplotlib tutorial."""

# Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

plt.style.use('seaborn-v0_8-whitegrid')


plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 12

print(f"Matplotlib version: {mpl.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")


# 1.1 Figure and Axes
fig = plt.figure(figsize=(10, 6))  # Initialize a figure with a specific size
ax = fig.add_subplot(1, 1, 1)  # Add a single subplot (1 row, 1 column, 1st plot)

x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)

ax.plot(x, y)

ax.set_title('A Simple Sine Wave')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.grid(True)

plt.show()


# 1.2 The plt Interface vs. Object-Oriented Interface
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(x, np.sin(x))
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('sin(x)')

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.plot(x, np.cos(x))
plt.title('Cosine Wave')
plt.xlabel('X')
plt.ylabel('cos(x)')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

axs[0].plot(x, np.sin(x))
axs[0].set_title('Sine Wave')
axs[0].set_xlabel('X')
axs[0].set_ylabel('sin(x)')

axs[1].plot(x, np.cos(x))
axs[1].set_title('Cosine Wave')
axs[1].set_xlabel('X')
axs[1].set_ylabel('cos(x)')

fig.tight_layout()
plt.show()


# 2.1 Basic Line Plot with Customization
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)
ax.plot(x, y3, label='sin(x)cos(x)', color='green', linestyle='-.', linewidth=2)

ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)

ax.axvline(x=np.pi, color='purple', linestyle='--', alpha=0.3, label='x=π')

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.2, 1.2)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')

ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

ax.grid(True, linestyle='--', alpha=0.7)

ax.legend(loc='upper right')

plt.show()


# 2.2 Line Styles, Markers, and Colors
x = np.linspace(0, 10, 30)
y = np.sin(x)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()  # Flatten the 2x2 array of axes for easier indexing

line_styles = ['-', '--', '-.', ':']
line_names = ['Solid', 'Dashed', 'Dash-dot', 'Dotted']

for i, (style, name) in enumerate(zip(line_styles, line_names)):
    axs[0].plot(x, y + i*0.5, linestyle=style, linewidth=2, label=name, marker='o', markersize=6)
axs[0].legend()
axs[0].set_title('Line Styles')
axs[0].set_ylabel('y')
axs[0].set_xlabel('x')

markers = ['o', 's', '^', 'd', 'x', '*']
marker_names = ['Circle', 'Square', 'Triangle', 'Diamond', 'X', 'Star']

for j, (marker, name) in enumerate(zip(markers, marker_names)):
    axs[1].plot(x[::3], y[::3] + j*0.5, marker=marker, markersize=8, label=name, linestyle='-', linewidth=2)
axs[1].legend()
axs[1].set_title('Markers')
axs[1].set_ylabel('y')
axs[1].set_xlabel('x')

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
color_names = ['Blue', 'Green', 'Red', 'Cyan', 'Magenta', 'Yellow', 'Black']

for k, (color, name) in enumerate(zip(colors, color_names)):
    axs[2].plot(x, y + k*0.4, color=color, linewidth=2, label=name, marker='o', markersize=6)
axs[2].legend()
axs[2].set_title('Colors')
axs[2].set_ylabel('y')
axs[2].set_xlabel('x')

for i in range(4):
    axs[3].plot(x[::3], y[::3] + i*0.5, 
               linestyle=line_styles[i], 
               marker=markers[i], 
               color=colors[i], 
               linewidth=2, 
               markersize=8, 
               label=f'Style {i+1}')
axs[3].legend()
axs[3].set_title('Combined Styles')
axs[3].set_ylabel('y')
axs[3].set_xlabel('x')

plt.tight_layout()
plt.show()


# 3.1 Basic Scatter Plot
np.random.seed(42)  # For reproducibility
x = np.random.normal(size=100)
y = x + np.random.normal(size=100, scale=0.5)

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(x, y, 
                     c=np.abs(x*y),  # Color points by x*y value
                     s=100*np.abs(x),  # Size points by x value
                     alpha=0.7,  # Transparency
                     cmap='viridis')  # Color map

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('|x*y|')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Scatter Plot with Color and Size Variation')

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()


# 3.2 Bubble Plot (Scatter with size variation)
np.random.seed(42)
x = np.random.rand(20)
y = np.random.rand(20)
size = np.random.rand(20) * 1000  # Variable size
colors = np.random.rand(20)  # Variable color

fig, ax = plt.subplots(figsize=(10, 6))

bubble = ax.scatter(x, y, s=size, c=colors, alpha=0.6, cmap='plasma')

cbar = fig.colorbar(bubble, ax=ax)
cbar.set_label('Color Value')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Bubble Plot (Scatter with Size Variation)')

plt.show()


# 4.1 Bar Chart
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [25, 40, 30, 55, 15]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(categories, values, color='skyblue', edgecolor='black', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, str(height), 
            ha='center', va='bottom')

ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Simple Bar Chart')

plt.xticks(rotation=45)

plt.show()


# 4.2 Grouped Bar Chart
categories = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
values1 = [15, 30, 25, 40, 20]
values2 = [25, 20, 30, 35, 15]
values3 = [20, 25, 15, 30, 25]

width = 0.25
x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.bar(x - width, values1, width, label='Series 1', color='skyblue', edgecolor='black')
bars2 = ax.bar(x, values2, width, label='Series 2', color='lightgreen', edgecolor='black')
bars3 = ax.bar(x + width, values3, width, label='Series 3', color='salmon', edgecolor='black')

ax.set_xlabel('Groups')
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')

ax.set_xticks(x)
ax.set_xticklabels(categories)

ax.legend()

ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


# 4.3 Stacked Bar Chart
categories = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
values1 = [15, 30, 25, 40, 20]
values2 = [25, 20, 30, 35, 15]
values3 = [20, 25, 15, 30, 25]

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(categories, values1, label='Series 1', color='skyblue', edgecolor='black')
bars2 = ax.bar(categories, values2, bottom=values1, label='Series 2', color='lightgreen', edgecolor='black')

bottoms = [a + b for a, b in zip(values1, values2)]
bars3 = ax.bar(categories, values3, bottom=bottoms, label='Series 3', color='salmon', edgecolor='black')

ax.set_xlabel('Groups')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart')

ax.legend()

ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.show()


# 4.4 Horizontal Bar Chart
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [25, 40, 30, 55, 15]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(categories, values, color='skyblue', edgecolor='black', alpha=0.7)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, str(width), 
            ha='left', va='center')

ax.set_xlabel('Values')
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Chart')

ax.grid(True, axis='x', linestyle='--', alpha=0.7)

plt.show()


# 4.5 Histogram
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=1000)

fig, ax = plt.subplots(figsize=(10, 6))

n, bins, patches = ax.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

x = np.linspace(-4, 4, 100)
y = np.exp(-x**2/2) / np.sqrt(2*np.pi) * len(data) * (bins[1] - bins[0])
ax.plot(x, y, 'r-', linewidth=2)

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Normal Distribution')

ax.text(2, 90, r'$\mu=0, \sigma=1$', fontsize=14)
ax.text(2, 80, f'n = {len(data)}', fontsize=14)

plt.show()


# 5.1 Pie Chart
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
sizes = [25, 40, 15, 10, 10]
explode = (0.1, 0, 0, 0, 0)  # Explode the 1st slice (Category A)

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(sizes, 
                                   explode=explode, 
                                   labels=labels, 
                                   autopct='%1.1f%%',  # Show percentage
                                   shadow=True, 
                                   startangle=90,  # Rotate to start from top
                                   textprops={'fontsize': 12})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title('Pie Chart', fontsize=14)

ax.axis('equal')

plt.show()


# 5.2 Donut Chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 25, 25, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts = ax.pie(sizes, 
                       labels=labels, 
                       colors=colors,
                       wedgeprops={'width': 0.5},  # This creates the donut shape
                       startangle=90)

centre_circle = plt.Circle((0, 0), 0.25, fc='white')
ax.add_artist(centre_circle)

total = sum(sizes)
ax.text(0, 0, f'Total\n{total}', ha='center', va='center', fontsize=18)

ax.set_title('Donut Chart', fontsize=14)

ax.axis('equal')

plt.show()


# 6.1 Annotations and Text
x = np.linspace(0, 10, 100)
y = np.sin(x) * np.exp(-0.1 * x)

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(x, y, 'b-', linewidth=2)

point_x, point_y = 4, np.sin(4) * np.exp(-0.1 * 4)
ax.plot(point_x, point_y, 'ro', markersize=10)

ax.annotate('Local Maximum', 
            xy=(point_x, point_y),  # Position of the point to annotate
            xytext=(point_x + 1, point_y + 0.2),  # Position of the text
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=12)

ax.text(7, 0.5, r'$f(x) = \sin(x) \cdot e^{-0.1x}$', fontsize=14)

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(1, -0.5, 'Damped Sine Wave', fontsize=14, bbox=props)

ax.annotate('Decay begins', 
            xy=(1.5, np.sin(1.5) * np.exp(-0.1 * 1.5)),  # Point to annotate
            xytext=(3, -0.4),  # Text position
            arrowprops=dict(facecolor='green', 
                            shrink=0.05, 
                            width=2, 
                            headwidth=10, 
                            alpha=0.7),
            fontsize=12)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Text Annotations Example')

ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()


# 6.2 Customizing Ticks and Labels
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

axs[0].plot(x, y, 'b-', linewidth=2)

axs[0].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
axs[0].set_xticklabels(['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])

axs[0].tick_params(axis='x', direction='in', length=6, width=2, colors='blue',
                grid_color='gray', grid_alpha=0.7)
axs[0].tick_params(axis='y', direction='out', length=6, width=2, colors='red',
                grid_color='gray', grid_alpha=0.7)

axs[0].xaxis.set_minor_locator(MultipleLocator(np.pi/4))
axs[0].yaxis.set_minor_locator(MultipleLocator(0.25))

axs[0].set_xlabel('X-axis', fontsize=14)
axs[0].set_ylabel('Y-axis', fontsize=14)
axs[0].set_title('Custom Ticks and Labels', fontsize=16)

axs[0].grid(True, which='both', linestyle='--', alpha=0.5)

x_log = np.logspace(0, 5, 100)
y_log = x_log**0.5

axs[1].loglog(x_log, y_log, 'r-', linewidth=2)

axs[1].set_xlabel('X-axis (log scale)', fontsize=14)
axs[1].set_ylabel('Y-axis (log scale)', fontsize=14)
axs[1].set_title('Logarithmic Scale with Scientific Notation', fontsize=16)

axs[1].grid(True, which='both', linestyle='--', alpha=0.5)

axs[1].ticklabel_format(style='sci', axis='both', scilimits=(0, 0))

plt.tight_layout()
plt.show()


# 7.1 Subplots Grid
fig, axs = plt.subplots(2, 3, figsize=(15, 8))

axs = axs.flatten()

x = np.linspace(0, 10, 100)

axs[0].plot(x, np.sin(x))
axs[0].set_title('Line Plot')

axs[1].scatter(x[::5], np.cos(x[::5]), c=x[::5], cmap='viridis')
axs[1].set_title('Scatter Plot')

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 15]
axs[2].bar(categories, values)
axs[2].set_title('Bar Plot')

data = np.random.normal(0, 1, 1000)
axs[3].hist(data, bins=20, alpha=0.7)
axs[3].set_title('Histogram')

axs[4].step(x, np.sin(x), where='post')
axs[4].set_title('Step Plot')

axs[5].fill_between(x, 0, np.sin(x), alpha=0.5)
axs[5].set_title('Fill Plot')

plt.tight_layout()
plt.show()


# 7.2 Subplot with Different Sizes (GridSpec)
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(15, 10))

gs = GridSpec(2, 3, figure=fig, height_ratios=[2, 1], width_ratios=[1, 2, 1])

ax1 = fig.add_subplot(gs[0, :])  # Spans all columns in the first row
ax2 = fig.add_subplot(gs[1, 0])  # Bottom-left
ax3 = fig.add_subplot(gs[1, 1])  # Bottom-middle
ax4 = fig.add_subplot(gs[1, 2])  # Bottom-right

x = np.linspace(0, 10, 100)

ax1.plot(x, np.sin(x), 'r-', linewidth=2)
ax1.set_title('Main Plot (Spanning All Columns)')

ax2.scatter(x[::5], np.cos(x[::5]))
ax2.set_title('Subplot 1')

ax3.bar(['A', 'B', 'C', 'D'], [3, 7, 5, 9])
ax3.set_title('Subplot 2')

ax4.fill_between(x, 0, np.exp(-x/3), alpha=0.5)
ax4.set_title('Subplot 3')

plt.tight_layout()
plt.show()


# 8.1 3D Surface Plot
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Z Value')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot')

ax.view_init(elev=30, azim=45)

plt.show()


# 8.2 3D Scatter Plot
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
n = 100
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
colors = np.sqrt(x**2 + y**2 + z**2)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=colors, cmap='plasma', s=50, alpha=0.7)

cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Distance from Origin')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Scatter Plot')

ax.set_box_aspect([1, 1, 1])

plt.show()
