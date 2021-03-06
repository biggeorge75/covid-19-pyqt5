from PyQt5 import QtCore, QtGui, QtWidgets
from covid import Covid
from datetime import datetime
from bs4 import BeautifulSoup
import requests


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 247)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(633, 247))
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("covid.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(93, 154, 182);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.orsz_fert = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_fert.setFont(font)
        self.orsz_fert.setObjectName("orsz_fert")
        self.gridLayout.addWidget(self.orsz_fert, 5, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("padding: 3px;\n"
                                    "color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 8, 0, 3, 2)
        self.orsz_elh_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_elh_val.setFont(font)
        self.orsz_elh_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.orsz_elh_val.setObjectName("orsz_elh_val")
        self.gridLayout.addWidget(self.orsz_elh_val, 8, 5, 1, 1)
        self.orsz_fert_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_fert_val.setFont(font)
        self.orsz_fert_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.orsz_fert_val.setObjectName("orsz_fert_val")
        self.gridLayout.addWidget(self.orsz_fert_val, 8, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setStyleSheet("margin-left: 15px;\n"
                                 "margin-top: 5px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("covid-19.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.orsz_gyogy = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_gyogy.setFont(font)
        self.orsz_gyogy.setObjectName("orsz_gyogy")
        self.gridLayout.addWidget(self.orsz_gyogy, 5, 4, 1, 1)
        self.ossz_elh = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_elh.setFont(font)
        self.ossz_elh.setStyleSheet("")
        self.ossz_elh.setObjectName("ossz_elh")
        self.gridLayout.addWidget(self.ossz_elh, 0, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 4, 1, 1)
        self.ossz_fert = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_fert.setFont(font)
        self.ossz_fert.setStyleSheet("")
        self.ossz_fert.setObjectName("ossz_fert")
        self.gridLayout.addWidget(self.ossz_fert, 0, 3, 1, 1)
        self.time = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 11, 0, 2, 8)
        self.orsz_elh = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_elh.setFont(font)
        self.orsz_elh.setObjectName("orsz_elh")
        self.gridLayout.addWidget(self.orsz_elh, 5, 5, 1, 1)
        self.ossz_gyogy_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_gyogy_val.setFont(font)
        self.ossz_gyogy_val.setStyleSheet("color: rgb(213, 0, 0);")
        self.ossz_gyogy_val.setObjectName("ossz_gyogy_val")
        self.gridLayout.addWidget(self.ossz_gyogy_val, 1, 4, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 5, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 3, 1, 1)
        self.ossz_gyogy = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_gyogy.setFont(font)
        self.ossz_gyogy.setStyleSheet("")
        self.ossz_gyogy.setObjectName("ossz_gyogy")
        self.gridLayout.addWidget(self.ossz_gyogy, 0, 4, 1, 1)
        self.ossz_elh_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_elh_val.setFont(font)
        self.ossz_elh_val.setStyleSheet("color: rgb(213, 0, 0);")
        self.ossz_elh_val.setObjectName("ossz_elh_val")
        self.gridLayout.addWidget(self.ossz_elh_val, 1, 5, 1, 1)
        self.orsz_valasztasa = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.orsz_valasztasa.setFont(font)
        self.orsz_valasztasa.setObjectName("orsz_valasztasa")
        self.gridLayout.addWidget(self.orsz_valasztasa, 5, 0, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 2, 1, 1)
        self.ossz_fert_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.ossz_fert_val.setFont(font)
        self.ossz_fert_val.setStyleSheet("color: rgb(213, 0, 0);")
        self.ossz_fert_val.setObjectName("ossz_fert_val")
        self.gridLayout.addWidget(self.ossz_fert_val, 1, 3, 1, 1)
        self.orsz_gyogy_val = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.orsz_gyogy_val.setFont(font)
        self.orsz_gyogy_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.orsz_gyogy_val.setObjectName("orsz_gyogy_val")
        self.gridLayout.addWidget(self.orsz_gyogy_val, 8, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
#######################################################################################################################
        self.data()

        self.covid = Covid()

        self.confirmed = self.covid.get_total_confirmed_cases()
        self.recovered = self.covid.get_total_recovered()
        self.deaths = self.covid.get_total_deaths()

        countries = self.covid.list_countries()
        self.countries_list = []

        for i in countries:
            self.countries_list.append(i["name"])
        self.countries_list.sort()

        self.ossz_fert_val.setText(str(self.confirmed))
        self.ossz_gyogy_val.setText(str(self.recovered))
        self.ossz_elh_val.setText(str(self.deaths))

        self.comboBox.addItems(self.countries_list)

        Hungary = self.covid.get_status_by_country_name("Hungary")
        self.comboBox.setCurrentText(str(Hungary["country"]))

        self.resultCountries()
        self.comboBox.currentTextChanged.connect(self.resultCountries)

    def resultCountries(self):
        try:
            self.cur = self.comboBox.currentText()
            self.curCovid = self.covid.get_status_by_country_name(self.cur)

            self.orszConfirmed = self.curCovid["confirmed"]
            self.orszRecovered = self.curCovid["recovered"]
            self.orszDeaths = self.curCovid["deaths"]
            self.lastUpdate = self.curCovid["last_update"]

            self.orsz_fert_val.setText(str(self.orszConfirmed))
            self.orsz_gyogy_val.setText(str(self.orszRecovered))
            self.orsz_elh_val.setText(str(self.orszDeaths))

            update = self.lastUpdate
            your_dt = datetime.fromtimestamp(int(update) / 1000)
            if self.comboBox.currentTextChanged:
                if self.comboBox.currentText() == "Hungary":
                    self.orsz_fert_val.setText(str(self.confirmedH_adat))
                    self.orsz_gyogy_val.setText(str(self.recoveredH_adat))
                    self.orsz_elh_val.setText(str(self.deathsH_adat))

                self.orsz_valasztasa.setText("ország választása")

                if self.comboBox.currentText() == "Hungary":
                    self.time.setText("koronavirus.gov.hu > " + self.updateH_adat)
                else:
                    self.time.setText(
                        str(your_dt.strftime(self.comboBox.currentText() + " frissítve: " + "%Y-%m-%d %H:%M")))
        except:
            self.time.setText(self.comboBox.currentText() + " adatait nem sikerült lekérdezni!")
            self.orsz_fert_val.setText(str(''))
            self.orsz_gyogy_val.setText(str(''))
            self.orsz_elh_val.setText(str(''))

    def data(self):
        self.url = f"https://koronavirus.gov.hu/"

        self.response = requests.get(self.url, "lxml")
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.confirmedH = self.soup.select(".number")[0]
        self.confirmedH_adat = self.confirmedH.text
        self.recoveredH = self.soup.select(".number")[1]
        self.recoveredH_adat = self.recoveredH.text
        self.deathsH = self.soup.select(".number")[2]
        self.deathsH_adat = self.deathsH.text
        self.mintavH = self.soup.select(".number")[4]
        self.mintavH_adat = self.mintavH.text
        self.updateH = self.soup.select(".well-lg > p")[0]
        self.updateH_adat = self.updateH.text
#######################################################################################################################
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Covid-19 Statisztika"))
        self.orsz_fert.setText(_translate("Form", "Fertőzöttek"))
        self.orsz_elh_val.setText(_translate("Form", "0"))
        self.orsz_fert_val.setText(_translate("Form", "0"))
        self.label.setAccessibleDescription(_translate("Form", "0"))
        self.orsz_gyogy.setText(_translate("Form", "Gyógyultak"))
        self.ossz_elh.setText(_translate("Form", "Elhunytak"))
        self.ossz_fert.setText(_translate("Form", "Fertőzöttek"))
        self.time.setText(_translate("Form", "time"))
        self.orsz_elh.setText(_translate("Form", "Elhunytak"))
        self.ossz_gyogy_val.setText(_translate("Form", "0"))
        self.ossz_gyogy.setText(_translate("Form", "Gyógyultak"))
        self.ossz_elh_val.setText(_translate("Form", "0"))
        self.orsz_valasztasa.setText(_translate("Form", "ország választása"))
        self.ossz_fert_val.setText(_translate("Form", "0"))
        self.orsz_gyogy_val.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
