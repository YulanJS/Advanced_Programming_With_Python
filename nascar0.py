# ----------------------------------------------------------------------
# Name:        nascar0
# Purpose:     demonstrate animation with tkinter
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Implement a GUI app with animation in tkinter.

Create then animate two car images in response to a START and STOP
buttons.
"""
import tkinter


class Nascar:

    """
    class to support a GUI with animated images.

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    parent: (tkinter.Tk) the root window object
    canvas: (tkinter.Canvas) A Canvas widget defining the race area.
    red_car_image: (tkinter.PhotoImage) image of a red car.
    old_car_image: (tkinter.PhotoImage) image of an old car.
    red_car: (integer) object ID of the red car image created on canvas.
    old_car: (integer) object ID of the old car image created on canvas.
    """
    slow = 1
    fast = 2
    right = 475
    left = 25

    def __init__(self, parent):
        parent.title('CS 122')
        self.parent = parent
        # create a START button and associate it with the start method
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()  # register it with a geometry manager
        # create a STOP button and associate it with the stop method
        stop_button = tkinter.Button(parent, text='STOP', width=20,
                                     command=self.stop)
        stop_button.grid()  # register it with a geometry manager
        # create a Canvas widget for the animated objects
        self.canvas = tkinter.Canvas(parent, width=500, height=200,
                                     background='lawn green')

        self.red_car_image = tkinter.PhotoImage(file='redcar.gif')
        self.red_car = self.canvas.create_image(25, 50,
                                                image=self.red_car_image)

        self.old_car_image = tkinter.PhotoImage(file='oldcar.gif')
        self.old_car = self.canvas.create_image(25, 150,
                                                image=self.old_car_image)

        self.canvas.grid()
        self.pixels = {self.old_car: self.slow, self.red_car: self.fast}

    def start(self):
        """
        This method is invoked when the user presses the START button
        :return: None
        """
        self.go = True
        # self.canvas.move(self.red_car, 20, 0)
        self.animate()  # continuous move

    def animate(self):
        # to do continuous animation
        if self.go:
            self.drive(self.red_car)
            self.drive(self.old_car)
            self.parent.after(1, self.animate)  # Try again in 1 second

    def drive(self, car):
        x, y = self.canvas.coords(car)
        if x >= 475:
            self.pixels[car] = -abs(self.pixels[car])
        elif x <= 25:
            self.pixels[car] = abs(self.pixels[car])
        self.canvas.move(car, self.pixels[car], 0)

    def stop(self):
        """
        This method is invoked when the user presses the STOP button
        :return: None
        """
        self.go = False


def main():
    root = tkinter.Tk()  # create the GUI aplication main window
    race_app = Nascar(root)  # instantiate our Nascar object
    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()
