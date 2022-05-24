import sys
from PyQt5 import QtWidgets
import design
import pandas as pd
import pyqtgraph as pg
import numpy as np

import distribution
from distribution import plots
from distribution import definition

import quantitative_indicators
from quantitative_indicators import definition

class AnotherWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.
        self.label = QtWidgets.QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.smt = []
        self.window1 = AnotherWindow()

        # connect buttons and actions with 'def'
        self.btnAddData.clicked.connect(self.addButton)
        self.btnDeleteData.clicked.connect(self.removeButton)
        self.btnPlotGraphics.clicked.connect(self.updateGraphData)

        self.actionLoadFile.triggered.connect(self.loadExcelData)
        self.actionSaveFile.triggered.connect(self.saveExcelData)
        self.actionPearson.triggered.connect(self.addDataForGraph)
        self.actionPearsonNormal.triggered.connect(self.addDataForGraph)

        self.actionStudent.triggered.connect(self.calculateStudentT)
        self.actionPearsonNormal.triggered.connect(self.calculatePearsonNormal)

        self.actionManWhitney.triggered.connect(self.calculateManWhitney)
        self.actionKolmogorovSmirnov.triggered.connect(self.calculateKolmogorovSmirnov)

        self.actionReporting.triggered.connect(lambda checked: self.toggle_window(self.window1))

        # generate test-data (only for save)
        #self.loadData()

    def toggle_window(self, window):
            window.show()


    def calculateStudentT(self):
        self.currentTitle = self.tableWidget.horizontalHeaderItem(0).text()
        res = quantitative_indicators.definition.student_t_criterion(self.currentTitle)
        self.label_6.setText(res)

        title = QtWidgets.QLabel(res + ' | test')
        coeffEdit = QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.gridLayout.rowCount(),self.gridLayout.columnCount(), title, coeffEdit)

    def calculatePearsonNormal(self):
        self.currentTitle = self.tableWidget.horizontalHeaderItem(0).text()
        res = quantitative_indicators.definition.pearson_normal(self.currentTitle)
        self.label_6.setText(res)

    def calculateManWhitney(self):
        self.currentTitle = self.tableWidget.horizontalHeaderItem(0).text()
        res = quantitative_indicators.definition.mann_whitney_criterion(self.currentTitle)
        self.label_6.setText(res)

    def calculateKolmogorovSmirnov(self):
        self.currentTitle = self.tableWidget.horizontalHeaderItem(0).text()
        res = quantitative_indicators.definition.kolmogorov_smirnov_criterion(self.currentTitle)
        self.label_6.setText(res)

    # plot graph
    def updateGraphData(self):
        x1, y1 = distribution.plots.get_xy_plot_values(self.smt)

        distribution.plots.show_plot(title=self.currentTitle, data=self.smt)
        #self.plot(x1, y1, "", 'black')

    # save to .xlsx
    def saveExcelData(self):
        rep = QtWidgets.QFileDialog.getSaveFileName(None, 'Выбор места сохранения', '', 'Excel Files (*.xlsx *.xls);;CSV Files (*.csv)')
        columnHeaders = []

        # create column header list
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # create dataframe object recordset
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()
        df.to_excel(rep[0], index=False)
        print('Excel file exported.')

    def addDataForGraph(self):
        temp = []
        temp_1 = []
        self.currentTitle = self.tableWidget.horizontalHeaderItem(0).text()
        for i in range(self.tableWidget.rowCount()):
            temp.append(self.tableWidget.item(i, 0).text())

        temp = list(map(int, temp))
        print(temp)
        self.smt = temp

        temp_1 = distribution.definition.check_pearson_correlation_coefficient(self.smt)
        print(temp_1)

        self.lineMathMean.setText(temp_1[0])
        self.lineStd.setText(temp_1[1])
        self.lineCorrNormal.setText(temp_1[2])
        self.lineCorrLogistic.setText(temp_1[3])
        self.lineCorrRavnomer.setText(temp_1[4])

    # upload from .xlsx
    def loadExcelData(self):
        rep = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла для загрузки', '', 'Excel Files (*.xls*)')

        df = pd.read_excel(rep[0])
        if df.size == 0:
            return

        # filling TableWidget columns and rows
        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)

        self.tableWidget.setColumnWidth(2, 300)

    # add rows in tableWidget
    def addButton(self):

        # if radio selected Rows
        if self.radioData.isChecked():

            # change after last selected Item
            if self.tableWidget.selectedIndexes():
                self.uniformAddingData()

            # change to tail (default)
            else:
                currentRow = self.tableWidget.rowCount()
                count = self.spinBox_2.value()
                for i in range(count):
                    self.tableWidget.insertRow(currentRow)

        # if radio selected Columns
        else:

            # change after last selected Item
            if self.tableWidget.selectedIndexes():
                self.uniformAddingData()

            # change to tail (default)
            else:
                currentColumn = self.tableWidget.columnCount()
                count = self.spinBox_2.value()
                for i in range(count):
                    self.tableWidget.insertColumn(currentColumn)


        # clearing WidgetTable
        if self.tableWidget.rowCount() < 1 or self.tableWidget.columnCount() < 1:
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)

    # remove rows in tableWidget
    def removeButton(self):

        # if radio selected Rows
        if self.radioData.isChecked():

            # change to tail (default)
            if self.tableWidget.rowCount() > 0:

                # change selected Items
                if self.tableWidget.selectedIndexes():
                    index_list = []

                    # fill index_list
                    for model_index in self.tableWidget.selectedIndexes():
                        index_list.append(model_index.row())

                    # remove duplicate from index_list
                    list_index = list(set(index_list))
                    list_index.sort(reverse=True)

                    for index in list_index:
                        self.tableWidget.removeRow(index)

                else:
                    currentRow = self.tableWidget.rowCount()
                    count = self.spinBox_2.value()
                    for i in range(count):
                        self.tableWidget.removeRow(currentRow - 1)

        # if radio selected Columns
        else:
            if self.tableWidget.columnCount() > 0:

                # change selected Items
                if self.tableWidget.selectedIndexes():
                    index_list = []

                    # fill index_list
                    for model_index in self.tableWidget.selectedIndexes():
                        index_list.append(model_index.column())

                    # remove duplicate from index_list
                    list_index = list(set(index_list))
                    list_index.sort(reverse=True)

                    for index in list_index:
                        self.tableWidget.removeColumn(index)

                else:
                    currentColumn = self.tableWidget.columnCount()
                    count = self.spinBox_2.value()
                    for i in range(count):
                        self.tableWidget.removeColumn(currentColumn - 1)
                    
        # clearing WidgetTable
        if self.tableWidget.rowCount() < 1 or self.tableWidget.columnCount() < 1:
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)

    def uniformAddingData(self):
            for i in self.tableWidget.selectedIndexes():
                currentRow = i.row()
                currentColumn = i.column()

            count = self.spinBox_2.value()
            if self.radioData.isChecked():
                for i in range(count):
                    self.tableWidget.insertRow(currentRow + 1)
            else:
                for i in range(count):
                    self.tableWidget.insertColumn(currentColumn + 1)

    # copy rows in tableWidget
    def copyRow(self):
        currentRow = self.tableWidget.currentRow()
        self.tableWidget.insertRow(currentRow)
        columnCount = self.tableWidget.columnCount()
        for j in range(columnCount):
            if not self.tableWidget.item(currentRow + 1, j) is None:
                self.tableWidget.setItem(currentRow, j,
                                         QtWidgets.QTableWidgetItem(self.tableWidget.item(currentRow + 1, j).text()))

    # create graphics, etc.
    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        #self.graphWidget.plot(x, y, name=plotname, pen=pen, symbolSize=12, symbolBrush=(color))

    # generate data (only for save .xlsx)
    def loadData(self):
        self.headerLabels = list('ABCDEFG')

        n = 30
        self.tableWidget.setRowCount(n)
        self.tableWidget.setColumnCount(len(self.headerLabels))
        self.tableWidget.setHorizontalHeaderLabels(self.headerLabels)

        for row in range(n):
            for col in range(len(self.headerLabels)):
                item = QtWidgets.QTableWidgetItem('Cell {0}-{1}'.format(self.headerLabels[col], row))
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setWindowTitle("Учёт статистики")
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
