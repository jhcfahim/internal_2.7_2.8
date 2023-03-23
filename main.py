"""
JHC Internal
Fahim Firdaus
2.7 and 2.8 - 12 credits
"""
import os

# Functions


def disposable_income(income_before_tax):
  """Calculates disposable income and prints it out to the user."""

  # Calculate the tax based on income before tax
  if income_before_tax <= 14000:
    tax = 0.105 * income_before_tax
  elif income_before_tax <= 48000:
    tax = 0.175 * (income_before_tax - 14000) + 945
  elif income_before_tax <= 70000:
    tax = 0.3 * (income_before_tax - 48000) + 7135
  elif income_before_tax <= 180000:
    tax = 0.33 * (income_before_tax - 70000) + 15755
  else:
    tax = 0.39 * (income_before_tax - 180000) + 51795

  # Calculates disposable income (income after tax) and rounds to 2dp
  income_after_tax = round(income_before_tax - tax, 2)

  # Print the income after tax to the user
  print(f"Your income after tax is: {income_after_tax}")

  # Return the income after tax value
  return income_after_tax


def is_valid_number(input_str):
  """Check that user has entered a float or a number."""

  # Check if the input string contains only digits or a valid float number
  if input_str.isdigit() or (('.' in input_str)
                             and input_str.replace('.', '', 1).isdigit()):
    return True
  else:
    return False


def check_num(question):
  """Tell user if they have not entered a valid response."""

  # Loop until the user enteres a valid number
  while True:
    user_input = input(question)

    # Check if the user's input is a valid number
    if is_valid_number(user_input):
      return float(user_input)
    else:
      print("Please enter a valid number for budget")


def file_exists(file_name):
  """Check if the file exists, and return result."""
  return os.path.isfile(file_name)


def create_budget_file():
    """Create a new budget file and calculate disposable income."""

    # Loop to get a unique file name
    while True:
        file_name = input("\nWhat would you like the file name to be? ")

        # Check if a file with that name already exists
        if not file_exists(file_name):
            break
        else:
            print("A file already exists with that name. Please choose a different name.")

    # Create a new file with the given name
    with open(file_name, "w") as f:
        f.write("Monthly Budget\n")
        f.write("--------------\n")

        # Loop to get the user's income before tax
        while True:
            income_before_tax = input("\nEnter your income before tax $: ")

            # Check if the input is a valid number
            if is_valid_number(income_before_tax):
                income_before_tax = float(income_before_tax)
                break
            else:
                print("Please enter a valid number for income.")

        # Calculate the disposable income (income after tax)
        income_after_tax = disposable_income(income_before_tax)

        # Add the different budget categories and their corresponding amount to the file
        add_categories(income_after_tax, f)

  
def add_categories(income_after_tax, f):
  """Allow users to add categories and budgets, and put those categories into a file."""

  # Make a new dictionary to store categories.
  categories = {}

  # Prompt the user to start adding categories and budgets.
  print("\nStart adding your categories and budgets below, when you want to stop, type 'quit' into the category section if you need help, type 'help' into the category section")

  # Loop through until discretionary income is zero, or user types "stop"
  while income_after_tax > 0:
   
    # Ask users to add categories and budget
    category = input("\nAdd a category: ")
    
    # Check if user wants to stop adding categories or needs help.
    if category == "stop":
      break
    elif category == "help":
      # Provide examples of categories and budgets.
      print("""\nIf you need help with choosing a category, consider listing out your regular monthly expenses such as rent/mortgage, utilities, groceries, transportation, and any other bills. 
You can also add categories for savings, entertainment, and personal expenses. 
Once you have a list of categories, enter them one by one when prompted. 
For the budget section, enter the amount of money you want to put aside for the specific category, make sure you don't go over your income!
\nFor example:
Category: food
Budget: 200
          """)

    # If user doesn't need help, ask for the budget
    else:
      budget = check_num("Add a budget (enter a number) $: ")

      # Check if the budget is more than discretionary income
      if budget > income_after_tax:
        print("Your budget is bigger than available income. Please enter a smaller budget.")

      # Add category and budget to the dictionary, subtract budget from discreionary income 
      else:
        categories[category] = budget
        # Remove budget from discretionary income
        income_after_tax -= budget
        if income_after_tax == 0:
            print("You have used all your budget.")
            break

  # Write the categories and budgets into the file.    
  for category, budget in categories.items():
    f.write(f"{category}: {budget}\n\n")


def edit_budget_category():
    """Allow users to edit already existing budgets"""
    # Ask user for what file they want to change
    file_edit = input("\nWhat file do you want to edit? ")
    # Check if the file exists
    if not os.path.isfile(file_edit):
        print("There is no file with that name.")
        return
    # Open the file for editing
    with open(file_edit, "r+") as f:
        # Print current contents of file
        contents = f.read()
        print(contents)
        # Ask user which category they want to edit
        category_exists = False
        while not category_exists:
            category_to_edit = input("Which category do you want to edit? ")
            # Find line number of category to edit
            f.seek(0)
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith(category_to_edit):
                    category_exists = True
                    category_line_number = i
                    category_name, category_value = line.strip().split(":")
                    break
            if not category_exists:
                print("Category does not exist in the budget.")

        # Ask user whether they want to change the category name or value.
        action = ""
        while action not in ["value", "name"]: 
            action = input("Do you want to change the name or value of the category? ").lower()
            if action not in ["value", "name"]:
                print("Invalid action. Please enter 'value' or 'name'.")
        # If user wants to change the value, prompt for new value and update.
        if action == "value":
            new_value = input("What is the new value for the category? ")
            category_value = new_value
        # If user wants to change the name, prompt for new name and update.
        elif action == "name":
            new_name = input("What is the new name for the category? ")
            category_name = new_name

        # Make the new line for the category and update the list of lines in the file.
        new_line = category_name + ":" + category_value + "\n"
        lines[category_line_number] = new_line

        # Write the updated lines to the files and truncate any remaining content.
        f.seek(0)
        f.writelines(lines)
        f.truncate()
        print("\nCategory updated successfully.")

      
# Welcome Message
print("""
Monthly Budget Program
----------------------\n
Actions:
Make a new budget (new)
Edit an existing budget (edit)
Quit the program (quit)
""")

# Ask users what they want to do
while True:
  user_action = input("\nPlease select an action: ").lower()
  if user_action == "new":
    create_budget_file()
  elif user_action == "edit":
    edit_budget_category()
  # Quit the program
  elif user_action == "quit":
    # Goodbye message
    print("Goodbye! Thanks for using the program.")
    break
  # Else user did not input a correct action
  else:
    # Prints please try again
    print("Please try again")
    