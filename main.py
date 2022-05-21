import sys
from PyQt5 import QtWidgets
import design
import os
import pyqtgraph as pg

import numpy as np

styles = {'color': 'black', 'font-size': '20px'}
hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #################
        self.graphWidget.setBackground('#bbccaa')
        self.graphWidget.setTitle("Демонстрационный пример", color="black", size="22pt")
        self.graphWidget.setLabel('left', 'Температура (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Время (ч)', **styles)
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.addLegend()
        self.graphWidget.setXRange(0, 11, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)
        self.plot(hour, temperature_1, "Измерение_1", 'r')
        self.plot(hour, temperature_2, "Измерение_1", 'black')
        #################

        self.btnLoad.clicked.connect(self.browse_folder)
        self.btnSave.clicked.connect(self.browse_folder)
        self.btnAddData.clicked.connect(self.addRow)
        self.btnDeleteData.clicked.connect(self.removeRow)
        self.btnCopy.clicked.connect(self.copyRow)

    def addRow(self):
        currentRow = self.tableWidget.currentRow()
        count = self.spinBox_2.value()
        for i in range(count):
            self.tableWidget.insertRow(currentRow + 1)

    def removeRow(self):
        if self.tableWidget.rowCount() > 0:
            currentRow = self.tableWidget.currentRow()
            count = self.spinBox_2.value()
            for i in range(count):
                self.tableWidget.removeRow(currentRow)

    def copyRow(self):
        currentRow = self.tableWidget.currentRow()
        self.tableWidget.insertRow(currentRow)
        columnCount = self.tableWidget.columnCount()
        for j in range(columnCount):
            if not self.tableWidget.item(currentRow + 1, j) is None:
                self.tableWidget.setItem(currentRow, j,
                                         QtWidgets.QTableWidgetItem(self.tableWidget.item(currentRow + 1, j).text()))

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=15, symbolBrush=(color))

    def browse_folder(self):
        # self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # if directory:
        #  for file_name in os.listdir(directory):
        #      self.listWidget.addItem(file_name)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setWindowTitle("Учёт статистики")
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
