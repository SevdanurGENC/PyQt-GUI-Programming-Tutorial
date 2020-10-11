from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # Add toolbar and items
        toolbox = QToolBox()
        layout.addWidget(toolbox, 0, 0)
        label = QLabel()
        toolbox.addItem(label, "Students")
        label = QLabel()
        toolbox.addItem(label, "Teachers")
        label = QLabel()
        toolbox.addItem(label, "Directors")

        # show number of items
        print(toolbox.count())

        # disable tab
        toolbox.setItemEnabled(0, False)

        # mouseover tooltip
        toolbox.setItemToolTip(0, "This is a tooltip")

        # tests if items are enabled
        print(toolbox.isItemEnabled(0))
        print(toolbox.isItemEnabled(1))

        # insert item
        item = QLabel()
        toolbox.insertItem(1, item, "Python")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())


#Methods
#The QToolBox has many methods that can be used, you’ve seen .addItem() before but there are many more.

#addItem()
#count()
#currentIndex()
#insertItem()
#itemToolTip()
#itemText()
#itemIcon()
#isItemEnabled()
#removeItem()
#setItemEnabled()
#setItemIcon()
#setItemText()
#setItemToolTip()