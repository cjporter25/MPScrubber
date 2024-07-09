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


# PrimaryKey TEXT,
# DatePulled TEXT,
# DatePosted TEXT,
# Year INT,
# Price INT,
# Mileage INT,
# Description TEXT,
# Location TEXT,
# Link TEXT


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

        # Generate button
        generate_button = QPushButton("Generate")
        generate_button.setStyleSheet("margin: 10px; padding: 10px;")
        generate_button.clicked.connect(self.generate_report)
        main_layout.addWidget(generate_button, alignment=Qt.AlignCenter)

        # Add a spacer item to push everything up
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))



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
        self.locStPaul = QCheckBox("St. Paul")
        self.locMinneapolis = QCheckBox("Minneapolis")

        # Initialize instance variables for Database filters
        
        self.dbYearMin = QLineEdit()
        self.dbYearMax = QLineEdit()
        self.dbPriceMin = QLineEdit()
        self.dbPriceMax = QLineEdit()
        self.dbMileageMin = QLineEdit()
        self.dbMileageMax = QLineEdit()
        self.dbMakeAcura = QCheckBox("Acura")
        self.dbMakeAudi = QCheckBox("Audi")
        self.dbMakeBuick = QCheckBox("Buick")
        self.dbMakeChevy = QCheckBox("Chevy")
        self.dbMakeChrysler = QCheckBox("Chrysler")
        self.dbMakeDodge = QCheckBox("Dodge")
        self.dbMakeFord = QCheckBox("Ford")
        self.dbMakeGMC = QCheckBox("GMC")
        self.dbMakeHonda = QCheckBox("Honda")
        self.dbMakeHyundai = QCheckBox("Hyundai")
        self.dbMakeJeep = QCheckBox("Jeep")
        self.dbMakeLexus = QCheckBox("Lexus")
        self.dbMakeNissan = QCheckBox("Nissan")
        self.dbMakeRam = QCheckBox("Ram")
        self.dbMakeToyota= QCheckBox("Toyota")
        self.datePostedNewestFirst = QCheckBox("Date Posted: Newest First")
        self.datePostedOldestFirst = QCheckBox("Date Posted: Oldest First")
        self.dateScrapedNewestFirst = QCheckBox("Date Scraped: Newest First")
        self.dateScrapedOldestFirst = QCheckBox("Date Scraped: Oldest First")
        self.dbLocationAlpha = QCheckBox("Location: A-Z")
        self.dbLocationAlphaRev = QCheckBox("Location: Z-A")

    def create_facebook_filter_layout(self):
        layoutFB = QVBoxLayout()
        title_label = QLabel("Facebook Scraping Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutFB.addWidget(title_label)

        grid_layout = QGridLayout()

        # Price
        label1 = QLabel("Price (0 - $50,000)")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        self.fbPriceMin.setPlaceholderText("Min")
        self.fbPriceMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbPriceMin, 1, 1)
        grid_layout.addWidget(self.fbPriceMax, 1, 2)

        # Mileage
        label2 = QLabel("Mileage (0 - 200,000)")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.fbMileageMin.setPlaceholderText("Min")
        self.fbMileageMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbMileageMin, 3, 1)
        grid_layout.addWidget(self.fbMileageMax, 3, 2)

        # Year
        label3 = QLabel("Year (2000 - 2024)")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.fbYearMin.setPlaceholderText("Min")
        self.fbYearMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.fbYearMin, 5, 1)
        grid_layout.addWidget(self.fbYearMax, 5, 2)

        # Make
        label4 = QLabel("Make (15 per)")
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

        label5 = QLabel("Location (Choose 1)")
        grid_layout.addWidget(label5, 15, 0, 1, 3)
        grid_layout.addWidget(self.locMinneapolis, 16, 1)
        grid_layout.addWidget(self.locStPaul, 16, 2)

        # Sorting Type
        label6 = QLabel("Sorting Type (Choose 1)")
        grid_layout.addWidget(label6, 17, 0, 1, 3)
        grid_layout.addWidget(self.dateListedNewestFirst, 18, 1)
        grid_layout.addWidget(self.dateListedOldestFirst, 18, 2)
        grid_layout.addWidget(self.mileageLowestFirst, 19, 1)
        grid_layout.addWidget(self.mileageHighestFirst, 19, 2)
        grid_layout.addWidget(self.priceLowestFirst, 20, 1)
        grid_layout.addWidget(self.priceHighestFirst, 20, 2)

        layoutFB.addLayout(grid_layout)
        return layoutFB
    def create_report_filter_layout(self):
        layoutEX = QVBoxLayout()
        title_label = QLabel("Database Report Filters")
        title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutEX.addWidget(title_label)

        grid_layout = QGridLayout()

        # Year
        label1 = QLabel("Year")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        self.dbYearMin.setPlaceholderText("Min")
        self.dbYearMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbYearMin, 1, 1)
        grid_layout.addWidget(self.dbYearMax, 1, 2)

        # Price
        label2 = QLabel("Price")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        self.dbPriceMin.setPlaceholderText("Min")
        self.dbPriceMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbPriceMin, 3, 1)
        grid_layout.addWidget(self.dbPriceMax, 3, 2)

        # Mileage
        label3 = QLabel("Mileage")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        self.dbMileageMin.setPlaceholderText("Min")
        self.dbMileageMax.setPlaceholderText("Max")
        grid_layout.addWidget(self.dbMileageMin, 5, 1)
        grid_layout.addWidget(self.dbMileageMax, 5, 2)

        label4 = QLabel("Make")
                  # addWidget(widget, row, column, rowSpan, columnSpan, alignment)
        grid_layout.addWidget(label4, 6, 0, 1, 3)
        grid_layout.addWidget(self.dbMakeAudi, 7, 1)
        grid_layout.addWidget(self.dbMakeAcura, 7, 2)
        grid_layout.addWidget(self.dbMakeBuick, 8, 1)
        grid_layout.addWidget(self.dbMakeChevy, 8, 2)
        grid_layout.addWidget(self.dbMakeChrysler, 9, 1)
        grid_layout.addWidget(self.dbMakeDodge, 9, 2)
        grid_layout.addWidget(self.dbMakeFord, 10, 1)
        grid_layout.addWidget(self.dbMakeGMC, 10, 2)
        grid_layout.addWidget(self.dbMakeHonda, 11, 1)
        grid_layout.addWidget(self.dbMakeHyundai, 11, 2)
        grid_layout.addWidget(self.dbMakeJeep, 12, 1)
        grid_layout.addWidget(self.dbMakeLexus, 12, 2)
        grid_layout.addWidget(self.dbMakeNissan, 13, 1)
        grid_layout.addWidget(self.dbMakeRam, 13, 2)
        grid_layout.addWidget(self.dbMakeToyota, 14, 1)

        # Date Posted
        label6 = QLabel("Date Posted")
        grid_layout.addWidget(label6, 15, 0, 1, 3)
        grid_layout.addWidget(self.datePostedNewestFirst, 16, 1)
        grid_layout.addWidget(self.datePostedOldestFirst, 16, 2)

        # Date Pulled
        label6 = QLabel("Date Scraped")
        grid_layout.addWidget(label6, 17, 0, 1, 3)
        grid_layout.addWidget(self.dateScrapedNewestFirst, 18, 1)
        grid_layout.addWidget(self.dateScrapedOldestFirst, 18, 2)

        # Location
        label7 = QLabel("Location")
        grid_layout.addWidget(label7, 19, 0, 1, 3)
        grid_layout.addWidget(self.dbLocationAlpha, 20, 1)
        grid_layout.addWidget(self.dbLocationAlphaRev, 20, 2)

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
                "Location": {"St.Paul": self.locStPaul.isChecked(),
                             "Minneapolis": self.locMinneapolis.isChecked()},
            
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
                "Date Pulled": {"NewestFirst": self.dateScrapedNewestFirst.isChecked(),
                                "OldestFirst": self.dateScrapedOldestFirst.isChecked(),},
                "Year": {"Min": self.dbYearMin.text(), "Max": self.dbYearMax.text()},
                "Price": {"Min": self.dbPriceMin.text(), "Max": self.dbPriceMax.text()},
                "Mileage": {"Min": self.dbMileageMin.text(), "Max": self.dbMileageMax.text()},
                "Location": {"Alphabetical": self.dbLocationAlpha.isChecked(), 
                             "AlphabeticalRev": self.dbLocationAlphaRev.isChecked(),}
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

                       