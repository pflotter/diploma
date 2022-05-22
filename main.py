import sys
from PyQt5 import QtWidgets
import design
import pandas as pd
import pyqtgraph as pg

styles = {'color': 'black', 'font-size': '20px'}
hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45, 24, 56]
temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44, 65, 11]


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Generate demo-plot
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

        # connect buttons with 'def'
        self.btnLoad.clicked.connect(self.loadExcelData)
        self.btnSave.clicked.connect(self.saveExcelData)
        self.btnAddData.clicked.connect(self.addRow)
        self.btnDeleteData.clicked.connect(self.removeRow)
        self.btnCopy.clicked.connect(self.copyRow)

        # generate test-data (only for save)
        self.loadData()

    # save to .xlsx
    def saveExcelData(self):
        rep = QtWidgets.QFileDialog.getSaveFileName(None, 'Выбор места сохранения', '', 'Excel Files (*xlsx);;Excel Files (*.xls*);;CSV Files (*.csv)')
        print(rep)
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


    # upload from .xlsx
    def loadExcelData(self):
        rep = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла для загрузки', '', 'Excel Files (*.xls*)')

        df = pd.read_excel(rep[0])
        if df.size == 0:
            return

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
    def addRow(self):
        currentRow = self.tableWidget.currentRow()
        count = self.spinBox_2.value()
        for i in range(count):
            self.tableWidget.insertRow(currentRow + 1)

    # remove rows in tableWidget
    def removeRow(self):
        if self.tableWidget.rowCount() > 0:
            currentRow = self.tableWidget.currentRow()
            count = self.spinBox_2.value()
            for i in range(count):
                self.tableWidget.removeRow(currentRow)

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
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=15, symbolBrush=(color))

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
    #excel_file_path = 'data_test.xlsx'
    #worksheet_name = 'Sheet1'
    main()
