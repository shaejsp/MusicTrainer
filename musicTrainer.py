from tkinter import *

class myButton(Button):
	def __init__(self, parent, note, *args, **kwargs):
		Button.__init__(self, parent, *args, **kwargs)
		self.note = note

	def pressed(self, event):
		print(self.note)


def buttonPress(note):
	print(note['text'])


def quit():
	exit()


def main():
	root = Tk()
	root.title('Music Trainer')
	root.geometry("500x500")

	notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	buttons = []

	for i in range(len(notes)):
		b = myButton(root,notes[i], text=notes[i])  #, command=buttonPress(self))
		b.bind('<Button-1>', b.pressed)
		b.place(x=50*i, y=200)
		buttons.append(b)

	# B = Button(root, text = "Press Me", command=buttonPress('A'))
	# B.place(x = 0,y = 0)
	root.mainloop()


if __name__ == '__main__':
	main()
