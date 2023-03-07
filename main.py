'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import json


# Welcome Message
print("Monthly Budget Program")
print("----------------------\n")
print("Actions:")
print("1. Make a new budget (new)")
print("2. Edit an existing budget (edit)")
print("3. Quit the program (quit)")
# Ask users what they want to do
while True:
  user_action = input("\nPlease select an action: ")
# If user wants to make a new file
  if user_action == "new":
    # Ask user for name of file
    file_name = input("\nWhat would you like the file name to be? ")
    # Create file
    with open(file_name, "w") as f:
      test_dict = {"hello": "world"} # testing purposes
      json.dump(test_dict, f)
  # Ask user for income before tax

  # Calculate discretionary income

  # While discretionary income is greater than zero loop

    # Ask users to add categories and budget

    # Remove budget from discretionary income
  
    # Store categories in file

# Elif user wants to access a previous file
  elif user_action == "edit":
    print("picked edit") # testing purposes
  # Ask user for what file they want to change

  # Change category or budget

  # Quit the program

# If user types quit
  elif user_action == "quit":
  # Goodbye message
    print("Goodbye! Thanks for using the program.")
    break

# Else user did not input a correct action
  else:
  # Prints please try again
    print("Please try again")

quit()