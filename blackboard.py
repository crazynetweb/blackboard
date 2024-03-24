import tkinter as tk
from tkinter import colorchooser

class Blackboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackboard")

        # Create canvas
        self.canvas = tk.Canvas(root, bg="black", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw)

        # Create clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        # Create color chooser button
        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

        # Default drawing color
        self.drawing_color = "white"

        # Previous mouse position
        self.prev_x = None
        self.prev_y = None

    def draw(self, event):
        if self.prev_x and self.prev_y:
            x1 = self.prev_x
            y1 = self.prev_y
            x2 = event.x
            y2 = event.y
            self.canvas.create_line(x1, y1, x2, y2, fill=self.drawing_color, width=5)
        self.prev_x = event.x
        self.prev_y = event.y

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color[1]:  # If a color is chosen
            self.drawing_color = color[1]


if __name__ == "__main__":
    root = tk.Tk()
    blackboard = Blackboard(root)
    root.mainloop()
