import tkinter as tk
from tkinter import ttk
import os

class PokemonChallengeTabs:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokemon Challenge Tabs")
        self.root.geometry("800x600")

        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill=tk.BOTH)

        # Tab 1: chose a Game for a Solo Run
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Pick Your Solo Run")
        self.create_pick_solo_game_section(tab1)

        # Tab 2: Random Solo Challenge from gens 1 through 4
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text="Random Solo Challenge")
        self.create_random_solo_challenge_section(tab2)

        # Tab 3: chose a Game for an Ironmon Challenge
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text="Pick Your Ironmon Challenge")
        self.create_pick_ironmon_challenge_section(tab3)
        
        # Tab 4: Ironmon Challenge at random from gens 1 through 4
        tab4 = ttk.Frame(tab_control)
        tab_control.add(tab4, text="Random Ironmon Challenge")
        self.create_ironmon_challenge_section(tab4)

        self.root.mainloop()

    def create_pick_solo_game_section(self, frame):
        label = tk.Label(frame, text="Pick the Generation you want to Solo Run", font=("Helvetica", 16))
        label.place(x=225, y=20)
        
        # When clicked thses buttons will open a new window that will allow the user to choose what game they want to use for a solo challenge
        gen1_button = tk.Button(frame, text="Gen 1", command=self.solo_gen1_selected)
        gen1_button.place(x= 250, y=60)

        gen2_button = tk.Button(frame, text="Gen 2", command=self.solo_gen2_selected)
        gen2_button.place(x= 350, y=60)

        gen3_button = tk.Button(frame, text="Gen 3", command=self.solo_gen3_selected)
        gen3_button.place(x= 450, y=60)

        gen4_button = tk.Button(frame, text="Gen 4", command=self.solo_gen4_selected)
        gen4_button.place(x= 550, y=60)

    # when gen1_button is clicked the program for doing a pokemon Gen1 solo challenge will be opened
    def solo_gen1_selected(self): 
        os.system("python Solo_Gen1_chooser.py")

    # when gen2_button is clicked the program for doing a pokemon Gen2 solo challenge will be opened
    def solo_gen2_selected(self):
        os.system("python Solo_Gen2_chooser.py")

    # when gen3_button is clicked the program for doing a pokemon Gen3 solo challenge will be opened
    def solo_gen3_selected(self):
        os.system("python Solo_Gen3_chooser.py")

    # when gen4_button is clicked the program for doing a pokemon Gen4 solo challenge will be opened
    def solo_gen4_selected(self):
        os.system("python Solo_Gen4_chooser.py")

    # when open_random_solo_button is clicked the program for doing a random pokemon solo challenge for gens 1 through 4 will be opened
    def open_solo_challenge_generator(self):
        os.system("python Solo_Challenge_generator.py")

    def create_random_solo_challenge_section(self, frame):
        label = tk.Label(frame, text="Choses a Pokémon game and a Pokémon at random from Gens 1 through 4 for a Solo run", 
            font=("Helvetica", 16), wraplength=400)
        label.pack(pady=20)

        open_random_solo_button = tk.Button(frame, text="Open Random Solo Challenge", command=self.open_solo_challenge_generator)
        open_random_solo_button.pack(pady=10)

    def create_pick_ironmon_challenge_section(self, frame):
        label = tk.Label(frame, text="Pick the Generation you want to Solo Run", font=("Helvetica", 16))
        label.place(x=225, y=20)
        
        # When clicked thses buttons will open a new window that will allow the user to choose what game they want to use for a solo challenge
        gen1_button = tk.Button(frame, text="Gen 1", command=self.ironmon_gen1_selected)
        gen1_button.place(x= 250, y=60)

        gen2_button = tk.Button(frame, text="Gen 2", command=self.ironmon_gen2_selected)
        gen2_button.place(x= 350, y=60)

        gen3_button = tk.Button(frame, text="Gen 3", command=self.ironmon_gen3_selected)
        gen3_button.place(x= 450, y=60)

        gen4_button = tk.Button(frame, text="Gen 4", command=self.ironmon_gen4_selected)
        gen4_button.place(x= 550, y=60)

    # when gen1_button is clicked the program for doing an Gen1 ironmon challenge will be opened
    def ironmon_gen1_selected(self): 
        os.system("python ironmon_Gen1_chooser.py")

    # when gen2_button is clicked the program for doing an Gen2 ironmon challenge will be opened
    def ironmon_gen2_selected(self):
        os.system("python Ironmon_Gen2_chooser.py")

    # when gen3_button is clicked the program for doing an Gen3 ironmon challenge will be opened
    def ironmon_gen3_selected(self):
        os.system("python Ironmon_Gen3_chooser.py")

    # when gen4_button is clicked the program for doing an Gen4 ironmon challenge will be opened
    def ironmon_gen4_selected(self):
        os.system("python Ironmon_Gen4_chooser.py")

    # when open_Iromon_random_button is clicked the program for doing a random pokemon Ironmon challenge for gens 1 through 4 will be opened
    def open_ironmon_challenge_generator(self):
        os.system("python Ironmon_challenge_generator.py")

    def create_ironmon_challenge_section(self, frame):
        label = tk.Label(frame, text="Open Random Ironmon Challenge", font=("Helvetica", 16))
        
        label = tk.Label(frame, 
            text="Choses a Pokémon game, Starer Pokeball location and alternate Starters at random from Gens 1 through 4 for an Ironmon run", 
            font=("Helvetica", 16), wraplength=400)
        label.pack(pady=20)

        open_Iromon_random_button = tk.Button(frame, text="Open Ironmon Challenge Generator", command=self.open_ironmon_challenge_generator)
        open_Iromon_random_button.pack(pady=10)


if __name__ == "__main__":
    PokemonChallengeTabs()
