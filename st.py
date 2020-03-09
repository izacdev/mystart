print('o----')
print(' ||||')
price = 10
print(price)

name = 'john'
old = 21
is_new = True


name = input('what is your name? ')
color = input('what is your fav color? ')
print( name + ' likes ' + color)
na = ('izaaaaac')
print(na[1:-1])

first = 'sanco'
last = 'izac'
message = first + ' [' + last + '] is a coder'
print(message)

import tkinter as tk

counter = 0
def counter_label (lable):
    def count ():
        global counter 
        counter += 1
        label.config (text=str (counter))
        label.after(1000, count), count ()

phone = input("phone: ")
digits_mapping{
    "0" = "one"
    "1" = "one"
    "2" = "two"
    "3" = "three"
}
output = ""
for ch in phone:
output += digits_mapping.get (ch, "!") + " "
print(output)

        root = tk.tk ()
        root.title("counting seconds")
        lable = tk.lable
        (root,
        fg ="dark green")
        label.park()counter_lable
        (lable)button = tk.button
        (root, text = 'stop',
        width = 25,
        command = root.destroy)
        button.pack()root.mainLoop()



