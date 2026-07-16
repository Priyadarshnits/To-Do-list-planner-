#TO create a to-do list where the tasks can be manipulated by the user
tasks=[]
#using loop to run continously
while True :
#adding the choices of the tasks
 print("your menu is ")#displaying menu
 print("1.add task")
 print("2.view tasks")
 print("3.remove tasks")
 print("4.exit ")
 choice=int(input("enter your choice:"))
#to check if a valid option is being selected
 if not 1<=choice<=4 :
     print("invalid choice")
#to know which option has been selected
 if choice==1 :
    print("you can add your tasks")
    task_input=input("choose yes or no (Y/n):")
    while task_input=='y' :
        in_take=input("enter your task to be added:")
        in_take=in_take.title()#to make the first letter into capital automatically
        tasks.append(in_take)#add task to empty list
        print("the entered tasks are.........\n")
        print(tasks)
        task_input=input("do you want to add another task (y/n):")
 elif choice==2 :
    print("you can view your tasks")
    #to view the given tasks
    if len(tasks)==0:
        print("no tasks available")# checking length to avoiding crash
    else:
     print("your tasks are:....")
     for value,task in enumerate(tasks):
        print(f"{value+1}.{task}")#displaying tasks with numbers
 elif choice==3 :
    print("you can remove the tasks")
    for value,task in enumerate(tasks):
        print(f"{value+1}.{task}")#displaying tasks with numbers
    number=int(input("enter the number of the task to be removed by looking into the displayed task:"))
    actual=number-1
    tasks.pop(actual)#remove the tasks listed by user
    print("task removed sucessfully!!!!")
    print("the updated tasks is:",tasks)
    #to exit the to do list
 elif choice==4 :
    print("you are exiting now")
    print("thank you...")
    break # exit the loop

          
