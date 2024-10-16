import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os


# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        bmi_label.config(text=f"BMI: {bmi}")
        category = classify_bmi(bmi)
        category_label.config(text=f"Category: {category}")

        # Save data to a file
        save_data(weight, height, bmi, category)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")


# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Function to save data
def save_data(weight, height, bmi, category):
    with open("bmi_data.txt", "a") as file:
        file.write(f"{weight},{height},{bmi},{category}\n")


# Function to show historical data
def show_history():
    if not os.path.exists("bmi_data.txt"):
        messagebox.showinfo("No Data", "No historical data found.")
        return

    weights, heights, bmis, categories = [], [], [], []
    with open("bmi_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 4:
                weights.append(float(data[0]))
                heights.append(float(data[1]))
                bmis.append(float(data[2]))
                categories.append(data[3])

    # Display a plot of BMI values
    plt.plot(range(len(bmis)), bmis, marker='o', label='BMI Value')
    plt.xlabel('Entry Number')
    plt.ylabel('BMI')
    plt.title('BMI Trend Over Time')
    plt.legend()
    plt.show()


# Create the main application window
app = tk.Tk()
app.title("BMI Calculator")

# Create and place widgets for weight and height input
tk.Label(app, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(app)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(app)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place widgets for displaying BMI and category
bmi_label = tk.Label(app, text="BMI: ")
bmi_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

category_label = tk.Label(app, text="Category: ")
category_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Create and place buttons for calculating BMI and showing history
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

history_button = tk.Button(app, text="Show History", command=show_history)
history_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
app.mainloop()