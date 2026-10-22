# button
# import tkinter as tk

# root = tk.Tk()
# root.title("Button Example")

# def click():
#     label.config(text="Button Clicked!")

# button = tk.Button(root, text="Click Me", command=click)
# button.pack(pady=10)

# label = tk.Label(root, text="Welcome")
# label.pack()

# root.mainloop()


# canvas
# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Example")

# canvas = tk.Canvas(root, width=300, height=200, bg="white")
# canvas.pack()

# canvas.create_rectangle(20, 20, 100, 100, fill="blue")
# canvas.create_oval(130, 20, 220, 100, fill="green")
# canvas.create_line(20, 150, 250, 150, fill="red", width=3)

# root.mainloop()


# checkbutton
# import tkinter as tk

# root = tk.Tk()
# root.title("Checkbutton Example")

# var = tk.IntVar()

# check = tk.Checkbutton(root, text="I like Python", variable=var)
# check.pack(pady=10)

# def show():
#     label.config(text="Selected" if var.get() else "Not Selected")

# tk.Button(root, text="Check", command=show).pack()
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# entry
# import tkinter as tk

# root = tk.Tk()
# root.title("Entry Example")

# tk.Label(root, text="Enter your name:").pack()

# entry = tk.Entry(root)
# entry.pack(pady=5)

# def show():
#     label.config(text="Hello " + entry.get())

# tk.Button(root, text="Submit", command=show).pack()
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# frame
# import tkinter as tk

# root = tk.Tk()
# root.title("Frame Example")

# frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
# frame.pack(padx=20, pady=20)

# tk.Label(frame, text="Inside Frame", bg="lightblue").pack()
# tk.Button(frame, text="Click Me").pack(pady=5)

# root.mainloop()


# label
# import tkinter as tk

# root = tk.Tk()
# root.title("Label Example")

# label = tk.Label(
#     root,
#     text="Welcome to Tkinter!",
#     font=("Arial", 18),
#     fg="blue"
# )
# label.pack(pady=20)

# root.mainloop()


# listbox
# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox Example")

# listbox = tk.Listbox(root)

# for item in ["Python", "Java", "C++", "JavaScript"]:
#     listbox.insert(tk.END, item)

# listbox.pack(pady=10)

# def show():
#     selected = listbox.curselection()
#     if selected:
#         label.config(text=listbox.get(selected[0]))

# tk.Button(root, text="Show Selection", command=show).pack()
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# menubar
# import tkinter as tk

# root = tk.Tk()
# root.title("Menubutton Example")

# menubutton = tk.Menubutton(root, text="Select Option", relief="raised")

# menu = tk.Menu(menubutton, tearoff=0)
# menu.add_command(label="Python")
# menu.add_command(label="Java")

# menubutton.config(menu=menu)
# menubutton.pack(pady=20)

# root.mainloop()


# # menu
# import tkinter as tk

# root = tk.Tk()
# root.title("Menu Example")

# menubar = tk.Menu(root)

# filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.destroy)

# menubar.add_cascade(label="File", menu=filemenu)
# root.config(menu=menubar)

# root.mainloop()


# message
# import tkinter as tk

# root = tk.Tk()
# root.title("Message Example")

# message = tk.Message(
#     root,
#     text="Welcome to Python Tkinter. This is a Message widget.",
#     width=250,
#     bg="lightyellow"
# )
# message.pack(padx=20, pady=20)

# root.mainloop()


# radiobutton
# import tkinter as tk

# root = tk.Tk()
# root.title("Radiobutton Example")

# var = tk.StringVar(value="Python")

# tk.Radiobutton(
#     root, text="Python", variable=var, value="Python"
# ).pack()

# tk.Radiobutton(
#     root, text="Java", variable=var, value="Java"
# ).pack()

# tk.Radiobutton(
#     root, text="C++", variable=var, value="C++"
# ).pack()

# def show():
#     label.config(text="Selected: " + var.get())

