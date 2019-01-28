# A user is presented with the text below. the program allows them to select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.



def main():
    problem1()



def getList():
    print("Congratulations! You're running Superman's Task List program")
    print("What would you like to do?")
    print("1. List all tasks.")
    print("2. Add a task to the list")
    print("3. Delete a Task")
    print("0. To quit to the program")

toDo = []





def problem1():

    UserInput = ""

    while (UserInput != "0"):
        getList()
        UserInput = input("What would you like to do")

        # prints items in array
        if (UserInput == "1"):
            for itemsinarray in toDo:
                print(toDo)
            UserInput = input("What would you like to do?")
        # adds task
        elif (UserInput == "2"):
            addTask = input("Add a task")
            toDo.append(addTask)
            UserInput = input("What would you like to do?")
            #removes a task
        elif (UserInput == "3"):
            removeTask = input("Delete a Task")
            toDo.remove(removeTask)
            UserInput = input("What would you like to do")

            print(toDo[0])

        elif (UserInput == 0):
            break

if __name__ == '__main__':
    main()
