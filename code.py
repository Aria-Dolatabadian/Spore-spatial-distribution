import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('gps_spore_dataset.xlsx')

# Scale marker size
sizes = df['Spore_population'] * 2

# Plot
plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    df['Longitude'],
    df['Latitude'],
    c=df['Spore_population'],
    s=sizes,
    cmap='plasma',
    alpha=0.75
)

# Colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Spore Population')

# Labels
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Spatial Distribution of Spore Population')

# Grid (important for field interpretation)
plt.grid(True, linestyle='--', alpha=0.5)

# Preserve spatial proportions
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
