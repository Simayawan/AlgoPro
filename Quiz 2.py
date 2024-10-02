class Binusmaya:
    def __init__ (self, lecturers, classes, schedule):
        self.lecturers = lecturers
        self.classes = classes
        self.schedule = schedule

    def addrmvlec(self): #Add and Remove a Lecturer
        print("Add Lecturer [1]")
        print("Remove Lecturer [2]")
        lecinp = input("Type the Number")

        if lecinp == "1": 
            print(self.lecturers)
            print("Who do you want to add?")
            addname = input('Add Name')
            addprogram = input('Add Program')
            addid = input("Add ID")

            lecdata = {addname: [addprogram, addid]}

            print(lecdata)
            print("Is this Correct?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":
                if addname not in self.lecturers:
                    self.lecturers.update(lecdata)
                    print('lecturer added')
                    print(self.lecturers)

                elif addname in self.lecturers:
                    print("Lecturer already added")

                elif addprogram in self.lecturers:
                    print("Program is manned by other lecturers!")

                elif addid in self.lecturers:
                    print("ID Invalid")
                    
                


            elif yn.lower() == "no":
                print("Operation Cancelled")
        
        elif lecinp == "2":
            print(self.lecturers)
            print("Who do you want to remove?")
            rmvname = input('Type Name')

            print("Are you sure?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":
                if rmvname in self.lecturers:
                    del self.lecturers[rmvname]
                print("Lecturer removed")
                print(self.lecturers)
                

            elif yn == "no":
                print("Operation Cancelled")

        elif rmvname not in self.lecturers:
            print("No such lecturer exists!")

    def addrmvclass(self):
        
        print("Add Class [1]")
        print("Remove Class [2]")
        classinp = input("Type the Number")

        if classinp == "1": 
            print(self.classes)
            print("What class do you want to add?")
            addclass = input('Class Name')

            classdata = [addclass]

            print(classdata)
            print("Is this Correct?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":

                if addclass not in self.classes:
                    self.classes.append(addclass)
                    print('Class added')
                    print(self.classes)
                elif addclass in self.classes:
                    print("Duplicate Input")
                
                


            elif yn == "no":
                print("Operation Cancelled")

        
        if classinp == "2":
            print(self.classes)
            print("What class you want to remove?")
            rmvclass = input('Remove Class')
            classdata = {rmvclass}
            print("Are you sure?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":
                if rmvclass in self.classes:
                    self.classes.remove(rmvclass)
                    print("Class removed")
                    print(self.classes)

                elif classdata not in self.classes:
                    print("No such class exists!")

            elif yn == "no":
                print("Operation Cancelled")

            

    def addrmvsch(self):
        print("Add Schedule [1]")
        print("Remove Schedule [2]")
        schinp = input("Type the Number")

        if schinp == "1": 
            print(self.schedule)
            print("What do you want to add to the schedule?")
            schname = input('Add Lecturer Name')
            schprogram = input('Add Program')
            addtime = input("Add time")

            schdata = {schname: [schprogram, addtime]}

            print(schdata)
            print("Is this Correct?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":
                if schdata not in self.schedule:
                    self.schedule.append(schdata)
                    print('Schedule updated')
                elif schdata in self.schedule:
                    print("Duplicate Input")

                print(self.schedule)

            elif yn == "no":
                print("Operation Cancelled")

        
        
        if schinp == "2":
            print(self.schedule)
            print("What do you want to remove to the schedule?")
            rmvsch = input('Remove Name')
            print("Are you sure?")
            print("Yes or No?")
            yn = input("Type Yes or No").lower()
            if yn == "yes":
                found = False
                for sch in self.schedule:
                    if sch[0] == rmvsch:
                        self.schedule.remove(sch)
                        print('Schedule updated')
                        found = True
                        break
                if not found:
                    print("No schedule for that exists!")
                


            elif yn == "no":
                print("Operation Cancelled")


lecturers = {
            "Reimu Hakurei": ["Algorithm and Programming", "100106"],
        "Marisa Kirisame": ["Scientific Computation", "100107"],
        "Eiki Shiki": ["Pancasila", "100108"]}
    
classes = ["L1AC", "L1BC","L1CC"]

schedules = []

binusmaya = Binusmaya(lecturers, classes, schedules)
#test run
    
#binusmaya.addrmvlec() #--> add remove lecturer

#binusmaya.addrmvclass() #--> add remove class

#binusmaya.addrmvsch() #--> add remove schedule
