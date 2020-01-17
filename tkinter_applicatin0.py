import tkinter


class GenApp:

    """
    parent:(tkinter.Tk): the root window
    """
    def __init__(self, parent):
        parent.title('CS122')
        start_button = tkinter.Button(parent, text="Start", width=20,
                                      command=self.start)
        start_button.grid()
        # self.stop_image = tkinter.PhotoImage(file="stop.gif")
        stop_button = tkinter.Button(parent, text="Stop", width=20,
                                     command=self.stop)
        # stop_button = tkinter.Button(parent, text="Stop",
        # image=self.stop_image, command=self.stop)
        stop_button.grid()
        self.status = tkinter.Label(parent, text="Ready to start")
        # This label will be changed later.
        self.status.grid()

    def start(self):
        self.status.configure(text="In progress", foreground="green")

    def stop(self):
        self.status.configure(text="All done!", foreground="red")


def main():
    root = tkinter.Tk()  # create GUI application main window
    # root.title('CS122')
    # hello = tkinter.Label(root, text="Hello World")
    # hello.pack()
    gen_app = GenApp(root)  # most of implementation in class GenApp
    root.mainloop()  # enter the main event loop and wait
    # always calls root.mainloop() instead of gen_app.mainloop()


if __name__ == "__main__":
    main()
