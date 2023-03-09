'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import json


#Functions
def disposable_income(income):
      if income_before_tax <= 14000:
        tax = 0.105 * income_before_tax
      elif income_before_tax <= 48000:
        tax = 0.175 * (income_before_tax - 14, 000) + 1, 470
      elif income_before_tax <= 70000:
        tax = 0.3 * (income_before_tax - 48, 000) + 7, 950
      elif income_before_tax <= 180000:
        tax = 0.33 * (income_before_tax - 70, 000) + 14, 850
      else:
        tax = 0.39 * (income_before_tax - 180, 000) + 48, 540
  
      disposable_income = income_before_tax - tax

      print(f"Your income after tax is: {disposable_income}")
  
# Welcome Message
print("Monthly Budget Program")
print("----------------------\n")
print("Actions:")
print("1. Make a new budget (new)")
print("2. Edit an existing budget (edit)")
print("3. Quit the program (quit)")
# Ask users what they want to do
while True:
  user_action = input("\nPlease select an action: ").lower()
  # If user wants to make a new file
  if user_action == "new":
    # Ask user for name of file
    file_name = input("\nWhat would you like the file name to be? ")
    # Create file
    with open(file_name, "w") as f:
      test_dict = {"hello": "world"}  # testing purposes
      json.dump(test_dict, f)
  # Ask user for income before tax
      income_before_tax = int(input("Enter your income before tax $: "))
    # Calculate disposable income
      disposable_income(income_before_tax)
  # While disposable income is greater than zero loop

  # Ask users to add categories and budget

  # Remove budget from discretionary income

  # Store categories in file

# Elif user wants to access a previous file
  elif user_action == "edit":
    print("picked edit")  # testing purposes
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
