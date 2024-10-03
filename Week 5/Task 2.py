class player:
    def __init__ (self, storage, currency, health):
        self.storage = storage
        self.currency = currency
        self.health = health

    def Storage(self): #storage function which can add and remove items
        print(self.storage) #prints initial storage before additions
        print("Add Item[1]") #simple navigation bar
        print("Remove Item[2]")
        storinp = input("Input number") #input to pick your choice
        if storinp == "1": #if you input 1, does what the code below does
            additem = input("What do you want to add?") #input to add item
            self.storage.add(additem) #adds item to inventory
            print(self.storage) #prints current storage roster

        elif storinp == "2":#if you input 2, does what the code below does
            rmvitem = input("What do you want to remove?") #removes item from the storage roster
            if rmvitem in self.storage: #if the inputted item is in the list, it will remove it
                self.storage.remove(rmvitem) #removes said item
                print(self.storage) #prints new roster
            else:
                print("Item not in Inventory!") #if item that was typed was not in the list, then it will print that

    def Currency(self): #function for currency where it can decrease and increase
        print("You decided to buy something from Mystia's Izakaya")
        print("Mystia : Oh? A human? what would you like today?")
        print("Talk to her about something else [1]\n\
              Order from the Menu [2]")
        navchoice = input() # variable for the choice input

        if navchoice == "1": # if input = 1, does below
            print("You talk to her about some recipes,\n\
                  she was happy with the recipes you gave her.\n\
                  You were given 10 yen for the recipes")
            self.currency += 10 # adds 10 yen to the money in hand

            print(f"Your current balance is now {self.currency} yen") #prints new balance


        elif navchoice == "2": # if input = 2
            print("Menu:\n\
                Ramen [1]\n\
                Lamprey [2] \n\
                Ocha [3]")
            print(f"Your current balance is {self.currency} yen") #prints current ballance
            
            navmenu = input() #variable to input choice
            
            if navmenu == "1": # if input = 1, does below
                print("Mystia: The Ramen is 90 yen")
                self.currency -= 90 #decreases the money by 90
                print(f"Your current balance is {self.currency} yen")
                if self.currency < 0: #if money goes below 0, it prints below
                    print("Mysitia: Oi, you think I'm running a charity?")

            elif navmenu == "2": 
                print("Mystia: The Lamprey is 180 yen")
                self.currency -= 180
                print(f"Your current balance is {self.currency} yen")
                if self.currency < 0:
                    print("Mysitia: Oi, you think I'm running a charity?")

            if navmenu == "3":
                print("Mystia: This Ocha is 1000 yen")
                self.currency -= 1001 
                print(f"Your current balance is now {self.currency} yen")
                if self.currency < 0:
                    print("Mysitia: Oi, you think I'm running a charity?")

    def Health(self):
        print(f"Your health is {self.health}")
        print("where do you want to go?\n Forest of Magic[1]\n Scarlet Devil Mansion[2]\n Bamboo Forest of the Lost[3]")
        
        navmove = input("Type Number: ").lower()
        if navmove == "1":
            print("While rummaging around the Forest of Magic,\n\
                  you found a young Magician looking for mushrooms.\n\
                  She calls herself Marisa Kirisame and is offering\n\
                  to have a Danmaku Battle with you.")
            print("What will you do?\n\
                  Agree to Duel [1]\n\
                  Runaway [2]")
            navchoice = input()
            if navchoice == "1":
                print("MASTER SPARKKKKK! Marisa said with passion as a single Giant laser hits your body.")
                print("Marisa deals 100 damage")
                self.health -= 100 #decreases the health of the character by 100, meaning dead
                if self.health <= 0: #if it is 0 or goes into negatives, it prints out below
                    print("You are dead, you can't do Danmaku!")

            if navchoice == "2":
                print("You ran away but you suddenly bumped into Rumia\n\
                      Rumia found you delicious and has a dangerous look in her eyes")
                
                print("Rumia deals 100 damage")
                self.health -= 100
                if self.health <= 0:
                    print("You were eaten alive, at least Rumia said you tasted delicious")

        elif navmove == "2":

            print("While walking along the trail by Misty Lake, \n\
                  you found a quant red Mansion, looking for shelter you reached the gate \n\
                  where an oriental lady in green looks at you with sharp eyes.")
            print("What will you do?\n \
                  Approach Her [1]\n \
                  Runaway [2]")
            navchoice = input()
            if navchoice == "1":
                print("I am Hong Meiling, and the lady is in a bad mood today, \n\
                    I'll make Sakuya cook you to make her feel beter!")
                print("Meiling deals 100 damage")
                self.health -= 100
                if self.health <= 0:
                    print("You are dead, you caught Remilia on the wrong day!")

            if navchoice == "2":
                print("You ran away but you didn't see the lake and drowned in it")
                
                print("Water deals 100 emotional damage")
                self.health -= 100
                if self.health <= 0:
                    print("You are dead, you can't swim apparently")

        elif navmove == "3":

            print("You went to a Bamboo clearing and realized you are now lost.\n\
                  After some time you found a little girl with bunny ears.")
            print("What will you do?\n \
                    Approach Her [1]\n \
                    Runaway [2]")
            navchoice = input()
            if navchoice == "1":
                print("Oh hello there young one, I baked some cake, you want some?")
                print("Cake deals 100 damage")
                self.health -= 100
            if self.health <= 0:
                print("You are dead, you fell for Tewi's prank, Cyanide Cake!")

            if navchoice == "2":
                print("You ran away but you were still lost, you end up dying due to starvation")
                    
                print("Hunger deals 100 Damage")
                self.health -= 100
                if self.health <= 0:
                    print("You are dead, should've never gone into the Bamboo Forest of the Lost")


        else:
            print("You can't go there yet!")




inventory = {"Excorcising Stick", "Trigram Cannon", "Blade"}

currency = (1000)

health = (100)


Player = player(inventory, currency, health)

#Test Run

#Player.Currency() #Test Currency

#Player.Health() #Test Health

#Player.Storage() #Test Storage
