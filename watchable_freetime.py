import tkinter as tk

bedtime = 23
hometime = 19
freetime = bedtime - hometime

root = tk.Tk()
root.geometry('510x60')
root.resizable(False, False)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill = tk.BOTH, expand = True)
for i in range(freetime):
    canvas.create_rectangle(i*50+5, 5, (i+1)*50+5, 55, outline="black", fill="skyblue")

root.mainloop()