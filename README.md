# Text-editor
Hi !! this is text editor , made in Python 3.6

You need to install python3.6 to execute this file

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

# Demo (For Windows 8 | 10 | 11)
* Download file from [here](http://github.com/abhineetraj1/text-editor/raw/main/app.exe)
* Run app.exe file

# Programming language used
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
