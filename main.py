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

        #self.btnLoad.clicked.connect(lambda _, xl_path=excel_file_path, sheet_name=worksheet_name: self.loadExcelData(xl_path, sheet_name))
        self.btnLoad.clicked.connect(self.loadExcelData)
        self.btnSave.clicked.connect(self.saveExcelData)
        self.btnAddData.clicked.connect(self.addRow)
        self.btnDeleteData.clicked.connect(self.removeRow)
        self.btnCopy.clicked.connect(self.copyRow)
        #################

    def saveExcelData(self):
        rep = QtWidgets.QFileDialog.getSaveFileName()
        print(rep)

    #def loadExcelData(self, excel_file_dir, worksheet_name):
    def loadExcelData(self):
        rep = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла для загрузки', '', 'XLS File (*.xls*)')
                #getSaveFileName()
                #df = pd.read_excel(excel_file_dir, worksheet_name)

        df = pd.read_excel(rep[0])
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        #   returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)

        self.tableWidget.setColumnWidth(2, 300)

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
