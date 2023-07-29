import tkinter as tk
from PIL import ImageTk, Image
import random
from Poke_Dex_list import Gen1List, Gen2List
import Box_Art_images
import Pokemon_images

class Gen2Chooser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gen 2 Solo Challenge")
        self.root.geometry("1000x700")

        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, pady=10)

        self.Pokemon_Gold_button = tk.Button(button_frame, text="Pick Pokemon Gold", 
            command=lambda: self.generate_choice('Gold'))
        self.Pokemon_Gold_button.pack(side=tk.LEFT, padx=10)

        self.Pokemon_Silver_button = tk.Button(button_frame, text="Pick Pokemon Silver", 
            command=lambda: self.generate_choice('Silver'))
        self.Pokemon_Silver_button.pack(side=tk.LEFT, padx=10)

        self.Pokemon_Crystal_button = tk.Button(button_frame, text="Pick Pokemon Crystal", 
            command=lambda: self.generate_choice('Crystal'))
        self.Pokemon_Crystal_button.pack(side=tk.LEFT, padx=10)

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

    def generate_choice(self, picked_game):
        chosen_gen2 = random.choice(Gen1List + Gen2List)

        if picked_game in Box_Art_images.box_art:
            self.game_label.configure(text=f"The chosen game is: {picked_game}")
            self.display_image(Box_Art_images.box_art.get(picked_game), self.image_label)
            self.pokemon_label.configure(text="The chosen Pokémon for this run is: " + chosen_gen2)
            self.display_pokemon_image(Pokemon_images.poke_image.get(chosen_gen2), self.pokemon_image_label)
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
    Gen2Chooser()