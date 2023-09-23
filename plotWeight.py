import matplotlib.pyplot as plt
from datetime import datetime

# File to store data
data_file = "weight_data.txt"

# Global variables to store the data
days = []
weights = []


def load_data():
    """
    Load data from the data file.
    """
    try:
        with open(data_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    day, weight = line.split(',')
                    days.append(day)
                    weights.append(float(weight))
    except FileNotFoundError:
        pass


def save_data():
    """
    Save data to the data file.
    """
    with open(data_file, 'w') as file:
        for day, weight in zip(days, weights):
            file.write(f"{day},{weight}\n")


def add_weight():
    """
    Add a daily weight entry with the current date.
    """
    # yoo
    print("Hello World")
    print("Hello World")
    print("Hello World")
    weight = float(input())
    today = datetime.now().strftime('%m-%d')

    days.append(today)
    weights.append(weight)

    # Update the graph and save data
    save_data()
    update_graph()


def update_graph():
    """
    Update and display the weight graph.
    """
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    # Customize the color of the bars
    bar_color = '#3498db'  # A pleasing blue shade
    plt.bar(days, weights, color=bar_color)
    plt.xlabel('Month-Day')
    plt.ylabel('Weight (kg)')
    plt.title('Daily Weight Progress')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    # Display text on the bars
    for day, weight in zip(days, weights):
        plt.text(day, weight + 0.2, f'{weight:.1f}',
                 ha='center', va='bottom', color='black')

    plt.ylim(60, 75)
    plt.tight_layout()  # Improve spacing
    plt.show()


# Load existing data
load_data()

# Add new weight entries
add_weight()
