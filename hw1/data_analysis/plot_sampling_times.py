import matplotlib.pyplot as plt

# Read data from sampling_times.txt
pixel_values = []
sampling_methods = ['zero', 'nearest', 'linear']
nearest_times = {1: [], 4: [], 16: []}
linear_times = {1: [], 4: [], 16: []}

with open('/Users/tommyhosmer/Documents/Classes/Spring25/CS284/hw-webpages-tommy-mostafa/hw1/data_analysis/sampling_times.txt', 'r') as file:
    lines = file.readlines()
    current_pixel_value = None
    for line in lines:
        line = line.strip()
        if 'pixel' in line:
            current_pixel_value = int(line.split()[0])
            pixel_values.append(current_pixel_value)
        elif line and current_pixel_value is not None:
            parts = line.split()
            nearest_times[current_pixel_value].append(float(parts[1]))
            linear_times[current_pixel_value].append(float(parts[2]))

# Create bar plots
bar_width = 0.35
index = range(len(sampling_methods))

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

for i, pixel_value in enumerate(pixel_values):
    ax = axes[i]
    bar1 = ax.bar(index, nearest_times[pixel_value], bar_width, label='Nearest')
    bar2 = ax.bar([j + bar_width for j in index], linear_times[pixel_value], bar_width, label='Bilinear')

    # Add labels, title, and legend
    ax.set_xlabel('Miplevel Sampling Method')
    ax.set_ylabel('Time (ms)')
    ax.set_title(f'{pixel_value} Pixel')
    ax.set_xticks([j + bar_width / 2 for j in index])
    ax.set_xticklabels(sampling_methods)
    ax.legend()

    # Add value labels on top of each bar
    for bar in bar1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}', ha='center', va='bottom')

    for bar in bar2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}', ha='center', va='bottom')

# Display the bar plots
plt.tight_layout()
plt.savefig("sampling_times.png")