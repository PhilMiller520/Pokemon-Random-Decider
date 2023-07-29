import tkinter as tk
from PIL import ImageTk, Image
import random
import Poke_Games_List
from Poke_Dex_list import Gen1List, Gen2List, Gen3List, Gen4List
import Box_Art_images
import Pokemon_images

class SoloChallengeWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi-Gen Solo Challenge")
        self.root.geometry("1000x700")

        self.solo_challenge_button = tk.Button(self.root, text="Solo Run", command=self.run_challenge)
        self.solo_challenge_button.pack(pady=20)

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH)

        frame1 = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2)
        frame1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.game_label = tk.Label(frame1, text="")
        self.game_label.pack()

        self.image_label = tk.Label(frame1)
        self.image_label.pack()

        frame2 = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2)
        frame2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.pokemon_label = tk.Label(frame2, text="")
        self.pokemon_label.pack()

        self.pokemon_image_label = tk.Label(frame2)
        self.pokemon_image_label.pack()

        self.root.mainloop()

    def run_challenge(self):
        picked_game = random.choice(Poke_Games_List.Poke_Games)
        chosen_gen1 = random.choice(Gen1List)
        chosen_gen2 = random.choice(Gen1List + Gen2List)
        chosen_gen3 = random.choice(Gen1List + Gen2List + Gen3List)
        chosen_gen4 = random.choice(Gen1List + Gen2List + Gen3List + Gen4List)

        if picked_game in ['Red', 'Blue', 'Yellow']:
            self.game_label.configure(text=f"The chosen game is: ")
            self.display_image(Box_Art_images.box_art.get(picked_game), self.image_label)
            self.pokemon_label.configure(text="The chosen Pokémon for this run is: " + chosen_gen1)
            self.display_pokemon_image(Pokemon_images.poke_image.get(chosen_gen1), self.pokemon_image_label)
        elif picked_game in ['Gold', 'Silver', 'Crystal']:
            self.game_label.configure(text=f"The chosen game is: ")
            self.display_image(Box_Art_images.box_art.get(picked_game), self.image_label)
            self.pokemon_label.configure(text="The chosen Pokémon for this run is: " + chosen_gen2)
            self.display_pokemon_image(Pokemon_images.poke_image.get(chosen_gen2), self.pokemon_image_label)
        elif picked_game in ['Ruby', 'Sapphire', 'Emerald', 'Fire Red', 'Leaf Green']:
            self.game_label.configure(text=f"The chosen game is: ")
            self.display_image(Box_Art_images.box_art.get(picked_game), self.image_label)
            self.pokemon_label.configure(text="The chosen Pokémon for this run is: " + chosen_gen3)
            self.display_pokemon_image(Pokemon_images.poke_image.get(chosen_gen3), self.pokemon_image_label)
        elif picked_game in ['Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver']:
            self.game_label.configure(text=f"The chosen game is: ")
            self.display_image(Box_Art_images.box_art.get(picked_game), self.image_label)
            self.pokemon_label.configure(text="The chosen Pokémon for this run is: " + chosen_gen4)
            self.display_pokemon_image(Pokemon_images.poke_image.get(chosen_gen4), self.pokemon_image_label)
        else:
            self.game_label.configure(text="Selection not valid")
            self.pokemon_label.configure(text="")
            self.display_image(None, self.image_label)
            self.display_pokemon_image(None, self.pokemon_image_label)

    def display_image(self, image_path, label):
        if image_path:
            image = Image.open(image_path)
            resized_image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(resized_image)
            label.configure(image=photo)
            label.image = photo  # Store a reference to prevent image garbage collection

    def display_pokemon_image(self, image_path, label):
        if image_path:
            image = Image.open(image_path)
            resized_image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(resized_image)
            label.configure(image=photo)
            label.image = photo  # Store a reference to prevent image garbage collection


if __name__ == "__main__":
    SoloChallengeWindow()
