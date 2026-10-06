import tkinter as tk

root = tk.Tk()
root.title("Dream House")

canvas = tk.Canvas(root, width=500, height=350, bg="skyblue")
canvas.pack()

# House body
canvas.create_rectangle(120, 150, 380, 300, fill="yellow")


# Door
canvas.create_rectangle(220, 220, 280, 300, fill="brown")

# Roof
canvas.create_polygon(
    100, 150,
    250, 50,
    400, 150,
    fill="brown"
)

# Left window
canvas.create_rectangle(145, 180, 195, 230, fill="lightblue")
canvas.create_line(170, 180, 170, 230, fill="black")
canvas.create_line(145, 205, 195, 205, fill="black")

# Right window
canvas.create_rectangle(305, 180, 355, 230, fill="lightblue")
canvas.create_line(330, 180, 330, 230, fill="black")
canvas.create_line(305, 205, 355, 205, fill="black")



root.mainloop()