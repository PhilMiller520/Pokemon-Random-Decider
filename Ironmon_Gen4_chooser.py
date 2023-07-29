import tkinter as tk
from PIL import ImageTk, Image
import random
from Poke_Dex_list import Gen1List, Gen2List, Gen3List, Gen4List
import Box_Art_images
import Pokemon_images

class Gen4IronmonChallengeWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gen 4 Ironmon Challenge")
        self.root.geometry("800x900")
        
        empty_space_label = tk.Label(self.root, text="")
        empty_space_label.pack(side=tk.TOP, pady=15)
       
        # Pokemon buttons (Diamond, Pearl, and Platinum)
        self.pokemon_Diamond_button = tk.Button(self.root, text="Pokemon Diamond", command=self.set_picked_game_Diamond)
        self.pokemon_Diamond_button.place(x=50, y=10)
        
        self.pokemon_Pearl_button = tk.Button(self.root, text="Pokemon Pearl", command=self.set_picked_game_Pearl)
        self.pokemon_Pearl_button.place(x=170, y=10)
        
        self.pokemon_Platinum_button = tk.Button(self.root, text="Pokemon Platinum", command=self.set_picked_game_Platinum)
        self.pokemon_Platinum_button.place(x=270, y=10)  
        
        self.Pokemon_HeartGold_button = tk.Button(self.root, text="Pokemon Heart Gold", command=self.set_picked_game_HeartGold)
        self.Pokemon_HeartGold_button.place(x=390, y=10)
        
        self.Pokemon_SoulSilver_button = tk.Button(self.root, text="Pokemon Soul Silver", command=self.set_picked_game_SoulSilver)
        self.Pokemon_SoulSilver_button.place(x=520, y=10)    

        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH)

        frame1 = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2, width=280)
        frame1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # the information in game_label from run_challenge will be displayed in frame1 
        self.game_label = tk.Label(frame1, text="")
        self.game_label.pack()
        
        self.image_label = tk.Label(frame1)
        self.image_label.pack()

        frame2 = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2, width=280)
        frame2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # the information for starter_location_label from run_challenge will be displayed in frame2         
        self.starter_location_label = tk.Label(frame2, text="")
        self.starter_location_label.pack()

        frame3 = tk.Frame(main_frame, highlightbackground="black", highlightthickness=2, width=280)
        frame3.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        # the information for alternate_starter_label from run_challenge will be displayed in frame3 
        self.alternate_starter_labels = []
        self.pokemon_image_labels = []
        self.photo_images = [] # Store references to PhotoImage objects

        for i in range(12):  # Initialize with empty labels for all possible generations
            # Create label for Pokemon name
            label = tk.Label(frame3, text="")
            label.grid(row=i * 2, column=0)
            self.alternate_starter_labels.append(label)

            # Create label for Pokemon image
            image_label = tk.Label(frame3)
            image_label.grid(row=i * 2 + 1, column=0)
            self.pokemon_image_labels.append(image_label)
        
        self.root.mainloop()

    def set_picked_game_Diamond(self):
        self.run_challenge("Diamond")

    def set_picked_game_Pearl(self):
        self.run_challenge("Pearl")

    def set_picked_game_Platinum(self):
        self.run_challenge("Platinum") 
    
    def set_picked_game_HeartGold(self):
        self.run_challenge("Heart Gold") 
    
    def set_picked_game_SoulSilver(self):
        self.run_challenge("Soul Silver")   
        
    # this will choose a random game, choose the pokeball location with the starter, and picks alternate starters  
    def run_challenge(self, picked_game=None):
        self.starter_location = random.choice(['Left', 'Middle', 'Right'])
        chosen_gen = []  # Initialize chosen_gen as an empty list

        if picked_game in ['Pearl', 'Diamond', 'Platinum', 'Heart Gold', 'Soul Silver']:
            chosen_gen = random.sample(Gen1List + Gen2List + Gen3List + Gen4List, k=4)

        self.game_label.after(10, self.update_game_label, picked_game)
        self.image_label.after(10, self.update_image_label, picked_game)
        self.starter_location_label.after(10, self.update_starter_location_label, self.starter_location)

        self.update_alternate_starter_labels(chosen_gen)

        self.root.update()  # Force window refresh

    def update_game_label(self, game): # displays which game was picked
        self.game_label.configure(text=f"The chosen game is {game}")

    def update_image_label(self, game): # displays the box art of the picked game
        self.display_image(Box_Art_images.box_art.get(game), self.image_label)

    def update_starter_location_label(self, location): # dispalys the starer pokemon pokeball location
        self.starter_location_label.configure(text=f"The chosen starter is in the {location} Pokeball")
        
    def update_alternate_text_label(self, index, pokemon): # displays alternate starter pokemon names
        self.alternate_starter_labels[index].configure(text=pokemon)
        
    def update_alternate_starter_labels(self, chosen_gen):
        self.alternate_starter_labels[0].configure(text="The alternate starter options are:")
        for i in range(1, len(self.alternate_starter_labels)):
            if i <= len(chosen_gen):
                pokemon = chosen_gen[i - 1]
                self.alternate_starter_labels[i].after(10, self.update_alternate_text_label, i, pokemon)
                self.pokemon_image_labels[i].after(10, self.update_alternate_starter_image, i, pokemon)
            else:
                self.alternate_starter_labels[i].configure(text="")
                self.pokemon_image_labels[i].configure(image="")

    def update_alternate_starter_image(self, index, pokemon):
        if pokemon:
            image_path = Pokemon_images.poke_image.get(pokemon)
            self.display_alternate_starter_images(image_path, self.pokemon_image_labels[index])
        else:
            self.pokemon_image_labels[index].configure(image="")
            self.pokemon_image_labels[index].image = None

    def display_image(self, image_path, label):
        if image_path:
            image = Image.open(image_path)
            resized_image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(resized_image)
            label.configure(image=photo)
            label.image = photo
            self.photo_images.append(photo)  # Store a reference to the PhotoImage object

    def display_alternate_starter_images(self, image_path, label):
        if image_path:
            image = Image.open(image_path)
            resized_image = image.resize((160, 160))
            photo = ImageTk.PhotoImage(resized_image)
            label.configure(image=photo)
            label.image = photo
        else:
            label.configure(image="")
            label.image = None

if __name__ == "__main__":
    Gen4IronmonChallengeWindow()