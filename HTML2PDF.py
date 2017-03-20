__author__ = 'Ahmed Assem'

""" this script make render html using webkit with specific 
width and height and print it as pdf (using qt4)
Usage :script.py inputfile.html width height
"""




import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from optparse import OptionParser
import os

web = None
printer = None
app = None

def convertIt():
    global web , printer
    web.print_(printer)
    print ("Pdf generated")
    QApplication.exit()

def htmlToPDF(htmlfile,pdffile,width, height):
    global web , printer, app
    web.resize(width,height)
    web.load(QUrl.fromLocalFile(htmlfile))
    printer.setPaperSize(QSizeF(width*0.75, height), QPrinter.Point)
    printer.setFullPage(True)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(pdffile)
    QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
    app.exec_()

def printHelp():
	helpMsg ="usage:\n   HTML2PDF <input file path> [-all] \n\t -all: to apply stamp for all pages"
	print (helpMsg)
	sys.exit()

if __name__=="__main__":
    parser = OptionParser(usage="usage: stem [options] -w width -h height -i <input file path>")
    parser.add_option("-i", "",
                      dest="inPutPDF",
                      help="Input file path", metavar="<input file path>")
    parser.add_option("-w", type="int",
                      dest="width",
                      help="width in pixel", metavar="width in pixel")
    parser.add_option("-t", type="int",
                      dest="height",
                      help="height in pixel", metavar="height in pixel")
    if sys.argv[1:]:
        (options, args) = parser.parse_args()
    else:
        parser.print_help()
        sys.exit(0)
    htmlfile = options.inPutPDF
    width = options.width
    height = options.height
    pdffile = htmlfile.replace(".html", ".pdf")
    app = QApplication([])
    web = QWebView()
    printer = QPrinter()
    htmlToPDF(htmlfile,pdffile,width, height)
    app.exit()
    web.close()
