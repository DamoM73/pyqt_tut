from calc_ui import *

def signals(self):
    # connects signals to slots
    self.nine_btn.clicked.connect(self.nine)

# slots    
def nine(self):
    self.output_lb.setText