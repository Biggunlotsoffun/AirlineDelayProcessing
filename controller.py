from PyQt5.QtWidgets import *
from view_3 import *
from PyQt5.QtGui import *
import csv
import math
import random
import numpy as np
import pandas as pd
import stats as st
import matplotlib.pyplot as plt


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submit_button.clicked.connect(self.analyze_data)
        self.to_drop_down.addItem('New York City')
        self.to_drop_down.addItem('Los Angeles')
        self.to_drop_down.addItem('Chicago')
        self.to_drop_down.addItem('Houston')
        self.to_drop_down.addItem('Phoenix')
        self.to_drop_down.addItem('Philadelphia')
        self.to_drop_down.addItem('San Antonio')
        self.to_drop_down.addItem('San Diego')
        self.to_drop_down.addItem('Dallas')
        self.to_drop_down.addItem('San Jose')
        self.to_drop_down.addItem('Austin')
        self.to_drop_down.addItem('Jacksonville')
        self.to_drop_down.addItem('Fort Worth')
        self.to_drop_down.addItem('Columbus')
        self.to_drop_down.addItem('San Francisco')
        self.to_drop_down.addItem('Charlotte')
        self.to_drop_down.addItem('Indianapolis')
        self.to_drop_down.addItem('Seattle')
        self.to_drop_down.addItem('Denver')
        self.to_drop_down.addItem('Washington D.C.')
        self.to_drop_down.addItem('Boston')
        self.to_drop_down.addItem('Nashville')
        self.to_drop_down.addItem('El Paso')
        self.to_drop_down.addItem('Detroit')
        self.to_drop_down.addItem('Memphis')
        self.to_drop_down.addItem('Portland')
        self.to_drop_down.addItem('Oklahoma City')
        self.to_drop_down.addItem('Las Vegas')
        self.to_drop_down.addItem('Louisville')
        self.to_drop_down.addItem('Baltimore')
        self.to_drop_down.addItem('Milwaukee')
        self.to_drop_down.addItem('Albuquerque')
        self.to_drop_down.addItem('Tucson')
        self.to_drop_down.addItem('Fresno')
        self.to_drop_down.addItem('Mesa')
        self.to_drop_down.addItem('Sacramento')
        self.to_drop_down.addItem('Atlanta')
        self.to_drop_down.addItem('Kansas City')
        self.to_drop_down.addItem('Colorado Springs')
        self.to_drop_down.addItem('Miami')
        self.to_drop_down.addItem('Raleigh')
        self.to_drop_down.addItem('Omaha')
        self.to_drop_down.addItem('Long Beach')
        self.to_drop_down.addItem('Virginia Beach')
        self.to_drop_down.addItem('Oakland')
        self.to_drop_down.addItem('Minneapolis')
        self.to_drop_down.addItem('Tulsa')
        self.to_drop_down.addItem('Wichita')
        self.to_drop_down.addItem('New Orleans')
        self.to_drop_down.addItem('Arlington')
        self.from_drop_down.addItem('New York City')
        self.from_drop_down.addItem('Los Angeles')
        self.from_drop_down.addItem('Chicago')
        self.from_drop_down.addItem('Houston')
        self.from_drop_down.addItem('Phoenix')
        self.from_drop_down.addItem('Philadelphia')
        self.from_drop_down.addItem('San Antonio')
        self.from_drop_down.addItem('San Diego')
        self.from_drop_down.addItem('Dallas')
        self.from_drop_down.addItem('San Jose')
        self.from_drop_down.addItem('Austin')
        self.from_drop_down.addItem('Jacksonville')
        self.from_drop_down.addItem('Fort Worth')
        self.from_drop_down.addItem('Columbus')
        self.from_drop_down.addItem('San Francisco')
        self.from_drop_down.addItem('Charlotte')
        self.from_drop_down.addItem('Indianapolis')
        self.from_drop_down.addItem('Seattle')
        self.from_drop_down.addItem('Denver')
        self.from_drop_down.addItem('Washington D.C.')
        self.from_drop_down.addItem('Boston')
        self.from_drop_down.addItem('Nashville')
        self.from_drop_down.addItem('El Paso')
        self.from_drop_down.addItem('Detroit')
        self.from_drop_down.addItem('Memphis')
        self.from_drop_down.addItem('Portland')
        self.from_drop_down.addItem('Oklahoma City')
        self.from_drop_down.addItem('Las Vegas')
        self.from_drop_down.addItem('Louisville')
        self.from_drop_down.addItem('Baltimore')
        self.from_drop_down.addItem('Milwaukee')
        self.from_drop_down.addItem('Albuquerque')
        self.from_drop_down.addItem('Tucson')
        self.from_drop_down.addItem('Fresno')
        self.from_drop_down.addItem('Mesa')
        self.from_drop_down.addItem('Sacramento')
        self.from_drop_down.addItem('Atlanta')
        self.from_drop_down.addItem('Kansas City')
        self.from_drop_down.addItem('Colorado Springs')
        self.from_drop_down.addItem('Miami')
        self.from_drop_down.addItem('Raleigh')
        self.from_drop_down.addItem('Omaha')
        self.from_drop_down.addItem('Long Beach')
        self.from_drop_down.addItem('Virginia Beach')
        self.from_drop_down.addItem('Oakland')
        self.from_drop_down.addItem('Minneapolis')
        self.from_drop_down.addItem('Tulsa')
        self.from_drop_down.addItem('Wichita')
        self.from_drop_down.addItem('New Orleans')
        self.from_drop_down.addItem('Arlington')
        #model = joblib.load("model.joblib")

    def analyze_data(self):
        # Load data from CSV file
        with open('2010.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        # Get selected departure and destination locations
        #from_location = self.from_drop_down.currentText()
        if self.from_drop_down.currentText() == 'New York City':
            from_location = 'NYC'
        elif self.from_drop_down.currentText() == 'Los Angeles':
            from_location = 'LAX'
        elif self.from_drop_down.currentText() == 'Chicago':
            from_location = 'ORD'
        elif self.from_drop_down.currentText() == 'Houston':
            from_location = 'IAH'
        elif self.from_drop_down.currentText() == 'Phoenix':
            from_location = 'PHX'
        elif self.from_drop_down.currentText() == 'Philadelphia':
            from_location = 'PHL'
        elif self.from_drop_down.currentText() == 'San Antonio':
            from_location = 'SAT'
        elif self.from_drop_down.currentText() == 'San Diego':
            from_location = 'SAN'
        elif self.from_drop_down.currentText() == 'Dallas':
            from_location = 'DFW'
        elif self.from_drop_down.currentText() == 'San Jose':
            from_location = 'SJC'
        elif self.from_drop_down.currentText() == 'Austin':
            from_location = 'AUS'
        elif self.from_drop_down.currentText() == 'Jacksonville':
            from_location = 'JAX'
        elif self.from_drop_down.currentText() == 'Fort Worth':
            from_location = 'DFW'
        elif self.from_drop_down.currentText() == 'Columbus':
            from_location = 'CMH'
        elif self.from_drop_down.currentText() == 'San Francisco':
            from_location = 'SFO'
        elif self.from_drop_down.currentText() == 'Charlotte':
            from_location = 'CLT'
        elif self.from_drop_down.currentText() == 'Indianapolis':
            from_location = 'IND'
        elif self.from_drop_down.currentText() == 'Seattle':
            from_location = 'SEA'
        elif self.from_drop_down.currentText() == 'Denver':
            from_location = 'DEN'
        elif self.from_drop_down.currentText() == 'Washington D.C.':
            from_location = 'DCA'
        elif self.from_drop_down.currentText() == 'Boston':
            from_location = 'BOS'
        elif self.from_drop_down.currentText() == 'Nashville':
            from_location = 'BNA'
        elif self.from_drop_down.currentText() == 'El Paso':
            from_location = 'ELP'
        elif self.from_drop_down.currentText() == 'Detroit':
            from_location = 'DTW'
        elif self.from_drop_down.currentText() == 'Memphis':
            from_location = 'MEM'
        elif self.from_drop_down.currentText() == 'Portland':
            from_location = 'PDX'
        elif self.from_drop_down.currentText() == 'Oklahoma City':
            from_location = 'OKC'
        elif self.from_drop_down.currentText() == 'Las Vegas':
            from_location = 'LAS'
        elif self.from_drop_down.currentText() == 'Louisville':
            from_location = 'SDF'
        elif self.from_drop_down.currentText() == 'Baltimore':
            from_location = 'BWI'
        elif self.from_drop_down.currentText() == 'Milwaukee':
            from_location = 'MKE'
        elif self.from_drop_down.currentText() == 'Albuquerque':
            from_location = 'ABQ'
        elif self.from_drop_down.currentText() == 'Tucson':
            from_location = 'TUS'
        elif self.from_drop_down.currentText() == 'Fresno':
            from_location = 'FAT'
        elif self.from_drop_down.currentText() == 'Mesa':
            from_location = 'AZA'
        elif self.from_drop_down.currentText() == 'Sacramento':
            from_location = 'SMF'
        elif self.from_drop_down.currentText() == 'Atlanta':
            from_location = 'ATL'
        elif self.from_drop_down.currentText() == 'Kansas City':
            from_location = 'MCI'
        elif self.from_drop_down.currentText() == 'Colorado Springs':
            from_location = 'COS'
        elif self.from_drop_down.currentText() == 'Miami':
            from_location = 'MIA'
        elif self.from_drop_down.currentText() == 'Raleigh':
            from_location = 'RDU'
        elif self.from_drop_down.currentText() == 'Omaha':
            from_location = 'OMA'
        elif self.from_drop_down.currentText() == 'Long Beach':
            from_location = 'LGB'
        elif self.from_drop_down.currentText() == 'Virginia Beach':
            from_location = 'ORF'
        elif self.from_drop_down.currentText() == 'Oakland':
            from_location = 'OAK'
        elif self.from_drop_down.currentText() == 'Minneapolis':
            from_location = 'MSP'
        elif self.from_drop_down.currentText() == 'Tulsa':
            from_location = 'TUL'
        elif self.from_drop_down.currentText() == 'Wichita':
            from_location = 'ICT'
        elif self.from_drop_down.currentText() == 'New Orleans':
            from_location = 'MSY'
        elif self.from_drop_down.currentText() == 'Arlington':
            from_location = 'DCA'

        if self.to_drop_down.currentText() == 'New York City':
            to_location = 'NYC'
        elif self.to_drop_down.currentText() == 'Los Angeles':
            to_location = 'LAX'
        elif self.to_drop_down.currentText() == 'Chicago':
            to_location = 'ORD'
        elif self.to_drop_down.currentText() == 'Houston':
            to_location = 'IAH'
        elif self.to_drop_down.currentText() == 'Phoenix':
            to_location = 'PHX'
        elif self.to_drop_down.currentText() == 'Philadelphia':
            to_location = 'PHL'
        elif self.to_drop_down.currentText() == 'San Antonio':
            to_location = 'SAT'
        elif self.to_drop_down.currentText() == 'San Diego':
            to_location = 'SAN'
        elif self.to_drop_down.currentText() == 'Dallas':
            to_location = 'DFW'
        elif self.to_drop_down.currentText() == 'San Jose':
            to_location = 'SJC'
        elif self.to_drop_down.currentText() == 'Austin':
            to_location = 'AUS'
        elif self.to_drop_down.currentText() == 'Jacksonville':
            to_location = 'JAX'
        elif self.to_drop_down.currentText() == 'Fort Worth':
            to_location = 'DFW'
        elif self.to_drop_down.currentText() == 'Columbus':
            to_location = 'CMH'
        elif self.to_drop_down.currentText() == 'San Francisco':
            to_location = 'SFO'
        elif self.to_drop_down.currentText() == 'Charlotte':
            to_location = 'CLT'
        elif self.to_drop_down.currentText() == 'Indianapolis':
            to_location = 'IND'
        elif self.to_drop_down.currentText() == 'Seattle':
            to_location = 'SEA'
        elif self.to_drop_down.currentText() == 'Denver':
            to_location = 'DEN'
        elif self.to_drop_down.currentText() == 'Washington D.C.':
            to_location = 'DCA'
        elif self.to_drop_down.currentText() == 'Boston':
            to_location = 'BOS'
        elif self.to_drop_down.currentText() == 'Nashville':
            to_location = 'BNA'
        elif self.to_drop_down.currentText() == 'El Paso':
            to_location = 'ELP'
        elif self.to_drop_down.currentText() == 'Detroit':
            to_location = 'DTW'
        elif self.to_drop_down.currentText() == 'Memphis':
            to_location = 'MEM'
        elif self.to_drop_down.currentText() == 'Portland':
            to_location = 'PDX'
        elif self.to_drop_down.currentText() == 'Oklahoma City':
            to_location = 'OKC'
        elif self.to_drop_down.currentText() == 'Las Vegas':
            to_location = 'LAS'
        elif self.to_drop_down.currentText() == 'Louisville':
            to_location = 'SDF'
        elif self.to_drop_down.currentText() == 'Baltimore':
            to_location = 'BWI'
        elif self.to_drop_down.currentText() == 'Milwaukee':
            to_location = 'MKE'
        elif self.to_drop_down.currentText() == 'Albuquerque':
            to_location = 'ABQ'
        elif self.to_drop_down.currentText() == 'Tucson':
            to_location = 'TUS'
        elif self.to_drop_down.currentText() == 'Fresno':
            to_location = 'FAT'
        elif self.to_drop_down.currentText() == 'Mesa':
            to_location = 'AZA'
        elif self.to_drop_down.currentText() == 'Sacramento':
            to_location = 'SMF'
        elif self.to_drop_down.currentText() == 'Atlanta':
            to_location = 'ATL'
        elif self.to_drop_down.currentText() == 'Kansas City':
            to_location = 'MCI'
        elif self.to_drop_down.currentText() == 'Colorado Springs':
            to_location = 'COS'
        elif self.to_drop_down.currentText() == 'Miami':
            to_location = 'MIA'
        elif self.to_drop_down.currentText() == 'Raleigh':
            to_location = 'RDU'
        elif self.to_drop_down.currentText() == 'Omaha':
            to_location = 'OMA'
        elif self.to_drop_down.currentText() == 'Long Beach':
            to_location = 'LGB'
        elif self.to_drop_down.currentText() == 'Virginia Beach':
            to_location = 'ORF'
        elif self.to_drop_down.currentText() == 'Oakland':
            to_location = 'OAK'
        elif self.to_drop_down.currentText() == 'Minneapolis':
            to_location = 'MSP'
        elif self.to_drop_down.currentText() == 'Tulsa':
            to_location = 'TUL'
        elif self.to_drop_down.currentText() == 'Wichita':
            to_location = 'ICT'
        elif self.to_drop_down.currentText() == 'New Orleans':
            to_location = 'MSY'
        elif self.to_drop_down.currentText() == 'Arlington':
            to_location = 'DCA'



        delay_count = 0
        total_flights = 0
        for row in data:
            if row['ORIGIN'] == from_location and row['DEST'] == to_location:
                total_flights += 1
                if row['ARR_DELAY'] != '' and float(row['ARR_DELAY']) > 0:
                    delay_count += 1
        if total_flights > 0:
            delay_percent = delay_count / total_flights * 100

            message = f"Your flight from {from_location} to {to_location} " \
                      f"has a {delay_percent:.2f}% chance of being delayed."

        else:
            message = f"No flights found from {from_location} to {to_location}."


        # Display result
        self.display_text.setText(message)
        #testing note