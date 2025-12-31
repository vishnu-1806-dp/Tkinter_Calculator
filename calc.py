import tkinter as tk

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")

def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    ".","0","=","+"
]

r = 1
c = 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: click(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Times New Roman", 12),
        width=5,
        height=2,
        bg="yellow" if b in "+-*/=" else "gray",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        r += 1
        c = 0

tk.Button(
    root,
    text="C",
    font=("Times New Roman", 12),
    command=clear,
    bg="red",
    fg="white",
    width=5,
    height=2
).grid(row=r, column=0, columnspan=4, pady=6)

root.mainloop()
