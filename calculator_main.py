#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from config import *
from tool import close_an_end_statue


class Calculator:
    """Calculator class"""

    def __init__(self, title, geometry, **kw):
        self.sign = ["+", "-", "*", "/", "%", "=", "+/-"]
        self.window = tk.Tk(**kw)
        self.window.title(title)
        self.window.geometry(geometry)
        self.window.resizable(False, False)

        self.makeMenuBar()
        self.makeLabel()
        self.makeButtons()

    def makeMenuBar(self):
        """Make the menu bar"""
        self.menuBar = tk.Menu(self.window)
        fileMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New", command=self.OnNew)
        fileMenu.add_command(label="Open", command=self.OnOpen)
        fileMenu.add_command(label="Save", command=self.OnSave)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.window.quit)

        editMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Edit", menu=editMenu)
        helpMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Help", menu=helpMenu)

        self.window.config(menu=self.menuBar)

    def makeLabel(self):
        """Make display screen """
        self.label = tk.Label(self.window,
                              font=font,
                              width=labelWidth,
                              height=labelHeight,
                              bg=labelBg,
                              anchor=labelAnchor,
                              justify=labelJustify)
        self.set_label_init()
        self.label_callBack()
        self.label.pack(side=tk.TOP)
        self.label.focus_set()

    def makeButtons(self):
        """Make button group"""
        for key, value in button_str.items():
            fm = tk.Frame(self.window)
            for val in value:
                tk.Button(fm,
                          text=val if val != "\b" else "<-",
                          font=btn_font,
                          width=btn_width,
                          height=btn_height,
                          command=self.btn_callBack(val)).pack(side=tk.TOP,
                                                               anchor=tk.W,
                                                               fill=tk.X,
                                                               expand=tk.YES)
            fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

    def listen_event(self, event):
        """Listen keyboard click events."""
        keyboard = event.char
        if keyboard in all_str:
            self._exec_calculation(keyboard)

    def _exec_calculation(self, value):
        """Operational logic processing"""
        global args, front_cal, back_cal, an_end_state
        if an_end_state and value not in self.sign:
            front_cal = ""
            args = ""
        an_end_state = close_an_end_statue(an_end_state)
        if value == "AC":
            self.set_label_init()
            front_cal = ""
        elif value == "\b":
            front_cal = self.go_back(front_cal)
        else:
            front_cal += value
            if value == "+/-":
                front_cal = front_cal.replace("+/-", "")
                if front_cal[-1]:
                    if front_cal[-1] == "-":
                        front_cal = self.go_back(front_cal, replace="+")
                    elif front_cal[-1] == "+":
                        front_cal = self.go_back(front_cal, replace="-")
                    else:
                        end_num = self.get_args_end(front_cal)
                        if "." in end_num:
                            new_end_num = str(0 - float(end_num))
                        else:
                            new_end_num = str(0 - int(end_num))
                        front_cal = front_cal.replace(end_num, new_end_num)
                else:
                    front_cal += "-"
                args = front_cal
            elif value == "=" or value == "\r":
                front_cal = front_cal.replace("\r", "=")
                front_cal = front_cal.replace("x", "*")
                args_list = front_cal.split("=")
                front_cal, back_cal = args_list[0], args_list[1]
                try:
                    back_cal = str(eval(front_cal))
                except ZeroDivisionError as e:
                    messagebox.showinfo("Error", message="Division by zero!")
                    front_cal = self.go_back(front_cal)
                    front_cal = self.go_back(front_cal)
                    self.set_label_str(front_cal)
                    return
                args = "{}=\r{}".format(front_cal, back_cal)
                front_cal = back_cal
                back_cal = ""
                an_end_state = True
            else:
                args = front_cal
            self.set_label_str(args)

    def get_args_end(self, value):
        """Get the last number in the value."""
        tmp_num = ""
        for num in value[::-1]:
            if num not in self.sign:
                tmp_num += num
            else:
                break
        return tmp_num[::-1]

    def label_callBack(self):
        """Label callback"""
        self.label.bind("<Key>", self.listen_event)

    def btn_callBack(self, val):
        """Button callback"""

        def get_val():
            self._exec_calculation(val)
            # return val

        return get_val

    def start(self, n=0):
        """Start this window"""
        self.window.mainloop(n)

    def OnNew(self):
        """Click the message shown in new menubar"""
        messagebox.showinfo(title="new", message="this is open a new file!(just for test)")

    def OnOpen(self):
        """Click the message shown in open menubar"""
        messagebox.showinfo(title="open", message="this is new a file(just for test)")

    def OnSave(self):
        """Click the message shown in save menubar"""
        messagebox.showinfo(title="save", message="this saves a file(just for test)")

    def set_label_init(self):
        """Init label"""
        global args, front_cal, back_cal
        self.label.config(text=0)
        args = ""
        front_cal = ""
        back_cal = ""

    def set_label_str(self, data):
        """Set up label display content."""
        self.label.config(text=data)

    def go_back(self, args, replace=None):
        """Back and replace"""
        args = args[:-1]
        if replace:
            args += replace
        if args:
            self.set_label_str(args)
        else:
            self.set_label_init()
        return args


def main():
    """this is main"""
    Calculator(title="Calculator", geometry=("300x360")).start()


if __name__ == "__main__":
    main()
