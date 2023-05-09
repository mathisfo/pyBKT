data = {
    "Arrays": {
        "Challenges": {"guesses": 0.29, "slips": 0.82},
        "Coding": {"guesses": 0.28, "slips": 0.76},
    },
    "Boolean Expressions": {
        "Challenges": {"guesses": 0.7, "slips": 0.28},
        "Coding": {"guesses": 0.2, "slips": 0.64},
    },
    "For Loops": {
        "Challenges": {"guesses": 0.26, "slips": 0.4},
        "Coding": {"guesses": 0.06, "slips": 0.5},
    },
    "If-Else": {
        "Challenges": {"guesses": 0.55, "slips": 0.24},
        "Coding": {"guesses": 0.12, "slips": 0.46},
    },
    "Nested Loops": {
        "Challenges": {"guesses": 0.59, "slips": 0.89},
        "Coding": {"guesses": 0.43, "slips": 0.84},
    },
    "Objects and Classes": {
        "Challenges": {"guesses": 0.22, "slips": 0.66},
        "Coding": {"guesses": 0.24, "slips": 0.68},
    },
    "Strings": {
        "Challenges": {"guesses": 0.33, "slips": 0.45},
        "Coding": {"guesses": 0.12, "slips": 0.57},
    },
    "Variables and Operations": {
        "Challenges": {"guesses": 0.11, "slips": 0.32},
        "Coding": {"guesses": 0.13, "slips": 0.48},
    },
    "While Loops": {
        "Challenges": {"guesses": 0.55, "slips": 0.38},
        "Coding": {"guesses": 0.07, "slips": 0.83},
    },
}


import matplotlib.pyplot as plt
import numpy as np

# Calculate the average slip rate for each skill
average_slip_rates = {
    skill: (data[skill]["Challenges"]["slips"] + data[skill]["Coding"]["slips"]) / 2
    for skill in data
}

# Sort skills by average slip rate in descending order
sorted_skills = sorted(
    average_slip_rates.keys(), key=lambda x: average_slip_rates[x], reverse=True
)

exercise_types = ["Challenges", "Coding"]

skills = sorted_skills

# Set up the figure and axes
fig, ax = plt.subplots()

# Define the width of each bar
bar_width = 0.2

# Create an array with the positions of the bars on the x-axis
ind = np.arange(len(skills))

# Plot guesses and slips for each skill and exercise type
for i, exercise_type in enumerate(exercise_types):
    guesses = [data[skill][exercise_type]['guesses'] for skill in skills]
    slips = [data[skill][exercise_type]['slips'] for skill in skills]

    color = 'blue' if exercise_type == 'Challenges' else 'green'
    ax.bar(ind + (i * bar_width), guesses, width=bar_width, color=color, label=f"{exercise_type} - Guesses")
    ax.bar(ind + ((i + 1) * bar_width), slips, width=bar_width, color=color, linestyle=':', label=f"{exercise_type} - Slips")

# Customize the chart
ax.set_title("Guesses and Slips by Skill and Exercise Type")
ax.set_ylabel("Probability")
ax.set_xticks(ind + bar_width)
ax.set_xticklabels(skills, rotation=45, ha='right')
ax.legend()

# Show the chart
plt.show()

