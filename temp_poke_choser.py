import tkinter as tk
import random

#lists pokeball locations for starters
StarterLocation = ['Left', 'Middle', 'Right'] 

#lists all games from gen1 through gen 4
Poke_Games = ['Red', 'Blue', 'Yellow', 'Gold', 'Silver', 'Cyrstal', 'Ruby', 'Sapphire', 'Emerald', 
        'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver'] 

#lits all pokemon in gen 1
Gen1List = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard','Squirtle', 'Wartortle'] 

#lits new pokemon introduced in gen 2
Gen2List = ['Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw'] 

#lits new pokemon introduced in gen 3
Gen3List = ['Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp'] 

#lits new pokemon introduced in gen 4
Gen4List = ['Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup']

#clears the message
def clear_message():
   Solo_message_label.config(text="")
   IronMon_Challenge_label.config(text="")

def Solo_Challenge():
    clear_message()
    #chooses a pokemon game at random
    PickedGame = (random.choice(Poke_Games))
    
    Solo_message_label.place(x=200, y=250)
    if PickedGame in ['Red', 'Blue', 'Yellow']:   
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1List))
    elif PickedGame in ['Gold', 'Silver', 'Cyrstal']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1List + Gen2List))
    elif PickedGame in ['Ruby', 'Sapphire', 'Emerald', 'Fire Red', 'Leaf Green']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1List + Gen2List + Gen3List))
    elif PickedGame in ['Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1List + Gen2List + Gen3List+ Gen4List))
    else: 
        Solo_message_label.config(text="selection not valid")
   
def IronMon_Challenge():
    clear_message()
    PickedGame = (random.choice(Poke_Games))
    Pokeball_Starter =(random.choice(StarterLocation))

    IronMon_Challenge_label.place(x=400, y=250)
    if PickedGame in ['Red', 'Blue']:   
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1List, k=3))) 
    elif PickedGame in ['Gold', 'Silver', 'Cyrstal']:
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1List + Gen2List, k=3))) 
    elif PickedGame in ['Ruby', 'Sapphire', 'Emerald', 'Fire Red', 'Leaf Green']:  
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1List + Gen2List + Gen3List, k=3)))
    elif PickedGame in ['Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver']:  
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1List + Gen2List + Gen3List+ Gen4List, k=4)))
    else: 
        IronMon_Challenge_label.config(text="""The chosen game is Yellow\n
         The Alternate Starter pokemon options are:\n""" + ", ".join(random.sample(Gen1List, k=3))) 

root = tk.Tk()

root.geometry("1000x800") #determins the height and with of the window
root.title("Pokemon Randomizer") #creates the title for the window

#displays the chosen text in a specified font and size
label = tk.Label(root, text="Choose Your Play Style", font=('Arial, 18')) 
#this determins the x & y quardanents for where the above text will be displayed in the window
label.pack(padx=20, pady=20) 

Solobtn = tk.Button(root, text="Solo Challenge", font=('Arial, 10'), command=Solo_Challenge)
Solobtn.place(x=200, y=100, height=100, width=100)

Solo_message_label = tk.Label(root, text="", width=250)
Solo_message_label.place(x=200, y=250, anchor="center")

IronMonbtn = tk.Button(root, wraplength=80, justify="left", text="Ironmon Challenge", font=('Arial, 10'), 
   command=IronMon_Challenge)
IronMonbtn.place(x=400, y=100, height=100, width=100)

IronMon_Challenge_label = tk.Label(root, text="", width=500)
IronMon_Challenge_label.place(x=400, y=250, anchor="center")

root.mainloop()








