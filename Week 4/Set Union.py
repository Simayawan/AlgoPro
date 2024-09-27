def Union(): #a function which is defined as a code to make a union of two different sets
    a = set(input("Input Numbers for Set A").split()) # "a" and "b" is a variable that is defined as a user input which will be turned as a set instead of a string
    b = set(input("Input Number for Set B").split()) # the .split() command will split the numbers with a coma instead of it outputting (1 2 3 4 5)

    listA = list(a) # this command declares listA as a list containing the user inputted elements from variable "a"
    listB = list(b) # this command declares listA as a list containing the user inputted elements from variable "a"

    listC = [] # this line means that listC will be an empty set, which will be used as a template for the unionized sets

    listA.sort() #all this line does is to sort the numbers or letters in the right order no matter what the order the user inputted
    listB.sort() #same as the line above

    for x in listA: #what these 3 lines does is to check for every element the user inputted in listA and to see if it's already in listC, if not then it will append elements in listA which is represented by "x" to list C.
        if x not in listC:
            listC.append(x)

    for x in listB: #it does the same as listA but for list B
        if x not in listC:
            listC.append(x)

    return print(listC) #this line means that the function ends with it printing the values of listC

Union() #what this line does is to make it possible to use the function above as without typing or calling the function, there will be no output. 
