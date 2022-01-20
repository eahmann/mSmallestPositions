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

        print("Input list of numbers. Enter numbers followed by 'Enter' key\nPress 'Enter' key again when finished")
         # Get user input for list of values
        while True:
            userInput = input("> ")
            if userInput:
                # Validate the user enters only integers
                try:
                    # Try to cast input to integer to validate input and append valid ipput to 'self.list'
                    self.list.append(int(userInput))
                except:
                    print("ERROR: Invalid input. Enter only integer number")
             # Validate the list is not empty
            elif not self.list:
                print("ERROR: You must enter at least 1 integer")
            else:
                # Valid input ends the while loop
                break

        # Get number of positions from user
        while True: 
            # Validate the user enters only integers
            try:
                 # get user input for 'm' and try to cast it to integer validate input
                self.m = int(input("Enter number of smallest positions to find\n> "))
                # Check that the number does not exceed the number of items in the list
                if self.m > len(self.list): 
                    print("ERROR: Number must not exceed number of elements in list")
                else:
                    # Valid input ends the while loop
                    break
            except:
                print("ERROR: Invalid input. Enter only integer number")

    def findPositions(self):
        """
        Find 'm' number of positions 
        Precondition: self.m > 0
        Postcondition: 'self.postions' contains m number of elements 
        """

        for i in range(self.m): # for 'm' number of iterations
            # Append result from indexOfMin + 1 to list of positons
            self.positions.append(self.indexOfMin() + 1)

    def indexOfMin(self):               
        """
        Find index of smallest integer in list
        Precondition: len(list) > 0
        Postcondition: The index of the first min value is returned from remaing unused indices
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

    def postionMap(self):
        """
        Prints to screen a formatted output of positions and and values
        Precondition: len(list) > 0
        Postcondition: The positions and values are printed to screen
        """
        print("\nposition : value")
        # Create a dictionary from positons and values and print it to screen
        for position,value in dict(zip([i + 1 for i in range(len(self.list))], self.list)).items(): print(position, ':', value)
        # Need to have a return here otherwise it will print 'None' in the __str__ method
        return "\n"

    def __str__(self):
        return f"{self.postionMap()}Position(s) of {self.m} smallest values: {self.positions}\nIndex of min iterations: {self.min_counter}"

print(mSmallestPositions())