import sys
import json
import os
import pprint
import random

from marketplaceFB.facebookMP_scraper import *
from marketplaceFB.facebookMP_reporting import *
from marketplaceFB.facebookMP_notifications import *


from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QListWidget, QCheckBox, 
                             QPushButton, QLabel, QGridLayout,
                             QSpacerItem, QSizePolicy, QLineEdit)
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal


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
        self.setGeometry(200, 200, 0, 0)  # Set window size and position
        # Set fixed window size
        self.setFixedSize(800, 1000)  # Width: 800, Height: 700

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

        # Add the buttons layout to the main layout
        main_layout.addLayout(self.create_button_layout())

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
        self.fbYearMin = QLineEdit()
        self.fbYearMin.setPlaceholderText("Min")
        self.fbYearMax = QLineEdit()
        self.fbYearMax.setPlaceholderText("Max")
        self.fbPriceMin = QLineEdit()
        self.fbPriceMin.setPlaceholderText("Min")
        self.fbPriceMax = QLineEdit()
        self.fbPriceMax.setPlaceholderText("Max")
        self.fbMileageMin = QLineEdit()
        self.fbMileageMin.setPlaceholderText("Min")
        self.fbMileageMax = QLineEdit()
        self.fbMileageMax.setPlaceholderText("Max")
        
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
        self.fbDateListedNewestFirst = QCheckBox("Date Listed: Newest First")
        self.fbDateListedOldestFirst = QCheckBox("Date Listed: Oldest First")
        self.mileageLowestFirst = QCheckBox("Mileage: Lowest First")
        self.mileageHighestFirst = QCheckBox("Mileage: Highest First")
        self.priceLowestFirst = QCheckBox("Price: Lowest First")
        self.priceHighestFirst = QCheckBox("Price: Highest First")
        self.locStPaul = QCheckBox("St. Paul")
        self.locMinneapolis = QCheckBox("Minneapolis")

        # Initialize instance variables for Database filters
        self.dbYearMin = QLineEdit()
        self.dbYearMin.setPlaceholderText("Min")
        self.dbYearMax = QLineEdit()
        self.dbYearMax.setPlaceholderText("Max")
        self.dbPriceMin = QLineEdit()
        self.dbPriceMin.setPlaceholderText("Min")
        self.dbPriceMax = QLineEdit()
        self.dbPriceMax.setPlaceholderText("Max")
        self.dbMileageMin = QLineEdit()
        self.dbMileageMin.setPlaceholderText("Min")
        self.dbMileageMax = QLineEdit()
        self.dbMileageMax.setPlaceholderText("Max")
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
        self.dbDatePostedNewestFirst = QCheckBox("Date Posted: Newest First")
        self.dbDatePostedOldestFirst = QCheckBox("Date Posted: Oldest First")
        self.dbYearNewestFirst = QCheckBox("Year: Newest First")
        self.dbYearOldestFirst = QCheckBox("Year: Oldest First")
        self.dbPriceHighestFirst = QCheckBox("Price: Highest First")
        self.dbPriceLowestFirst = QCheckBox("Price: Lowest First")
        self.dbMileageHighestFirst = QCheckBox("Mileage: Highest First")
        self.dbMileageLowestFirst = QCheckBox("Mileage: Lowest First")
        self.dbLocationAlpha = QCheckBox("Location: A-Z")
        self.dbLocationAlphaRev = QCheckBox("Location: Z-A")


        self.dbNewestEntries = QCheckBox("DB: Newest Entries")
        self.dbOldestEntries = QCheckBox("DB: Oldest Entries")
        self.dbAllEntries =  QCheckBox("DB: All Entries")
        self.dbNumEntriesPer = QLineEdit()
        self.dbNumEntriesPer.setPlaceholderText("#")


        # Initialize Worker Threads
        
        self.dbThread = QThread()

    def create_facebook_filter_layout(self):
        layoutFB = QVBoxLayout()
        title_label = QLabel("Facebook Scraping")
        # title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutFB.addWidget(title_label)

        grid_layout = QGridLayout()

        # Year
        label1 = QLabel("Year (2000 - 2024)")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        grid_layout.addWidget(self.fbYearMin, 1, 1)
        grid_layout.addWidget(self.fbYearMax, 1, 2)

        # Price
        label2 = QLabel("Price (0 - $50,000)")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        grid_layout.addWidget(self.fbPriceMin, 3, 1)
        grid_layout.addWidget(self.fbPriceMax, 3, 2)

        # Mileage
        label3 = QLabel("Mileage (0 - 200,000)")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
        grid_layout.addWidget(self.fbMileageMin, 5, 1)
        grid_layout.addWidget(self.fbMileageMax, 5, 2)

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
        grid_layout.addWidget(self.fbDateListedNewestFirst, 18, 1)
        grid_layout.addWidget(self.fbDateListedOldestFirst, 18, 2)
        grid_layout.addWidget(self.mileageLowestFirst, 19, 1)
        grid_layout.addWidget(self.mileageHighestFirst, 19, 2)
        grid_layout.addWidget(self.priceLowestFirst, 20, 1)
        grid_layout.addWidget(self.priceHighestFirst, 20, 2)


        # Add spacer items to fill vertical space
        grid_layout.setRowStretch(21, 1)  # Add spacer after the last item to fill remaining vertical space


        layoutFB.addLayout(grid_layout)
        return layoutFB
    
    def create_report_filter_layout(self):
        layoutEX = QVBoxLayout()
        title_label = QLabel("Database Report")
        # title_label.setStyleSheet("font-weight: bold; font-size: 18px; margin-bottom: 10px;")
        layoutEX.addWidget(title_label)

        grid_layout = QGridLayout()

        # Year
        label1 = QLabel("Year")
        grid_layout.addWidget(label1, 0, 0, 1, 3)
        grid_layout.addWidget(self.dbYearMin, 1, 1)
        grid_layout.addWidget(self.dbYearMax, 1, 2)

        # Price
        label2 = QLabel("Price")
        grid_layout.addWidget(label2, 2, 0, 1, 3)
        grid_layout.addWidget(self.dbPriceMin, 3, 1)
        grid_layout.addWidget(self.dbPriceMax, 3, 2)

        # Mileage
        label3 = QLabel("Mileage")
        grid_layout.addWidget(label3, 4, 0, 1, 3)
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

        # Sorting Type
        label5 = QLabel("Sorting Type (Choose 1)")
        grid_layout.addWidget(label5, 15, 0, 1, 3)
        grid_layout.addWidget(self.dbDatePostedNewestFirst, 16, 1)
        grid_layout.addWidget(self.dbDatePostedOldestFirst, 16, 2)
        grid_layout.addWidget(self.dbYearNewestFirst, 17, 1)
        grid_layout.addWidget(self.dbYearOldestFirst, 17, 2)
        grid_layout.addWidget(self.dbPriceHighestFirst, 18, 1)
        grid_layout.addWidget(self.dbPriceLowestFirst, 18, 2)
        grid_layout.addWidget(self.dbMileageHighestFirst, 19, 1)
        grid_layout.addWidget(self.dbMileageLowestFirst, 19, 2)
        grid_layout.addWidget(self.dbLocationAlpha, 20, 1)
        grid_layout.addWidget(self.dbLocationAlphaRev, 20, 2)

        label6 = QLabel("Portion of Database (Choose 1)")
        grid_layout.addWidget(label6, 21, 0, 1, 3)
        grid_layout.addWidget(self.dbNewestEntries, 22, 1)
        grid_layout.addWidget(self.dbOldestEntries, 22, 2)
        grid_layout.addWidget(self.dbAllEntries, 23, 1)

        label7 = QLabel("Number of Entries")
        grid_layout.addWidget(label7, 24, 0, 1, 3)
        grid_layout.addWidget(self.dbNumEntriesPer, 25, 1)

        layoutEX.addLayout(grid_layout)
        return layoutEX

    def create_button_layout(self):
        # Horizontal layout for action buttons
        buttonsLayout = QHBoxLayout()

        # Add buttons
        buttonScrape = QPushButton("Scrape Facebook")
        # Padding increases distance from text to edge of button
        # Margin increases distance from edge of button to other items
        
        buttonScrape.clicked.connect(self.button_scrape_facebook)
        buttonsLayout.addWidget(buttonScrape)

        buttonReport = QPushButton("Generate Database Report")
        buttonReport.clicked.connect(self.button_generate_database_report)
        buttonsLayout.addWidget(buttonReport)

        buttonBoth = QPushButton("Scrape and Generate")
        buttonBoth.clicked.connect(self.button_scrape_and_generate_report)
        buttonsLayout.addWidget(buttonBoth)

        buttonAutomate = QPushButton("Automate")
        buttonAutomate.clicked.connect(self.button_scrape_and_generate_report)
        buttonsLayout.addWidget(buttonAutomate)

        buttonTrends = QPushButton("See Trends")
        buttonTrends.clicked.connect(self.button_see_trends)
        buttonsLayout.addWidget(buttonTrends)

        return buttonsLayout

    def collect_filter_choices(self):
        userChoicesGUI = {
            "ScrappingFilters": {
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
                    "dateListedNewestFirst": self.fbDateListedNewestFirst.isChecked(),
                    "dateListedOldestFirst": self.fbDateListedOldestFirst.isChecked(),
                    "priceLowestFirst": self.priceLowestFirst.isChecked(),
                    "priceHighestFirst": self.priceHighestFirst.isChecked(),
                    "mileageLowestFirst": self.mileageLowestFirst.isChecked(),
                    "mileageHighestFirst": self.mileageHighestFirst.isChecked(),
                }
            },
            "DatabaseFilters": {
                "Database": {"NewestEntries": self.dbNewestEntries.isChecked(),
                             "OldestEntries": self.dbOldestEntries.isChecked(),
                             "AllEntries": self.dbAllEntries.isChecked(),},
                "Year": {"Min": self.dbYearMin.text(), "Max": self.dbYearMax.text()},
                "Price": {"Min": self.dbPriceMin.text(), "Max": self.dbPriceMax.text()},
                "Mileage": {"Min": self.dbMileageMin.text(), "Max": self.dbMileageMax.text()},
                "Location": {"Alphabetical": self.dbLocationAlpha.isChecked(), 
                             "AlphabeticalRev": self.dbLocationAlphaRev.isChecked(),},
                "Make": {
                    "Acura": self.dbMakeAcura.isChecked(),
                    "Audi": self.dbMakeAudi.isChecked(),
                    "Buick": self.dbMakeBuick.isChecked(),
                    "Chevy": self.dbMakeChevy.isChecked(),
                    "Chrysler": self.dbMakeChrysler.isChecked(),
                    "Dodge": self.dbMakeDodge.isChecked(),
                    "Ford": self.dbMakeFord.isChecked(),
                    "GMC": self.dbMakeGMC.isChecked(),
                    "Honda": self.dbMakeHonda.isChecked(),
                    "Hyundai": self.dbMakeHyundai.isChecked(),
                    "Jeep": self.dbMakeJeep.isChecked(),
                    "Lexus": self.dbMakeLexus.isChecked(),
                    "Nissan": self.dbMakeNissan.isChecked(),
                    "Ram": self.dbMakeRam.isChecked(),
                    "Toyota": self.dbMakeToyota.isChecked(),
            },
                "Sorting Type": {
                    "dateListedNewestFirst": self.dbDatePostedNewestFirst.isChecked(),
                    "dateListedOldestFirst": self.dbDatePostedOldestFirst.isChecked(),
                    "yearNewestFirst": self.dbYearNewestFirst.isChecked(),
                    "yearOldestFirst": self.dbYearOldestFirst.isChecked(),
                    "priceLowestFirst": self.dbPriceLowestFirst.isChecked(),
                    "priceHighestFirst": self.dbPriceHighestFirst.isChecked(),
                    "mileageLowestFirst": self.dbMileageLowestFirst.isChecked(),
                    "mileageHighestFirst": self.dbMileageHighestFirst.isChecked(),
                },
            }
        }
        return userChoicesGUI

    def button_scrape_facebook(self):
        fbFilters = self.collect_filter_choices()["ScrappingFilters"]
        # Call the function to scrape Facebook using the filters
        print("Scraping Facebook with filters:")
        pprint.pprint(fbFilters)
        minYear = self.convert_to_int_or_default(fbFilters["Year"]["Min"], "2000")
        maxYear = self.convert_to_int_or_default(fbFilters["Year"]["Max"], "2024")
        minPrice = self.convert_to_int_or_default(fbFilters["Price"]["Min"], "0")
        maxPrice = self.convert_to_int_or_default(fbFilters["Price"]["Max"], "50000")
        minMileage = self.convert_to_int_or_default(fbFilters["Mileage"]["Min"], "0")
        maxMileage = self.convert_to_int_or_default(fbFilters["Mileage"]["Max"], "200000")

        sorting = SORTING_FILTERS["Date Listed: Newest First"]
        brands = self.get_selected_brands(fbFilters)
        location = FB_MP_STPAUL
        print(type(location))
        bodyStyles = BODYSTYLE_FILTERS["Sedan-SUV-Truck"]
        vehicleTypes = VEHICLE_TYPE_FILTERS["Cars & Trucks"]
        scrapper = FB_Scrapper(minYear, maxYear, minPrice, 
                               maxPrice, minMileage, maxMileage,
                               brands, location, sorting,
                               bodyStyles, vehicleTypes)
        
        self.fbThread = QThread()
        self.worker = FB_Worker_Scrapper(scrapper)
        self.worker.moveToThread(self.fbThread)

        # Set "what to do" when thread is started
        self.fbThread.started.connect(self.worker.run)
        # Tell the thread to "quit" was the worker is finished
        self.worker.finished.connect(self.fbThread.quit)
        # Tell the worker to schedule itslef for deletion later when it's safe
        self.worker.finished.connect(self.worker.deleteLater)
        # Tell the thread to do the same
        self.fbThread.finished.connect(self.fbThread.deleteLater)

        # Start the Thread
        self.fbThread.start()

        self.fbThread.finished.connect(self.on_scrape_finished)

        return
 

    def button_generate_database_report(self):
        dbFilters = self.collect_filter_choices()["DatabaseFilters"]
        # Call the function to generate a report using the filters
        print("Generating report with filters:")
        pprint.pprint(dbFilters)
        minYear = self.convert_to_int_or_default(dbFilters["Year"]["Min"], "2000")
        maxYear = self.convert_to_int_or_default(dbFilters["Year"]["Max"], "2024")
        minPrice = self.convert_to_int_or_default(dbFilters["Price"]["Min"], "0")
        maxPrice = self.convert_to_int_or_default(dbFilters["Price"]["Max"], "50000")
        minMileage = self.convert_to_int_or_default(dbFilters["Mileage"]["Min"], "0")
        maxMileage = self.convert_to_int_or_default(dbFilters["Mileage"]["Max"], "200000")
        brands = self.get_selected_brands(dbFilters)
        location = ""

    def button_scrape_and_generate_report(self):
        filters = self.collect_filter_choices()
        # Call the function to scrape Facebook and generate a report using the filters
        print("Scraping Facebook and generating report with filters:")
        pprint.pprint(filters)
    
    def button_automated(self):
        filters = self.collect_filter_choices()["ScrappingFilters"]
        print("Automated Options")
        pprint.pprint(filters)
    def button_see_trends(self):
        brands = ["Dodge", "Chrysler", "Jeep"]
        db = FB_DatabaseManager()
        allBrands = db.fetch_brand_list()
        tm = FB_TrendsAnalyzer()

        tm.plot_compare_trends_without_data_points(db, brands)
        tm.plot_compare_trends_with_data_points(db, brands)
        tm.plot_compare_trends_without_data_points(db, allBrands)
        tm.plot_compare_trends_with_data_points(db, allBrands)
        
        goodDeals = tm.check_for_good_deal(db, brands)
        notif = FB_NotificationsManager()
        notif.confirmEnvVariables()
        notif.testServerConnection()
        # BNotifications.sendGoodDealsEmail(goodDeals)
        return

    def on_scrape_finished(self):
        print("Scrapping Complete!")

    # Should theoretically work for both scrapping and database selections
    def get_selected_brands(self, filters):
        selectedBrands = []
        # For every "make" key and "isClicked" value in the specific 
        #   "Make" chunk of the dictionary, add the clicked ones to a list
        for make, isClicked in filters["Make"].items():
            if isClicked:
                selectedBrands.append(make)
        # Should already be alphabetical, but just making sure
        return sorted(selectedBrands)
    def get_selected_fb_sorting_options(self, filters):
        sortingOption = ""
        numClicked = 0
        for sortType, isClicked in filters["Sorting Type"].items():
            if isClicked:
                numClicked += 1
                sortingOption = sortType
            if numClicked > 1:
                sortingOption = "dateListedNewestFirst"
                break
        return sortingOption
    def get_selected_db_sorting_options(self, filters):
        return

    # Offload stylesheet to an external file for main GUI code clarity
    def load_stylesheet(self, styleSheet):
        try:
            with open(styleSheet, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The stylesheet file '{styleSheet}' was not found.")
            return ""

    def convert_to_int_or_default(self, value, default):
        if value == "FREE" or value == "Free":
            return 0
        if value == None:
            return 0
        try:
            # Create new numeric string by removing non-digits
            numericString = ''.join(c for c in value if c.isdigit())
            # Type cast to Int
            num = int(numericString)
            return str(num)
        except ValueError:
            return default

class FB_Worker_Scrapper(QObject):
    # Emits a "signal" indicating a task has finished
    finished = pyqtSignal()
    # Emits a "signal" indicating a task is in progress
    # Usage: self.progress.emit(f"Progress: {i})
    progress = pyqtSignal(str)
    def __init__(self, FBScrapper):
        super().__init__()
        self.FBScrapper = FBScrapper
    def run(self):
        self.FBScrapper.scrape()
        self.finished.emit()
    

                       