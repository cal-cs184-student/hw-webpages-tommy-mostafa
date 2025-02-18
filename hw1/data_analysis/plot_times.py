import matplotlib.pyplot as plt

# Read data from times.txt
file_names = []
old_times = []
new_times = []

with open('/Users/tommyhosmer/Documents/Classes/Spring25/CS284/hw-webpages-tommy-mostafa/hw1/data_analysis/times.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip the header line
        parts = line.split()
        file_names.append(parts[0].strip(':'))
        old_times.append(float(parts[1]))
        new_times.append(float(parts[2]))

# Create bar chart
bar_width = 0.35
index = range(len(file_names))

fig, ax = plt.subplots()
bar1 = ax.bar(index, old_times, bar_width, label='Old Times')
bar2 = ax.bar([i + bar_width for i in index], new_times, bar_width, label='New Times')

# Add labels, title, and legend
ax.set_xlabel('File: svg/basic/test*.svg')
ax.set_ylabel('Time (ms)')
ax.set_title('Times vs File')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(file_names)
ax.legend()
# Add value labels on top of each bar
for bar in bar1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}', ha='center', va='bottom')

for bar in bar2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.1f}', ha='center', va='bottom')

# Display the bar chart
plt.tight_layout()
plt.savefig('times.png')