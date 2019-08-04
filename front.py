from tkinter import *

def output(event):
	print(event)
	try:
		txt = entry.get()
		if int(txt) < 18:
			label['text'] = 'go out'
		else:
			label['text'] = 'good for you'
	except ValueError:
		print('fail')

root = Tk()

root.title('ololo')

entry = Entry(root, width=16, font=9)
btn = Button(root, text='check')
label = Label(root, width=16, font=7)

entry.grid(row=0, column=0)
btn.grid(row=0, column=1)
label.grid(row=0, column=2)

btn.bind('<Button-1>', output)

root.mainloop()
