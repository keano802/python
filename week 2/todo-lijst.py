def to_do_list():
   tasks = []

   while True:
      print("\nTo-Do List:")
      print("1. View tasks")
      print("2. Add a task")
      print("3. Remove a task")
      print("4. Exit")

      choice = input("Enter your choice: ").strip()

      if choice == "1":
         if tasks:
            print("\nTasks:")
            for i, t in enumerate(tasks, 1):
               print(f"{i}. {t}")
         else:
            print("No tasks in the list.")

      elif choice == "2":
         task = input("Enter a task to add: ").strip()
         if task:
            tasks.append(task)
            print(f"Task '{task}' added to the list.")
         else:
            print("No task entered.")

      elif choice == "3":
         task_num = int(input("Enter the task number to remove: "))
         if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
         else:
            print("Invalid task number.")

      elif choice == "4":
         print("Exiting the program.")
         break

      else:
         print("Invalid choice. Please try again.")

to_do_list()