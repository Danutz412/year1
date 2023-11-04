# ask the user how many apples to remove
number_of_apples_to_remove = int(input("How many apples should I remove?\n"))

# variable to track the removed apples
removed_apples = 0

# loop until all apples are removed
while removed_apples < number_of_apples_to_remove:
    # print message
    print(" Removed apple.")

    # increment the apples count
    removed_apples += 1
