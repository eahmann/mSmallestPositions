class mSmallestPositions():
    # class scope variables
    list = []
    amount = 0
    positions = []

    def __init__(self):
        self.getUserInput()
        self.findPositions()
        self.printPositions()

    def getUserInput(self):
        # Get list of int values from user
        print("Enter numbers followed by 'Enter' key\nPress 'Enter' key again when finished")
        while True:
            userInput = input()
            if userInput:
                try:
                    self.list.append(int(userInput))
                except ValueError:
                    print("Invalid input. Enter only integer number")
            elif not self.list:
                print("You must enter at least 1 integer")
            else:
                break

        # Get number of positions from user
        while True:
            try:
                self.amount = int(input("Enter number of smallest positions to print\n"))
                if self.amount > len(self.list):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input. Enter only integer number")

    def findPositions(self):
        # Find 'self.amount' number of positions 
        for i in range(self.amount):       
            self.positions.append(self.indexOfMin(self.list) + 1)


        print("\n\nPostion(s) of", self.amount, "smallest values:", self.positions)

    def indexOfMin(self):
        # Make a list of remaining indices. Exclude those that are already added to 'self.positons'
        remaining_indices = [ind for ind in range(len(self.list)) if (ind + 1) not in self.positions]

        # Set 'index' to first remaing index
        index = remaining_indices[0]        

        # Loop to find first index of smalled value. 'index' contains the first value, so we use 'remaining_indices[1:]' to slice it from the list
        for i in remaining_indices[1:]:
            if self.list[i] < self.list[index]:
                index = i
        return index

msp = mSmallestPositions()