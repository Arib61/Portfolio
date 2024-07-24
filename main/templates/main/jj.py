import matplotlib.pyplot as plt

# List of hex color codes
colors = ['#ffffff', '#f6f4f0', '#fdffff', '#f3f1ef', '#e3e5e6', '#dd6c65', '#7be6d9', '#1f2341', '#fffffc', '#dfe7ec']

# Plotting the colors
plt.figure(figsize=(12, 2))
for i, color in enumerate(colors):
    plt.plot([i, i+1], [1, 1], color=color, linewidth=25)
plt.xlim(0, len(colors))
plt.axis('off')
plt.title("Affichage des couleurs")
plt.show()
