task = input("Enter your task: ") 
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Try to complete it soon.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that should be addressed today.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider doing it when convenient.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that you may want to finish today.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

    case _:
        print("Reminder: Invalid priority entered. Please use high, medium, or low.")
