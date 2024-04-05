import tkinter as tk

def perform_operation():
    number1 = float(entry_num1.get())
    number2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == 'Add':
        result = number1 + number2
    elif operation == 'Subtract':
        result = number1 - number2
    elif operation == 'Multiply':
        result = number1 * number2
    elif operation == 'Divide':
        if number2 != 0:
            result = number1 / number2
        else:
            result = 'Error! Division by zero.'
    else:
        result = 'Invalid Operation'
    
    label_result.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create variables
operation_var = tk.StringVar()
operation_var.set("Add")  # default value

# Create widgets
label_num1 = tk.Label(root, text="First Number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Second Number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Operation:")
label_operation.pack()

option_menu_operation = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
option_menu_operation.pack()

button_calculate = tk.Button(root, text="Calculate", command=perform_operation)
button_calculate.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Run the application
root.mainloop()
