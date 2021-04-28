# Python program to convert text file to pdf

# SUMMARY OF HOW IT WORKS
# GUI pops-up to browse for file to be converted
# Inserts todays date at start of PDF
# Takes first line of PDF and applies Heading formatting
# When saving it will ask what filename to use
# Then it will ask which folder to save to

#For the moment there is no error handling and the program will fail if "Cancel" is selected at any point

import datetime
from tkinter import Label, Tk, filedialog, simpledialog ,messagebox
from tkinter.filedialog import askopenfilename
from fpdf import FPDF

root = Tk()
root.withdraw()
messagebox.showinfo(title="Welcome", message="Welcome to the Text-To-PDF Converter")


#FIND TEXT FILE TO BE CONVERTED
root = Tk()
root.withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(title="Select the text file to be converted...",filetypes=(('Text files', "*.txt"),("all files", "*.*")))
    # show an "Open" dialog box and return the path to the selected file

#INITIALISE PDF FILE OBJECT AND ADD BLANK PAGE
pdf = FPDF()   
pdf.add_page()

# SET DEFAULT FONT AND FONT SIZE

pdf.set_font("Times", size = 12)

# OPEN TEXT FILE IN READ MODE
textFileObject = open(filename, "r")

# GET TODAYS DATE SO IT CAN BE INSERTED INTO PDF
todaysDate = datetime.datetime.now()

#INSERTS TODAYS DATE ONTO THE FIRST LINE (RIGHT ALIGNED)
pdf.cell(190, 10, txt = str(todaysDate.strftime("%d/%m/%Y")), ln=1,align = 'R') #190 cell width, 10 cell height, ln = 1: go to new line at end

# ASK IF FIRST LINE CONTAINS HEADING
ROOT = Tk()
ROOT.withdraw()

headingInFirstLine = messagebox.askyesno("Question","Is the first line of the file a heading?")
if headingInFirstLine == True:
    iterator = 0
else: iterator = 1

#PRINT EACH LINE TO PDF FILE OBJECT

for x in textFileObject:
    if iterator != 0: # IF NOT THE FIRST LINE THEN PRINT WITH DEFAULT STYLE
        pdf.multi_cell(190,5,txt =x, align = 'L') #multicell allows text to wrap across lines
    else: # IF THE LINE IS THE FIRST LINE IT WILL APPLY HEADING FORMATTING
        pdf.set_font("Times", 'B', size = 14)
        pdf.cell(190, 10, txt = x, ln = 1, align = 'C') #180 cell width, 10 cell height, ln = 1 - go to new line at end
        iterator += 1
        pdf.set_font("Times", size = 12)

# GUI TO ASK FOR OUTPUT FILENAME    
ROOT = Tk()
ROOT.withdraw()
#ASKS FOR FILENAME EXCL. FILE EXTENSION
outputFilename = simpledialog.askstring(title="Enter in filename for PDF", prompt="Please enter the output filename (excluding file extension)")
outputFilename = outputFilename + '.pdf' #add file extension to string

#RE-INITIALISE GUI
root = Tk()
root.withdraw()

# GUI PROMPT TO BROWSE FOR DIRECTORY WHERE FILE WILL BE SAVED
outputFolder = filedialog.askdirectory(title="Select the folder where file should be saved...")

outputFileFolder = outputFolder + '/' + outputFilename # COMBINE FINAL DIRECTORY AND OUTPUT FILENAME
pdf.output(outputFileFolder, dest='F') # DEST='F' INDICATES THAT IT WILL GO TO A DEFINED LOCAL DIRECTORY

#create class for PDF object
#create pdf class
