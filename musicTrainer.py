import tkinter as tk
from random import randint

global notes
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


class myButton(tk.Button):
    """ adds the note field to tkinter buttons """
    def __init__(self, parent, note, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.note = note

    def pressed(self, event):
        """
        event handler for when a button with a note on it is pressed - prints the note
        """
        print(self.note)


class noteQueue():
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


def quit():
    """
    eventhandler for the quit button - quits the application
    """
    exit()


def play(note):
    """
    plays a note

    :param note: the note to play
    """
    print(note)


def main():
    root = tk.Tk()
    root.title('Music Trainer')
    root.geometry("700x500")

    buttons = []

    queue = noteQueue()  # handles playing a random note

    # adds all of the buttons to the list
    for i in range(len(notes)):
        b = myButton(root, notes[i], text='{n:^3s}'.format(n=notes[i]), font='Courier 12',
                     bg='#c4c4c4')
        b.bind('<Button-1>', b.pressed)  # adds event handler
        b.place(x=50*i+5, y=200)
        buttons.append(b)

    # creates the quit button
    quitButton = tk.Button(root, text='Quit', command=quit)
    quitButton.place(x=5, y=5)

    # creates the play note button
    playButton = tk.Button(root, text='Play Note', command=queue.play)
    playButton.place(x=45, y=5)

    # creates the play next button
    playNextButton = tk.Button(root, text='Play Next', command=queue.next)
    playNextButton.place(x=115, y=5)

    # runs the main app
    root.mainloop()


if __name__ == '__main__':
    main()
