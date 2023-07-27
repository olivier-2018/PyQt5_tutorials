from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self, title:str=None):
        super().__init__()
        
        # Set Title
        self.setWindowTitle(title)
        
        # Set vertical layout 
        self.setLayout(QVBoxLayout())  
        
        # Create a label (text in window)
        my_label = QLabel("hello")    
        my_label.setFont(QFont("Helvetica", 18))
        self.layout().addWidget(my_label)
        
        # Create an entry box (text input box)
        my_entry = QLineEdit()
        my_entry.setObjectName("Name_field") # IDname for later ref
        my_entry.setText("Write something")
        self.layout().addWidget(my_entry)
        
        # Create a button
        my_button = QPushButton("Copy to label", clicked=lambda: fcn_button_press())
        self.layout().addWidget(my_button)
        
        # Show app
        self.show()
    
        def fcn_button_press():
            """Use the Entry text to format the label
            """
            # Capture text
            my_label.setText(f"Hello {my_entry.text()} !")
            # clear entry box
            my_entry.setText("Write something")
        
app = QApplication([])
mw = MainWindow(title="Hi")

# Run the app
app.exec()
