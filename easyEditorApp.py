import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Dialogue for opening files (and folders)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')

## ----------------Add Widgets ----------------------##
btn_dir = QPushButton("Folder")
list_files = QListWidget()

place_image = QLabel("Image")

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_mirror = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")


## ----------------Add Layout ----------------------##
row = QHBoxLayout()          # Main line

col1 = QVBoxLayout()         # divided into two columns
col1.addWidget(btn_dir)      # in the first - directory selection button
col1.addWidget(list_files)     # and file list

col2 = QVBoxLayout()
col2.addWidget(place_image, 95) # in the second - image

row_tools = QHBoxLayout()    # and button bar
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_mirror)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


## ---------------- Info from os ----------------------##
workdir = ''

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   list_files.clear()
   for filename in filenames:
       list_files.addItem(filename)


win.show()
btn_dir.clicked.connect(showFilenamesList)

app.exec()
