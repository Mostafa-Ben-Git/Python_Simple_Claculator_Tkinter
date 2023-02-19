import tkinter as tk


class Calculator:
    def __init__(self):
        self.base()
        self.Display()
        self.Buttons()
        self.grid_config()
        self.root.mainloop()

    def base(self):
        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.iconbitmap("./app.ico")
        self.root.title("Calculator by Mostafa Ben")
        self.root.config(background="#828282", borderwidth=10)

    def Display(self):
        self.entry = tk.Entry(
            self.root,
            bg="#312215",
            fg="#fff",
            font=("verdana", 25, "bold", "roman"),
            insertbackground="#ff7700",
            borderwidth=15,
        )  # FLAT RAISED SUNKEN GROOVE RIDGE
        self.entry.pack(fill="x", padx=20, pady=20, ipady=30)

    def Buttons(self):
        self.buttons = tk.Frame(self.root, bg="#828282")
        self.buttons.pack(fill="both", padx=20, pady=15, ipady=40)

        self.but_ac = tk.Button(
            self.buttons,
            bg="red",
            fg="white",
            text="AC",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.delete(0, "end"),
        )
        self.but_ac.grid(row=0, column=0, sticky="eswn", padx=10, pady=10)

        self.but_ce = tk.Button(
            self.buttons,
            bg="red",
            fg="white",
            text="CE",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.delete(len(self.entry.get()) - 1, tk.END),
        )
        self.but_ce.grid(row=0, column=1, sticky="eswn", padx=10, pady=10)

        self.but_perc = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="%",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "%"),
        )
        self.but_perc.grid(row=0, column=2, sticky="eswn", padx=10, pady=10)

        self.but_div = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="÷",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "÷"),
        )
        self.but_div.grid(row=0, column=3, sticky="eswn", padx=10, pady=10)

        self.but_7 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="7",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "7"),
        )
        self.but_7.grid(row=1, column=0, sticky="eswn", padx=10, pady=10)

        self.but_8 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="8",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "8"),
        )
        self.but_8.grid(row=1, column=1, sticky="eswn", padx=10, pady=10)

        self.but_9 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="9",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "9"),
        )
        self.but_9.grid(row=1, column=2, sticky="eswn", padx=10, pady=10)

        self.but_X = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="X",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "x"),
        )
        self.but_X.grid(row=1, column=3, sticky="eswn", padx=10, pady=10)

        self.but_4 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="4",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "4"),
        )
        self.but_4.grid(row=2, column=0, sticky="eswn", padx=10, pady=10)

        self.but_5 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="5",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "5"),
        )
        self.but_5.grid(row=2, column=1, sticky="eswn", padx=10, pady=10)

        self.but_6 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="6",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "6"),
        )
        self.but_6.grid(row=2, column=2, sticky="eswn", padx=10, pady=10)

        self.but_dif = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="-",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "-"),
        )
        self.but_dif.grid(row=2, column=3, sticky="eswn", padx=10, pady=10)

        self.but_1 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="1",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "1"),
        )
        self.but_1.grid(row=3, column=0, sticky="eswn", padx=10, pady=10)

        self.but_2 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="2",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "2"),
        )
        self.but_2.grid(row=3, column=1, sticky="eswn", padx=10, pady=10)

        self.but_3 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="3",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "3"),
        )
        self.but_3.grid(row=3, column=2, sticky="eswn", padx=10, pady=10)

        self.but_add = tk.Button(
            self.buttons,
            bg="red",
            fg="white",
            text="+",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "+"),
        )
        self.but_add.grid(row=3, column=3, sticky="eswn", padx=10, pady=10, rowspan=2)

        self.but_0 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="0",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "0"),
        )
        self.but_0.grid(row=4, column=0, sticky="eswn", padx=10, pady=10)

        self.but_00 = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text="00",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "00"),
        )
        self.but_00.grid(row=4, column=2, sticky="eswn", padx=10, pady=10)

        self.but_dot = tk.Button(
            self.buttons,
            bg="#1cc7d0",
            fg="white",
            text=".",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "."),
        )
        self.but_dot.grid(row=4, column=1, sticky="eswn", padx=10, pady=10)

        self.but_equal = tk.Button(
            self.buttons,
            bg="green",
            fg="white",
            text="=",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.result(self.entry.get()),
        )
        self.but_equal.grid(
            row=5, column=2, columnspan=2, sticky="eswn", padx=10, pady=10
        )

        self.but_left = tk.Button(
            self.buttons,
            bg="#d0701c",
            fg="white",
            text="(",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", "("),
        )
        self.but_left.grid(row=5, column=0, sticky="eswn", padx=10, pady=10)

        self.but_right = tk.Button(
            self.buttons,
            bg="#d0701c",
            fg="white",
            text=")",
            font=("Comic Sans MS", 15, "bold"),
            command=lambda: self.entry.insert("end", ")"),
        )
        self.but_right.grid(row=5, column=1, sticky="eswn", padx=10, pady=10)

    def grid_config(self):
        for i in range(4):
            self.buttons.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.buttons.grid_rowconfigure(j, weight=1)

    def result(self, s: str):
        s = s.replace("÷", "/")
        s = s.replace("x", "*")
        s = s.replace("%", "//100")
        try:
            res = eval(s)
            print(res)
            self.entry.delete(0, "end")
            self.entry.insert("end", f"{round(float(res),4)}")
        except Exception:
            self.entry.delete(0, "end")
            self.entry.insert("end", f"Invalid !!")


Calculator()
