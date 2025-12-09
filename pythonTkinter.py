                                 # 1st creating the tkinter module

# def greet(a,b):
#     print("Hello ",a)
#     print("how can i help you",b)
    

# greet("Ahmed","arbaz")
# greet("ali","junaid")



# import tkinter as tk

# root = tk.Tk()
# root.title("My First Tkinter App")
# root.geometry("300x200")
# root.resizable(False,False)



# root.mainloop()




                                    # 2nd creating a label widget

# import tkinter as tk

# root = tk.Tk()

# root.title("Label Example")

# root.geometry("300x200")

# label = tk.Label(root, text="Hello, Tkinter!",font='26',background='red',foreground='white')

# label.pack(pady=20)
# root.mainloop()



#                                  # 3rd creating a Input Box

# import tkinter as tk

# def show_name():
#     name = entry.get()        # input value
#     label.config(text="Hello " + name)

# root = tk.Tk()
# root.geometry("400x300")

# entry = tk.Entry(root)
# entry.pack()

# btn = tk.Button(root, text="Show", command=show_name)
# btn.pack()

# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()




#                                 # 4th creating a Button Widget

# import tkinter as tk
# def on_button_click():
#     label.config(text="Button Clicked!")

# root = tk.Tk()
# root.title("Button Example")
# root.geometry("300x200")

# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack(pady=20)

# label = tk.Label(root, text="")
# label.pack()

# root.mainloop()





#                               # 5th creating a Number Display using loops
import tkinter as tk

def show_numbers():
    nums = ""
    for i in range(1, 6):
        nums += str(i) + " "
    label.config(text=nums)

root = tk.Tk()
root.geometry("500x500")

btn = tk.Button(root, text="Show 1-5", command=show_numbers)
btn.pack(pady="50")

label = tk.Label(root, text="", font="60", bg='black',fg="white")

label.pack(pady="50")

root.mainloop()






                                    # creating a simple Calculator

# import tkinter as tk
# def calculate():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         operation = operation_var.get()

#         if operation == "Add":
#             result = num1 + num2
#         elif operation == "Subtract":
#             result = num1 - num2
#         elif operation == "Multiply":
#             result = num1 * num2
#         elif operation == "Divide":
#             result = num1 / num2
#         else:
#             result = "Invalid Operation"

#         result_label.config(text="Result: " + str(result))
#     except ValueError:
#         result_label.config(text="Invalid Input")

# root = tk.Tk()
# root.title("Simple Calculator")

# entry1 = tk.Entry(root)
# entry1.pack(pady=5)

# entry2 = tk.Entry(root)
# entry2.pack(pady=5)

# operation_var = tk.StringVar(value="Add")
# operations = ["Add", "Subtract", "Multiply", "Divide"]

# operation_menu = tk.OptionMenu(root, operation_var, *operations)
# operation_menu.pack(pady=5)

# calc_button = tk.Button(root, text="Calculate", command=calculate)
# calc_button.pack(pady=10)

# result_label = tk.Label(root, text="Result: ")
# result_label.pack(pady=5)

# root.mainloop()