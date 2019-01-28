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
UserInput = input("What would you like to do")




def problem1():
    while (UserInput != "q"):

        getList()
        if (UserInput == "1"):
            for itemsinarray in toDo:
                print(itemsinarray)
            UserInput = input("What would you like to do?")

        elif (UserInput == "2"):
            addTask = input("Add a task")
            toDo.append(addTask)
            UserInput = input("What would you like to do?")

        elif (UserInput == "3"):
            removeTask = input("Delete a Task")
            toDo.remove(removeTask)
            UserInput = input("What would you like to do")

            print(toDo[0])

        elif (UserInput == 0):
            break

if __name__ == '__main__':
    main()
