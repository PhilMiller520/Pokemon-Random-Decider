# Pokemon-Random-Decider

The program will consist of three challenge modes:
  1. Solo challenge:
  2. Ironmon challenge
  3. Kaizo challenge

Solo and Ironmon will have their own buttons that when pressed will do the following:
  1. Solo challenge:
    1. it will choose a pokemon game at random and display the game title
    2. it will then choose a pokemon at random from that game and display it
  2. Ironmon challenge:
    1. it will choose a pokemon game at random and display the game title
    2. it will then decide which pokeball the starter will be in.
    3. it will then pick, at minimum, 3 alternative starers the player can choose from (should they be picked in the randomized rom as starters, this is a sperate program that I have not made)
  3. Kaizo challenge:
    1. as the process for choosing a starter in a Kaizo challenge is the same as an Ironmon a check box will be created to change the text in the Ironmon box to state that its now a Kaizo challenge
Images of the box art for the game and pokemon chosen will be displayed

As of 4/17/2023 the buttons for Solo and Ironmon challenges have been created and their message have been displayed.
the check box for Kaizo and the pictures will be added soonish
At this time only pokemon generations 1 through 4 are covered.

as of 4/18/2023 the checkbox button has been added and the pokedexs for gens 1 through 4 have been completed. Also adjusted the placement of the labels and buttons
as of 5/19/2023 the following files have been created for the main file to call. the imported files are Gen1_List, Gen2_List, Gen3_List, Gen4_List and Poke_Games_List.

As of 7/29/2023 the following changes have been made: 

1. The following items have been replaced by Poke_Dex_list.py
 > - Gen1_List.py
> - Gen2_List.py
> - Gen3_List.py
> - Gen4_List.py

2. temp_poke_choser.py has been replaced by Pokemon_Challenge_tabs.py
3. Pokemon_Challenge_tabs.py has the following features
> - There are 4 tabs
> > - The 1st tab (Pick Your Solo Run) has 4 buttons for solo runs specifically for gens 1 through 4
> > - When a Gen (Gens 1 through 4) button is clicked a new modal will be displayed that will let the user randomly choose a Pokémon from a specific game from that generation
> > - The 2nd tab (Random Solo Challenge) has 1 button that opens a new modal for the Solo_challenge_generator.py
> > - The 3rd tab (Pick Your Ironmon Challenge) has 4 buttons for ironmon challenges specifically for gens 1 through 4
> > > - When a Gen (Gens 1 through 4) button is clicked a new modal will be displayed that will let the user randomly choose a Pokémon from a specific game from that generation
4. The 2nd tab (Random Ironmon Challenge) has 1 button that opens a new modal for the Ironmon_challenge_generator.py
5. All mentions of Kaizomon have been removed
6. All random generator programs (any program that is called from the Pokemon_Challenge_tabs.py program) now display box art images of the Pokémon games and images of the Pokémons.
