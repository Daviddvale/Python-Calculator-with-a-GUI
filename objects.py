import tkinter as tk

# ButtonBase class for reusable button creation
class ButtonBase:
    def __init__(self, frame, text, command, width=6, height=2, bg="white"):
        self.button = tk.Button(frame, text=text, font=("Arial", 15), command=command, width=width, height=height, bg=bg)

class Calculator:
    def __init__(self):
        # Create the main calculator window
        self.calc = tk.Tk()
        self.calc.title("Calculator")

        # Create main frame
        self.frame = tk.Frame(self.calc)
        self.frame.pack()

        # Initialize display label with default "0"
        self.string_var = tk.StringVar()
        self.string_var.set("0")
        self.label = tk.Label(self.frame, text="0", font=("Arial", 25), bg="white", width=16)
        self.label.grid(row=0, column=0, columnspan=4)

        # Initialize buttons
        self.create_buttons()
        
        # Configure keyboard bindings
        self.bind_keys()

    # Update label display
    def update_label(self):
        self.label.config(text=self.string_var.get())

    # Clear display
    def clear(self):
        self.string_var.set("0")
        self.update_label()

    # Append character to display or replace initial "0"
    def append(self, char):
        if self.string_var.get() == "0":
            self.string_var.set(char)
        else:
            self.string_var.set(self.string_var.get() + char)
        self.update_label()

    # Evaluate the current expression in display
    def evaluate(self):
        try:
            result = eval(self.string_var.get())
            self.string_var.set(str(result))
        except Exception:
            self.string_var.set("Error")
        self.update_label()

    # Create buttons and arrange in grid using a loop
    def create_buttons(self):
        # Button configuration list: (text, command, row, column, optional columnspan)
        buttons = [
            ("1", lambda: self.append("1"), 1, 0),
            ("2", lambda: self.append("2"), 1, 1),
            ("3", lambda: self.append("3"), 1, 2),
            ("+", lambda: self.append("+"), 1, 3),
            ("4", lambda: self.append("4"), 2, 0),
            ("5", lambda: self.append("5"), 2, 1),
            ("6", lambda: self.append("6"), 2, 2),
            ("-", lambda: self.append("-"), 2, 3),
            ("7", lambda: self.append("7"), 3, 0),
            ("8", lambda: self.append("8"), 3, 1),
            ("9", lambda: self.append("9"), 3, 2),
            ("*", lambda: self.append("*"), 3, 3),
            ("0", lambda: self.append("0"), 4, 0),
            (".", lambda: self.append("."), 4, 1),
            ("=", self.evaluate, 4, 2),
            ("/", lambda: self.append("/"), 4, 3),
            ("C", self.clear, 5, 0, 4)  # Clear button spans 4 columns
        ]

        # Create and place each button in the grid
        for text, command, row, col, *colspan in buttons:
            button = ButtonBase(self.frame, text, command,width=27 if text == "C" else 6, bg="orange" if text == "C" else "white").button
            button.grid(row=row, column=col, columnspan=colspan[0] if colspan else 1)

    # Add keyboard shortcuts to calculator buttons
    def bind_keys(self):
        self.calc.bind("<Return>", lambda event: self.evaluate())
        self.calc.bind("<KP_Enter>", lambda event: self.evaluate())
        self.calc.bind("<BackSpace>", lambda event: self.clear())
        for char in '1234567890+-*/.':
            self.calc.bind(char, lambda event, char=char: self.append(char))
        self.calc.bind("<Escape>", lambda event: self.calc.destroy())

    # Start the main loop
    def run(self):
        self.calc.mainloop()

# Create and run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()