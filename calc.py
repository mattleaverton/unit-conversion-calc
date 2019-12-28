import tkinter as tk


class Application(tk.Frame):
    def __init__(self):
        self.master = tk.Tk()
        # self.master.bind("<FocusIn>", self.window_focus)

        super().__init__(self.master)
        self.inch_entry = None
        self.inch_var = None
        self.inch_active = False
        self.mm_entry = None
        self.mm_var = None
        self.mm_active = False

        self.pack()
        self.create_widgets()

        self.inch_entry.focus()
        self.inch_entry.select_range(0, tk.END)
        self.inch_active = True
        self.mm_active = False

    def window_focus(self, _event):
        # self.mm_entry.focus()
        # self.mm_entry.select_range(0, tk.END)
        if _event.widget._name == "!entry":
            self.inch_entry.focus()
            self.inch_entry.select_range(0, tk.END)
            self.inch_active = True
            self.mm_active = False
        elif _event.widget._name == "!entry2":
            self.mm_entry.focus()
            self.mm_entry.select_range(0, tk.END)
            self.inch_active = False
            self.mm_active = True

    def in_callback(self, *args):
        if args[0] == "PY_VAR0":
            # inch entry
            if self.inch_active:
                inches = self.inch_var.get()
                try:
                    num = eval(inches)
                    num *= 25.4
                except:
                    num = 0
                self.mm_var.set("{0:.3f}".format(num))
        elif args[0] == "PY_VAR1":
            # mm entry
            if self.mm_active:
                mm = self.mm_var.get()
                try:
                    num = eval(mm)
                    num /= 25.4
                except:
                    num = 0
                self.inch_var.set("{0:.3f}".format(num))

    def create_widgets(self):
        label1 = tk.Label(self, text="in", font=("systemfixed", 60))
        label1.grid(row=0, padx=(0, 25))
        label2 = tk.Label(self, text="mm", font=("systemfixed", 60))
        label2.grid(row=1, padx=(0, 25))

        inches = tk.StringVar()
        inches.trace("w", self.in_callback)
        e1 = tk.Entry(self, textvariable=inches, font=("systemfixed", 60), width=8)
        e1.bind("<FocusIn>", self.window_focus)

        mm = tk.StringVar()
        mm.trace("w", self.in_callback)
        e2 = tk.Entry(self, textvariable=mm, font=("systemfixed", 60), width=8)
        e2.bind("<FocusIn>", self.window_focus)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        self.inch_entry = e1
        self.inch_var = inches
        self.mm_entry = e2
        self.mm_var = mm


app = Application()
app.mainloop()
