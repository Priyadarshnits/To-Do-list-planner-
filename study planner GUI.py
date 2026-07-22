import tkinter as tk

window = tk.Tk()

window.title("Study Planner")
window.geometry("500x400")
heading=tk.Label(
    window,text="Study Planner",
    font=("Times New Roman",20,"bold","italic")
    )
heading.pack(pady=20)
task_label=tk.Label(
    window,
    text="Enter your tasks:",
    font=("Arial",12)
    )

task_label.pack(pady=25)

task_entry=tk.Entry(
    window,
    width=35)
task_entry.pack(pady=5)

def add_task(event=None):
    task=task_entry.get().title()
    task_list.insert(tk.END,task)
    with open("tasks.txt","a")as file:
        file.write(task+"\n")
    task_entry.delete(0,tk.END)
    
task_entry.bind("<Return>",add_task)

add_button=tk.Button(
    window,
    text="Add task",
    command=add_task
    )
add_button.pack(pady=10)

tk.Label(window,text="To-do Task").pack()

task_list=tk.Listbox(
    window,
    width=40,
    height=10)
task_list.pack(pady=10)

def complete_task(event=None):
    selected=task_list.curselection()
    if selected:
        index=selected[0]
        task=task_list.get(index)
        if not task.startswith("\u2713 "):
            completed_list.insert(tk.END,"\u2713 "+ task)
            task_list.delete(index)
    with open("tasks.txt","w",encoding="utf-8")as file:
        for task in task_list.get(0,tk.END):
            file.write(task+"\n")

    with open("completed.txt","w",encoding="utf-8")as file:
        for task in completed_list.get(0,tk.END):
            file.write(task+"\n")
task_list.bind("<Right>",complete_task)

complete_button=tk.Button(window,
                text="\u2713 ""compeleted task",
                command=complete_task)
complete_button.pack(pady=5)

def remove_task(event=None):
    selected=task_list.curselection()

    if selected:
        task_list.delete(selected[0])
        with open("tasks.txt","w")as file:
            for task in task_list.get(0,tk.END):
                file.write(task +"\n")
task_list.bind("<Delete>",remove_task)


        
remove_button=tk.Button(
    window,
    text="Remove task",
    command=remove_task
    )
remove_button.pack(pady=10)


tk.Label(window,text="Completed Task").pack()

completed_list=tk.Listbox(
    window,
    width=40,
    height=10)
completed_list.pack(pady=10)

try:
    with open("completed.txt","r",encoding="utf-8")as file:
        for line in file:
            completed_list.insert(tk.END,line.strip())
except FileNotFoundError:
    pass

with open("tasks.txt","r")as file:
    for line in file:
        task_list.insert(tk.END,line.strip())

        
def undo_task(event=None):
    selected=completed_list.curselection()
    if selected:
        index=selected[0]
        task=completed_list.get(index)
        task=task.replace("\u2713","")
        task_list.insert(tk.END,task)
        completed_list.delete(index)
        with open("tasks.txt","w") as file:
             for task in task_list.get(0,tk.END):
              file.write(task+"\n")
        with open("completed.txt","w",encoding="utf-8")as file:
            for task in completed_list.get(0,tk.END):
                file.write(task +"\n")
                  
            
completed_list.bind("<Left>",undo_task)

undo_button=tk.Button(window,
                      text="Undo completed task",
                      command=undo_task
                      )
undo_button.pack(pady=10)

window.mainloop()

