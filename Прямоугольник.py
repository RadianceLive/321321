import tkinter as tk

WIDTH, HEIGHT = 600, 400
RECT_WIDTH, RECT_HEIGHT = 100, 60
SHADOW_OFFSET_X, SHADOW_OFFSET_Y = 20, 20

root = tk.Tk()
root.title("Работа")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

rect_x, rect_y = 200, 150


def draw():
    canvas.delete("all")

    canvas.create_polygon(
        rect_x + SHADOW_OFFSET_X, rect_y + SHADOW_OFFSET_Y,
        rect_x + RECT_WIDTH + SHADOW_OFFSET_X, rect_y + SHADOW_OFFSET_Y + 10,
        rect_x + RECT_WIDTH + SHADOW_OFFSET_X, rect_y + RECT_HEIGHT + SHADOW_OFFSET_Y,
        rect_x + SHADOW_OFFSET_X - 10, rect_y + RECT_HEIGHT + SHADOW_OFFSET_Y,
        fill="gray", outline=""
    )

    canvas.create_rectangle(rect_x, rect_y, rect_x + RECT_WIDTH, rect_y + RECT_HEIGHT, fill="green")


def move(event):
    global rect_x, rect_y
    step = 10

    if event.keysym == "w":
        rect_y -= step
    elif event.keysym == "s":
        rect_y += step
    elif event.keysym == "a":
        rect_x -= step
    elif event.keysym == "d":
        rect_x += step

    draw()

root.bind("<KeyPress>", move)

draw()

root.mainloop()
