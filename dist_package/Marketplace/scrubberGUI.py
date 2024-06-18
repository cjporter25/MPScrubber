import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QListWidget, 
    QCheckBox, 
    QPushButton
)
from PyQt5.QtCore import Qt

class ScrubberGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        # Create a layout
        main_layout = QHBoxLayout()

        # Left side: List of options with checkboxes
        self.option_list = QListWidget()
        self.option_list.addItems(["Option 1", "Option 2", "Option 3"])

        # Right side: Generate button
        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(self.generate_clicked)

        # Add checkboxes to the option list
        self.checkboxes = []
        for i in range(self.option_list.count()):
            checkbox = QCheckBox()
            self.checkboxes.append(checkbox)
            self.option_list.setItemWidget(self.option_list.item(i), checkbox)

        # Add widgets to the main layout
        main_layout.addWidget(self.option_list)
        main_layout.addWidget(generate_button)

        self.resize(500, 500)

        # Apply dark mode style sheet
        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                color: #ffffff;
            }
            QPushButton {
                background-color: #555555;
                color: #ffffff;
                border: 1px solid #ffffff;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
            QPushButton:pressed {
                background-color: #999999;
            }
        """)

        self.setLayout(main_layout)  

    def generate_clicked(self):
        selected_options = [
            self.option_list.item(i).text()
            for i in range(self.option_list.count())
            if self.checkboxes[i].isChecked()
        ]

        print("Selected Options:", selected_options)
    
    def initUI(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a button
        self.button = QPushButton("Test Button")
        self.button.clicked.connect(self.button_clicked)

        # Add the button to the layout
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

    def button_clicked(self):
        print("Button clicked!")

# EXAMPLE BASIC GUI
#import tkinter as tk
#class MainWindow:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("MP-Scrubber")

#        self.frame = tk.Frame(self.root, width=200, height=200, bg="white")
#        self.frame.pack()
#
#        self.button = tk.Button(self.frame, text="Test", command=self.button_clicked)
#        self.button.pack(side="left", padx=10, pady=100)
#
#    def button_clicked(self):
#        print("Button was clicked!")
                       