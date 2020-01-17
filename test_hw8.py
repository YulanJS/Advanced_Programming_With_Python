import glob
import tkinter as tki


class ImageViewer(tki.Tk):
    def __init__(self):
        """Create the ImageViewer."""
        super().__init__()
        # Attributes for the image handling.
        self.image_names=['Boccardo_Gate.gif', 'Campus_Villiage.gif',
                          'King_Library.gif', 'Schmitz_General_Campus.gif',
                          'Student_Wellness_Center.gif', 'Tower_Lawn.gif',
                          'University_Campus.gif']
        self.index = 0
        self.photo = None
        #Button init
        btn= tki.Button(self.root,text="NextPic",command=self.show_image)
        btn.grid(sticky = tki.S)
        # We'll use a Label to display the images.

        self.label = tki.Label(self)
        self.label.pack(padx=5, pady=5)
        # Delay should be in ms.
        self.delay = 1000*2.5
        # Display the first image.
        self.show_image()

    def show_image(self):
        """Display an image."""
        # We need to use PIL.Image to open png files, since
        # tkinter's PhotoImage only reads gif and pgm/ppm files.
        image = Image.open(self.image_names[index])
        # We need to keep a reference to the image!
        self.photo = ImageTk.PhotoImage(image)
        self.index += 1
        if self.index == len(self.image_names):
            self.index = 0
        # Set the image
        self.label['image'] = self.photo
        # Tell tkinter we want this method to be called again after a delay.
        self.after(self.delay, self.show_image)

app = ImageViewer()
app.mainloop()