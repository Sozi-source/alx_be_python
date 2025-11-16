task = input("Enter your task: ") 
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Try to complete it soon."
    
    case "medium":
        reminder = f"Reminder: {task} is a {priority} priority task"
        if time_bound == "yes":
            reminder += " that should be addressed today."
        else:
            reminder += ". Consider doing it when convenient."
    
    case "low":
        reminder = f"Note: '{task}' is a {priority} priority task"
        if time_bound == "no":
            reminder += " that you may want to finish today"
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low"

print(reminder)
