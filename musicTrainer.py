import tkinter as tk
from random import randint

"""
TODO:
 - record the notes
 - design logo in photoshop
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
buttonBkg = '#e3e3e3'

global redBkg
redBkg = '#bd3131'


class NoteQueue():
    def __init__(self):
        self.noteSelection = notes.copy()
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
        pos = randint(0, len(self.noteSelection)-1)
        print('Position: {p}'.format(p=pos))
        print('NoteSelection: {p}'.format(p=self.noteSelection))
        self.note = self.noteSelection[pos]
        self.play()

    def toggleNote(self, note):
        """
        remove or add a note to the list of notes that can be played

        :param note: the note to be added or removed
        :return: -1 if the note was removed, 1 if the note was added
        """
        if note in self.noteSelection:  # remove the note
            self.noteSelection.remove(note)
            return -1
        else:  # add the note
            self.noteSelection.append(note)
            return 1

    def validNote(self, note):
        """
        determine if a not is valid based on the possible notes 

        :param note: the note in question
        :return: a boolean, true if the note is valid, false otherwise
        """
        return note in self.noteSelection


class Application(tk.Frame):
    def __init__(self, master=None):
        """
        constructor for the Application class
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.queue = NoteQueue()
        self.firstTry = True
        self.score = 0
        self.total = 0
        self.initWindow()

    def initWindow(self):
        """
        set up the window
        """
        font = 'Courier 12'
        blueButton = '#ceddf5'
        buttonWidth = 10

        self.master.title("Music Trainer")
        self.pack(fill='both', expand=1)

        logo = tk.Label(self, text='logo (img) here', font=font, width=22)
        logo.place(x=20, y=20)

        # creates the quit button
        self.quitButton = tk.Button(self, text='Quit', font=font, width=int(buttonWidth/2), 
                                    bg=redBkg, command=self.quit)
        self.quitButton.place(x=620, y=20)

        # # creates the play note button
        self.playButton = tk.Button(self, text='Play Note', bg=blueButton, font=font, 
                                    width=buttonWidth, height=2, command=self.queue.play)
        self.playButton.place(x=20, y=100)

        # creates the play next button
        self.playNextButton = tk.Button(self, text='Play Next', bg=blueButton, font=font,
                                        state='disabled', width=buttonWidth, height=2,
                                        command=self.playNextPressed)
        self.playNextButton.place(x=140, y=100)

        # CREATES BUTTONS - can't use a loop or the event handlers will default to G# (notes[11])
        # since the callback isn't dynamic, so unfortunately must be hard coded

        self.buttons = {}

        # i = 11 when the loop ends, and in python i can still be accessed out of scope, so each
        # event handler routes to G# event handler
        # for i in range(len(notes)):
        #     self.buttons[notes[i]] = tk.Button(self, text=notes[i], font=font,
        #                                        bg=buttonBkg,
        #                                        command=lambda: self.noteButtonPressed(notes[i]))
        #     self.buttons[notes[i]].place(x=5 + (50*i), y=200)

        # A button
        self.buttons[notes[0]] = tk.Button(self, text=notes[0], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[0]),
                                           width=buttonWidth)
        self.buttons[notes[0]].place(x=20, y=180)

        # A# button
        self.buttons[notes[1]] = tk.Button(self, text=notes[1], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[1]),
                                           width=buttonWidth)
        self.buttons[notes[1]].place(x=140, y=180)

        # B button
        self.buttons[notes[2]] = tk.Button(self, text=notes[2], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[2]),
                                           width=buttonWidth)
        self.buttons[notes[2]].place(x=20, y=220)

        # C button
        self.buttons[notes[3]] = tk.Button(self, text=notes[3], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[3]),
                                           width=buttonWidth)
        self.buttons[notes[3]].place(x=20, y=260)

        # C# button
        self.buttons[notes[4]] = tk.Button(self, text=notes[4], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[4]),
                                           width=buttonWidth)
        self.buttons[notes[4]].place(x=140, y=260)

        # D button
        self.buttons[notes[5]] = tk.Button(self, text=notes[5], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[5]),
                                           width=buttonWidth)
        self.buttons[notes[5]].place(x=20, y=300)

        # D# button
        self.buttons[notes[6]] = tk.Button(self, text=notes[6], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[6]),
                                           width=buttonWidth)
        self.buttons[notes[6]].place(x=140, y=300)

        # E button
        self.buttons[notes[7]] = tk.Button(self, text=notes[7], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[7]),
                                           width=buttonWidth)
        self.buttons[notes[7]].place(x=20, y=340)

        # F button
        self.buttons[notes[8]] = tk.Button(self, text=notes[8], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[8]),
                                           width=buttonWidth)
        self.buttons[notes[8]].place(x=20, y=380)

        # F# button
        self.buttons[notes[9]] = tk.Button(self, text=notes[9], font=font, bg=buttonBkg,
                                           command=lambda: self.noteButtonPressed(notes[9]),
                                           width=buttonWidth)
        self.buttons[notes[9]].place(x=140, y=380)

        # G button
        self.buttons[notes[10]] = tk.Button(self, text=notes[10], font=font, bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[10]),
                                           width=buttonWidth)
        self.buttons[notes[10]].place(x=20, y=420)

        # G# button
        self.buttons[notes[11]] = tk.Button(self, text=notes[11], font=font, bg=buttonBkg,
                                            command=lambda: self.noteButtonPressed(notes[11]),
                                           width=buttonWidth)
        self.buttons[notes[11]].place(x=140, y=420)

        # deals with the optional includes
        includeLabel = tk.Label(self, text='Include', font=font + ' bold')
        includeLabel.place(x=400, y=100)

        notesLabel = tk.Label(self, text='Notes', font=font)
        notesLabel.place(x=400, y=140)

        # CHECK BOXES GO HERE
        self.noteChecks = {}

        # A checkbutton
        self.noteChecks[notes[0]] = tk.Checkbutton(self, text=notes[0], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[0]))
        self.noteChecks[notes[0]].place(x=400, y=180)
        self.noteChecks[notes[0]].select()

        # A# checkbutton
        self.noteChecks[notes[1]] = tk.Checkbutton(self, text=notes[1], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[1]))
        self.noteChecks[notes[1]].place(x=400, y=200)
        self.noteChecks[notes[1]].select()

        # B checkbutton
        self.noteChecks[notes[2]] = tk.Checkbutton(self, text=notes[2], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[2]))
        self.noteChecks[notes[2]].place(x=400, y=220)
        self.noteChecks[notes[2]].select()

        # C checkbutton
        self.noteChecks[notes[3]] = tk.Checkbutton(self, text=notes[3], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[3]))
        self.noteChecks[notes[3]].place(x=400, y=240)
        self.noteChecks[notes[3]].select()

        # C# checkbutton
        self.noteChecks[notes[4]] = tk.Checkbutton(self, text=notes[4], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[4]))
        self.noteChecks[notes[4]].place(x=400, y=260)
        self.noteChecks[notes[4]].select()

        # D checkbutton
        self.noteChecks[notes[5]] = tk.Checkbutton(self, text=notes[5], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[5]))
        self.noteChecks[notes[5]].place(x=400, y=280)
        self.noteChecks[notes[5]].select()

        # D# checkbutton
        self.noteChecks[notes[6]] = tk.Checkbutton(self, text=notes[6], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[6]))
        self.noteChecks[notes[6]].place(x=400, y=300)
        self.noteChecks[notes[6]].select()

        # E checkbutton
        self.noteChecks[notes[7]] = tk.Checkbutton(self, text=notes[7], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[7]))
        self.noteChecks[notes[7]].place(x=400, y=320)
        self.noteChecks[notes[7]].select()

        # F checkbutton
        self.noteChecks[notes[8]] = tk.Checkbutton(self, text=notes[8], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[8]))
        self.noteChecks[notes[8]].place(x=400, y=340)
        self.noteChecks[notes[8]].select()

        # F# checkbutton
        self.noteChecks[notes[9]] = tk.Checkbutton(self, text=notes[9], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[9]))
        self.noteChecks[notes[9]].place(x=400, y=360)
        self.noteChecks[notes[9]].select()

        # G checkbutton
        self.noteChecks[notes[10]] = tk.Checkbutton(self, text=notes[10], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[10]))
        self.noteChecks[notes[10]].place(x=400, y=380)
        self.noteChecks[notes[10]].select()

        # G# checkbutton
        self.noteChecks[notes[11]] = tk.Checkbutton(self, text=notes[11], font=font, 
                                                   var=tk.IntVar(value=1), 
                                                   command=lambda: self.noteBoxChecked(notes[11]))
        self.noteChecks[notes[11]].place(x=400, y=400)
        self.noteChecks[notes[11]].select()

        octavesLabel = tk.Label(self, text='Octaves', font=font)
        octavesLabel.place(x=520, y=140)

        # CHECK BOXES GO HERE

        # this is the bar that keeps track of the score
        self.scoreLabel = tk.Label(self, text='0/0', font=font)
        self.scoreLabel.place(x=300, y=120)
        scoreFrame = tk.Frame(master=self, width=50, height=600, bg='red')
        scoreFrame.pack(expand=False)
        wrongLabel = tk.Label(scoreFrame, text='', borderwidth=2, relief='solid', 
                              width=8, height=20)
        wrongLabel.pack(anchor='sw')

        self.rightLabel = tk.Label(scoreFrame, borderwidth=2, relief='solid', width=8, 
                                   height=0, anchor='sw')
        # self.rightLabel.pack()
        scoreFrame.place(x=300, y=145)

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

            self.total += 1

            if self.firstTry:
                self.score += 1
            # call the function to redraw the green part of the label
            self.redrawScoreBar()
        # else turn the pressed button red
        else:
            self.firstTry = False
            self.buttons[buttonNote].config(bg=redBkg, state='disabled')


    def redrawScoreBar(self):
        """
        calculate the coordinates for the green 'correct' bar and redraw the label that displays
        the score
        """
        self.scoreLabel.config(text='{s}/{t}'.format(s=self.score, t=self.total))
        percent = self.score/self.total
        newHeight = int(percent*20)
        self.rightLabel.config(height=newHeight, bg='green')
        newY = int(15.25 * (20 - newHeight))  # 15.25 is height in pixels of 1 height unit
        self.rightLabel.place(x=0, y=newY)

    def noteBoxChecked(self, note):
        """
        adds the note of the checkbox to the queue's notes

        :param note: the note as a string
        """
        if self.queue.toggleNote(note) < 0:
            # we removed the note
            if not self.queue.validNote(note):
                self.queue.next()


    def playNextPressed(self):
        """
        called when the play next button is pressed, resets all of the note buttons and
        calls queue.next()
        """
        self.firstTry = True
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
