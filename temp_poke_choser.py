import tkinter as tk
import random

#lists pokeball locations for starters
StarterLocation = ['Left', 'Middle', 'Right'] 

#lists all games from gen1 through gen 4
Poke_Games = ['Red', 'Blue', 'Yellow', 'Gold', 'Silver', 'Cyrstal', 'Ruby', 'Sapphire', 'Emerald', 
        'Fire Red', 'Leaf Green', 'Diamond', 'Pearl', 'Platinum', 'Heart Gold', 'Soul Silver'] 

#lits all pokemon in gen 1
Gen1List = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard','Squirtle', 'Wartortle', 
'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle','Kakuna', 'Beedrill','Pidgey','Pidgeotto', 'Pidgeot', 
'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash',
'Nidoran female', 'Nidorina', 'Nidoqueen', 'Nidoran male', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 
'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 
'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape',
'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke',
'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem',
'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetchd', 'Doduo', 'Dodrio', 'Seel', 
'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 
'Krabby','Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan',
'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra',
'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 
'Tauros','Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 
'Omanyte', 'Omastar','Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 
'Dratini', 'Dragonair', 'Dragonite','Mewtwo', 'Mew'] 

#lits new pokemon introduced in gen 2
Gen2List = ['Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw',
'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat',
'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy',
'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom',
'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus',
'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull',
'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub',
'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 
'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby',
'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi'] 

#lits new pokemon introduced in gen 3
Gen3List = ['Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 
'Poochyena','Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 
'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia',
'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask',
'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty',
'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun',
'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 
'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu',
'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy',
'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet',
'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo',
'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum',
'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 
'Jirachi', 'Deoxys'] 

#lits new pokemon introduced in gen 4
Gen4List = ['Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup',
'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio',
'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim',
'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 
'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky',
'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 
'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 
'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 
'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 
'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit',
'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai',
'Shaymin', 'Arceus']

#clears the message
def clear_message():
   Solo_message_label.config(text="")
   IronMon_Challenge_label.config(text="")

def Solo_Challenge():
    clear_message()
    #chooses a pokemon game at random
    PickedGame = (random.choice(Poke_Games))
    
    Solo_message_label.place(x=230, y=250)
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

    IronMon_Challenge_label.place(x=490, y=250)
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








