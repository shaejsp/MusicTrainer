import tkinter as tk
from random import randint

"""
TODO:
 - implement tracking for how many they got right
 - add ability to choose which notes you want to practice
 - add ability to limit to one octave, 3 octaves, 5, or 7 (acts as a multiplier for score)
 - actually implement the sound playing
 - MAYBE: add notes from guitar -> would be better as another
    proj for guessing where the notes go on the fretboard
 - MAYBE: add notes from bass guitar -> would be better as another
    proj for guessing where the notes go on the fretboard
 """

global notes
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

global buttonBkg
buttonBkg = '#c4c4c4'


class NoteQueue():
    def __init__(self):
        self.note = 'Unassigned'
        self.next()  # randomly assigns first note

    def play(self):
        """
        play a note
        """
        print('playing: {n}'.format(n=self.note))

    def next(self):
        """
        get a random note from the list of notes and play it
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
        self.playButton = tk.Button(self, text='Play Note',  font='Courier 12', width=10,
                                    height=2, command=self.queue.play)
        self.playButton.place(x=20, y=100)

        # creates the play next button
        self.playNextButton = tk.Button(self, text='Play Next', font='Courier 12',
                                        state='disabled', width=10, height=2,
                                        command=self.playNextPressed)
        self.playNextButton.place(x=140, y=100)

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
                                           command=lambda: self.noteButtonPressed(notes[0]),
                                           width=10)
        self.buttons[notes[0]].place(x=20, y=180)

        # A# button
        self.buttons[notes[1]] = tk.Button(self, text=notes[1], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[1]),
                                           width=10)
        self.buttons[notes[1]].place(x=140, y=180)

        # B button
        self.buttons[notes[2]] = tk.Button(self, text=notes[2], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[2]),
                                           width=10)
        self.buttons[notes[2]].place(x=20, y=220)

        # C button
        self.buttons[notes[3]] = tk.Button(self, text=notes[3], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[3]),
                                           width=10)
        self.buttons[notes[3]].place(x=20, y=260)

        # C# button
        self.buttons[notes[4]] = tk.Button(self, text=notes[4], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[4]),
                                           width=10)
        self.buttons[notes[4]].place(x=140, y=260)

        # D button
        self.buttons[notes[5]] = tk.Button(self, text=notes[5], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[5]),
                                           width=10)
        self.buttons[notes[5]].place(x=20, y=300)

        # D# button
        self.buttons[notes[6]] = tk.Button(self, text=notes[6], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[6]),
                                           width=10)
        self.buttons[notes[6]].place(x=140, y=300)

        # E button
        self.buttons[notes[7]] = tk.Button(self, text=notes[7], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[7]),
                                           width=10)
        self.buttons[notes[7]].place(x=20, y=340)

        # F button
        self.buttons[notes[8]] = tk.Button(self, text=notes[8], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[8]),
                                           width=10)
        self.buttons[notes[8]].place(x=20, y=380)

        # F# button
        self.buttons[notes[9]] = tk.Button(self, text=notes[9], font='Courier 12', bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[9]),
                                           width=10)
        self.buttons[notes[9]].place(x=140, y=380)

        # G button
        self.buttons[notes[10]] = tk.Button(self, text=notes[10], font='Courier 12', bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[10]),
                                           width=10)
        self.buttons[notes[10]].place(x=20, y=420)

        # G# button
        self.buttons[notes[11]] = tk.Button(self, text=notes[11], font='Courier 12', bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[11]),
                                           width=10)
        self.buttons[notes[11]].place(x=140, y=420)

    def noteButtonPressed(self, buttonNote):
        """
        called when a note button is pressed, if the button is correct, turn the button green.
        If the button is incorrect, turn it red and disable it

        :param buttonNote: the note on the button that was pressed
        """
        print('{} button pressed'.format(buttonNote))
        # if correct -> enable playNextButton, reset colors for all buttons
        if self.queue.note == buttonNote:
            self.playNextButton.config(state='normal')
            for b in self.buttons.values():
                b.config(state='disabled')
            self.buttons[buttonNote].config(bg='green', state='normal')
        # else turn the pressed button red
        else:
            self.buttons[buttonNote].config(bg='red', state='disabled')

    def playNextPressed(self):
        """
        called when the play next button is pressed, resets all of the note buttons and
        calls queue.next()
        """
        for b in self.buttons.values():
            if b['bg'] != buttonBkg:
                b.config(bg=buttonBkg)
            if b['state'] != 'normal':
                b.config(state='normal')
        self.queue.next()
        self.playNextButton.config(state='disabled')

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
