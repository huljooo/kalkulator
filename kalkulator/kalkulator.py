import tkinter as tk
import math

ALLOWED_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "sqrt": math.sqrt,
    "pow": math.pow,
    "pi": math.pi,
    "e": math.e
}

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zaawansowany Kalkulator")
        self.geometry("400x600")
        self.configure(bg="#2e2e2e")
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, relief="sunken", bg="#1e1e1e", fg="white", justify="right")
        self.display.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["7", "8", "9", "/", "√"],
            ["4", "5", "6", "*", "^"],
            ["1", "2", "3", "-", "log"],
            ["0", ".", "(", ")", "+"],
            ["sin", "cos", "tan", "π", "e"],
            ["C", "⌫", "=", "", ""]
        ]

        for row in buttons:
            frame = tk.Frame(self, bg="#2e2e2e")
            frame.pack(expand=True, fill="both")
            for btn_text in row:
                if btn_text:
                    b = tk.Button(
                        frame, text=btn_text, font=("Arial", 18), bg="#4d4d4d", fg="white",
                        command=lambda txt=btn_text: self.on_button_click(txt)
                    )
                    b.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate()
            return
        elif char == "π":
            self.expression += "pi"
        elif char == "e":
            self.expression += "e"
        elif char == "√":
            self.expression += "sqrt("
        elif char == "^":
            self.expression += "**"
        elif char in ["sin", "cos", "tan", "log"]:
            self.expression += f"{char}("
        else:
            self.expression += str(char)

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            # Bezpieczne obliczenie
            result = eval(self.expression, {"__builtins__": None}, ALLOWED_FUNCTIONS)
            self.expression = str(result)
        except Exception as e:
            self.expression = "Błąd"

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()
