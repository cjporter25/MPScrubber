import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QListWidget, QCheckBox, 
                             QPushButton, QLabel, QGridLayout,
                             QSpacerItem, QSizePolicy, QLineEdit)
from PyQt5.QtCore import Qt
import pprint

class ScrubberGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MBSCRUBBER")
        # (x), (y), (width), (height)
        # 100/100 means 100 pixels down and to the right from the top
        #       left of the screen
        self.setGeometry(100, 100, 600, 400)  # Set window size and position

        self.init_variables()

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
        filters_layout.addLayout(self.create_facebook_filter_layout())
        filters_layout.addLayout(self.create_report_filter_layout())

        # Add the filters layout to the main layout
        main_layout.addLayout(filters_layout)

        # Add a spacer item to push the Generate button to the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Generate button
        generate_button = QPushButton("Generate")
        generate_button.setStyleSheet("margin: 10px; padding: 10px;")
        generate_button.clicked.connect(self.generate_report)
        main_layout.addWidget(generate_button, alignment=Qt.AlignCenter)

         # Apply style sheet
        stylesheet = self.load_stylesheet("marketplaceFB/GUI_styles.qss")
        if stylesheet:
            self.setStyleSheet(stylesheet)
        else:
            sys.exit(1)
        
        self.setLayout(main_layout)  
    def init_variables(self):
        # Initialize instance variables for Facebook filters
        self.price_min_fb = QLineEdit()
        self.price_max_fb = QLineEdit()
        self.mileage_min_fb = QLineEdit()
        self.mileage_max_fb = QLineEdit()
        self.year_min_fb = QLineEdit()
        self.year_max_fb = QLineEdit()
        self.fbMakeAcura = QCheckBox("Acura")
        self.fbMakeAudi = QCheckBox("Audi")
        self.fbMakeBuick = QCheckBox("Buick")
        self.fbMakeChevy= QCheckBox("Chevy")
        self.fbMakeChrysler= QCheckBox("Chrysler")
        self.fbMakeDodge= QCheckBox("Dodge")
        self.fbMakeFord= QCheckBox("Ford")
        self.fbMakeGMC= QCheckBox("GMC")
        self.fbMakeHonda= QCheckBox("Honda")
        self.fbMakeHyundai= QCheckBox("Hyundai")
        self.fbMakeJeep= QCheckBox("Jeep")
        self.fbMakeLexus= QCheckBox("Lexus")
        self.fbMakeNissan= QCheckBox("Nissan")
        self.fbMakeRam= QCheckBox("Ram")
        self.fbMakeToyota= QCheckBox("Toyota")
        self.sorting_checkbox1_fb = QCheckBox("Sort 1")
        self.sorting_checkbox2_fb = QCheckBox("Sort 2")

        # Initialize instance variables for Database filters
        self.date_pulled_checkbox1 = QCheckBox("Date 1")
        self.date_pulled_checkbox2 = QCheckBox("Date 2")
        self.year_min_ex = QLineEdit()
        self.year_max_ex = QLineEdit()
        self.price_min_ex = QLineEdit()
        self.price_max_ex = QLineEdit()
        self.mileage_min_ex = QLineEdit()
        self.mileage_max_ex = QLineEdit()
        self.location_checkbox1 = QCheckBox("Location 1")
        self.location_checkbox2 = QCheckBox("Location 2")

    def create_facebook_filter_layout(self):
        layoutFB = QVBoxLayout()
        title_label = QLabel("Facebook Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutFB.addWidget(title_label)

        grid_layout = QGridLayout()

        # Price
        label1 = QLabel("Price")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        self.price_min_fb.setPlaceholderText("Min")
        self.price_max_fb.setPlaceholderText("Max")
        grid_layout.addWidget(self.price_min_fb, 1, 1)
        grid_layout.addWidget(self.price_max_fb, 1, 2)

        # Mileage
        label2 = QLabel("Mileage")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.mileage_min_fb.setPlaceholderText("Min")
        self.mileage_max_fb.setPlaceholderText("Max")
        grid_layout.addWidget(self.mileage_min_fb, 3, 1)
        grid_layout.addWidget(self.mileage_max_fb, 3, 2)

        # Year
        label3 = QLabel("Year")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.year_min_fb.setPlaceholderText("Min")
        self.year_max_fb.setPlaceholderText("Max")
        grid_layout.addWidget(self.year_min_fb, 5, 1)
        grid_layout.addWidget(self.year_max_fb, 5, 2)

        # Make
        label4 = QLabel("Make")
        # addWidget(widget, row, column, rowSpan, columnSpan, alignment)
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        grid_layout.addWidget(self.fbMakeAudi, 7, 1)
        grid_layout.addWidget(self.fbMakeAcura, 7, 2)
        grid_layout.addWidget(self.fbMakeBuick, 7, 3)
        grid_layout.addWidget(self.fbMakeChevy, 8, 1)
        grid_layout.addWidget(self.fbMakeChrysler, 8, 2)
        grid_layout.addWidget(self.fbMakeDodge, 8, 3)
        grid_layout.addWidget(self.fbMakeFord, 9, 1)
        grid_layout.addWidget(self.fbMakeGMC, 9, 2)
        grid_layout.addWidget(self.fbMakeHonda, 9, 3)
        grid_layout.addWidget(self.fbMakeHyundai, 10, 1)
        grid_layout.addWidget(self.fbMakeJeep, 10, 2)
        grid_layout.addWidget(self.fbMakeLexus, 10, 3)
        grid_layout.addWidget(self.fbMakeNissan, 11, 1)
        grid_layout.addWidget(self.fbMakeRam, 11, 2)
        grid_layout.addWidget(self.fbMakeToyota, 11, 3)

        # Sorting Type
        label5 = QLabel("Sorting Type")
        grid_layout.addWidget(label5, 12, 0, 1, 3)
        grid_layout.addWidget(self.sorting_checkbox1_fb, 13, 1)
        grid_layout.addWidget(self.sorting_checkbox2_fb, 13, 2)

        layoutFB.addLayout(grid_layout)
        return layoutFB
    def create_report_filter_layout(self):
        layoutEX = QVBoxLayout()
        title_label = QLabel("Database Report Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutEX.addWidget(title_label)

        grid_layout = QGridLayout()

        # Date Pulled
        label1 = QLabel("Date Pulled")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        grid_layout.addWidget(self.date_pulled_checkbox1, 1, 1)
        grid_layout.addWidget(self.date_pulled_checkbox2, 1, 2)

        # Year
        label2 = QLabel("Year")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.year_min_ex.setPlaceholderText("Min")
        self.year_max_ex.setPlaceholderText("Max")
        grid_layout.addWidget(self.year_min_ex, 3, 1)
        grid_layout.addWidget(self.year_max_ex, 3, 2)

        # Price
        label3 = QLabel("Price")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.price_min_ex.setPlaceholderText("Min")
        self.price_max_ex.setPlaceholderText("Max")
        grid_layout.addWidget(self.price_min_ex, 5, 1)
        grid_layout.addWidget(self.price_max_ex, 5, 2)

        # Mileage
        label4 = QLabel("Mileage")
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        self.mileage_min_ex.setPlaceholderText("Min")
        self.mileage_max_ex.setPlaceholderText("Max")
        grid_layout.addWidget(self.mileage_min_ex, 7, 1)
        grid_layout.addWidget(self.mileage_max_ex, 7, 2)

        # Location
        label5 = QLabel("Location")
        grid_layout.addWidget(label5, 8, 0, 1, 3)
        grid_layout.addWidget(self.location_checkbox1, 9, 1)
        grid_layout.addWidget(self.location_checkbox2, 9, 2)

        layoutEX.addLayout(grid_layout)
        return layoutEX

    def generate_report(self):
        filters = {
            "facebookFilters": {
                "Price": {"Min": self.price_min_fb.text(), "Max": self.price_max_fb.text()},
                "Mileage": {"Min": self.mileage_min_fb.text(), "Max": self.mileage_max_fb.text()},
                "Year": {"Min": self.year_min_fb.text(), "Max": self.year_max_fb.text()},
                "Make": {
                    "Acura": self.fbMakeAcura.isChecked(),
                    "Audi": self.fbMakeAudi.isChecked(),
                    "Buick": self.fbMakeBuick.isChecked(),
                    "Chevy": self.fbMakeChevy.isChecked(),
                    "Chrysler": self.fbMakeChrysler.isChecked(),
                    "Dodge": self.fbMakeDodge.isChecked(),
                    "Ford": self.fbMakeFord.isChecked(),
                    "GMC": self.fbMakeGMC.isChecked(),
                    "Honda": self.fbMakeHonda.isChecked(),
                    "Hyundai": self.fbMakeHyundai.isChecked(),
                    "Jeep": self.fbMakeJeep.isChecked(),
                    "Lexus": self.fbMakeLexus.isChecked(),
                    "Nissan": self.fbMakeNissan.isChecked(),
                    "Ram": self.fbMakeRam.isChecked(),
                    "Toyota": self.fbMakeToyota.isChecked(),
                },
                "Sorting Type": {
                    "Sort 1": self.sorting_checkbox1_fb.isChecked(),
                    "Sort 2": self.sorting_checkbox2_fb.isChecked()
                }
            },
            "excelFilters": {
                "Date Pulled": {
                    "Date 1": self.date_pulled_checkbox1.isChecked(),
                    "Date 2": self.date_pulled_checkbox2.isChecked()
                },
                "Year": {"Min": self.year_min_ex.text(), "Max": self.year_max_ex.text()},
                "Price": {"Min": self.price_min_ex.text(), "Max": self.price_max_ex.text()},
                "Mileage": {"Min": self.mileage_min_ex.text(), "Max": self.mileage_max_ex.text()},
                "Location": {
                    "Location 1": self.location_checkbox1.isChecked(),
                    "Location 2": self.location_checkbox2.isChecked()
                }
            }
        }

        pprint.pprint(filters)

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

                       