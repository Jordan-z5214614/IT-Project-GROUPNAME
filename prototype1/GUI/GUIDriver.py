#!/usr/bin/env python3

import PyQt5.QtWidgets as Q
import PyQt5.QtCore as Qt
class GUI:

    def __init__(self):

        self.RPM = 0
        self.power = 0
        self.target = 0

        self.app = Q.QApplication([])
        self.window = Q.QWidget()

        self.createSupervisorBox("1")

        layout = Q.QGridLayout()
        layout.addWidget(self.supervisorBox)

        self.window.setLayout(layout)
    def createSupervisorBox(self,number):
        self.supervisorBox = Q.QGroupBox("Supervisory Computer " + number)

        layout = Q.QGridLayout()
        self.createTurbineBox("1")
        layout.addWidget(self.turbineBox,0,0)
        self.createTurbineBox("2")
        layout.addWidget(self.turbineBox,0,1)

        self.supervisorBox.setLayout(layout)
    def createTurbineBox(self,number):
        self.turbineBox = Q.QGroupBox("Turbine " + number)

        modeSelect = Q.QGroupBox("Mode:")
        autoRadioButton = Q.QRadioButton("Auto")
        manRadioButton = Q.QRadioButton("Manual")
        autoRadioButton.setChecked(True)

        modeLayout = Q.QHBoxLayout()
        modeLayout.addWidget(autoRadioButton)
        modeLayout.addWidget(manRadioButton)
        modeSelect.setLayout(modeLayout)

        paramDisp = Q.QGroupBox()
        paramLayout = Q.QGridLayout()

        RPMLabel = Q.QLabel(paramDisp)
        RPMLabel.setText("RPM:")
        RPMVal = Q.QLabel(paramDisp)
        RPMVal.setText(str(self.RPM))
        powerLabel = Q.QLabel(paramDisp)
        powerLabel.setText("Power Output:")
        powerOut = Q.QProgressBar()
        powerOut.setRange(0,100)
        powerOut.setValue(self.power)
        targetLabel = Q.QLabel(paramDisp)
        targetLabel.setText("Target RPM:")
        targetVal = Q.QLabel(paramDisp)
        targetVal.setText(str(self.target))
        targetSlide = Q.QSlider(Qt.Qt.Horizontal,paramDisp)
        targetSlide.setValue(self.target)
        startButton = Q.QPushButton("START")
        stopButton = Q.QPushButton("STOP")

        paramLayout = Q.QGridLayout()
        paramLayout.addWidget(RPMLabel, 0,0,1,1)
        paramLayout.addWidget(RPMVal, 0,4,1,1)
        paramLayout.addWidget(powerLabel, 1,0,1,1)
        paramLayout.addWidget(powerOut, 2,0,1,-1)
        paramLayout.addWidget(targetLabel, 3,0,1,1)
        paramLayout.addWidget(targetVal, 3,4,1,1)
        paramLayout.addWidget(targetSlide, 4,0,1,-1)
        paramLayout.addWidget(startButton, 5,0,2,2)
        paramLayout.addWidget(stopButton, 5,3,2,2)

        paramDisp.setLayout(paramLayout)

        layout = Q.QGridLayout()
        layout.addWidget(modeSelect,0,0,1,5)
        layout.addWidget(paramDisp,1,0,6,5)
        self.turbineBox.setLayout(layout)

if __name__=='__main__':
    gui = GUI()
    gui.window.show()
    gui.app.exec_()
