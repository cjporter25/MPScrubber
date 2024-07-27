# New System move - 4.15.24 - Christopher J. Porter
import sys
#import threading
#import csv
#import time
#import psutil

# Marketplace Imports
from marketplaceFB.facebookMP_GUI import *
from marketplaceFB.facebookMP_performance import *

app = QApplication(sys.argv)
window = ScrubberGUI() 
# Set the window to stay on top
window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
window.show()

# Bring the window to the front
window.raise_()
window.activateWindow()

# Reset the window flags to default so it doesn't always stay on top
# after it gains focus
window.setWindowFlags(window.windowFlags() & ~Qt.WindowStaysOnTopHint)
window.show()   
sys.exit(app.exec_())
# Start network monitoring
# start_network_monitoring()






