class mSmallestPositions():
    # class scope variables
    list = [] # list of values from user
    m = 0 # amount of positions to find
    positions = [] # positions of min values in list
    min_counter = 0 # iteration counter for indexOfMin

    def __init__(self):
        self.getUserInput()
        self.findPositions()

    def getUserInput(self):
        """
        Get user input and validate
        Precondition: None 
        Postcondition: len(list) > 0, m <= len(list)
        """
        print("Enter numbers followed by 'Enter' key\nPress 'Enter' key again when finished")
        while True:
            userInput = input("> ")
            if userInput:
                # Validate the user enters only integers
                try:
                    # Append valid ipput to 'self.list'
                    self.list.append(int(userInput))
                except:
                    print("ERROR: Invalid input. Enter only integer number")
            elif not self.list: # Validate the list is not empty
                print("ERROR: You must enter at least 1 integer")
            else:
                break # Valid input ends the while loop

        while True: # Get number of positions from user
            try:
                self.m = int(input("Enter number of smallest positions to print\n> ")) # get user input for 'm' and try to cast it to integer validate input
                if self.m > len(self.list): # Check that the number does not exceed the number of items in the list
                    print("ERROR: Number must not exceed number of elements in list")
                else:
                    break # Valid input ends the while loop
            except:
                print("ERROR: Invalid input. Enter only integer number")

    def findPositions(self):
        """
        Find 'm' number of positions 
        Precondition: 
        Postcondition:  
        """

        for i in range(self.m): # for 'm' number of iterations
            self.positions.append(self.indexOfMin() + 1)

    def indexOfMin(self):               
        """
        Find index of smallest integer in list
        Precondition: 
        Postcondition:  
        """

        # Make a list of remaining indices. Exclude those that are already added to 'self.positons'
        remaining_indices = [ind for ind in range(len(self.list)) if (ind + 1) not in self.positions]

        # Set 'index' to first remaing index
        index = remaining_indices[0]        

        # Loop to find first index of smalled value. 'index' contains the first value, so we use 'remaining_indices[1:]' to slice it from the list
        for i in remaining_indices[1:]:
            # If any value is less than the value at 'self.list[index]', then update the index to reflect the position of the lowest value
            if self.list[i] < self.list[index]:
                index = i
            # Count iterations of the loop
            self.min_counter += 1
        # return the index of the min value
        return index

    def __str__(self):
        return f"\nPositions:      {[i + 1 for i in range(len(self.list))]}\nList of values: {self.list} \nPosition(s) of {self.m} smallest values: {self.positions}\nIndex of min iterations: {self.min_counter}"
        

print(mSmallestPositions())