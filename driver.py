import datetime
from task import Task
from todolinkedlist import LinkedList

def main():
    due_dates=[
        datetime.datetime(2025, 10, 5),  
        datetime.datetime(2025, 10, 9),
        datetime.datetime(2025, 10, 15),
        datetime.datetime(2025, 10, 20),
        datetime.datetime(2025, 10, 31),
        datetime.datetime(2025, 11, 2),
        datetime.datetime(2025, 11, 8),
        datetime.datetime(2025, 11, 12),
        datetime.datetime(2025, 11, 13),
        datetime.datetime(2025, 12, 8)
    ]
    #self, id: int, description: str, post_date: datetime.datetime, completed: bool, priority: int=10)
    tasks = [
        Task(i + 1, f"Task #{i +1}", due_dates[i], False, (i%10)+1)
        for i in range (10)
    ]

    task_list = LinkedList()
    for t in tasks:
        task_list.add_to_back(t)

    print("All tasks")
    print(task_list)

    # Update task list with correct priority
    print("Changing priority")
    current = task_list.head
    while current is not None:
        current.data.update_priority()  # call Task’s method directly
        current = current.next
    print(task_list)

    # Only include tasks with high priority
    print("Conditional String: Show Tasks with High Priority")
    lam = lambda n: n.data.priority<=5
    print(task_list.conditional_str(lam))

    #new list with only urgent (priority=1) tasks
    print("\n--- FILTER (PRIORITY == 1) ---")
    urgent = task_list.filter(lambda n: n.data.priority == 1)
    if urgent:    
        print(urgent)
    else:
        print("No urgent tasks found")
if __name__=="__main__":
    main()