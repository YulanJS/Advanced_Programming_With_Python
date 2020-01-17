import tkinter


class PaintApp:
    default_color = 'red'

    def __init__(self, parent):
        parent.title("CS122 - Let's Paint!")

        color_frame = tkinter.Frame(parent)
        # group three buttons in one row
        color_frame.grid()
        green_button = tkinter.Button(color_frame, text='Green', width=10,
                                      command=self.green)
        green_button.grid(column=0, row=0)
        red_button = tkinter.Button(color_frame, text='Red', width=10,
                                    command=self.red)
        red_button.grid(column=1, row=0)
        blue_button = tkinter.Button(color_frame, text='Blue', width=10,
                                     command=self.blue)
        blue_button.grid(column=2, row=0)

        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        self.canvas.create_rectangle(0, 0, 300, 300)
        # draw a house
        self.canvas.create_rectangle(175, 150, 275, 250)
        self.canvas.create_polygon(165, 150, 225, 100, 285, 150,
                                   outline="black", fill='white')
        # draw a flower
        self.canvas.create_oval(50, 200, 75, 225)
        self.canvas.create_oval(50, 175, 75, 200)
        self.canvas.create_oval(50, 225, 75, 250)
        self.canvas.create_oval(25, 187, 50, 212)
        self.canvas.grid()
        self.canvas.bind("<Button-1>", self.paint)  # when click left
        erase_button = tkinter.Button(parent, text='ERASER', width=30,
                                      command=self.erase)
        erase_button.grid()
        self.color = self.default_color
        self.erase()

    def green(self):
        self.color = "green"

    def red(self):
        self.color = "red"

    def blue(self):
        self.color = "blue"

    def erase(self):
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')

    def paint(self, event):
        shape = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfigure(shape, fill=self.color)


def main():
    root = tkinter.Tk()
    paint_app = PaintApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
