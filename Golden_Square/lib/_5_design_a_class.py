# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.



## Todo class

    # add_task function
        # return list of updated tasks
    
    # mark_task_complete

    # get_tasks  -  Remove tasks from list if complete 

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})

    def mark_task_complete(self, task):
        for item in self.tasks:
            if item["task"] == task:
                item["complete"] = True

    def get_tasks(self):
        return [item["task"] for item in self.tasks if not item["complete"]]





todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Clean the house")
todo_list.add_task("Finish report")

print("Tasks before marking as complete:")
print(todo_list.get_tasks())

todo_list.mark_task_complete("Clean the house")

print("Tasks after marking 'Clean the house' as complete:")
print(todo_list.get_tasks())