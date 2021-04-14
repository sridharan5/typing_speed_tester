# from time import sleep
# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# content = ttk.Frame(root)
# frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)
#
# onevar = BooleanVar(value=True)
# twovar = BooleanVar(value=False)
# threevar = BooleanVar(value=True)
#
# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")
#
# # grids
# content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)
#
#
# root.mainloop()
# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("450x200")

x = 0

# defining the function for the test
def game():
	global x

	# loop for destroying the window
	# after on test
	if x == 0:
		window.destroy()
		x = x+1

	# defining function for results of test
	def check_result():
		if entry.get() == words[word]:

			# here start time is when the window
			# is opened and end time is when
			# window is destroyed
			end = timer()

			# we deduct the start time from end
			# time and calculate results using
			# timeit function
			print(end-start)
		else:
			print("Wrong Input")

	words = ['programming', 'coding', 'algorithm',
			'systems', 'python', 'software']

	# Give random words for testing the speed of user
	word = random.randint(0, (len(words)-1))

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("450x200")

	# use lable method of tkinter for labling in window
	x2 = Label(windows, text=words[word], font="times 20")

	# place of labling in window
	x2.place(x=150, y=10)
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows)
	entry.place(x=280, y=55)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
				command=check_result, width=12, bg='grey')
	b2.place(x=150, y=100)

	b3 = Button(windows, text="Try Again",
				command=game, width=12, bg='grey')
	b3.place(x=250, y=100)
	windows.mainloop()


x1 = Label(window, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg='grey')
b1.place(x=150, y=100)

# calling window
window.mainloop()
