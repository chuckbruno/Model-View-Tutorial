
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class PaletteTableModel(QtCore.QAbstractTableModel):
    def __init__(self, colors=[[]], headers=[], parent=None):
        super(PaletteTableModel, self).__init__(parent)

        self.__colors = colors
        self.__headers = headers

    def rowCount(self, parent):
        return len(self.__colors)

    def columnCount(self, parent):
        return len(self.__colors[0])

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            return self.__colors[row][column].name()

        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return "Hex code: " + self.__colors[row][column].name()

        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            column = index.column()
            value = self.__colors[row][column]
            pixmap = QtGui.QPixmap(26, 26)
            pixmap.fill(value)

            icon = QtGui.QIcon(pixmap)
            return icon

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            return self.__colors[row][column].name()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()

            color = QtGui.QColor(value)
            if color.isValid():
                self.__colors[row][column] = color
                self.dataChanged.emit(index, index)

                return True

        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
            else:
                return "Color %s" % section

    # ==================================
    # inserting & removing
    # ==================================

    def insertRow(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            defaultValue = [QtGui.QColor("#000000" for i in range(self.column.count(None)))]
            self.__colors.insert(position, defaultValue)

        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        rowCount = len(self.__colors)
        for i in range(columns):
            for j in range(rowCount):
                self.__colors[j].insert(position, QtGui.QColor("#000000"))

        self.endInsertColumns()

        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("plastique")

    # all of our views
    listView = QtWidgets.QListView()
    listView.show()

    comboBox = QtWidgets.QComboBox()
    comboBox.show()

    tableView = QtWidgets.QTableView()
    tableView.show()

    red = QtGui.QColor(255, 0, 0)
    green = QtGui.QColor(0, 255, 0)
    blue = QtGui.QColor(0, 0, 255)

    rowCount = 4
    columnCount = 6

    headers = ["Palette", "Colors", "Brushed", "Omg", "Technical", "Artist"]
    tableData = [[QtGui.QColor("#FFFF00") for i in range(columnCount)] for j in range(rowCount)]
    model = PaletteTableModel(tableData, headers)
    model.insertColumns(0, 5)

    listView.setModel(model)
    comboBox.setModel(model)
    tableView.setModel(model)

    sys.exit(app.exec_())
