import tkinter as tk
import random
import Gen1_List #program that lists all the pokemon from gen 1
import Gen2_List #program that lists all the pokemon added to the global dex from gen 2
import Gen3_List #program that lists all the pokemon added to the global dex from gen 3
import Gen4_List #program that lists all the pokemon added to the global dex from gen 4
import Poke_Games_List #lists all games from gen1 through gen 4

#lists pokeball locations for starters
StarterLocation = ['Left', 'Middle', 'Right'] 

#clears the message
def clear_message():
   Solo_message_label.config(text="")
   IronMon_Challenge_label.config(text="")

def Solo_Challenge():
    clear_message()
    #chooses a pokemon game at random
    PickedGame = (random.choice(Poke_Games_List.Poke_Games))
    
    Solo_message_label.place(x=230, y=250)
    if PickedGame in ['Red', 'Blue', 'Yellow']:   
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
                " "
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1_List.Gen1List))
    elif PickedGame in ['Gold', 'Silver', 'Crystal']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
                " "
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1_List.Gen1List + Gen2_List.Gen2List))
    elif PickedGame in ['Ruby', 'Sapphire', 'Emerald', 'Fire Red', 'Leaf Green']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
                " "
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1_List.Gen1List + Gen2_List.Gen2List + Gen3_List.Gen3List))
    elif PickedGame in ['Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver']:  
           Solo_message_label.config(text=f"""The chosen game is {PickedGame}\n
                " "
              The chosen pokemon for this run is: """ 
              + random.choice(Gen1_List.Gen1List + Gen2_List.Gen2List + Gen3_List.Gen3List + 
                  Gen4_List.Gen4List))
    else: 
        Solo_message_label.config(text="selection not valid")
   
def IronMon_Challenge():
    clear_message()
    PickedGame = (random.choice(Poke_Games_List.Poke_Games))
    Pokeball_Starter =(random.choice(StarterLocation))

    IronMon_Challenge_label.place(x=490, y=250)
    if PickedGame in ['Red', 'Blue']:   
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              The chosen starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1_List.Gen1List, k=3))) 
    elif PickedGame in ['Gold', 'Silver', 'Crystal']:
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1_List.Gen1List + Gen2_List.Gen2List, k=3))) 
    elif PickedGame in ['Ruby', 'Sapphire', 'Emerald', 'Fire Red', 'Leaf Green']:  
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
              + ", ".join(random.sample(Gen1_List.Gen1List + Gen2_List.Gen2List + 
                        Gen3_List.Gen3List, k=3)))
    elif PickedGame in ['Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver']:  
           IronMon_Challenge_label.config(text=f"""The chosen game is {PickedGame}\n
              Your starter is in the {Pokeball_Starter} Pokeball\n
              The Alternate Starter pokemon options are:\n""" 
               + ", ".join(random.sample(Gen1_List.Gen1List + Gen2_List.Gen2List + 
                        Gen3_List.Gen3List + Gen4_List.Gen4List, k=4)))
    else: 
        IronMon_Challenge_label.config(text="""The chosen game is Yellow\n
         The Alternate Starter pokemon options are:\n""" + 
            ", ".join(random.sample(Gen1_List.Gen1List, k=3))) 

def toggle_text():
      if var.get():
            IronMonbtn.config(text="Kaizo Challenge")
      else:
            IronMonbtn.config(text="Ironmon Challenge")

root = tk.Tk()

root.geometry("1000x800") #determins the height and with of the window
root.title("Pokemon Randomizer") #creates the title for the window

#displays the chosen text in a specified font and size
label = tk.Label(root, text="Choose Your Play Style", font=('Arial, 18')) 
#this determins the x & y quardanents for where the above text will be displayed in the window
label.pack(padx=20, pady=20) 

#solo challenge button and its placement
Solobtn = tk.Button(root, text="Solo Challenge", font=('Arial, 10'), command=Solo_Challenge)
Solobtn.place(x=200, y=100, height=100, width=100)

#solo challenge message text stating which game and pokemon have been chosen
Solo_message_label = tk.Label(root, text="", width=500)
Solo_message_label.place(x=230, y=250, anchor="center")

#Ironmon challenge button and its placement
IronMonbtn = tk.Button(root, wraplength=80, justify="left", text="Ironmon Challenge", font=('Arial, 10'), 
   command=IronMon_Challenge)
IronMonbtn.place(x=450, y=100, height=100, width=100)

#Ironmon challenge message text stating which game, pokeball location and pokemons have been chosen
IronMon_Challenge_label = tk.Label(root, text="", width=500)
IronMon_Challenge_label.place(x=490, y=250, anchor="center")

#checkbox to change the text ironmon to kiazo in the ironmon button
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text = "Swap for Kiazo mode", variable=var, command=toggle_text)
checkbox.place(x=550, y=100)

root.mainloop()








