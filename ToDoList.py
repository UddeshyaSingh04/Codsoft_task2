import tkinter as tk

class TodoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_entry = tk.Entry(root, width=30, font=('Arial', 14)) 
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Arial', 12, 'bold'))
        self.add_button.pack()

        self.task_list = tk.Listbox(root, width=50, height=10, font=('Arial', 12))
        self.task_list.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:  
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="light blue")
root.geometry("300x400")

todo_list = TodoList(root)
root.mainloop()
