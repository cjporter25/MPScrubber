import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QListWidget, QCheckBox, 
                             QPushButton, QLabel, QGridLayout,
                             QSpacerItem, QSizePolicy, QLineEdit)
from PyQt5.QtCore import Qt

# Color Palette Constants
PRIMARY_GREEN = "#217346"
SECONDARY_GREEN = "#A9D18E"
PRIMARY_BLUE = "#1877F2"
SECONDARY_BLUE = "#E7F3FF"
DARK_GREY = "#333333"
LIGHT_GREY = "#F0F2F5"
ALERT_RED = "#FF0000"
WHITE = "#FFFFFF"




class ScrubberGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MBSCRUBBER")
        self.setGeometry(100, 100, 600, 400)  # Set window size and position

        # Main vertical layout
        main_layout = QVBoxLayout()

        # Add main title
        main_title = QLabel("MBSCRUBBER")
        main_title.setAlignment(Qt.AlignCenter)
        main_title.setStyleSheet("font-weight: bold; font-size: 24px; margin: 20px;")
        main_layout.addWidget(main_title)

        # Horizontal layout for filter sections
        filters_layout = QHBoxLayout()

        # Add Facebook and Excel layouts to the filters layout
        filters_layout.addLayout(self.create_facebook_layout())
        filters_layout.addLayout(self.create_excel_layout())

        # Add the filters layout to the main layout
        main_layout.addLayout(filters_layout)

        # Add a spacer item to push the Generate button to the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Generate button
        generate_button = QPushButton("Generate")
        generate_button.setStyleSheet("margin: 10px; padding: 10px;")
        generate_button.clicked.connect(self.generate_clicked)
        main_layout.addWidget(generate_button, alignment=Qt.AlignCenter)

         # Apply style sheet
        stylesheet = self.load_stylesheet("marketplace/stylesGUI.qss")
        if stylesheet:
            self.setStyleSheet(stylesheet)
        else:
            sys.exit(1)
        
        self.setLayout(main_layout)  

    def create_facebook_layout(self):
        filters = ["Price", "Mileage", "Year", "Make", "Sorting Type"]

        layoutFB = QVBoxLayout()
        title_label = QLabel("Facebook Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutFB.addWidget(title_label)

        grid_layout = QGridLayout()

        # Price
        label1 = QLabel("Price")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        price_min = QLineEdit()
        price_min.setPlaceholderText("Min")
        price_max = QLineEdit()
        price_max.setPlaceholderText("Max")
        grid_layout.addWidget(price_min, 1, 1)
        grid_layout.addWidget(price_max, 1, 2)

        # Mileage
        label2 = QLabel("Mileage")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        mileage_min = QLineEdit()
        mileage_min.setPlaceholderText("Min")
        mileage_max = QLineEdit()
        mileage_max.setPlaceholderText("Max")
        grid_layout.addWidget(mileage_min, 3, 1)
        grid_layout.addWidget(mileage_max, 3, 2)

        # Year
        label3 = QLabel("Year")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        year_min = QLineEdit()
        year_min.setPlaceholderText("Min")
        year_max = QLineEdit()
        year_max.setPlaceholderText("Max")
        grid_layout.addWidget(year_min, 5, 1)
        grid_layout.addWidget(year_max, 5, 2)

        # Make
        label4 = QLabel("Make")
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        make_checkbox1 = QCheckBox()
        make_checkbox2 = QCheckBox()
        grid_layout.addWidget(make_checkbox1, 7, 1)
        grid_layout.addWidget(make_checkbox2, 7, 2)

        # Sorting Type
        label5 = QLabel("Sorting Type")
        grid_layout.addWidget(label5, 8, 0, 1, 3)
        sorting_checkbox1 = QCheckBox()
        sorting_checkbox2 = QCheckBox()
        grid_layout.addWidget(sorting_checkbox1, 9, 1)
        grid_layout.addWidget(sorting_checkbox2, 9, 2)

        layoutFB.addLayout(grid_layout)
        return layoutFB
    
    def create_excel_layout(self):
        layoutEX = QVBoxLayout()
        title_label = QLabel("Excel Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutEX.addWidget(title_label)

        grid_layout = QGridLayout()

        # Date Pulled
        label1 = QLabel("Date Pulled")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        date_pulled_checkbox1 = QCheckBox()
        date_pulled_checkbox2 = QCheckBox()
        grid_layout.addWidget(date_pulled_checkbox1, 1, 1)
        grid_layout.addWidget(date_pulled_checkbox2, 1, 2)

        # Year
        label2 = QLabel("Year")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        year_min = QLineEdit()
        year_min.setPlaceholderText("Min")
        year_max = QLineEdit()
        year_max.setPlaceholderText("Max")
        grid_layout.addWidget(year_min, 3, 1)
        grid_layout.addWidget(year_max, 3, 2)

        # Price
        label3 = QLabel("Price")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        price_min = QLineEdit()
        price_min.setPlaceholderText("Min")
        price_max = QLineEdit()
        price_max.setPlaceholderText("Max")
        grid_layout.addWidget(price_min, 5, 1)
        grid_layout.addWidget(price_max, 5, 2)

        # Mileage
        label4 = QLabel("Mileage")
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        mileage_min = QLineEdit()
        mileage_min.setPlaceholderText("Min")
        mileage_max = QLineEdit()
        mileage_max.setPlaceholderText("Max")
        grid_layout.addWidget(mileage_min, 7, 1)
        grid_layout.addWidget(mileage_max, 7, 2)

        # Location
        label5 = QLabel("Location")
        grid_layout.addWidget(label5, 8, 0, 1, 3)
        location_checkbox1 = QCheckBox()
        location_checkbox2 = QCheckBox()
        grid_layout.addWidget(location_checkbox1, 9, 1)
        grid_layout.addWidget(location_checkbox2, 9, 2)

        layoutEX.addLayout(grid_layout)
        return layoutEX

    def generate_clicked(self):
        selectedOptions = [
            self.option_list.item(i).text()
            for i in range(self.option_list.count())
            if self.checkboxes[i].isChecked()
        ]

        print("Selected Options:", selectedOptions)

    # Offload stylesheet to an external file for main GUI code clarity
    def load_stylesheet(self, styleSheet):
        try:
            with open(styleSheet, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The stylesheet file '{styleSheet}' was not found.")
            return ""
    def button_clicked(self):
        print("Button clicked!")

                       