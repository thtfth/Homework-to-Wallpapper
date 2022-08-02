import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
from PyQt5.QtCore import *

class MainWindow(qtw.QWidget):
    def __init__(self):

        global folder_path
        global subject1Detail
        global subject2Detail
        global subject3Detail
    


        def pick_folder():
            
            dialog = qtw.QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            path.insert(folder_path)
            return folder_path


#        def saveSubject1():
#
#            subject1Detail = detail1.toPlainText()
#            print(subject1Detail)
# 
#
#        def saveSubject2():
#            
#            subject2Detail = detail2.toPlainText()
#            print(subject2Detail)
#    
#
#        def saveSubject3():
#            
#            subject3Detail = detail3.toPlainText()
#            print(subject3Detail)
#        
#
#        def saveAll():
#            saveAlert = qtw.QMessageBox()
#            saveAlert.setWindowTitle("Info saved!")
#            saveAlert.setText(f"Your homework has been save to a text file under this folder! \n {subject1Detail}")
#            pass
            




        super().__init__()

        custom_font = qtg.QFont()
        custom_font.setFamily("Segoe UI")
        custom_font.setPointSize(11)

        # self.label.setAlignment(Qt.AlignCenter)

        
        qtw.QApplication.setFont(custom_font, "QLabel")
        # Set a title
        self.setWindowTitle('Homework to Wallpaper!')

        # Set a vertical layout
        self.setLayout(qtw.QVBoxLayout()) 

        # Create a label
        warning = qtw.QLabel("WARNING: THIS PROGRAM WILL CHANGE YOUR WALLPAPER INSTANTLY AFTER IT'S FINISHED. PLS REMEMBER TO RECORD THE OLD WALLPAPER FILE LOCATION")
        copyright = qtw.QLabel("Copyright to Leo Yu")

        # Browse for the folder location
        path = qtw.QLineEdit()
        path.setObjectName("folder location")
        path.setText("")

        # Browse button
        browse = qtw.QPushButton("Browse Folder", clicked = lambda: pick_folder())

        

        # boxes
        #subject1 = qtw.QLabel('Subject #1')
        #detail1 = qtw.QTextEdit()
        #detailSubject1 = qtw.QPushButton("Save Subject1", clicked = lambda: saveSubject1())

        #subject2 = qtw.QLabel('Subject #2')
        #detail2 = qtw.QTextEdit()
        #detailSubject2 = qtw.QPushButton("SaveSubject2", clicked = lambda: saveSubject2())

        #subject3 = qtw.QLabel('Subject #3')
        #detail3 = qtw.QTextEdit()
        #detailSubject3 = qtw.QPushButton("SaveSubject3", clicked = lambda: saveSubject3())

        #save = qtw.QPushButton('Save', clicked = lambda: saveAll())

        # Fixed. Don't need to change the font manually. Just use custom_font.
        # Change the font size for the label
        # warning.setFont(qtg.QFont(custom_font, 11))

        # layout?
        self.layout().addWidget(warning)
        self.layout().addWidget(copyright)

        self.layout().addWidget(path)
        self.layout().addWidget(browse)

        #self.layout().addWidget(subject1)
        #self.layout().addWidget(detail1)
        #self.layout().addWidget(detailSubject1)

        #self.layout().addWidget(subject2)
        #self.layout().addWidget(detail2)
        #self.layout().addWidget(detailSubject2)

        #self.layout().addWidget(subject3)
        #self.layout().addWidget(detail3)
        #self.layout().addWidget(detailSubject3)

        #self.layout().addWidget(save)


        self.show()




app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_() 

