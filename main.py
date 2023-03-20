"""
JHC Internal
Fahim Firdaus
2.7 and 2.8 - 12 credits
"""
import os

#Functions
def disposable_income(income):
  if income_before_tax <= 14000:
    tax = 0.105 * income_before_tax
  elif income_before_tax <= 48000:
    tax = 0.175 * (income_before_tax - 14000) + 1470
  elif income_before_tax <= 70000:
    tax = 0.3 * (income_before_tax - 48000) + 7950
  elif income_before_tax <= 180000:
    tax = 0.33 * (income_before_tax - 70000) + 14850
  else:
    tax = 0.39 * (income_before_tax - 180000) + 48540

  income_after_tax = round(income_before_tax - tax, 2)

  print(f"Your income after tax is: {income_after_tax}")
  return income_after_tax


def is_valid_number(input_str):
  if input_str.isdigit() or (('.' in input_str)
                             and input_str.replace('.', '', 1).isdigit()):
    return True
  else:
    return False


def check_num(question):
  while True:
    user_input = input(question)
    if is_valid_number(user_input):
      return float(user_input)
    else:
      print("Please enter a valid number for budget")



# Welcome Message
print("""
Monthly Budget Program
----------------------\n
Actions:
1. Make a new budget (new)
2. Edit an existing budget (edit)
3. Quit the program (quit)
""")

# Ask users what they want to do
while True:
  user_action = input("\nPlease select an action: ").lower()

  # If user wants to make a new file
  if user_action == "new":
    # Ask user for name of file
    file_name = input("\nWhat would you like the file name to be? ")

    # Create file
    with open(file_name, "w") as f:
      f.write("Monthly Budget\n")
      f.write("--------------\n")
      # Ask user for income before tax
      while True:
        income_before_tax = input("Enter your income before tax $: ")
        if is_valid_number(income_before_tax):
          income_before_tax = float(income_before_tax)
          break
        else:
          print("Please enter a valid number for income.")

      # Call disposable_income function with income_before_tax as argument
      income_after_tax = disposable_income(income_before_tax)

      # While disposable income is greater than zero loop+
      categories = {}
      while income_after_tax > 0:
        # Ask users to add categories and budget
        category = input("Add a category: ")
        if category == "stop":
          break
        else:
          budget = check_num("Add a budget: ")
          if budget > income_after_tax:
            print("Your budget is bigger than available income. Please enter a smaller budget.")
          else:
            categories[category] = budget
          # Remove budget from discretionary income
            income_after_tax -= budget
            if income_after_tax == 0:
              print("You have used all your budget.")
              break

      
      for category, budget in categories.items():
        f.write(f"{category}: {budget}\n\n")

  # Elif user wants to access a previous file
  elif user_action == "edit":
    # Ask user for what file they want to change
    file_edit = input("What file do you want to edit? ")
    if not os.path.isfile(file_edit):
      print("There is no file with that name.")
      continue
    # Open file for editing
    with open(file_edit, "r+") as f:
      # Print current contents of file
      contents = f.read()
      print(contents)
      # Ask user which category they want to edit
      category_to_edit = input("Which category do you want to edit? ")
      # Find line number of category to edit
      f.seek(0)
      lines = f.readlines()
      category_exists = False
      for i, line in enumerate(lines):
          if line.startswith(category_to_edit):
              category_exists = True
              category_line_number = i
              category_name, category_value = line.strip().split(":")
              break
      if not category_exists:
        print("Category does not exist in the budget.")
      
      action = input("Do you want to change the name or value of the category? ").lower()

      if action == "value":
        new_value = input("What is the new value for the category? ")
        category_value = new_value

      elif action == "name":
        new_name = input("What is the new name for the category? ")
        category_name = new_name

      new_line = category_name + ":" + category_value + "\n"
      lines[category_line_number] = new_line

      f.seek(0)
      f.writelines(lines)
      f.truncate()
      print("Category updated successfully.")
  
  # Quit the program
  elif user_action == "quit":
    # Goodbye message
    print("Goodbye! Thanks for using the program.")
    break

  # Else user did not input a correct action
  else:
    # Prints please try again
    print("Please try again")


