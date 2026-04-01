import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Load dataset
df = pd.read_excel('gps_spore_36samples.xlsx')

# Scale marker size
sizes = df['Spore_population'] * 3

# ---- Create large figure with controlled layout ----
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(1, 2, width_ratios=[20, 1], wspace=0.05)

ax = fig.add_subplot(gs[0])
cax = fig.add_subplot(gs[1])  # dedicated colorbar axis

# Scatter plot
scatter = ax.scatter(
    df['Longitude'],
    df['Latitude'],
    c=df['Spore_population'],
    s=sizes,
    cmap='viridis',
    alpha=0.8
)

# ---- Full-height colorbar ----
cbar = fig.colorbar(scatter, cax=cax)
cbar.set_label('Spore Population')

# Labels
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Spatial Distribution of Spore Population (3×6 Plot Design)')

# ---- Expand axes to avoid clipping ----
x_range = df['Longitude'].max() - df['Longitude'].min()
y_range = df['Latitude'].max() - df['Latitude'].min()

ax.set_xlim(df['Longitude'].min() - x_range * 0.25,
            df['Longitude'].max() + x_range * 0.25)

ax.set_ylim(df['Latitude'].min() - y_range * 0.25,
            df['Latitude'].max() + y_range * 0.25)

# Grid
ax.grid(True, linestyle='--', alpha=0.5)

# Keep spatial proportions correct
ax.set_aspect('equal', adjustable='box')

plt.show()
