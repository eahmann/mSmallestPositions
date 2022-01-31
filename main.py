class mSmallestPositions():
    # class scope variables
    list = [x for x in range(20)] # list of values from user
    m = 5 # amount of positions to find
    positions = [] # positions of min values in list
    min_counter = 0 # iteration counter for indexOfMin

    def __init__(self):
        # self.getUserInput()
        self.findPositions()

    def getUserInput(self):
        """
        Get user input and validate
        Precondition: None 
        Postcondition: len(list) > 0, 0 <= m <= len(list)
        """

        print("Input integer numbers followed by 'Enter' key. Enter numbers space delimited or one per line.\nPress 'Enter' key again when finished")
         # Get user input for list of values
        while True:
            userInput = input("> ")
            if userInput:
                try:
                    self.list.append(int(userInput.strip()))
                except:
                    try:
                        self.list.extend([int(i) for i in userInput.strip().split(" ")])
                    except:
                        print("ERROR: Invalid input. Enter only integer number(s)")
            elif not self.list:
                print("ERROR: List is empty. You must enter at least 1 integer")
            else:
                break

        # Get number of positions from user
        while True: 
            try:
                self.m = int(input("Enter number of smallest positions to find\n> "))
                if self.m > len(self.list): 
                    print("ERROR: Number must not exceed number of elements in list")
                else:
                    break
            except:
                print("ERROR: Invalid input. Enter only integer number")

    def findPositions(self):
        """
        Find 'm' number of positions 
        Precondition: self.m > 0
        Postcondition: 'self.postions' contains m number of elements 
        """
        # Create a m lenth list of m smallest positions
        for i in range(self.m): 
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
            self.min_counter += 1
        return index

    def postionMap(self):
        """
        Prints to screen a formatted output of positions and and values
        Precondition: len(list) > 0
        Postcondition: The positions and values are printed to screen
        """
        print("\nposition : value")
        # Create a dictionary from positons and values and print it to screen
        for position,value in dict(zip([i + 1 for i in range(len(self.list))], self.list)).items(): print('{:>8} : {}'.format(position, value))
        return "\n"

    def __str__(self):
        return f"{self.postionMap()}Position(s) of {self.m} smallest values: {self.positions}\nIndex of min iterations: {self.min_counter}"

print(mSmallestPositions())