import os,time,random
from print_color import print_in_color

print_in_color("ToDo List Management System", 'red')
print()
print()

toDoList=[]
fileExists=False

try: 
  f=open("tasks.todo","r")
  toDoList=eval(f.read())
  f.close()
except: 
  fileExists=True

def prettyPrint():
  print()
  for row in toDoList:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

def add():
  toDoTask=[]
  print("ADD")
  print()
  task=input("What's the task? ")
  date=input("When is it? ")
  priority=input("Select priority (High, Medium, Low): ").lower().strip()
  toDoTask.append(task)
  toDoTask.append(date)
  toDoTask.append(priority)
  toDoList.append(toDoTask)

priority_map = {
  "high": 1,
  "medium": 2,
  "low": 3
}
        
def viewall():
  sorted_task=sorted(toDoList, key=lambda task: priority_map.get(task[2]))
  print()
  for row in sorted_task:
    for j in row:
      print(f"{j:^9}", end=" | ")
    print()
    print("--------------------------------------")


def priorityHigh():
  print()
  for row in toDoList:
    if "high" in row:
      for j in row:
        print(f"{j:^9}", end=" | ")
      print()
      print("--------------------------------------")
    else:
      continue

def priorityLow():
  print()
  for row in toDoList:
    if "low" in row:
      for j in row:
        print(f"{j:^9}", end=" | ")
      print()
      print("--------------------------------------")
    else:
      continue

def priorityMedium():
  print()
  for row in toDoList:
    if "medium" in row:
      for j in row:
        print(f"{j:^9}", end=" | ")
      print()
      print("--------------------------------------")
    else:
      continue

def removeFromList(item):
  for ele in toDoList:
    if item in ele:
      ele.remove(item)
      print_in_color(f"{item} was removed from the list!\n", "yellow")
    elif item not in ele:
      print_in_color(f"{item} was not in the list.\n", "cyan")  

while True:
  action=input("What do you want to do? Add, view, remove, edit?[a/v/r/e] ")
  print()
  print_in_color("","green")
  time.sleep(3)
  os.system('clear')

  if action=="a":
    add()
  
  elif action =="v":
    print("VIEW")
    print()
    menu= input("Press 1 for view all. Press 2 for view by priority.")
    if menu=="1": 
      viewall()

    if menu=="2":
      priority_select=input("Which priority? ").lower().strip()
      if priority_select[0] == "h":
        priorityHigh()
      elif priority_select[0] =="l":
        priorityLow()
      elif priority_select[0] =="m":
        priorityMedium()
        
  elif action=="r":
    task_remove = input("Which tak you want to remove? ")
    removeFromList(task_remove)

  if fileExists:
    os.mkdir("backups")
    name=f"backup{random.randint(1,1000000000)}.txt"
    os.popen(f"cp tasks.todo backups/{name}")
  
  f=open("tasks.todo","w")
  f.write(str(toDoList))
  f.close()
  
  time.sleep(2)
  os.system('clear')