# Form implementation generated from reading ui file 'ui_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FPSLayout = QtWidgets.QHBoxLayout()
        self.FPSLayout.setObjectName("FPSLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.FPSLayout.addItem(spacerItem)
        self.FPSLabel = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FPSLabel.sizePolicy().hasHeightForWidth())
        self.FPSLabel.setSizePolicy(sizePolicy)
        self.FPSLabel.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(11)
        self.FPSLabel.setFont(font)
        self.FPSLabel.setObjectName("FPSLabel")
        self.FPSLayout.addWidget(self.FPSLabel)
        self.FPSSpinBox = QtWidgets.QSpinBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FPSSpinBox.sizePolicy().hasHeightForWidth())
        self.FPSSpinBox.setSizePolicy(sizePolicy)
        self.FPSSpinBox.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.FPSSpinBox.setFont(font)
        self.FPSSpinBox.setStyleSheet("QSpinBox {\n"
"    border-radius: 10px;\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"    background-color: rgb(204, 204, 255);\n"
"    font: 16px Fira Code;\n"
"    text-align: center;\n"
"}")
        self.FPSSpinBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.FPSSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FPSSpinBox.setMinimum(1)
        self.FPSSpinBox.setMaximum(65536)
        self.FPSSpinBox.setValue(10)
        self.FPSSpinBox.setObjectName("FPSSpinBox")
        self.FPSLayout.addWidget(self.FPSSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.FPSLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.FPSLayout, 2, 0, 1, 1)
        self.ProgressBarLayout = QtWidgets.QHBoxLayout()
        self.ProgressBarLayout.setObjectName("ProgressBarLayout")
        self.ProgressBar = QtWidgets.QProgressBar(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressBar.sizePolicy().hasHeightForWidth())
        self.ProgressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        self.ProgressBar.setFont(font)
        self.ProgressBar.setStyleSheet("QProgressBar {\n"
"    font: 12pt Fira Code SemiBold;\n"
"    border: 2px solid black;\n"
"    background-color: rgb(0, 128, 77);\n"
"    color: black;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(128, 255, 212);\n"
"    width: 20px;\n"
"}")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ProgressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.ProgressBar.setObjectName("ProgressBar")
        self.ProgressBarLayout.addWidget(self.ProgressBar)
        self.gridLayout_2.addLayout(self.ProgressBarLayout, 4, 0, 1, 1)
        self.VideoImageOutputLayout = QtWidgets.QHBoxLayout()
        self.VideoImageOutputLayout.setObjectName("VideoImageOutputLayout")
        self.VideoLabelOutput = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoLabelOutput.sizePolicy().hasHeightForWidth())
        self.VideoLabelOutput.setSizePolicy(sizePolicy)
        self.VideoLabelOutput.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.VideoLabelOutput.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.VideoLabelOutput.setText("")
        self.VideoLabelOutput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.VideoLabelOutput.setObjectName("VideoLabelOutput")
        self.VideoImageOutputLayout.addWidget(self.VideoLabelOutput)
        self.FramesLabelOutput = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FramesLabelOutput.sizePolicy().hasHeightForWidth())
        self.FramesLabelOutput.setSizePolicy(sizePolicy)
        self.FramesLabelOutput.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.FramesLabelOutput.setText("")
        self.FramesLabelOutput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FramesLabelOutput.setObjectName("FramesLabelOutput")
        self.VideoImageOutputLayout.addWidget(self.FramesLabelOutput)
        self.gridLayout_2.addLayout(self.VideoImageOutputLayout, 0, 0, 1, 1)
        self.LoggersLayout = QtWidgets.QHBoxLayout()
        self.LoggersLayout.setObjectName("LoggersLayout")
        self.VideoLoggerText = QtWidgets.QTextEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoLoggerText.sizePolicy().hasHeightForWidth())
        self.VideoLoggerText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.VideoLoggerText.setFont(font)
        self.VideoLoggerText.setStyleSheet("QTextEdit {\n"
"    font: 11pt Fira Code;\n"
"    border: 2px solid black;\n"
"    background-color: rgb(230, 255, 242);\n"
"    color: black;\n"
"}")
        self.VideoLoggerText.setReadOnly(True)
        self.VideoLoggerText.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.VideoLoggerText.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.VideoLoggerText.setObjectName("VideoLoggerText")
        self.LoggersLayout.addWidget(self.VideoLoggerText)
        self.FramesConversionLoggerText = QtWidgets.QTextEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FramesConversionLoggerText.sizePolicy().hasHeightForWidth())
        self.FramesConversionLoggerText.setSizePolicy(sizePolicy)
        self.FramesConversionLoggerText.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.FramesConversionLoggerText.setFont(font)
        self.FramesConversionLoggerText.setStyleSheet("QTextEdit {\n"
"    font: 11pt Fira Code;\n"
"    border: 2px solid black;\n"
"    background-color: rgb(230, 255, 255);\n"
"    color: black;\n"
"}")
        self.FramesConversionLoggerText.setReadOnly(True)
        self.FramesConversionLoggerText.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.FramesConversionLoggerText.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.FramesConversionLoggerText.setObjectName("FramesConversionLoggerText")
        self.LoggersLayout.addWidget(self.FramesConversionLoggerText)
        self.gridLayout_2.addLayout(self.LoggersLayout, 3, 0, 1, 1)
        self.ButtonsLayout = QtWidgets.QHBoxLayout()
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ButtonsLayout.addItem(spacerItem2)
        self.UploadVideoButton = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UploadVideoButton.sizePolicy().hasHeightForWidth())
        self.UploadVideoButton.setSizePolicy(sizePolicy)
        self.UploadVideoButton.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.UploadVideoButton.setFont(font)
        self.UploadVideoButton.setStyleSheet("QPushButton {\n"
"    font: 11pt Fira Code SemiBold;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 153, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(128, 204, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 77, 128);\n"
"}")
        self.UploadVideoButton.setAutoDefault(True)
        self.UploadVideoButton.setObjectName("UploadVideoButton")
        self.ButtonsLayout.addWidget(self.UploadVideoButton)
        self.Line1 = QtWidgets.QFrame(parent=Form)
        self.Line1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.Line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.Line1.setObjectName("Line1")
        self.ButtonsLayout.addWidget(self.Line1)
        self.ConvertButton = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvertButton.sizePolicy().hasHeightForWidth())
        self.ConvertButton.setSizePolicy(sizePolicy)
        self.ConvertButton.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setStyleSheet("QPushButton {\n"
"    font: 11pt Fira Code SemiBold;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 255, 128);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(128, 255, 191);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 128, 64);\n"
"}")
        self.ConvertButton.setObjectName("ConvertButton")
        self.ButtonsLayout.addWidget(self.ConvertButton)
        self.CancelButton = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet("QPushButton {\n"
"    font: 11pt Fira Code SemiBold;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 85);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 128, 170);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(128, 0, 42);\n"
"}")
        self.CancelButton.setObjectName("CancelButton")
        self.ButtonsLayout.addWidget(self.CancelButton)
        self.Line2 = QtWidgets.QFrame(parent=Form)
        self.Line2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.Line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.Line2.setObjectName("Line2")
        self.ButtonsLayout.addWidget(self.Line2)
        self.ClearVideoButton = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearVideoButton.sizePolicy().hasHeightForWidth())
        self.ClearVideoButton.setSizePolicy(sizePolicy)
        self.ClearVideoButton.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.ClearVideoButton.setFont(font)
        self.ClearVideoButton.setStyleSheet("QPushButton {\n"
"    font: 11pt Fira Code SemiBold;\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 204, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 230, 128);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(128, 102, 0);\n"
"}")
        self.ClearVideoButton.setObjectName("ClearVideoButton")
        self.ButtonsLayout.addWidget(self.ClearVideoButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ButtonsLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.ButtonsLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.FPSLabel.setText(_translate("Form", "FPS:"))
        self.FPSSpinBox.setToolTip(_translate("Form", "<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Converted FPS</h2>\n"
"<p>Set the converted frames per second manually within this radio box, with the default setting to 10 frames, and can be customized anyway.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Minimum and maximum converted frames per second: 1 and 65,536.</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
""))
        self.UploadVideoButton.setToolTip(_translate("Form", "<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Upload Video</h2>\n"
"<p>Upload a single video file into the first left-sided widget shown on the screen (primarly as a thumbnail).</p>\n"
"\n"
"<div class=\"tooltip\">Accepted 8 video file(s) format:\n"
"  <span class=\"tooltiptext\">MP4, AVI, MOV, WMV, MKV, FLV, MPEG, and 3GP.</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
""))
        self.UploadVideoButton.setText(_translate("Form", "Upload Video"))
        self.ConvertButton.setToolTip(_translate("Form", "<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Convert</h2>\n"
"<p>Convert the single upload video file into a sequence of frames (captured in a N-frames per second) in the FPS Radio Button below. The sequences of converted frames are being shown on the right-sided widget one-by-one for each converted frames.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Considering some file video formats may be slowing down the conversion process (as for MKV files), and other aspects, i.e. video\'s length, default video\'s FPS, video\'s dimension size (in a pixel format), etc.</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
""))
        self.ConvertButton.setText(_translate("Form", "Convert"))
        self.CancelButton.setToolTip(_translate("Form", "<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Cancel</h2>\n"
"<p>Cancel the conversion process. The cancellation is executed without giving any further warnings beforehand, and the sequence of the converted frames will be also immedieately being deleted.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Whenever you feel the conversion process took long enough to be done, or maybe you uploaded a wrong video file, then just cancel the conversion process.</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
""))
        self.CancelButton.setText(_translate("Form", "Cancel"))
        self.ClearVideoButton.setToolTip(_translate("Form", "<!DOCTYPE html>\n"
"<html>\n"
"<style>\n"
".tooltip {\n"
"  position: relative;\n"
"  display: inline-block;\n"
"  border-bottom: 1px dotted black;\n"
"}\n"
"\n"
".tooltip .tooltiptext {\n"
"  visibility: hidden;\n"
"  width: 120px;\n"
"  background-color: #555;\n"
"  color: #fff;\n"
"  text-align: center;\n"
"  border-radius: 6px;\n"
"  padding: 5px 0;\n"
"  position: absolute;\n"
"  z-index: 1;\n"
"  bottom: 125%;\n"
"  left: 50%;\n"
"  margin-left: -60px;\n"
"  opacity: 0;\n"
"  transition: opacity 0.3s;\n"
"}\n"
"\n"
".tooltip .tooltiptext::after {\n"
"  content: \"\";\n"
"  position: absolute;\n"
"  top: 100%;\n"
"  left: 50%;\n"
"  margin-left: -5px;\n"
"  border-width: 5px;\n"
"  border-style: solid;\n"
"  border-color: #555 transparent transparent transparent;\n"
"}\n"
"\n"
".tooltip:hover .tooltiptext {\n"
"  visibility: visible;\n"
"  opacity: 1;\n"
"}\n"
"</style>\n"
"<body style=\"text-align:center;\">\n"
"\n"
"<h2>Clear All</h2>\n"
"<p>Clear the uploaded video file (and some excess converted frames on the other side of the widget), including all the created logger tasks since the operation has been done.</p>\n"
"\n"
"<div class=\"tooltip\">Useful tips:\n"
"  <span class=\"tooltiptext\">Make sure to do this operation when there\'s no conversion process ongoing!</span>\n"
"</div>\n"
"\n"
"</body>\n"
"</html>\n"
""))
        self.ClearVideoButton.setText(_translate("Form", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
