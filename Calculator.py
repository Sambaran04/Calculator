import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        self.entry = tk.Entry(master, width=25, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        buttons = ["7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   "0", ".", "=", "/"]

        for i in range(4):
            for j in range(4):
                button = tk.Button(master, text=buttons[i*4+j], width=5, height=2, command=lambda text=buttons[i*4+j]: self.button_click(text))
                button.grid(row=i+1, column=j, padx=5, pady=5)

        clear_button = tk.Button(master, text="Clear", width=10, height=2, command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        quit_button = tk.Button(master, text="Quit", width=10, height=2, command=master.quit)
        quit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.entry.get()))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        else:
            self.entry.insert(tk.END, text)

    def clear(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()