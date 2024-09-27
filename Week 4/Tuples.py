def strtup(tuple, string): # defines the function

    new_word = '' #makes an empty variable to store data for the final output.
    for x in range(len(string)): # the range function turns the string into a range of numbers starting from 0 until the amount of letters there are in the word.
        new_word += string[x] * tuple[x] # this line basically adds a new letter in the word every time it was multiplied by the numbers assigned to it in the tuple.

    if len(tuple) != len(string): # this line basically means that if the length of the tuple is not the same as the length of the string, it will print out the statement below.
        print("the amount of numbers must be equal to the amount of letters in the world!" )
    
    return print(new_word) #this ends the function with it printing the new_word variable.

#test run.
strtup((1, 2, 3, 4), 'alex')
