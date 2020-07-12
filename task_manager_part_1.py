# Task 20: Task Manager 
# Part 1

# Boolean
login_success = False

# User input
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# Reads through the user text file for matches in username and password
with open("user.txt", "r+") as file:
    while login_success == False:
        for line in file:
            split_line = line.split(",")
            user_check = split_line[0].strip()
            pass_check = split_line[1].strip()
            if username == user_check and password == pass_check:
                print("User logged in successfully")
                login_success = True

        file.seek(0)
        
# If incorrect credentials request correct credentials
        if not login_success:
            print("Incorrect credentials.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

# If username and password is correct, display the menu selection
while True:
    print("\nPlease select of the following options: ")
    print("r - register user") 
    print("a - add task") 
    print("va - view all tasks") 
    print("vm - view my tasks") 
    print("e - exit")
    menu_choice = input("What would you like to do: ").lower()
                    

# If 'r' is chosen, register a new user, ask for a new password and username  
# Confirm the password and write the information to the user.txt file
    if menu_choice == "r":
        print("Register New User")
        new_user = input("Please input the new user name: ")
        file = open("user.txt", "r+")
        
        duplicate_found = False
        for line in file:
            split_line = line.split(",")
            user_check = split_line[0].strip()
            if new_user == user_check:
                print("That user name has already been taken")
                duplicate_found = True
                                    
# Checks passwords and confirms
        new_password = input("Please input your password for the new user: ")
        if new_password == input("Confirm password: "):
            file.write("\n" + new_user + ", ")
            file.write(new_password)
            file.close()
            print("New user and password added")  
        else:
            print("Password doesn't match.")


# If 'a' is chosen, ask for the username of the person who the task will be assigned to, title, description and due date of task
# Write new information to task_file
    if menu_choice == "a":
        print("Add A New Task")
        with open("user.txt") as fin:
            assigned_person = input("Who is the task assigned to: ")
            task_title = input("What is the title of task: ")
            task_detail = input("What is the details of the task: ")
            date_assigned = input("Please input today's date: ")
            task_due = input("Please input the task deadline: ")
            task_complete = input("Is the task completed? (Yes or No): ")
            with open("tasks.txt", "a") as task1:
                task1.write("\n" + assigned_person + ", " + task_title + ", " + task_detail + ", " + date_assigned + ", " + task_due + ", " + task_complete)
                print("New task added")


# If "va" is chosen, print all tasks formatted
    if menu_choice == "va":
        file = open("tasks.txt", "r+")
        for line in file:
         task = line.split(",")
         print("\nTask manager: " + task[0] + "\n" + "Task title: " + task[1] + "\n" + "Task details: " + task[2] + "\n" + "Date assigned: " + task[3] + "\n" + "Deadline: " + task[4] + "\n" + "Complete(Yes or No): " + task[5])

                    
# If "vm" is chosen, print tasks specific to the logged in user
    if menu_choice == "vm":
        task_count = 0
        file = open("tasks.txt", "r+")
        print("")
        for line in file:
            task = line.split(", ")
            if task[0] == username:
              task_count+=1
              print("\nTask manager: " + task[0] + "\n" + "Task title: " + task[1] + "\n" + "Task details: " + task[2] + "\n" + "Date assigned: " + task[3] + "\n" + "Deadline: " + task[4] + "\n" + "Complete(Yes or No): " + task[5])

                            
# If "e" is chosen, exit the program
    if menu_choice == "e":
        break
            
