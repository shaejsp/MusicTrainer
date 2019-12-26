import tkinter as tk
from random import randint

from pprint import pprint

global notes
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

global buttonBkg
buttonBkg = '#c4c4c4'


class NoteQueue():
    def __init__(self):
        self.note = 'C'  # sets the base note to C

    def play(self):
        """
        plays a note
        """
        print('playing: {n}'.format(n=self.note))

    def next(self):
        """
        gets a random note from the list of notes and play it
        """
        pos = randint(0, 11)
        self.note = notes[pos]
        self.play()


class Application(tk.Frame):
    def __init__(self, master=None):
        """
        constructor for the Application class
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.queue = NoteQueue()
        self.initWindow()

    def initWindow(self):
        """
        set up the window
        """
        self.master.title("Music Trainer")
        self.pack(fill='both', expand=1)

        # creates the quit button
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.place(x=5, y=5)

        # # creates the play note button
        self.playButton = tk.Button(self, text='Play Note', command=self.queue.play)
        self.playButton.place(x=45, y=5)

        # creates the play next button
        self.playNextButton = tk.Button(self, text='Play Next', command=self.queue.next)
        self.playNextButton.place(x=115, y=5)

        # CREATES BUTTONS - can't use a loop or the event handlers will default to G# (notes[11])
        # since the callback isn't dynamic, so unfortunately must be hard coded

        self.buttons = {}

        # i = 11 when the loop ends, and in python i can still be accessed out of scope, so each
        # event handler routes to G# event handler
        # for i in range(len(notes)):
        #     self.buttons[notes[i]] = tk.Button(self, text=notes[i], font='Courier 12',
        #                                        bg=buttonBkg,
        #                                        command=lambda: self.noteButtonPressed(notes[i]))
        #     self.buttons[notes[i]].place(x=5 + (50*i), y=200)

        # A button
        self.buttons[notes[0]] = tk.Button(self, text=notes[0], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[0]))
        self.buttons[notes[0]].place(x=5, y=200)

        # A# button
        self.buttons[notes[1]] = tk.Button(self, text=notes[1], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[1]))
        self.buttons[notes[1]].place(x=55, y=200)

        # B button
        self.buttons[notes[2]] = tk.Button(self, text=notes[2], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[2]))
        self.buttons[notes[2]].place(x=105, y=200)

        # C button
        self.buttons[notes[3]] = tk.Button(self, text=notes[3], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[3]))
        self.buttons[notes[3]].place(x=155, y=200)

        # C# button
        self.buttons[notes[4]] = tk.Button(self, text=notes[4], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[4]))
        self.buttons[notes[4]].place(x=205, y=200)

        # D button
        self.buttons[notes[5]] = tk.Button(self, text=notes[5], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[5]))
        self.buttons[notes[5]].place(x=255, y=200)

        # D# button
        self.buttons[notes[6]] = tk.Button(self, text=notes[6], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[6]))
        self.buttons[notes[6]].place(x=305, y=200)

        # E button
        self.buttons[notes[7]] = tk.Button(self, text=notes[7], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[7]))
        self.buttons[notes[7]].place(x=355, y=200)

        # F button
        self.buttons[notes[8]] = tk.Button(self, text=notes[8], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[8]))
        self.buttons[notes[8]].place(x=405, y=200)

        # F# button
        self.buttons[notes[9]] = tk.Button(self, text=notes[9], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[9]))
        self.buttons[notes[9]].place(x=455, y=200)

        # G button
        self.buttons[notes[10]] = tk.Button(self, text=notes[10], font='Courier 12', bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[10]))
        self.buttons[notes[10]].place(x=505, y=200)

        # G# button
        self.buttons[notes[11]] = tk.Button(self, text=notes[11], font='Courier 12', bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[11]))
        self.buttons[notes[11]].place(x=555, y=200)

    def noteButtonPressed(self, buttonNote):
        """
        called when a note button is pressed, if the button is correct, turn the button green.
        If the button is incorrect, turn it red and disable it

        :param buttonNote: the note on the button that was pressed
        """
        print('{} button pressed'.format(buttonNote))
        # if correct -> enable playNextButton, turn all buttons to grey
        if self.queue.note == buttonNote:
            self.buttons[buttonNote].config(bg='green')

            # self.playNextButton.config(state='normal')
            # for b in self.buttons.values():
            #     if b['bg'] != buttonBkg:
            #         b.config(bg=buttonBkg)
            #     if b['state'] != 'normal':
            #         b.config(state='normal')
        # else turn that button red
        else:
            self.buttons[buttonNote].config(bg='#ff3348', state='disabled', fg='white')

    def quit(self):
        """
        called when the quit button is pressed, exits the program
        """
        exit()


def main():
    # runs the main app
    root = tk.Tk()
    root.geometry("700x500")  # sets size
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
