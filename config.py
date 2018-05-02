from enum import Enum

BarTitle = Enum("BarTitle", "File, Edit, Help")
FileMenu = Enum("FileMenu", "New, Open, Save")

font = ("宋体", 18)
btn_font = ("宋体", 15)

labelWidth = 58
labelHeight = 3
labelBg = "#FFFFF0"
labelAnchor = "se"
labelJustify = "right"

button_str = dict(one=["AC", "7", "4", "1", "\b"],
                  two=["+/-", "8", "5", "2", "0"],
                  three=["%", "9", "6", "3", "."],
                  four=["/", "x", "-", "+", "="])

all_str = "0123456789.+-*/x%=\r\b"

btn_width = 5
btn_height = 2

args = ""
front_cal = ""
back_cal = ""

an_end_state = False