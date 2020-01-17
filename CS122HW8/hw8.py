import tkinter
from itertools import cycle
import random
from tkinter import messagebox as msg
import sys
import argparse
"""
It is an image matching game.

Users are asked to click start and stop to match with the initial static 
picture. If matched, a user gains one point, and the switching of 
pictures becomes faster. A spartan logo at the bottom shows the progress 
of the game. When user gains five points, user wins and game ends.
Users can set difficulty level, background color and verbose option in 
command line.
"""


class ImageMatching(tkinter.Tk):
    """
    The class of the image matching game.
    Arguments:
        parent(tkinter.Tk): root window
        difficulty(string): easy, medium, or hard
        color(string): yellow or blue
    Attributes:
        image_files(list): a list of strings that are the gif
                           picture names
        canvas(tkinter.Canvas): canvas
        score_label(tkinter.Label): the label to show scores
        start_button(tkinter.Button): the button to start
        stop_button(tkinter.Button): the button to stop
        reset_button(tkinter.Button): the button to reset
        pictures(iterator): cycle of pictures
        picture_display(tkinter.Label) the label to display one of the
        pictures in the cycle of pictures
        index(int): use index to choose a random static picture
        target_image_name(string): the name of the static picture
        target_image(tkinter.PhotoImage): the static picture to match
        score(int): score of the game
        difficulty(string): easy, medium, hard
        delay(int): the time of delay to show next picture for the
                    slideshow
        logo_image(tkinter.PhotoImage): the logo of Spartan, which will
        move to the right when user gains one score
        logo: image id of the spartan logo
        update(boolean): If true, pictures start rotating, if false,
        pictures stop rotating.
        current_picture(string): name of the picture in the cycle when
        user press stop
    """
    def __init__(self, parent, difficulty, color):
        tkinter.Tk.__init__(self)
        self.image_files = ['Boccardo_Gate.gif', 'Campus_Villiage.gif',
                            'King_Library.gif', 'Schmitz_GeneralCampus.gif',
                            'Student_Wellness_Center.gif', 'Tower_Lawn.gif',
                            'University_Campus.gif']
        parent.title("Image Matching")
        self.canvas = tkinter.Canvas(parent, width=400, height=1000)
        # background color: blue or yellow
        self.canvas.configure(background=color)
        # buttons_frame
        buttons_frame = tkinter.Frame(parent)
        buttons_frame.grid()
        self.score_label = tkinter.Label(buttons_frame, text='Score: ' + '0',
                                         font='none 12 bold',
                                         background='white')
        self.score_label.grid(column=0, row=0)
        self.start_button = tkinter.Button(buttons_frame, padx=5, pady=5,
                                           text='Start',
                                           font='none 12 bold',
                                           foreground='white',
                                           background='blue',
                                           command=self.start)
        self.start_button.grid(column=1, row=0)
        self.stop_button = tkinter.Button(buttons_frame, padx=5, pady=5,
                                          text='Stop',
                                          font='none 12 bold',
                                          background='yellow',
                                          command=self.stop)
        self.stop_button.grid(column=2, row=0)
        self.reset_button = tkinter.Button(buttons_frame, padx=5, pady=5,
                                           text='Reset', font='none 12 bold',
                                           foreground='white',
                                           background='blue',
                                           command=self.reset)
        self.reset_button.grid(column=3, row=0)
        # slideshow change avoid copy
        self.pictures = cycle((tkinter.PhotoImage(file=image), image)
                              for image in self.image_files)
        self.picture_display = tkinter.Label(parent)
        self.picture_display.grid()
        # random target picture
        self.index = random.randint(0, len(self.image_files) - 1)
        self.target_image_name = self.image_files[self.index]
        self.target_image = tkinter.PhotoImage(
            file=self.target_image_name)
        self.canvas.create_image(200, 75, image=self.target_image)
        self.score = 0
        # set initial delay value(related to the speed of switching
        # pictures) according to the difficulty argument
        # the larger the delay, the slower the speed
        self.difficulty = difficulty
        if difficulty == 'easy':
            self.delay = 300
        elif difficulty == 'medium':
            self.delay = 200
        else:
            self.delay = 100
        # the logo to move when users gain one score
        self.logo_image = tkinter.PhotoImage(file='Spartans_logo.gif')
        self.logo = self.canvas.create_image(20, 300, image=self.logo_image)
        self.canvas.grid()

    def start(self):
        """
        When user clicks start button, set update and call show.
        """
        self.update = True
        self.show()

    def show(self):
        """
        When user clicks start, update is true. This function switches
        pictures and call itself after the time of delay to switch
        pictures or stop switching pictures.
        :return:
        """
        if self.update:
            image_obj, image_name = next(self.pictures)
            self.picture_display.config(image=image_obj)
            # the picture present from the cycle of pictures
            self.current_picture = image_name
            self.after(self.delay, self.show)

    def stop(self):
        """
        When user clicks stop, this function shows whether the current
        picture matches with the static picture, update scores, delay
        and the position of spartan logo. If win(five matches),
        show a message box to inform user that he wins.
        """
        # change update to False to stop rotating the pictures.
        self.update = False
        # check if it matches with static picture
        if self.current_picture == self.target_image_name:
            self.score += 1
            self.score_label.config(text='Score: ' + str(self.score))
            # for each score users gain,
            # logo moves 1/5 of the width of screen
            self.canvas.move(self.logo, 72, 0)
            if self.score == 5:
                self.reset()
                msg.showinfo("Game Over", "You Win!")
            # speed up rotations after one match.
            if self.delay >= 40:
                self.delay -= 20

    def reset(self):
        """
        when user clicks reset button, reset the position of spartan
        logo, the score value and delay.
        """
        if self.score != 0:
            self.canvas.move(self.logo, -self.score * 72, 0)
        self.score = 0
        self.score_label.config(text='Score: ' + str(self.score))
        if self.difficulty == 'easy':
            self.delay = 300
        elif self.difficulty == 'medium':
            self.delay = 200
        else:
            self.delay = 100


def get_arguments():
    """
    Parse and validate command line arguments
    :return: tuple containing difficulty(a string of "easy", "medium",
    or "hard"), color(a string of yellow or blue),
    verbose option(boolean).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('difficulty', help='Which difficulty level '
                                           'would you like?',
                        choices=['easy', 'medium', 'hard'])
    parser.add_argument('color', help='Which background color do you'
                                      'like?',
                        choices=['yellow', 'blue'])
    parser.add_argument('-v', '--verbose', help='Print details?',
                        action='store_true')
    arguments = parser.parse_args()
    difficulty = arguments.difficulty
    color = arguments.color
    verbose = arguments.verbose
    return difficulty, color, verbose


def main():
    # print('Usage: hw8.py difficulty background_color')
    root = tkinter.Tk()
    difficulty, color, verbose = get_arguments()
    if verbose:
        print(f'Staring a picture matching game with background color'
              f'{color} and difficulty level {difficulty}')
    match_app = ImageMatching(root, difficulty, color)
    # fix the size of root
    root.resizable(False, False)
    match_app.mainloop()


if __name__ == "__main__":
    main()
