import json

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

    income_after_tax = income_before_tax - tax

    print(f"Your income after tax is: {income_after_tax}")
    return income_after_tax


def is_valid_income(input_str):
    if input_str.isdigit() or (('.' in input_str) and input_str.replace('.', '', 1).isdigit()):
        return True
    else:
        return False

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
                if is_valid_income(income_before_tax):
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
                    budget = int(input("Add a budget: "))
                    categories[category] = budget
                    
                    # Remove budget from discretionary income
                    income_after_tax -= budget
        
            for category, budget in categories.items():
              f.write(f"{category}: {budget}\n\n")
            
    # Elif user wants to access a previous file
    elif user_action == "edit":
        print("picked edit")  # testing purposes
        
        # Ask user for what file they want to change

        # Change category or budget
        
    # Quit the program
    elif user_action == "quit":
        # Goodbye message
        print("Goodbye! Thanks for using the program.")
        break
        
    # Else user did not input a correct action
    else:
        # Prints please try again
        print("Please try again")
