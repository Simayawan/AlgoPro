class Gun():
    def __init__(self, shoot, accuracy):
        self.shoot = shoot
        self.accuracy = accuracy
    
    def Shoot(self): #makes a function for ammo
        print(f'You have {self.shoot} inside your magizine')
        print("Shoot [1]")
        print("Save Ammo [2]")
        
        navchoice = input("Choice: ")

        if navchoice == "1":
            print("How many times do you want to shoot?")
            inpshoot = int(input("Input: "))

            if inpshoot > self.shoot:
                print(f"You are out of Ammo, you shot {self.shoot} bullets")
            elif inpshoot:
                
                print(f"You shot {inpshoot} times")
                self.shoot -= inpshoot
                print(f"Your Current Ammo count is {self.shoot}")

                if self.shoot == 0:
                    print("you ran out of bullets")
            else:
                print("Invalid input, must be intergers")

        elif navchoice == "2":
            print("Ended")

    def Accuracy(self): #makes a simple minigame
        print(f'your gun accuracy is {self.accuracy}%')
        print(f'You have {self.shoot} inside your magazine')
        print("Shoot [1]")
        print("Save Ammo [2]")
            
        navchoice = input("Choice: ")

        if navchoice == "1":
            print("Which direction?")
            print("Up [1]\nDown [2]\nLeft [3]\nRight [4]")
            
            navdirect = input()
            
            if navdirect == "1":
                print ("You missed")

            elif navdirect == "2":
                print ("You missed")

            elif navdirect == "3":
                print ("You hit the target!")

            elif navdirect == "4":
                print ("You missed")


        elif navchoice == "2":
            print("Ended")


ammo = 19

accuracy = 90

gun = Gun(ammo, accuracy)

#gun.Shoot() #shoots gun

#gun.Accuracy() #accuracy simple game
