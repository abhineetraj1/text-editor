# text-editor
Hi !! this is text editor , made in Python 3.6

## Functions:-

1) For saving file
```
def save_file():
	mn= sd.askstring("Save","Enter the filename")
	sl.copy(os.listdir()[0],mn)
	open(mn,"w").write(ed.get("1.0",END))
	msg.showinfo("Save","Your file is saved")
```

2) For openning file
```
def open_file():
	mn= sd.askstring("Open","Enter the filename")
	open(mn,"r+").read()
	ed.insert(END,open(mn,"r+").read())
```
