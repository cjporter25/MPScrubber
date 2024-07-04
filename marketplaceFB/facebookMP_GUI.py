import sys
import json
import os
import pprint

from marketplaceFB.facebookMP_scraper import *
from marketplaceFB.facebookMP_reporting import *


from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QListWidget, QCheckBox, 
                             QPushButton, QLabel, QGridLayout,
                             QSpacerItem, QSizePolicy, QLineEdit)
from PyQt5.QtCore import Qt



class ScrubberGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MBSCRUBBER")
        # (x), (y), (width), (height)
        # 100/100 means 100 pixels down and to the right from the top
        #       left of the screen
        self.setGeometry(200, 200, 800, 700)  # Set window size and position

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
        filters_layout.addLayout(self.create_facebook_filter_layout(), 1)
        filters_layout.addLayout(self.create_report_filter_layout(), 1)

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
        self.fbPriceMin = QLineEdit()
        self.fbPriceMax = QLineEdit()
        self.fbMileageMin = QLineEdit()
        self.fbMileageMax = QLineEdit()
        self.fbYearMin = QLineEdit()
        self.fbYearMax = QLineEdit()
        self.fbMakeAcura = QCheckBox("Acura")
        self.fbMakeAudi = QCheckBox("Audi")
        self.fbMakeBuick = QCheckBox("Buick")
        self.fbMakeChevy = QCheckBox("Chevy")
        self.fbMakeChrysler = QCheckBox("Chrysler")
        self.fbMakeDodge = QCheckBox("Dodge")
        self.fbMakeFord = QCheckBox("Ford")
        self.fbMakeGMC = QCheckBox("GMC")
        self.fbMakeHonda = QCheckBox("Honda")
        self.fbMakeHyundai = QCheckBox("Hyundai")
        self.fbMakeJeep = QCheckBox("Jeep")
        self.fbMakeLexus = QCheckBox("Lexus")
        self.fbMakeNissan = QCheckBox("Nissan")
        self.fbMakeRam = QCheckBox("Ram")
        self.fbMakeToyota= QCheckBox("Toyota")
        self.dateListedNewestFirst = QCheckBox("Date Listed: Newest First")
        self.dateListedOldestFirst = QCheckBox("Date Listed: Oldest First")
        self.mileageLowestFirst = QCheckBox("Mileage: Lowest First")
        self.mileageHighestFirst = QCheckBox("Mileage: Highest First")
        self.priceLowestFirst = QCheckBox("Price: Lowest First")
        self.priceHighestFirst = QCheckBox("Price: Highest First")

        # Initialize instance variables for Database filters
        self.datePulledNewestFirst = QCheckBox("Date Pulled: Newest First")
        self.datePulledOldestFirst = QCheckBox("Date Pulled: Oldest First")
        self.dbYearMin = QLineEdit()
        self.dbYearMax = QLineEdit()
        self.dbPriceMin = QLineEdit()
        self.dbPriceMax = QLineEdit()
        self.dbMileageMin = QLineEdit()
        self.dbMileageMax = QLineEdit()
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
        self.fbPriceMin.setPlaceholderText("Min")
        self.fbPriceMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbPriceMin, 1, 1)
        grid_layout.addWidget(self.fbPriceMax, 1, 2)

        # Mileage
        label2 = QLabel("Mileage")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.fbMileageMin.setPlaceholderText("Min")
        self.fbMileageMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbMileageMin, 3, 1)
        grid_layout.addWidget(self.fbMileageMax, 3, 2)

        # Year
        label3 = QLabel("Year")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.fbYearMin.setPlaceholderText("Min")
        self.fbYearMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbYearMin, 5, 1)
        grid_layout.addWidget(self.fbYearMax, 5, 2)

        # Make
        label4 = QLabel("Make")
        # addWidget(widget, row, column, rowSpan, columnSpan, alignment)
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        grid_layout.addWidget(self.fbMakeAudi, 7, 1)
        grid_layout.addWidget(self.fbMakeAcura, 7, 2)
        grid_layout.addWidget(self.fbMakeBuick, 8, 1)
        grid_layout.addWidget(self.fbMakeChevy, 8, 2)
        grid_layout.addWidget(self.fbMakeChrysler, 9, 1)
        grid_layout.addWidget(self.fbMakeDodge, 9, 2)
        grid_layout.addWidget(self.fbMakeFord, 10, 1)
        grid_layout.addWidget(self.fbMakeGMC, 10, 2)
        grid_layout.addWidget(self.fbMakeHonda, 11, 1)
        grid_layout.addWidget(self.fbMakeHyundai, 11, 2)
        grid_layout.addWidget(self.fbMakeJeep, 12, 1)
        grid_layout.addWidget(self.fbMakeLexus, 12, 2)
        grid_layout.addWidget(self.fbMakeNissan, 13, 1)
        grid_layout.addWidget(self.fbMakeRam, 13, 2)
        grid_layout.addWidget(self.fbMakeToyota, 14, 1)

        # Sorting Type
        label5 = QLabel("Sorting Type")
        grid_layout.addWidget(label5, 15, 0, 1, 3)
        grid_layout.addWidget(self.dateListedNewestFirst, 16, 1)
        grid_layout.addWidget(self.dateListedOldestFirst, 16, 2)
        grid_layout.addWidget(self.mileageLowestFirst, 17, 1)
        grid_layout.addWidget(self.mileageHighestFirst, 17, 2)
        grid_layout.addWidget(self.priceLowestFirst, 18, 1)
        grid_layout.addWidget(self.priceHighestFirst, 18, 2)

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
        grid_layout.addWidget(self.datePulledNewestFirst, 1, 1)
        grid_layout.addWidget(self.datePulledOldestFirst, 1, 2)

        # Year
        label2 = QLabel("Year")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.dbYearMin.setPlaceholderText("Min")
        self.dbYearMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbYearMin, 3, 1)
        grid_layout.addWidget(self.dbYearMax, 3, 2)

        # Price
        label3 = QLabel("Price")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.dbPriceMin.setPlaceholderText("Min")
        self.dbPriceMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbPriceMin, 5, 1)
        grid_layout.addWidget(self.dbPriceMax, 5, 2)

        # Mileage
        label4 = QLabel("Mileage")
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        self.dbMileageMin.setPlaceholderText("Min")
        self.dbMileageMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbMileageMin, 7, 1)
        grid_layout.addWidget(self.dbMileageMax, 7, 2)

        # Location
        label5 = QLabel("Location")
        grid_layout.addWidget(label5, 8, 0, 1, 3)
        grid_layout.addWidget(self.location_checkbox1, 9, 1)
        grid_layout.addWidget(self.location_checkbox2, 9, 2)

        layoutEX.addLayout(grid_layout)
        return layoutEX

    def generate_report(self):
        filters = {
            "scrappingFilters": {
                "Price": {"Min": self.fbPriceMin.text(), "Max": self.fbPriceMax.text()},
                "Mileage": {"Min": self.fbMileageMin.text(), "Max": self.fbMileageMax.text()},
                "Year": {"Min": self.fbYearMin.text(), "Max": self.fbYearMax.text()},
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
                    "dateListedNewestFirst": self.dateListedNewestFirst.isChecked(),
                    "dateListedOldestFirst": self.dateListedOldestFirst.isChecked(),
                    "mileageLowestFirst": self.mileageLowestFirst.isChecked(),
                    "mileageHighestFirst": self.mileageHighestFirst.isChecked(),
                    "priceLowestFirst": self.priceLowestFirst.isChecked(),
                    "priceHighestFirst": self.priceHighestFirst.isChecked(),
                }
            },
            "databaseFilters": {
                "Date Pulled": {
                    "datePulledNewestFirst": self.datePulledNewestFirst.isChecked(),
                    "datePulledOldestFirst": self.datePulledOldestFirst.isChecked(),
                },
                "Year": {"Min": self.dbYearMin.text(), "Max": self.dbYearMax.text()},
                "Price": {"Min": self.dbPriceMin.text(), "Max": self.dbPriceMax.text()},
                "Mileage": {"Min": self.mileage_min_ex.text(), "Max": self.mileage_max_ex.text()},
                "Location": {
                    "Location 1": self.location_checkbox1.isChecked(),
                    "Location 2": self.location_checkbox2.isChecked(),
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

                       