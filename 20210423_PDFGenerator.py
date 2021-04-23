# Python program to convert text file to pdf file

# SUMMARY OF HOW IT WORKS
# GUI to browse for file to be converted
# Inserts todays date at start of PDF
# Takes first line of PDF and applies Heading formatting
# When saving it will ask what filename to use
# Then it will ask which folder to save to


import datetime
from tkinter import Tk
from tkinter import filedialog, simpledialog,Label
from tkinter.filedialog import askopenfilename
from fpdf import FPDF

#FIND TEXT FILE TO BE CONVERTED
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

pdf = FPDF()   
pdf.add_page()
   
# set style and size of font
pdf.set_font("Times", size = 12)

# OPEN TEXT FILE IN READ MODE
f = open(filename, "r")

# GET TODAYS DATE SO IT CAN BE INSERTED INTO PDF
todaysDate = datetime.datetime.now()

#INSERTS TODAYS DATE ONTO THE FIRST LINE (RIGHT ALIGNED)
pdf.cell(190, 10, txt = str(todaysDate.strftime("%d/%m/%Y")), ln=1,align = 'R') #180 cell width, 10 cell height, ln = 1 - go to new line at end

iterator = 0
for x in f:
    if iterator != 0:
        #Applied Heading formatting to first line
        pdf.multi_cell(190,5,txt =x, align = 'L') #multicell allows text to wrap across lines, 
    else: 
        pdf.set_font("Times", 'B', size = 14)
        pdf.cell(190, 10, txt = x, ln = 1, align = 'C') #180 cell width, 10 cell height, ln = 1 - go to new line at end
        iterator += 1
        pdf.set_font("Times", size = 12)

# GUI TO ASK FOR OUTPUT FILENAME    
ROOT = Tk()
ROOT.withdraw()
#ASKS FOR FILENAME EXCL. FILE EXTENSION
outputFilename = simpledialog.askstring(title="Enter in filename for PDF", prompt="Please enter the output filename (excluding file extension)")
outputFilename = outputFilename + '.pdf'

#RE-INITIALISE GUI
root = Tk()
root.withdraw()

# GUI PROMPT TO BROWSE FOR DIRECTORY WHERE FILE WILL BE SAVED
outputFolder = filedialog.askdirectory()

outputFileFolder = outputFolder + '/' + outputFilename # COMBINE FINAL DIRECTORY AND OUTPUT FILENAME
pdf.output(outputFileFolder, dest='F') # DEST='F' INDICATES THAT IT WILL GO TO A DEFINED LOCAL DIRECTORY