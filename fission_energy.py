# fission_energy.py
# This script calculates the energy released in a nuclear fission reaction of Uranium-235

# Constants
SPEED_OF_LIGHT = 3.0e8  # Speed of light in m/s (c)
MASS_LOSS_PER_FISSION = 3.2e-11  # Mass lost per fission (kg)

# Calculate energy using Einstein's equation E = mc^2
energy_released = MASS_LOSS_PER_FISSION * SPEED_OF_LIGHT ** 2

# Print result
print(f"Energy released per fission reaction: {energy_released} Joules")


# fission_energy.py
# Calculates the energy released in a nuclear fission reaction of Uranium-235

# Constants
SPEED_OF_LIGHT = 3.0e8  # Speed of light in m/s (c)
MASS_LOSS_PER_FISSION = 3.2e-11  # Mass lost per fission (kg)
ATOMS_PER_GRAM = 2.56e21  # Number of U-235 atoms in 1 gram

# Calculate energy for a single fission reaction
energy_per_fission = MASS_LOSS_PER_FISSION * SPEED_OF_LIGHT ** 2

# Calculate total energy for 1 gram of Uranium-235
total_energy = energy_per_fission * ATOMS_PER_GRAM

# Print results
print(f"Energy released per fission reaction: {energy_per_fission} Joules")
print(f"Total energy released by 1 gram of U-235: {total_energy} Joules")

# Storing the data

import csv

# File name
output_file = "energy_output.csv"

# Data to save
data = [
    ["Reaction", "Energy (Joules)"],
    ["Single Fission", energy_per_fission],
    ["1 gram of U-235", total_energy]
]

# Writing data to CSV
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Results saved to {output_file}")

# Script for Visualisation of data

import matplotlib.pyplot as plt

# Data for visualization
reactions = ["Single Fission", "1 gram of U-235"]
energy_values = [energy_per_fission, total_energy]

# Create bar graph
plt.figure(figsize=(8, 5))
plt.bar(reactions, energy_values, color=["blue", "red"])
plt.yscale("log")  # Use logarithmic scale for better visualization
plt.xlabel("Reaction Type")
plt.ylabel("Energy Released (Joules)")
plt.title("Energy Released in Nuclear Fission")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save and show plot
plt.savefig("energy_output.png")
plt.show()

# Scaling Up for Different Isotopes
# Dictionary of isotopes with mass loss per fission (kg)
isotopes = {
    "Uranium-235": 3.2e-11,
    "Plutonium-239": 3.1e-11,
    "Thorium-232": 2.9e-11
}

# Store energy values
energy_data = {}

for isotope, mass_loss in isotopes.items():
    energy_per_fission = mass_loss * SPEED_OF_LIGHT ** 2
    total_energy = energy_per_fission * ATOMS_PER_GRAM
    energy_data[isotope] = total_energy
    print(f"{isotope}: {total_energy:.2e} Joules")

# Visualization for all isotopes
plt.figure(figsize=(8, 5))
plt.bar(energy_data.keys(), energy_data.values(), color=["blue", "green", "red"])
plt.yscale("log")
plt.xlabel("Isotope")
plt.ylabel("Total Energy Released (Joules)")
plt.title("Comparison of Energy Released by Different Isotopes")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("isotope_energy_output.png")
plt.show()

# Machine Learning Model to Predict Energy Outputs

from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare dataset (mass loss → energy)
mass_losses = np.array([3.2e-11, 3.1e-11, 2.9e-11]).reshape(-1, 1)  # Features
energies = np.array([energy_data["Uranium-235"], energy_data["Plutonium-239"], energy_data["Thorium-232"]])  # Labels

# Train model
model = LinearRegression()
model.fit(mass_losses, energies)

# Predict energy for an unknown isotope (e.g., Uranium-233, mass loss = 3.0e-11 kg)
new_mass_loss = np.array([[3.0e-11]])
predicted_energy = model.predict(new_mass_loss)

print(f"Predicted Energy for Uranium-233: {predicted_energy[0]:.2e} Joules")

