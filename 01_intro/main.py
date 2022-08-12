
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("cleanlooks")

    data = ["one", "two", "three", "four", "five"]
    listView = QtWidgets.QListView()
    listView.show()

    model = QtCore.QStringListModel(data)
    listView.setModel(model)

    comboxbox = QtWidgets.QComboBox()
    comboxbox.setModel(model)
    comboxbox.show()

    listview2 = QtWidgets.QListView()
    listview2.setModel(model)
    listview2.show()
    sys.exit(app.exec_())
