# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obci_window.ui'
#
# Created: Wed Apr  4 19:07:42 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OBCILauncher(object):
    def setupUi(self, OBCILauncher):
        OBCILauncher.setObjectName(_fromUtf8("OBCILauncher"))
        OBCILauncher.resize(848, 512)
        OBCILauncher.setWindowTitle(QtGui.QApplication.translate("OBCILauncher", "OBCI Launcher", None, QtGui.QApplication.UnicodeUTF8))
        OBCILauncher.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        OBCILauncher.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(OBCILauncher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QtCore.QSize(40, 0))
        self.groupBox.setTitle(QtGui.QApplication.translate("OBCILauncher", "Experiment scenarios", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scenarios = QtGui.QTreeWidget(self.groupBox)
        self.scenarios.setObjectName(_fromUtf8("scenarios"))
        self.scenarios.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_4.addWidget(self.scenarios)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("OBCILauncher", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.info = QtGui.QLabel(self.groupBox_3)
        self.info.setText(QtGui.QApplication.translate("OBCILauncher", "asjdn asjklndjk naskljdh jkashdjk ashdkjhas kjashd akljshdk jlasd kjahdkjashd kjahsdjk hasdjlhasdklj hadkljashd lashd kjash djkashdkj ahsd lash", None, QtGui.QApplication.UnicodeUTF8))
        self.info.setWordWrap(True)
        self.info.setOpenExternalLinks(True)
        self.info.setObjectName(_fromUtf8("info"))
        self.gridLayout_2.addWidget(self.info, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setText(QtGui.QApplication.translate("OBCILauncher", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setText(QtGui.QApplication.translate("OBCILauncher", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontalLayout.addWidget(self.stop_button)
        self.reset_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setText(QtGui.QApplication.translate("OBCILauncher", "Reset all", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.horizontalLayout.addWidget(self.reset_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.parameters_of = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_of.sizePolicy().hasHeightForWidth())
        self.parameters_of.setSizePolicy(sizePolicy)
        self.parameters_of.setMinimumSize(QtCore.QSize(0, 0))
        self.parameters_of.setTitle(QtGui.QApplication.translate("OBCILauncher", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.parameters_of.setObjectName(_fromUtf8("parameters_of"))
        self.gridLayout_3 = QtGui.QGridLayout(self.parameters_of)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.parameters = QtGui.QTreeWidget(self.parameters_of)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters.sizePolicy().hasHeightForWidth())
        self.parameters.setSizePolicy(sizePolicy)
        self.parameters.setMinimumSize(QtCore.QSize(390, 1))
        self.parameters.setObjectName(_fromUtf8("parameters"))
        self.parameters.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout_3.addWidget(self.parameters, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.details_label = QtGui.QLabel(self.parameters_of)
        self.details_label.setText(QtGui.QApplication.translate("OBCILauncher", "Details mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.details_label.setObjectName(_fromUtf8("details_label"))
        self.horizontalLayout_4.addWidget(self.details_label)
        self.details_mode = QtGui.QComboBox(self.parameters_of)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_mode.sizePolicy().hasHeightForWidth())
        self.details_mode.setSizePolicy(sizePolicy)
        self.details_mode.setObjectName(_fromUtf8("details_mode"))
        self.horizontalLayout_4.addWidget(self.details_mode)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.splitter, 0, 0, 1, 1)
        OBCILauncher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OBCILauncher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setTitle(QtGui.QApplication.translate("OBCILauncher", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        OBCILauncher.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OBCILauncher)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OBCILauncher.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(OBCILauncher)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("OBCILauncher", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        OBCILauncher.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave_as = QtGui.QAction(OBCILauncher)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesaveas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setText(QtGui.QApplication.translate("OBCILauncher", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave = QtGui.QAction(OBCILauncher)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setText(QtGui.QApplication.translate("OBCILauncher", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(OBCILauncher)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setText(QtGui.QApplication.translate("OBCILauncher", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAdd_to_sidebar = QtGui.QAction(OBCILauncher)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_add-bookmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_to_sidebar.setIcon(icon3)
        self.actionAdd_to_sidebar.setText(QtGui.QApplication.translate("OBCILauncher", "Add to sidebar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_to_sidebar.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_to_sidebar.setIconVisibleInMenu(True)
        self.actionAdd_to_sidebar.setObjectName(_fromUtf8("actionAdd_to_sidebar"))
        self.actionExit = QtGui.QAction(OBCILauncher)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setText(QtGui.QApplication.translate("OBCILauncher", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRemove_from_sidebar = QtGui.QAction(OBCILauncher)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_from_sidebar.setIcon(icon5)
        self.actionRemove_from_sidebar.setText(QtGui.QApplication.translate("OBCILauncher", "Remove from sidebar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_from_sidebar.setShortcut(QtGui.QApplication.translate("OBCILauncher", "Ctrl+Shift+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_from_sidebar.setIconVisibleInMenu(True)
        self.actionRemove_from_sidebar.setObjectName(_fromUtf8("actionRemove_from_sidebar"))
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionAdd_to_sidebar)
        self.toolBar.addAction(self.actionRemove_from_sidebar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(OBCILauncher)
        QtCore.QMetaObject.connectSlotsByName(OBCILauncher)

    def retranslateUi(self, OBCILauncher):
        pass

import resources_rc
