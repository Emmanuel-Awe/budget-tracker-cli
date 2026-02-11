import msvcrt
from pathlib import Path
import json
class ExpenseApp:
    
    
    # Creating the variables with initial values for the app
    def __init__(self):
        self.totalExpense = 0
        self.expenses = []

        self.initialBudget = 1000
        self.budget = self.initialBudget
        
        self.loadJsonFile() 

    def getFileDir(self):
        return(
            Path.home()
            / "OneDrive"
            / "Desktop"
            / "Documents"
            / "Data Analyst or Machine Learning"
            / "Personal"
            / "Python"
            / "Budget project 1"
        )


    def mainMenu(self):
        while True:
            print("\nWelcome to the Budget Tracker!")
            print(f"Your summary is calculated with a budget of {self.initialBudget}\n")
            print("A) To add an expense type 'add'\n")
            print("B) To delete an expense type 'delete'\n")
            print("C) To edit an expense type 'edit'\n")
            print("D) To edit your budget type 'budget'\n")
            print("E) To show a summary of your expenses and the remaing budget left 'summary'\n")
            print("f) To leave type 'done'\n")
        
            userChoice = input("\nWhat would you like to do today: ")
            userChoice = userChoice.lower()
        
            if userChoice == "add":
                self.addExpense()
            elif userChoice == "delete":
                self.deleteExpense()
            elif userChoice == "edit":
                self.editExpense()
            elif userChoice == "budget":
                self.editBudget()
            elif userChoice == "summary":
                self.showSummary()
            elif userChoice == "done":
                self.createTextFile()
                self.createJsonFile()
                break
            else:
                print("\nSorry the choice you have put in does not exist please try again :)")
            
    
    def calculateTotals(self):
        self.totalExpense = sum(e["Cost"] for e in self.expenses)
 
        
        self.budget = self.initialBudget - self.totalExpense  
    
    def addExpense(self):
        print("\nTo add an expense to your expense list simply type in the name, then type in the cost")
        
        while True:
            expenseName = input("\nEnter an expense name (or 'done' to finish): ").strip()
            if expenseName.strip().lower() != "done":
                while True:
                    try:
                        expense = int(input("Enter the cost: "))
                        self.expenses.append({"Expense Name": expenseName , "Cost" : expense})
                        
                        self.calculateTotals()
                        break
                
                    except ValueError:
                        print("Sorry only numbers or integers are accepted :)")
            elif expenseName.strip().lower() == "done":
                return
                       
            
    # We would continue with the mindset of deleting an expense
    # Function to delete an expense from the list
    def deleteExpense(self):
        
        #To iterate through all expenses and show the user
        if len(self.expenses) == 0:
            print("Sorry there is no expense to delete.")
            print("Press any key to return to the main menu.")
            self.waitForAnyKey()
        else:
            print("\nThese are all your recorded expenses and their costs:")
            for i in range(len(self.expenses)):
                print(f"{self.expenses[i]['Expense Name'].capitalize()} which cost {self.expenses[i]['Cost']}")
            # Code to allow the user pick what they would like to delete
            selectedExpense = ""
            while True:
                selectedExpense = input("\nWhat would you like to delete from the above expenses(Type one expense only or type done to go to main menu): ")
                cleanedInput = selectedExpense.strip().lower()
            
                if cleanedInput == "done":
                    break
            
                found = False
            
                for i in range(len(self.expenses)):
                    if cleanedInput == self.expenses[i]["Expense Name"].strip().lower():
                        print(f"{selectedExpense.capitalize()} has been deleted.")
                        self.expenses.pop(i)
                        self.calculateTotals()
                        print("\nThese are all your recorded expenses and their costs:")
                        if len(self.expenses) == 0:
                            print("Sorry there is no expense to delete.")
                            print("Press any key to return to the main menu.")
                            self.waitForAnyKey()
                            return
                        for i in range(len(self.expenses)):
                            print(f"{self.expenses[i]['Expense Name'].capitalize()} which cost {self.expenses[i]['Cost']}")
                        found = True
                        break
                
                if not found:
                    print("\nThe selected item is not in the expense list")
        
                   
    def editExpense(self):       
        while True:        
                #To iterate through all expenses and show the user
                print("\nThese are all your recorded expenses and their costs:")
                
                # Incase the user does not have expenses to show
                if len(self.expenses) == 0:
                    print("\nSorry no expenses have been entered")
                    print("Press any key to return to the main menu.")
                    self.waitForAnyKey()
                    return
                else:
                    for i in range(len(self.expenses)):
                        print(f"{self.expenses[i]['Expense Name'].capitalize()} which cost {self.expenses[i]['Cost']}")
                    selectedExpense = input("Which expense would you like to edit? (or type 'done' to go back): ")
                    cleanedInput = selectedExpense.strip().lower()
                    
                    # To leave the edit loop, go back to main menu
                    if cleanedInput == "done":
                        break
                    # Try to find the expense
                    found = False          
                
                
                    for i in range(len(self.expenses)):
                        if cleanedInput == self.expenses[i]["Expense Name"].strip().lower():
                            found = True
                            print(f"{self.expenses[i]['Expense Name'].capitalize()} has been allocated an expense of {self.expenses[i]['Cost']}")
                            
                            # To ask the user whether they would like to edit the Expense name or expense price
                            decision = input("\nIf you would like to edit the name type 'name'or if you would like to edit the price type 'price'?: ").lower().strip()
                            if decision == "name":
                                newExpenseName = input("\nType in the new expense name you would like: ").capitalize().strip()
                                self.expenses[i]["Expense Name"]= newExpenseName.capitalize() 
                                print(f"{selectedExpense.capitalize()} has been updated to {self.expenses[i]['Expense Name']}.")
                            
                            elif decision == "price":
                                while True:
                                    try:
                                        newExpensePrice = int(input("\nType in the new expense price you would like: "))
                                        self.expenses[i]["Cost"] = newExpensePrice
                                        self.calculateTotals()
                                        print(f"{selectedExpense.capitalize()} has been updated with a new price of {self.expenses[i]["Cost"]}.")
                                        break
                                    except ValueError:
                                        print("Sorry only whole numbers are accepted please try again")
                        

                            else: 
                                print("Sorry you have typed in the wrong input try again") 
                            break
                    if not found:
                        print("\nThe selected item is not in the expense list.")
                                            
     
    def editBudget(self):
        print(f"\nYour Initial budget was: {self.initialBudget}")
        print(f"Your current budget is: {self.budget}")
        
        while True:
            print("\nWould you like to change your Initial budget or return to the Main Menu")
            decision = input("Type 'menu' to return to menu and 'budget' to change budget: ")
            decision = decision.lower().strip()
            
            if decision == "budget":
                while True:
                    try:
                        newBudget = int(input("\nWhat new budget would you like: "))
                        self.initialBudget = newBudget 
                        self.calculateTotals()
                        print(f"Your new initial budget is: {self.initialBudget}")
                        break
                    except ValueError:
                        print("Sorry only whole numbers are accepted please try again")
         
                
            elif decision == "menu":
                break
            else:
                print("\nSorry you have put in an incorrect input please try again :)")
                
    def waitForAnyKey(self):
        print("\nPress any key to return to the main menu :)")
        msvcrt.getch()
        return
        
    def showSummary(self):    
        self.calculateTotals()
        print(f"\nYour Initial budget was: {self.initialBudget}")
        print(f"Your current budget is: {self.budget}")
        print("\nThese are all your recorded expenses and their costs:")  
        
        # Incase the user does not have expenses to show
        if len(self.expenses) == 0:
            print("\nYou have no expenses lucky you :)")
        else:
            for i in range(len(self.expenses)):
                print(f"{self.expenses[i]['Expense Name'].capitalize()} which cost {self.expenses[i]['Cost']}") 
                
        print("\n===== Budget Summary =====")
        print(f"Budget:        {self.initialBudget}")
        print(f"Total expense: {self.totalExpense}")
        if self.budget < 0:
            print(f"Remaining:     {abs(self.budget)} over your budget")
        else:
            print(f"Remaining:     {self.budget}")    
        
        self.waitForAnyKey()  
        return  
    
    def createTextFile(self):
        self.calculateTotals()
        
        file_Dir = self.getFileDir()
        
        file_Dir.mkdir(exist_ok=True)
        file = file_Dir / "Receipt.txt"
        
        with open(file, "w", encoding= "utf-8") as r:
            r.write(f"Your Initial budget was: {self.initialBudget}")
            r.write(f"\nYour current budget is: {self.budget}\n")
            r.write("\nThese are all your recorded expenses and their costs:")  
        
            # Incase the user does not have expenses to show
            if len(self.expenses) == 0:
                r.write("\nYou have no expenses lucky you :)")
            else:
                for i in range(len(self.expenses)):
                    r.write(f"\n{self.expenses[i]['Expense Name'].capitalize()} which cost {self.expenses[i]['Cost']}") 
                    
            r.write("\n\n===== Budget Summary =====")
            r.write(f"\nBudget:        {self.initialBudget}")
            r.write(f"\nTotal expense: {self.totalExpense}")
            if self.budget < 0:
                r.write(f"\nRemaining:     {abs(self.budget)} over your budget")
            else:
                r.write(f"\nRemaining:     {self.budget}")
                
    def createJsonFile(self):
        self.calculateTotals()
        
        file_Dir = self.getFileDir()
        file_Dir.mkdir(exist_ok=True)
        file = file_Dir / "Receipt.json"
        
        data = {
            "initial_budget" : self.initialBudget,
            "current_budget" : self.budget,
            "expenses" : []
        }
        
        for expense in self.expenses:
            data["expenses"].append({
                "name" : expense["Expense Name"],
                "cost" : expense["Cost"]
            })
            
        try:         
            with open(file, "w", encoding= "utf-8") as j:
                json.dump(data, j, indent=4)
        
        except PermissionError:
            print("⚠️ Could not save Receipt.json (file may be open elsewhere).")

    def loadJsonFile(self):
        file_Dir = self.getFileDir()
        file = file_Dir / "Receipt.json"
        
         # First run: nothing to load
        if not file.exists():
            return

        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Restore core state
            self.initialBudget = data.get("initial_budget", self.initialBudget)
            self.budget = data.get("current_budget", self.budget)

            # Restore expenses safely
            self.expenses = []
            for expense in data.get("expenses", []):
                if "name" in expense and "cost" in expense:
                    self.expenses.append({
                        "Expense Name": expense["name"],
                        "Cost": expense["cost"]
                    })

            self.calculateTotals()

        except json.JSONDecodeError:
            print("⚠️ Saved JSON is corrupted. Starting with empty data.")
        except PermissionError:
            print("⚠️ Permission error: could not read Receipt.json.")
            
        
        
    
app = ExpenseApp()
app.mainMenu()