# tk.Button(root, text="Submit", command=show).pack(pady=5)
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# # radiobutton
# import tkinter as tk

# root = tk.Tk()
# root.title("Radiobutton Example")

# var = tk.StringVar(value="Python")

# tk.Radiobutton(
#     root, text="Python", variable=var, value="Python"
# ).pack()

# tk.Radiobutton(
#     root, text="Java", variable=var, value="Java"
# ).pack()

# tk.Radiobutton(
#     root, text="C++", variable=var, value="C++"
# ).pack()

# def show():
#     label.config(text="Selected: " + var.get())

# tk.Button(root, text="Submit", command=show).pack(pady=5)
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# scale 
# import tkinter as tk

# root = tk.Tk()
# root.title("Horizontal Scale")

# scale = tk.Scale(
#     root,
#     from_=0,
#     to=100,
#     orient=tk.HORIZONTAL
# )
# scale.pack(pady=10)

# def show():
#     label.config(text="Value: " + str(scale.get()))

# tk.Button(root, text="Show Value", command=show).pack()
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# scale vertical
# import tkinter as tk

# root = tk.Tk()
# root.title("Vertical Scale")

# scale = tk.Scale(
#     root,
#     from_=0,
#     to=100,
#     orient=tk.VERTICAL
# )
# scale.pack(pady=10)

# def show():
#     label.config(text="Value: " + str(scale.get()))

# tk.Button(root, text="Show Value", command=show).pack()
# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()


# scrollbar
# import tkinter as tk

# root = tk.Tk()
# root.title("Scrollbar Example")

# scrollbar = tk.Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)

# for i in range(1, 31):
#     listbox.insert(tk.END, "Item " + str(i))

# listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# scrollbar.config(command=listbox.yview)

# root.mainloop()


# text
# import tkinter as tk

# root = tk.Tk()
# root.title("Text Example")

# text = tk.Text(root, height=5, width=30)
# text.pack(pady=10)

# def show_text():
#     result.config(text=text.get("1.0", tk.END))

# tk.Button(root, text="Show Text", command=show_text).pack()

# result = tk.Label(root, text="")
# result.pack()

# root.mainloop()


# toplevel
# import tkinter as tk

# root = tk.Tk()
# root.title("Main Window")

# def open_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Second Window")
#     new_window.geometry("250x150")

#     tk.Label(
#         new_window, text="This is a new window"
#     ).pack(pady=30)

# tk.Button(
#     root, text="Open New Window", command=open_window
# ).pack(pady=30)

# root.mainloop()


# spinbox
# import tkinter as tk

# root = tk.Tk()
# root.title("Main Window")

# def open_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Second Window")
#     new_window.geometry("250x150")

#     tk.Label(
#         new_window, text="This is a new window"
#     ).pack(pady=30)

# tk.Button(
#     root, text="Open New Window", command=open_window
# ).pack(pady=30)

# root.mainloop()


# panedwindow
# import tkinter as tk

# root = tk.Tk()
# root.title("PanedWindow Example")
# root.geometry("400x200")

# paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
# paned.pack(fill=tk.BOTH, expand=True)

# left = tk.Label(paned, text="Left Panel", bg="lightblue")
# right = tk.Label(paned, text="Right Panel", bg="lightgreen")

# paned.add(left)
# paned.add(right)

# root.mainloop()


# labelframe
# import tkinter as tk

# root = tk.Tk()
# root.title("LabelFrame Example")

# frame = tk.LabelFrame(
#     root, text="Student Details", padx=10, pady=10
# )
# frame.pack(padx=20, pady=20)

# tk.Label(frame, text="Name:").pack()

# tk.Entry(frame).pack(pady=5)

# tk.Button(frame, text="Submit").pack()

# root.mainloop()


# # message row
# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("MessageBox Example")

# def show_message():
#     messagebox.showinfo("Information", "Welcome to Tkinter!")

# tk.Button(
#     root, text="Show Message", command=show_message
# ).pack(pady=30)

# root.mainloop()