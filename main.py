import tkinter as tk
from tkinter import messagebox
import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None

def show_pokemon_info():
    pokemon_name = entry.get()
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        result_text.set(f"Name: {pokemon_info['name']}\n"
                        f"Height: {pokemon_info['height']}\n"
                        f"Weight: {pokemon_info['weight']}\n"
                        f"Abilities: {', '.join(pokemon_info['abilities'])}\n"
                        f"Types: {', '.join(pokemon_info['types'])}")
    else:
        messagebox.showerror("Error", "Pokemon not found!")

# Set up the main application window
root = tk.Tk()
root.title("Pokemon Info Finder")
root.geometry("300x230")
root.configure(bg='darkseagreen')

# Create the input field
entry_label = tk.Label(root, text="Enter Pokemon Name:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create a button to fetch Pokemon data
fetch_button = tk.Button(root, text="Get Info", command=show_pokemon_info)
fetch_button.pack(pady=10)

# Create a label to display the Pokemon info
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.pack(pady=10)

# Run the application
root.mainloop()
