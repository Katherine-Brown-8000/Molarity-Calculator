import json
import requests

url = "https://raw.githubusercontent.com/Katherine-Brown-8000/Molarity-Calculator/refs/heads/main/Atomic_Mass_Dictionary.json"
response = requests.get(url)

if response.status_code == 200:
    atomic_mass = json.loads(response.text)
else:
    print('Failed to retrieve the data.')

compound = input("Enter name of your compound in abriviations such as Cl: ").strip()
mass = float(input("Enter mass of compound (g): "))
liters_of_solution = float(input('Enter volume in liters in (L), not (mL): '))

molar_mass = atomic_mass.get(compound)

if molar_mass is None:
    print(f"Error: Molar mass for {compound} not found")
else:
    moles_of_solute = mass / molar_mass
    Molarity = moles_of_solute / liters_of_solution

print(f"The Molarity of {compound} in {liters_of_solution} is {Molarity}")
