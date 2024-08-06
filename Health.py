class Health():

    def __init__(self):
        self.logs = []
        self.goals = {
            "Calories": None,
            "Exercise_min": None,
            "Water_liter": None
        }

    def set_goals(self):
        print("============================================================================")
        print("\nSet your fitness goals: ")
        self.goals["Calories"] = int(input("Enter daily calorie goal: "))
        self.goals["Exercise_min"] = int(input("Enter daily exercise goal (in minutes): "))
        self.goals["Water_liter"] = float(input("Enter daily water intake goal (in liters): "))
        print("Goals set\n")
        print("============================================================================")

    def log_entry(self):
        print("============================================================================")
        date = input("Enter the date (YYYY-MM-DD): ")
        calories = int(input("Enter calories consumed: "))
        exercise_min = int(input("Enter minutes of exercise: "))
        water_liter = float(input("Enter liters of water consumed: "))
        print("============================================================================")

        entry = {
            "Date": date,
            "Calories": calories,
            "Exercise_min": exercise_min,
            "Water_liter": water_liter
        }
        self.logs.append(entry)
        print("Entry Added\n")

    def display(self):
        if not self.logs:
            print("No logs available")
            return
        else:
            print("Health and Fitness Display")
            for log in self.logs:
                print("============================================================================")
                print(f"Date: {log['Date']}")
                print(f"Calories consumed: {log['Calories']} / {self.goals['Calories']} (goal)")
                print(f"Exercise Minutes: {log['Exercise_min']} / {self.goals['Exercise_min']} (goal)")
                print(f"Water Liters: {log['Water_liter']} / {self.goals['Water_liter']} (goal)")
                print("============================================================================")
                
    def start(self):
        while True:
            print("============================================================================")
            print("\nHealth & Fitness")
            print("1. Set Goals")
            print("2. Log Today's entry")
            print("3. Display")
            print("4. Exit")
            print("============================================================================")

            try:
                choice = int(input("Enter: "))
                if choice == 1:
                    self.set_goals()
                elif choice == 2:
                    self.log_entry()
                elif choice == 3:
                    self.display()
                elif choice == 4:
                    print("Exiting Program")
                    break
                else:
                    print("Invalid choice, please select a valid option.")
            except ValueError:
                print("\nPlease enter a number from 1 to 4.")

if __name__ == "__main__":
    x = Health()
    x.start()



            
        
